#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 4) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/normRows.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	int M;
	int N;
	double* b;
	double* x;
	double* x_sol;
	double** A;

	M = atoi(argv[2]);
	N = atoi(argv[3]);

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	string filename_output;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
		filename_output = "outputs/dense_row_norms_" + to_string(M) + "_" + to_string(N) + ".txt";
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
		filename_output = "outputs/dense_norm_row_norms_" + to_string(M) + "_" + to_string(N) + ".txt";
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/normRows.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	ofstream file(filename_output);
	if (!file.is_open()) {
		cout << "ERROR: Invalid output file for row norms." << endl;
		exit(1);
	}
	double sqrNorm_line;
	for (int i = 0; i < M; i++) {
		sqrNorm_line = sqrNorm(A[i], N);
		file << sqrt(sqrNorm_line) << endl;
	}
	file.close();

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}