#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

// ./bin/RKAB_twin_tomo_sol.exe ct_error 17192 5625 500 1 1
// ./bin/RKAB_twin_tomo_sol.exe ct_error 17192 5625 500 2 1
// ./bin/RKAB_twin_tomo_sol.exe ct_error 17192 5625 500 4 1
// ./bin/RKAB_twin_tomo_sol.exe ct_error 17192 5625 500 8 1

// ./bin/RKAB_twin_tomo_sol.exe ct_error 17192 5625 1000 1 1
// ./bin/RKAB_twin_tomo_sol.exe ct_error 17192 5625 1000 2 1
// ./bin/RKAB_twin_tomo_sol.exe ct_error 17192 5625 1000 4 1
// ./bin/RKAB_twin_tomo_sol.exe ct_error 17192 5625 1000 8 1

// ./bin/RKAB_twin_tomo_sol.exe ct_gaussian 19558 16384 300 1 1
// ./bin/RKAB_twin_tomo_sol.exe ct_gaussian 19558 16384 300 2 1
// ./bin/RKAB_twin_tomo_sol.exe ct_gaussian 19558 16384 300 4 1
// ./bin/RKAB_twin_tomo_sol.exe ct_gaussian 19558 16384 300 8 1

// ./bin/RKAB_twin_tomo_sol.exe ct_gaussian 19558 16384 1000 1 1
// ./bin/RKAB_twin_tomo_sol.exe ct_gaussian 19558 16384 1000 2 1
// ./bin/RKAB_twin_tomo_sol.exe ct_gaussian 19558 16384 1000 4 1
// ./bin/RKAB_twin_tomo_sol.exe ct_gaussian 19558 16384 1000 8 1

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_twin_tomo_sol.exe <data_set> <M> <M> <seed> <max_it_stop> <threads>'" << endl;
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
	string output_foler;
	if (matrix_type.compare("ct_poisson") == 0) {
		string filename_row_idx = "../data/ct_poisson/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_cols = "../data/ct_poisson/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_values_csr = "../data/ct_poisson/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_b = "../data/ct_poisson/b_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_x = "../data/ct_poisson/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		output_foler = "outputs/tomo_poisson/";
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
		output_foler = "outputs/tomo_gauss/";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_twin_tomo_sol.exe <data_set> <M> <M> <seed> <max_it_stop> <threads>'" << endl;
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
	double* thread_down = new double[N];
	double* thread_up = new double[N];
	double* prev_down = new double[N];
	double* prev_up = new double[N];
	double* x_sol = new double[N];
	double scale;
	int line;
	long long it;

	string filename_sol = output_foler + "RKAB_twin_sol_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(threads) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_sol(filename_sol);
	if (!file_sol.is_open()) {
		cout << "ERROR: Invalid input file for error output file." << endl;
		exit(1);
	}

	for (int i = 0; i < N; i++) {
		x_down[i] = 0;
		x_up[i] = 0;
	}
	it = 0;
	while(it < max_it_stop) {
		it++;
		for (int j = 0; j < N; j++) {
			prev_down[j] = x_down[j];
			x_down[j] = 0;
		}
		for (int t = 0; t < threads; t++) {
			for (int j = 0; j < N; j++)
				thread_down[j] = prev_down[j];
			for (int line = BLOCK_LOW(t, threads, M); line < BLOCK_LOW(t, threads, M)+BLOCK_SIZE(t, threads, M); line++) {
				scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, thread_down))/sqrNorm_line[line]/threads;
				scaleVecLine(line, row_idx, cols, values_csr, scale, thread_down);
			}
			for (int j = 0; j < N; j++) {
				x_down[j] += thread_down[j]/threads;
			}
		}
		for (int j = 0; j < N; j++) {
			prev_up[j] = x_up[j];
			x_up[j] = 0;
		}
		for (int t = 0; t < threads; t++) {
			for (int j = 0; j < N; j++)
				thread_up[j] = prev_up[j];
			for (int line = BLOCK_LOW(t, threads, M)+BLOCK_SIZE(t, threads, M)-1; line >= BLOCK_LOW(t, threads, M); line--) {
				scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, thread_up))/sqrNorm_line[line]/threads;
				scaleVecLine(line, row_idx, cols, values_csr, scale, thread_up);
			}
			for (int j = 0; j < N; j++) {
				x_up[j] += thread_up[j]/threads;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		x_sol[i] = 0.5*(x_up[i]+x_down[i]);
	}
	for (int i = 0; i < N; i++) {
		file_sol << x_sol[i] << endl;
	}
	file_sol.close();

	delete[] x_down;
	delete[] x_up;
	delete[] thread_down;
	delete[] thread_up;
	delete[] x_sol;
	delete[] prev_up;
	delete[] prev_down;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;

	return 0;
}