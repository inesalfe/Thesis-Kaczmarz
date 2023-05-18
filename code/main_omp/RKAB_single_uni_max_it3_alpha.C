#include "aux_func.h"
#include <iostream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 8) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_single_uni_max_it3_alpha.exe <data_set> <n_runs> <M> <N> <it_per_thread> <alpha> <max_it_stop>'" << endl;
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
	double alpha = atof(argv[6]);
	long long max_it_stop = atoll(argv[7]);

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
		cout << "'./bin/RKAB_single_uni_max_it3_alpha.exe <data_set> <n_runs> <M> <N> <it_per_thread> <alpha> <max_it_stop>'" << endl;
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
		#pragma omp parallel private(line, scale, t_id, x_k_thread) firstprivate(it)
		{
			x_k_thread = new double[N];
			t_id = omp_get_thread_num();
			int block_begin = it_per_thread*t_id;
			while(it < max_it_stop) {
				it++;
				#pragma omp barrier
				line = block_begin%M;
				scale = alpha * (b_shuffle[line]-dotProduct(A_shuffle[line], x_k, N))/sqrNorm_line_shuffle[line];
				for (int j = 0; j < N; j++) {
					x_k_thread[j] = x_k[j] + scale * A_shuffle[line][j];
				}
				for (int i = 1; i < it_per_thread; i++) {
					line = (block_begin+i)%M;
					scale = alpha * (b_shuffle[line]-dotProduct(A_shuffle[line], x_k_thread, N))/sqrNorm_line_shuffle[line];
					for (int j = 0; j < N; j++) {
						x_k_thread[j] += scale * A_shuffle[line][j];
					}
				}
				for (int i = 0; i < N; i++) {
					x_k_thread[i] -= x_k[i];
				}
				block_begin += num_threads*it_per_thread;
				#pragma omp barrier
				#pragma omp critical
			    	for (int i = 0; i < N; i++)
			            x_k[i] += x_k_thread[i]/num_threads;
			}
			delete[] x_k_thread;
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
