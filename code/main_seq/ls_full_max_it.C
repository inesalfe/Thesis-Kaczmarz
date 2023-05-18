#include "kacz.h"
#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/ls_full_max_it.exe <method> <data_set> <n_runs> <M> <N> <max_it>'" << endl;
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

	M = atoi(argv[4]);
	N = atoi(argv[5]);

	int max_it = atoi(argv[6]);

	double start = omp_get_wtime();

	string matrix_type = argv[2];
	if (matrix_type.compare("ls_dense_norm") == 0) {
		string filename_A = "../data/ls_dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ls_dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ls_dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("ls_dense") == 0) {
		string filename_A = "../data/ls_dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ls_dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ls_dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/ls_full_max_it.exe <method> <data_set> <n_runs> <M> <N> <max_it>'" << endl;
		exit(1);
	}

	string alg = argv[1];
	if (alg.compare("REK_max_it") == 0) {
		x_sol = REK_max_it(M, N, A, b, x, max_it, n_runs);
	}
	else if (alg.compare("RGS_max_it") == 0) {
		x_sol = RGS_max_it(M, N, A, b, x, max_it, n_runs);
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
