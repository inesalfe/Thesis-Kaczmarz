#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

// ./bin/RKA_twin_tomo_reg_stop.exe ct_gaussian 19558 16384 3 100 1
// 15 1.71248
// ./bin/RKA_twin_tomo_reg_stop.exe ct_gaussian 19558 16384 3 100 2
// 22 2.00675
// ./bin/RKA_twin_tomo_reg_stop.exe ct_gaussian 19558 16384 3 100 4
// 20 2.85399
// ./bin/RKA_twin_tomo_reg_stop.exe ct_gaussian 19558 16384 3 100 8
// 77 2.43729

// ./bin/RKA_twin_tomo_reg_stop.exe ct_poisson 19558 16384 3 100 1
// 24 1.49183
// ./bin/RKA_twin_tomo_reg_stop.exe ct_poisson 19558 16384 3 100 2
// 33 1.74332
// ./bin/RKA_twin_tomo_reg_stop.exe ct_poisson 19558 16384 3 100 4
// 66 1.88024
// ./bin/RKA_twin_tomo_reg_stop.exe ct_poisson 19558 16384 3 750 8
// 507 1.3708

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_twin_tomo_reg_stop.exe <data_set> <M> <M> <seed> <max_it_stop> <threads>'" << endl;
		exit(1);
	}

	int NNZ;
	double* b;
	double* x;
	int* row_idx;
	int* cols;
	double* values_csr;

	int M = atoi(argv[2]);
	int N = atoi(argv[3]);
	int seed = atoi(argv[4]);
	long long max_it_stop = atoll(argv[5]);
	int threads = atoi(argv[6]);

	double start_total = omp_get_wtime();
	string matrix_type = argv[1];
	if (matrix_type.compare("ct_poisson") == 0) {
		string filename_row_idx = "../data/ct_poisson/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_cols = "../data/ct_poisson/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_values_csr = "../data/ct_poisson/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_b = "../data/ct_poisson/b_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_x = "../data/ct_poisson/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else if (matrix_type.compare("ct_gaussian") == 0) {
		string filename_row_idx = "../data/ct_gaussian/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_cols = "../data/ct_gaussian/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_values_csr = "../data/ct_gaussian/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_b = "../data/ct_gaussian/b_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_x = "../data/ct_gaussian/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_twin_tomo_reg_stop.exe <data_set> <M> <M> <seed> <max_it_stop> <threads>'" << endl;
		exit(1);
	}

	vector<double> sqrNorm_line(M);
	double sqr_matrixNorm = 0;
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values_csr);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values_csr;
			delete[] b;
			delete[] x;
			exit(1);
		}
		sqr_matrixNorm += sqrNorm_line[i];
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_down = new double[N];
	double* x_up = new double[N];
	double* prev_down = new double[N];
	double* prev_up = new double[N];
	double scale;
	int line;
	long long it;

	int it_per_cycle = (M+N)/threads;

	vector<double> store_diff;
	double curr_diff;
	for (int i = 0; i < N; i++) {
		x_down[i] = 0;
		x_up[i] = 0;
	}
	it = 0;
	double start = omp_get_wtime();
	while(it < max_it_stop) {
		it++;
		for (int i = 0; i < it_per_cycle; i++) {
			for (int j = 0; j < N; j++) {
				prev_down[j] = x_down[j];
			}
			for (int t = 0; t < threads; t++) {
				line = BLOCK_LOW(t, threads, M+N) + i;
				// cout << line;
				if (line < M) {
					scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, prev_down))/sqrNorm_line[line];
					scaleDivideVecLine(line, threads, row_idx, cols, values_csr, scale, x_down);
				}
				else {
					if (prev_down[line%M] < 0)
						x_down[line%M] -= prev_down[line%M]/threads;
				}
			}
			for (int j = 0; j < N; j++) {
				prev_up[j] = x_up[j];
			}
			for (int t = 0; t < threads; t++) {
				line = BLOCK_LOW(t, threads, M+N) + BLOCK_SIZE(t, threads, M+N) - 1 - i;
				// cout << " " << line << endl;
				if (line < M) {
					scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, prev_up))/sqrNorm_line[line];
					scaleDivideVecLine(line, threads, row_idx, cols, values_csr, scale, x_up);
				}
				else {
					if (prev_up[line%M] < 0)
						x_up[line%M] -= prev_up[line%M]/threads;
				}
			}
		}
		curr_diff = sqrNormDiff(x_up, x_down, N);
		if (store_diff.size() == 0) {
			store_diff.push_back(curr_diff);
		}
		else {
			if (curr_diff < store_diff[0]) {
				store_diff.clear();
				store_diff.push_back(curr_diff);
			}
			else {
				store_diff.push_back(curr_diff);
				if (store_diff.size() == 8) {
					break;
				}
			}
		}
	}
	double end = omp_get_wtime();

	double* x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0.5*(x_down[i]+x_up[i]);
	}
	cout << M << " " << N << " " << it-7 << " " << end - start << " " << sqrt(sqrNormDiff(x_sol, x, N)) << " " << sqrt(curr_diff) << " " << endl;
	delete[] x_sol;

	delete[] x_down;
	delete[] x_up;
	delete[] prev_up;
	delete[] prev_down;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;

	return 0;
}