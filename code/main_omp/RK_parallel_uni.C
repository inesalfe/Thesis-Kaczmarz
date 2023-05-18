#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
#include <random>
#include <algorithm>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RK_parallel_uni.exe <data_set> <n_runs> <eps> <M> <N> <max_it_stop>'" << endl;
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
	long long max_it_stop = atoll(argv[6]);

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
		cout << "'./bin/RK_parallel_uni.exe <data_set> <n_runs> <eps> <M> <N> <max_it_stop>'" << endl;
		exit(1);
	}

	double start_total = omp_get_wtime();

	importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);

	double* sqrNorm_line = new double[M];
	double sqr_matrixNorm = 0;
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
		sqr_matrixNorm += sqrNorm_line[i];
	}

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
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
	
	long long avg_it = 0;

	int t_id;
	bool solution_found;
	double norm_dif;
	double sqr_norm_res;
	double dif;
	double dot_p;
	int num_threads;
	long long it_final;

	#pragma omp parallel
	{
		#pragma omp single
			num_threads = omp_get_num_threads();
	}

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		shuffle(begin(samp_line), end(samp_line), rng);
		it = 0;
		solution_found = false;
		start = omp_get_wtime();
		#pragma omp parallel firstprivate(it)
		{
			while(!solution_found) {
				it++;
				#pragma omp single
				{
					line = samp_line[it%M];
					dot_p = 0;
				}
				#pragma omp for reduction(+:dot_p)
					for (int i = 0; i < N; i++)
						dot_p += A[line][i]*x_k[i];
				#pragma omp single
					scale = (b[line]-dot_p)/sqrNorm_line[line];
				#pragma omp for
					for (int i = 0; i < N; i++) {
						if (it%max_it_stop == 0)
							x_prev[i] = x_k[i];
						x_k[i] += scale * A[line][i];
					}
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

	delete[] x_k;
	delete[] x_prev;
	delete[] res;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;
	delete[] sqrNorm_line;

	return 0;
}
