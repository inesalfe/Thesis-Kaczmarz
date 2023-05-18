#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

// ./bin/RKAB_tomo_sol.exe ct_error 17192 5625 50000000 100000

// ./bin/RKAB_tomo_sol.exe ct_gaussian 9786 4096 10000000 10000

// ./bin/RKAB_tomo_sol.exe ct_gaussian 19558 16384 10000000 10000

int main (int argc, char *argv[]) {

	if(argc != 8) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_tomo_sol.exe <data_set> <M> <M> <seed> <threads> <it_per_thread> <max_it_stop>'" << endl;
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
	int threads = atoi(argv[5]);
	int it_per_thread = atoi(argv[6]);
	long long max_it_stop = atoll(argv[7]);

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
		cout << "'./bin/RKAB_tomo_sol.exe <data_set> <M> <M> <seed> <threads> <it_per_thread> <max_it_stop>'" << endl;
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
	vector<mt19937> gen(threads);

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* x_k_thread = new double[N];
	double scale;
	int line;
	long long it;

	string filename_sol = output_foler + "RKAB_sol_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(threads) + "_" + to_string(it_per_thread) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_sol(filename_sol);
	if (!file_sol.is_open()) {
		cout << "ERROR: Invalid input file for error output file." << endl;
		exit(1);
	}

	for (int i = 0; i < N; i++) {
		x_k[i] = 0;
	}
	for (int i = 0; i < threads; i++) {
        gen[i] = mt19937(i+1);
    }
	it = 0;
	while(it < max_it_stop) {
		it++;
		for (int i = 0; i < N; i++) {
			x_prev[i] = x_k[i];
			x_k[i] = 0;
		}
		for (int i = 0; i < threads; i++) {
			for (int j = 0; j < N; j++)
				x_k_thread[j] = x_prev[j];
			for (int k = 0; k < it_per_thread; k++) {
				line = dist(gen[i]);
				scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_k_thread))/sqrNorm_line[line];
				scaleVecLine(line, row_idx, cols, values_csr, scale, x_k_thread);
			}
			for (int j = 0; j < N; j++) {
				x_k[j] += x_k_thread[j]/threads;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		file_sol << x_k[i] << endl;
	}
	file_sol.close();

	delete[] x_k;
	delete[] x_prev;
	delete[] x_k_thread;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;

	return 0;
}