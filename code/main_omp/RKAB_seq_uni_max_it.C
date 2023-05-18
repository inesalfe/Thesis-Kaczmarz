#include "aux_func.h"
#include <iostream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 9) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_seq_uni_max_it.exe <data_set> <n_runs> <M> <N> <blocks> <it_per_thread> <max_it_stop> <block_repeat>'" << endl;
		exit(1);
	}

	double* b;
	double* x;
	double* x_sol;
	double** A;

	int n_runs = atoi(argv[2]);

	int M = atoi(argv[3]);
	int N = atoi(argv[4]);
	int blocks = atoi(argv[5]);
	int it_per_thread = atoi(argv[6]);
	long long max_it_stop = atoll(argv[7]);
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
		cout << "'./bin/RKAB_seq_uni_max_it.exe <data_set> <n_runs> <M> <N> <blocks> <it_per_thread> <max_it_stop> <block_repeat>'" << endl;
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
	double* x_k_thread = new double[N];
	double* x_prev = new double[N];
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
	int block_begin;

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		shuffle(begin(samp_line), end(samp_line), rng);
		it = -1;
		block_begin = 0;
		start = omp_get_wtime();
		while(it < max_it_stop) {
			it++;
			for (int i = 0; i < N; i++) {
				x_prev[i] = x_k[i];
				x_k[i] = 0;
			}
			for (int i = 0; i < blocks; i++) {
				for (int j = 0; j < N; j++)
					x_k_thread[j] = x_prev[j];
				for (int n = 0; n < block_repeat; n++) {
					for (int k = 0; k < it_per_thread; k++) {
						line = samp_line[(block_begin+k)%M];
						scale = (b[line]-dotProduct(A[line], x_k_thread, N))/sqrNorm_line[line];
						for (int j = 0; j < N; j++) {
							x_k_thread[j] += scale * A[line][j];
						}
					}
				}
				for (int j = 0; j < N; j++) {
					x_k[j] += x_k_thread[j]/blocks;
				}
				block_begin += it_per_thread;
			}
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

	delete[] x_k;
	delete[] x_k_thread;
	delete[] x_prev;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;
	delete[] sqrNorm_line;

	return 0;
}
