#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <omp.h>
#include <random>
#include <algorithm>
using namespace std;

// ./bin/SRKAWOR_alpha_tomo.exe ct_gaussian 19558 16384 3 1 10000000 1 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_gaussian 19558 16384 3 2 10000000 1.5 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_gaussian 19558 16384 3 4 10000000 2 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_gaussian 19558 16384 3 8 10000000 4 10000

// ./bin/SRKAWOR_alpha_tomo.exe ct_poisson 19558 16384 3 1 10000000 1 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_poisson 19558 16384 3 2 10000000 1.5 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_poisson 19558 16384 3 4 10000000 2 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_poisson 19558 16384 3 8 10000000 4 10000

// ./bin/SRKAWOR_alpha_tomo.exe ct_gaussian 19558 16384 3 1 30000000 1 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_gaussian 19558 16384 3 2 30000000 1.5 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_gaussian 19558 16384 3 4 30000000 2 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_gaussian 19558 16384 3 8 30000000 4 10000

// ./bin/SRKAWOR_alpha_tomo.exe ct_poisson 19558 16384 3 1 30000000 1 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_poisson 19558 16384 3 2 30000000 1.5 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_poisson 19558 16384 3 4 30000000 2 10000
// ./bin/SRKAWOR_alpha_tomo.exe ct_poisson 19558 16384 3 8 30000000 4 10000

int main (int argc, char *argv[]) {

	if(argc != 9) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/SRKAWOR_alpha_tomo.exe <data_set> <M> <M> <seed> <threads> <max_it_stop> <alpha> <step_save>'" << endl;
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
	long long max_it_stop = atoll(argv[6]);
	double alpha = atof(argv[7]);
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
		cout << "'./bin/SRKAWOR_alpha_tomo.exe <data_set> <M> <M> <seed> <threads> <max_it_stop> <alpha> <step_save>'" << endl;
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
	double* res = new double[M];
	double scale;
	int line;
	long long it;

	string filename_error = output_foler + "SRKAWOR_alpha_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(threads) + "_" + to_string(max_it_stop) + "_" + to_string(alpha) + ".txt";
	ofstream file_error(filename_error);
	if (!file_error.is_open()) {
		cout << "ERROR: Invalid input file for error output file." << endl;
		exit(1);
	}

	string filename_res = output_foler + "SRKAWOR_alpha_res_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(threads) + "_" + to_string(max_it_stop) + "_" + to_string(alpha) + ".txt";
	ofstream file_res(filename_res);
	if (!file_res.is_open()) {
		cout << "ERROR: Invalid input file for residual output file." << endl;
		exit(1);
	}

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);
	shuffle(begin(samp_line), end(samp_line), rng);
	for (int i = 0; i < N; i++) {
		x_k[i] = 0;
	}
	it = 0;
	while(it < max_it_stop) {
		it++;
		for (int i = 0; i < N; i++) {
			x_prev[i] = x_k[i];
		}
		for (int i = 0; i < threads; i++) {
			line = samp_line[(threads*it+i)%M];
			scale = alpha * (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_prev))/sqrNorm_line[line];
			scaleDivideVecLine(line, threads, row_idx, cols, values_csr, scale, x_k);
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
	delete[] res;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;

	return 0;
}