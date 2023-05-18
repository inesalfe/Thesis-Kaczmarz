#include "kacz.h"
#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 8) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/rand_full.exe <method> <data_set> <n_runs> <eps> <M> <N> <step_sc>'" << endl;
		exit(1);
	}

	int M;
	int N;
	double* b;
	double* x;
	double* x_sol;
	double** A;

	int n_runs = atoi(argv[3]);
	double eps = atof(argv[4]);

	M = atoi(argv[5]);
	N = atoi(argv[6]);
	int step_sc = atoi(argv[7]);

	double start = omp_get_wtime();

	string matrix_type = argv[2];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("dense_rand") == 0) {
		filename_A = "../data/dense_rand/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_rand/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_rand/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("dense_coherent") == 0) {
		filename_A = "../data/dense_coherent/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_coherent/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_coherent/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("ct") == 0) {
		filename_A = "../data/ct/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/ct/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/ct/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("sparse_real") == 0) {
		filename_A = "../data/sparse_real/A_" + to_string(M) + "_" + to_string(N) + ".mtx";
		filename_b = "../data/sparse_real/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/sparse_real/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseMatrixMTX(M, N, filename_A, A);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/rand_full.exe <method> <data_set> <n_runs> <eps> <M> <N>'" << endl;
		exit(1);
	}

	string alg = argv[1];
	if (alg.compare("RK") == 0) {
		x_sol = RK(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("NSSRK") == 0) {
		x_sol = NSSRK(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("GSSRK") == 0) {
		x_sol = GSSRK(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("GRK") == 0) {
		x_sol = GRK(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("REK") == 0) {
		x_sol = REK(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RGS") == 0 && M >= N) {
		x_sol = RGS(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_cyclic") == 0) {
		x_sol = RK_cyclic(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_rand") == 0) {
		x_sol = RK_rand(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_rand") == 0) {
		x_sol = RK_norep_rand(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_rand_copy") == 0) {
		x_sol = RK_norep_rand_copy(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle") == 0) {
		x_sol = RK_norep_rand_noshuffle(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_copy") == 0) {
		x_sol = RK_norep_rand_noshuffle_copy(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_quasirand") == 0) {
		x_sol = RK_quasirand(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_quasirand_sobol") == 0) {
		x_sol = RK_quasirand_sobol(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_copy") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_copy(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_errorSC") == 0) {
		x_sol = RK_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("NSSRK_errorSC") == 0) {
		x_sol = NSSRK_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("GSSRK_errorSC") == 0) {
		x_sol = GSSRK_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("GRK_errorSC") == 0) {
		x_sol = GRK_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("REK_errorSC") == 0) {
		x_sol = REK_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RGS_errorSC") == 0 && M >= N) {
		x_sol = RGS_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_cyclic_errorSC") == 0) {
		x_sol = RK_cyclic_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_rand_errorSC") == 0) {
		x_sol = RK_rand_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_rand_errorSC") == 0) {
		x_sol = RK_norep_rand_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_rand_errorSC_copy") == 0) {
		x_sol = RK_norep_rand_errorSC_copy(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_errorSC") == 0) {
		x_sol = RK_norep_rand_noshuffle_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_rand_noshuffle_errorSC_copy") == 0) {
		x_sol = RK_norep_rand_noshuffle_errorSC_copy(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_quasirand_errorSC") == 0) {
		x_sol = RK_quasirand_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_quasirand_sobol_errorSC") == 0) {
		x_sol = RK_quasirand_sobol_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_errorSC") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_errorSC(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
	}
	else if (alg.compare("RK_norep_quasirand_sobol_noshuffle_errorSC_copy") == 0) {
		x_sol = RK_norep_quasirand_sobol_noshuffle_errorSC_copy(M, N, A, b, x, 1E-25, eps, step_sc, n_runs);
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
