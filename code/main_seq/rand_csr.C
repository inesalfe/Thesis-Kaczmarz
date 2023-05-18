#include "kacz_csr.h"
#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <math.h>
#include <omp.h>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/rand_csr.exe <method> <data_set> <n_runs> <eps> <M> <N>'" << endl;
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
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("sparse_real") == 0) {
		string filename_row_idx = "../data/sparse_real/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_cols = "../data/sparse_real/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csr = "../data/sparse_real/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";
		// string filename_col_idx = "../data/sparse_real/col_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		// string filename_rows = "../data/sparse_real/rows_" + to_string(M) + "_" + to_string(N) + ".bin";
		// string filename_values_csc = "../data/sparse_real/values_csc_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/sparse_real/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/sparse_real/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		// importCSCMatrixSparseBIN(M, N, NNZ, filename_col_idx, filename_rows, filename_values_csc, col_idx, rows, values_csc);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixDenseBIN(filename_A, M, N, NNZ, row_idx, cols, values_csr);
		// importCSCMatrixDenseBIN(filename_A, M, N, NNZ, col_idx, rows, values_csc);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else if (matrix_type.compare("ct") == 0) {
		string filename_row_idx = "../data/ct/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_cols = "../data/ct/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csr = "../data/ct/values_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ct/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ct/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/rand_csr.exe <method> <data_set> <n_runs> <eps> <M> <N>'" << endl;
		exit(1);
	}

	string alg = argv[1];
	if (alg.compare("RK") == 0) {
		x_sol = RK_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	// else if (alg.compare("REK") == 0) {
	// 	x_sol = REK_csr_csc(M, N, row_idx, cols, values_csr, col_idx, rows, values_csc, b, x, 1E-25, eps, 1000, n_runs);
	// }
	// else if (alg.compare("RGS") == 0) {
	// 	x_sol = RGS_csr_csc(M, N, row_idx, cols, values_csr, col_idx, rows, values_csc, b, x, 1E-25, eps, 1000, n_runs);
	// }
	else if (alg.compare("NSSRK") == 0) {
		x_sol = NSSRK_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("GSSRK") == 0) {
		x_sol = GSSRK_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("GRK") == 0) {
		x_sol = GRK_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_cyclic") == 0) {
		x_sol = RK_cyclic_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_rand") == 0) {
		x_sol = RK_rand_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand") == 0) {
		x_sol = RK_norep_rand_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_copy") == 0) {
		x_sol = RK_norep_rand_csr_copy(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle") == 0) {
		x_sol = RK_norep_rand_noshuffle_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_copy") == 0) {
		x_sol = RK_norep_rand_noshuffle_csr_copy(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_quasirand") == 0) {
		x_sol = RK_quasirand_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_quasirand_sobol") == 0) {
		x_sol = RK_quasirand_sobol_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_csr(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_copy") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_csr_copy(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_errorSC") == 0) {
		x_sol = RK_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	// else if (alg.compare("REK_errorSC") == 0) {
	// 	x_sol = REK_csr_csc_errorSC(M, N, row_idx, cols, values_csr, col_idx, rows, values_csc, b, x, 1E-25, eps, 1000, n_runs);
	// }
	// else if (alg.compare("RGS_errorSC") == 0) {
	// 	x_sol = RGS_csr_csc_errorSC(M, N, row_idx, cols, values_csr, col_idx, rows, values_csc, b, x, 1E-25, eps, 1000, n_runs);
	// }
	else if (alg.compare("NSSRK_errorSC") == 0) {
		x_sol = NSSRK_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("GSSRK_errorSC") == 0) {
		x_sol = GSSRK_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("GRK_errorSC") == 0) {
		x_sol = GRK_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_cyclic_errorSC") == 0) {
		x_sol = RK_cyclic_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_rand_errorSC") == 0) {
		x_sol = RK_rand_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_errorSC") == 0) {
		x_sol = RK_norep_rand_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_errorSC_copy") == 0) {
		x_sol = RK_norep_rand_csr_errorSC_copy(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_errorSC") == 0) {
		x_sol = RK_norep_rand_noshuffle_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_errorSC_copy") == 0) {
		x_sol = RK_norep_rand_noshuffle_csr_errorSC_copy(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_quasirand_errorSC") == 0) {
		x_sol = RK_quasirand_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_quasirand_sobol_errorSC") == 0) {
		x_sol = RK_quasirand_sobol_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_errorSC") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_csr_errorSC(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_errorSC_copy") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_csr_errorSC_copy(M, N, row_idx, cols, values_csr, b, x, 1E-25, eps, 1000, n_runs);
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