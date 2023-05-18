#include "kacz.h"
#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 8) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/sparse_full.exe <method> <data_set> <n_runs> <eps> <M> <N> <den>'" << endl;
		exit(1);
	}

	int M;
	int N;
	int den;
	double* b;
	double* x;
	double* x_sol;
	double** A;

	int n_runs = atoi(argv[3]);
	double eps = atof(argv[4]);

	M = atoi(argv[5]);
	N = atoi(argv[6]);
	den = atoi(argv[7]);

	double start = omp_get_wtime();

	string matrix_type = argv[2];
	if (matrix_type.compare("sparse") == 0) {
		string filename_row_idx = "../data/sparse/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(den) + ".bin";
		string filename_cols = "../data/sparse/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(den) + ".bin";
		string filename_values_csr = "../data/sparse/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(den) + ".bin";
		string filename_b = "../data/sparse/b_" + to_string(M) + "_" + to_string(N) + "_" + to_string(den) + ".bin";
		string filename_x = "../data/sparse/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(den) + ".bin";
		importDenseMatrixSparseBIN(M, N, filename_row_idx, filename_cols, filename_values_csr, A);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/sparse_full.exe <method> <data_set> <n_runs> <eps> <M> <N> <den>'" << endl;
		exit(1);
	}

	string alg = argv[1];
	if (alg.compare("RK") == 0) {
		x_sol = RK(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("NSSRK") == 0) {
		x_sol = NSSRK(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("GSSRK") == 0) {
		x_sol = GSSRK(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("GRK") == 0) {
		x_sol = GRK(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_cyclic") == 0) {
		x_sol = RK_cyclic(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_rand") == 0) {
		x_sol = RK_rand(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand") == 0) {
		x_sol = RK_norep_rand(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_copy") == 0) {
		x_sol = RK_norep_rand_copy(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle") == 0) {
		x_sol = RK_norep_rand_noshuffle(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_copy") == 0) {
		x_sol = RK_norep_rand_noshuffle_copy(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_quasirand") == 0) {
		x_sol = RK_quasirand(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_quasirand_sobol") == 0) {
		x_sol = RK_quasirand_sobol(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_copy") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_copy(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_errorSC") == 0) {
		x_sol = RK_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("NSSRK_errorSC") == 0) {
		x_sol = NSSRK_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("GSSRK_errorSC") == 0) {
		x_sol = GSSRK_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("GRK_errorSC") == 0) {
		x_sol = GRK_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_cyclic_errorSC") == 0) {
		x_sol = RK_cyclic_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_rand_errorSC") == 0) {
		x_sol = RK_rand_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_errorSC") == 0) {
		x_sol = RK_norep_rand_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_errorSC_copy") == 0) {
		x_sol = RK_norep_rand_errorSC_copy(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_errorSC") == 0) {
		x_sol = RK_norep_rand_noshuffle_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_errorSC_copy") == 0) {
		x_sol = RK_norep_rand_noshuffle_errorSC_copy(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_quasirand_errorSC") == 0) {
		x_sol = RK_quasirand_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_quasirand_sobol_errorSC") == 0) {
		x_sol = RK_quasirand_sobol_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_errorSC") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_errorSC(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_errorSC_copy") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_errorSC_copy(M, N, A, b, x, 1E-25, eps, 1000, n_runs);
	}
	else {
		cout << "Error: Invalid algorithm." << endl;
		delete[] A[0];
		delete[] A;
		delete[] b;
		delete[] x;
		return 0;
	}

	double stop = omp_get_wtime();
	auto duration = stop - start;
	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration << endl;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}
