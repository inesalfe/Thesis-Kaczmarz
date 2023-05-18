#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <omp.h>
#include <random>
#include <algorithm>
using namespace std;

// ./bin/SRKABWOR_tomo.exe ct_gaussian 19558 16384 3 1 15000 100 1
// ./bin/SRKABWOR_tomo.exe ct_gaussian 19558 16384 3 2 15000 100 1
// ./bin/SRKABWOR_tomo.exe ct_gaussian 19558 16384 3 4 15000 100 1
// ./bin/SRKABWOR_tomo.exe ct_gaussian 19558 16384 3 8 15000 100 1

// ./bin/SRKABWOR_tomo.exe ct_poisson 19558 16384 3 1 15000 100 1
// ./bin/SRKABWOR_tomo.exe ct_poisson 19558 16384 3 2 15000 100 1
// ./bin/SRKABWOR_tomo.exe ct_poisson 19558 16384 3 4 15000 100 1
// ./bin/SRKABWOR_tomo.exe ct_poisson 19558 16384 3 8 15000 100 1

// ./bin/SRKABWOR_tomo.exe ct_gaussian 19558 16384 3 1 15000 300 1
// ./bin/SRKABWOR_tomo.exe ct_gaussian 19558 16384 3 2 15000 300 1
// ./bin/SRKABWOR_tomo.exe ct_gaussian 19558 16384 3 4 15000 300 1
// ./bin/SRKABWOR_tomo.exe ct_gaussian 19558 16384 3 8 15000 300 1

// ./bin/SRKABWOR_tomo.exe ct_poisson 19558 16384 3 1 15000 300 1
// ./bin/SRKABWOR_tomo.exe ct_poisson 19558 16384 3 2 15000 300 1
// ./bin/SRKABWOR_tomo.exe ct_poisson 19558 16384 3 4 15000 300 1
// ./bin/SRKABWOR_tomo.exe ct_poisson 19558 16384 3 8 15000 300 1

int main (int argc, char *argv[]) {

	if(argc != 9) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/SRKABWOR_tomo.exe <data_set> <M> <M> <seed> <threads> <it_per_thread> <max_it_stop> <step_save>'" << endl;
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
	int step_save = atoi(argv[8]);

	double start_total = omp_get_wtime();
	string matrix_type = argv[1];
	string output_foler;
	if (matrix_type.compare("ct_poisson") == 0) {
		string filename_row_idx = "../data/ct_poisson/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_cols = "../data/ct_poisson/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_values_csr = "../data/ct_poisson/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_b = "../data/ct_poisson/b_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_x = "../data/ct_poisson/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		output_foler = "errors/tomo_poisson/";
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
		output_foler = "errors/tomo_gauss/";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/SRKABWOR_tomo.exe <data_set> <M> <M> <seed> <threads> <it_per_thread> <max_it_stop> <step_save>'" << endl;
		exit(1);
	}

	vector<double> sqrNorm_line(M);
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
	}

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* x_k_thread = new double[N];
	double* res = new double[M];
	double scale;
	int line;
	long long it;

	string filename_error = output_foler + "SRKABWOR_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(threads) + "_" + to_string(it_per_thread) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_error(filename_error);
	if (!file_error.is_open()) {
		cout << "ERROR: Invalid input file for error output file." << endl;
		exit(1);
	}

	string filename_res = output_foler + "SRKABWOR_res_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(threads) + "_" + to_string(it_per_thread) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_res(filename_res);
	if (!file_res.is_open()) {
		cout << "ERROR: Invalid input file for residual output file." << endl;
		exit(1);
	}

	int block_begin;

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);
	shuffle(begin(samp_line), end(samp_line), rng);
	for (int i = 0; i < N; i++) {
		x_k[i] = 0;
	}
	it = 0;
	block_begin = 0;
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
				line = samp_line[(block_begin+k)%M];
				scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_k_thread))/sqrNorm_line[line];
				scaleVecLine(line, row_idx, cols, values_csr, scale, x_k_thread);
			}
			for (int j = 0; j < N; j++) {
				x_k[j] += x_k_thread[j]/threads;
			}
			block_begin += it_per_thread;
		}
		if (it%step_save == 0) {
			for (int i = 0; i < M; i++) {
				res[i] = b[i] - dotProductCSR(i, row_idx, cols, values_csr, x_k);
			}
			file_res << it << " " << sqrt(sqrNorm(res, M)) << endl;
			file_error << it << " " << sqrt(sqrNormDiff(x_k, x, N)) << endl;
		}
	}
	file_res.close();
	file_error.close();

	delete[] x_k;
	delete[] x_prev;
	delete[] x_k_thread;
	delete[] res;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;

	return 0;
}