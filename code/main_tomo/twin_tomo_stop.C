#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

// ./bin/twin_tomo_stop.exe ct_gaussian 19558 16384 3 50
// 13 4.45699

// ./bin/twin_tomo_stop.exe ct_poisson 19558 16384 3 50
// 26 4.01255

int main (int argc, char *argv[]) {

	if(argc != 6) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/twin_tomo_stop.exe <data_set> <M> <M> <seed> <max_it_stop>'" << endl;
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
		cout << "'./bin/twin_tomo_stop.exe <data_set> <M> <M> <seed> <max_it_stop> <step_save>'" << endl;
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

	double* x_k_down = new double[N];
	double* x_k_up = new double[N];
	double scale;
	int line;
	long long it;
	
	vector<double> store_diff;
	double curr_diff;
	for (int i = 0; i < N; i++) {
		x_k_down[i] = 0;
		x_k_up[i] = 0;
	}
	it = 0;
	double start = omp_get_wtime();
	while(it < max_it_stop) {
		it++;
		for (int i = 0; i < M; i++) {
			line = i;
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_k_down))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values_csr, scale, x_k_down);	
			line = M-1-i;
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_k_up))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values_csr, scale, x_k_up);			
		}
		curr_diff = sqrNormDiff(x_k_up, x_k_down, N);
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
		x_sol[i] = 0.5*(x_k_down[i]+x_k_up[i]);
	}
	cout << M << " " << N << " " << it-7 << " " << end - start << " " << sqrt(sqrNormDiff(x_sol, x, N)) << endl;
	delete[] x_sol;

	delete[] x_k_down;
	delete[] x_k_up;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;

	return 0;
}