#include "aux_func.h"
#include <iostream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int main (int argc, char *argv[]) {

	if(argc != 9) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_uni_max_it4.exe <data_set> <n_runs> <M> <N> <it_per_thread> <max_it_stop> <blocks> <block_repeat>'" << endl;
		exit(1);
	}

	double* b;
	double* x;
	double* x_sol;
	double** A;

	int n_runs = atoi(argv[2]);

	int M = atoi(argv[3]);
	int N = atoi(argv[4]);
	int it_per_thread = atoi(argv[5]);
	long long max_it_stop = atoll(argv[6]);
	int blocks = atoi(argv[7]);
	int block_repeat = atoi(argv[8]);

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else if (matrix_type.compare("dense_rand") == 0) {
		filename_A = "../data/dense_rand/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_rand/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_rand/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_uni_max_it4.exe <data_set> <n_runs> <M> <N> <it_per_thread> <max_it_stop> <blocks> <block_repeat>'" << endl;
		exit(1);
	}

	double start_total = omp_get_wtime();

	importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNorm(A[i], N);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] A[0];
			delete[] A;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	double* x_k = new double[N];
	double* x_k_thread;
	double* x_k_block;
	x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	long long it;

	double start; 
	double stop;
	double duration = 0;

	int t_id;
	int num_threads;

	#pragma omp parallel
	{
		#pragma omp single
			num_threads = omp_get_num_threads();
	}

	double * aux = new double[(long)M*(long)N];
	double** A_shuffle = new double*[M];
	for (long i = 0; i < M; i++)
		A_shuffle[i] = &aux[i * N];
	double * b_shuffle = new double[M];
	double * sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		shuffle(begin(samp_line), end(samp_line), rng);
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				A_shuffle[i][j] = A[samp_line[i]][j];
			}
			b_shuffle[i] = b[samp_line[i]];
			sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
		}
		it = -1;
		start = omp_get_wtime();
		#pragma omp parallel private(line, scale, t_id, x_k_thread, x_k_block) firstprivate(it)
		{
			x_k_thread = new double[N];
			x_k_block = new double[N];
			t_id = omp_get_thread_num();
			int low_block_id = BLOCK_LOW(t_id, num_threads, blocks);
			int size_blocks = BLOCK_SIZE(t_id, num_threads, blocks);
			while(it < max_it_stop) {
				it++;
				#pragma omp barrier
				for (int block_it = 0; block_it < size_blocks; block_it++) {
					line = BLOCK_LOW(low_block_id+block_it, blocks, M) + (it*it_per_thread)%BLOCK_SIZE(low_block_id+block_it, blocks, M);
					scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k, N))/sqrNorm_line_shuffle[line];
					for (int j = 0; j < N; j++) {
						x_k_block[j] = x_k[j] + scale * A_shuffle[line][j];
					}
					for (int i = 1; i < it_per_thread; i++) {
						line = BLOCK_LOW(low_block_id+block_it, blocks, M) + (it*it_per_thread+i)%BLOCK_SIZE(low_block_id+block_it, blocks, M);
						scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k_block, N))/sqrNorm_line_shuffle[line];
						for (int j = 0; j < N; j++) {
							x_k_block[j] += scale * A_shuffle[line][j];
						}
					}
					for (int n = 0; n < block_repeat-1; n++) {
						for (int i = 0; i < it_per_thread; i++) {
							line = BLOCK_LOW(low_block_id+block_it, blocks, M) + (it*it_per_thread+i)%BLOCK_SIZE(low_block_id+block_it, blocks, M);
							scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k_block, N))/sqrNorm_line_shuffle[line];
							for (int j = 0; j < N; j++) {
								x_k_block[j] += scale * A_shuffle[line][j];
							}
						}
					}
					if (block_it == 0)
						for (int i = 0; i < N; i++) {
							x_k_thread[i] = (x_k_block[i] - x_k[i])/blocks;
						}
					else
						for (int i = 0; i < N; i++) {
							x_k_thread[i] += (x_k_block[i] - x_k[i])/blocks;
						}
				}
				#pragma omp barrier
				#pragma omp critical
			    	for (int i = 0; i < N; i++)
			            x_k[i] += x_k_thread[i];
			}
			delete[] x_k_thread;
			delete[] x_k_block;
		}	
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
	}
	cout << M << " " << N << " " << duration << " " << max_it_stop << " ";

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration_total << endl;

	delete[] A_shuffle[0];
	delete[] A_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;
	
	delete[] x_k;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;
	delete[] sqrNorm_line;

	return 0;
}
