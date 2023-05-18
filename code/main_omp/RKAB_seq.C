#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 10) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_seq.exe <data_set> <n_runs> <eps> <M> <N> <blocks> <it_per_thread> <max_it_stop> <block_repeat>'" << endl;
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
	int blocks = atoi(argv[6]);
	int it_per_thread = atoi(argv[7]);
	long long max_it_stop = atoll(argv[8]);
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
		cout << "'./bin/RKAB_repeat_seq.exe <data_set> <n_runs> <eps> <M> <N> <blocks> <it_per_thread> <max_it_stop> <block_repeat>'" << endl;
		exit(1);
	}

	double start_total = omp_get_wtime();

	importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);

	vector<double> sqrNorm_line(M);
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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());
	vector<mt19937> gen(blocks);

	double* res = new double[M];
	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* x_k_thread = new double[N];
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

	bool solution_found;
	double norm_dif;
	double dif;
	double sqr_norm_res;

	vector<vector<int>> lines_used(blocks);
	for (int i = 0; i < blocks; i++)
		lines_used[i] = vector<int>(it_per_thread);

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		it = 0;
		solution_found = false;
        gen.clear();
        for (int i = 0; i < blocks; i++) {
            gen[i] = mt19937(run*blocks+i+1);
        }
		start = omp_get_wtime();
		while(!solution_found) {
			it++;
			for (int i = 0; i < N; i++) {
				x_prev[i] = x_k[i];
				x_k[i] = 0;
			}
			for (int i = 0; i < blocks; i++) {
				for (int j = 0; j < N; j++)
					x_k_thread[j] = x_prev[j];
				for (int k = 0; k < it_per_thread; k++) {
					line = dist(gen[i]);
					lines_used[i][k] = line;
					scale = (b[line]-dotProduct(A[line], x_k_thread, N))/sqrNorm_line[line];
					for (int j = 0; j < N; j++) {
						x_k_thread[j] += scale * A[line][j];
					}
				}
				for (int n = 0; n < block_repeat-1; n++) {
					for (int k = 0; k < it_per_thread; k++) {
						line = lines_used[i][k];
						scale = (b[line]-dotProduct(A[line], x_k_thread, N))/sqrNorm_line[line];
						for (int j = 0; j < N; j++) {
							x_k_thread[j] += scale * A[line][j];
						}
					}
				}
				for (int j = 0; j < N; j++) {
					x_k[j] += x_k_thread[j]/blocks;
				}
			}
			if (it%max_it_stop == 0) {
				norm_dif = 0;
				for (int i = 0; i < N; i++) {
					dif = x_k[i] - x_prev[i];
					norm_dif += dif*dif;
				}
				if (norm_dif < 1E-25) {
					for (int i = 0; i < M; i++) {
						res[i] = b[i] - dotProduct(A[i], x_k, N);
					}
					sqr_norm_res = 0;
					for (int i = 0; i < M; i++)
						sqr_norm_res += res[i]*res[i];
					if (sqr_norm_res < eps) {
						solution_found = true;
					}
				}
			}
		}	
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it;
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
	delete[] x_k;
	delete[] x_k_thread;
	delete[] x_prev;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}
