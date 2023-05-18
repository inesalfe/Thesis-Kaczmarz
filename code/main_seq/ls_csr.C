#include "kacz_csr.h"
#include "aux_func.h"
#include "csr.h"
#include "csc.h"
#include <iostream>
#include <math.h>
#include <omp.h>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/ls_csr.exe <method> <data_set> <n_runs> <eps> <M> <N>'" << endl;
		exit(1);
	}

	int M;
	int N;
	int NNZ;
	double* b;
	double* x;
	double* x_sol;
	int* row_idx;
	int* cols;
	double* values_csr;
	int* col_idx;
	int* rows;
	double* values_csc;

	int n_runs = atoi(argv[3]);
	double eps = atof(argv[4]);

	M = atoi(argv[5]);
	N = atoi(argv[6]);

	double start = omp_get_wtime();

	string matrix_type = argv[2];
	if (matrix_type.compare("ls_sparse_csr") == 0) {
		string filename_row_idx = "../data/ls_sparse_csr/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_cols = "../data/ls_sparse_csr/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csr = "../data/ls_sparse_csr/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_col_idx = "../data/ls_sparse_csr/col_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_rows = "../data/ls_sparse_csr/rows_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csc = "../data/ls_sparse_csr/values_csc_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ls_sparse_csr/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ls_sparse_csr/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importCSCMatrixSparseBIN(M, N, NNZ, filename_col_idx, filename_rows, filename_values_csc, col_idx, rows, values_csc);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/ls_csr.exe <method> <data_set> <n_runs> <eps> <M> <N>'" << endl;
		exit(1);
	}

	string alg = argv[1];
	if (alg.compare("REK_errorSC") == 0) {
		x_sol = REK_csr_csc_errorSC(M, N, row_idx, cols, values_csr, col_idx, rows, values_csc, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RGS_errorSC") == 0) {
		x_sol = RGS_csr_csc_errorSC(M, N, row_idx, cols, values_csr, col_idx, rows, values_csc, b, x, 1E-25, eps, 1000, n_runs);
	}
	else {
		cout << "Error: Invalid algorithm." << endl;
		delete[] row_idx;
		delete[] cols;
		delete[] values_csr;
		delete[] col_idx;
		delete[] rows;
		delete[] values_csc;
		delete[] b;
		delete[] x;
		return 0;
	}

	double stop = omp_get_wtime();
	double duration = stop - start;
	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration << endl;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] col_idx;
	delete[] rows;
	delete[] values_csc;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}