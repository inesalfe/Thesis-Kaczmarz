#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <Eigen/Dense>

using Eigen::FullPivLU;
using Eigen::BDCSVD;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using namespace std;

// ./bin/sing_vals.exe square_dense_gravity 1000 1000
// ./bin/sing_vals.exe square_dense_phillips 1000 1000
// ./bin/sing_vals.exe square_dense_shaw 1000 1000

int main(int argc, char *argv[]) {

	if(argc != 4) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/sing_vals.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	int M;
	int N;
	double** A_matrix;
	double* b_vector;
	double* x_vector;

	M = atoi(argv[2]);
	N = atoi(argv[3]);

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	string filename;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A_matrix, b_vector, x_vector);
   		filename = "outputs/eigen/sing_vals_dense_" + to_string(M) + "_" + to_string(N) + ".txt";
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A_matrix, b_vector, x_vector);
   		filename = "outputs/eigen/sing_vals_dense_norm_" + to_string(M) + "_" + to_string(N) + ".txt";
	}
	else if (matrix_type.compare("sparse_real") == 0) {
		filename_A = "../data/sparse_real/A_" + to_string(M) + "_" + to_string(N) + ".mtx";
		filename_b = "../data/sparse_real/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/sparse_real/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseMatrixMTX(M, N, filename_A, A_matrix);
		importbVectorBIN(M, filename_b, b_vector);
		importxVectorBIN(N, filename_x, x_vector);
   		filename = "outputs/eigen/sing_vals_sparse_real_" + to_string(M) + "_" + to_string(N) + ".txt";
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/sing_vals.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	MatrixXd m(M,N);
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++)
				m(i,j) = A_matrix[i][j];

	VectorXd b(M);
		for (int i = 0; i < M; i++)
			b(i) = b_vector[i];

	VectorXd x(N);
		for (int i = 0; i < N; i++)
			x(i) = x_vector[i];

	delete[] A_matrix[0];
	delete[] A_matrix;
	delete[] b_vector;
	delete[] x_vector;

	BDCSVD<MatrixXd> svd(m);
    auto sigma = svd.singularValues();

	ofstream file(filename);
	if (!file.is_open()) {
		cout << "ERROR: Invalid input file to write singular values." << endl;
		exit(1);
	}
	for (int i = 0; i < sigma.size(); i++) {
		file << sigma[i] << endl;
	}
	file.close();

	return 0;

}