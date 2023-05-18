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

	if(argc != 10) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_uni.exe <data_set> <n_runs> <eps> <M> <N> <it_per_thread> <max_it_stop> <blocks> <block_repeat>'" << endl;
		exit(1);
	}

	double* b;
	double* x;
	double* x_sol;
	double** A;

	int n_runs = atoi(argv[2]);
	double eps = atof(argv[3]);

	int M = atoi(argv[4]);
	int N = atoi(argv[5]);
	int it_per_thread = atoi(argv[6]);
	long long max_it_stop = atoll(argv[7]);
	int blocks = atoi(argv[8]);
	int block_repeat = atoi(argv[9]);

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
		cout << "'./bin/RKAB_uni.exe <data_set> <n_runs> <eps> <M> <N> <it_per_thread> <max_it_stop> <blocks> <block_repeat>'" << endl;
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

	double* res = new double[M];
	double* x_prev = new double[N];
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
	double norm_dif;
	double dif;
	double sqr_norm_res;

	double start; 
	double stop;
	double duration = 0;

	int t_id;
	int num_threads;

	long long avg_it = 0;
	long long it_final;
	bool solution_found;

	#pragma omp parallel
	{
		#pragma omp single
			num_threads = omp_get_num_threads();
	}

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		shuffle(begin(samp_line), end(samp_line), rng);
		it = -1;
		solution_found = false;
		start = omp_get_wtime();
		#pragma omp parallel private(line, scale, t_id, x_k_thread, x_k_block) firstprivate(it)
		{
			x_k_thread = new double[N];
			x_k_block = new double[N];
			t_id = omp_get_thread_num();
			int low_block_id = BLOCK_LOW(t_id, num_threads, blocks);
			int size_blocks = BLOCK_SIZE(t_id, num_threads, blocks);
			int block_begin = it_per_thread*low_block_id;
			while(!solution_found) {
				it++;
				#pragma omp barrier
				if (it%max_it_stop == 0) {
					#pragma omp for
						for (int i = 0; i < N; i++) {
							x_prev[i] = x_k[i];
						}
				}
				for (int block_it = 0; block_it < size_blocks; block_it++) {
					line = samp_line[block_begin%M];
					scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
					for (int j = 0; j < N; j++) {
						x_k_block[j] = x_k[j] + scale * A[line][j];
					}
					for (int i = 1; i < it_per_thread; i++) {
						line = samp_line[(block_begin+i)%M];
						scale = (b[line]-dotProduct(A[line], x_k_block, N))/sqrNorm_line[line];
						for (int j = 0; j < N; j++) {
							x_k_block[j] += scale * A[line][j];
						}
					}
					for (int n = 0; n < block_repeat-1; n++) {
						for (int i = 0; i < it_per_thread; i++) {
							line = samp_line[(block_begin+i)%M];
							scale = (b[line]-dotProduct(A[line], x_k_block, N))/sqrNorm_line[line];
							for (int j = 0; j < N; j++) {
								x_k_block[j] += scale * A[line][j];
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
					block_begin += it_per_thread;
				}
				block_begin += (blocks-size_blocks)*it_per_thread;
				#pragma omp barrier
				#pragma omp critical
			    	for (int i = 0; i < N; i++)
			            x_k[i] += x_k_thread[i];
				if (it%max_it_stop == 0) {
					#pragma omp single
						norm_dif = 0;
					#pragma omp for reduction(+:norm_dif)
						for (int i = 0; i < N; i++) {
							dif = x_k[i] - x_prev[i];
							norm_dif += dif*dif;
						}
					if (norm_dif < 1E-25) {
						#pragma omp for
							for (int i = 0; i < M; i++) {
								res[i] = b[i] - dotProduct(A[i], x_k, N);
							}
						#pragma omp single
							sqr_norm_res = 0;
						#pragma omp for reduction(+:sqr_norm_res)
							for (int i = 0; i < M; i++)
								sqr_norm_res += res[i]*res[i];
						#pragma omp single
							if (sqr_norm_res < eps) {
								it_final = it;
								solution_found = true;
							}
					}
				}
			}
			delete[] x_k_thread;
			delete[] x_k_block;
		}	
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it_final;
	}
	avg_it /= n_runs;
	cout << M << " " << N << " " << duration << " " << avg_it << " ";

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration_total << endl;

	delete[] res;
	delete[] x_prev;
	delete[] x_k;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;
	delete[] sqrNorm_line;

	return 0;
}
