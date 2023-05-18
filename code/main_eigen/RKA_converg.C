#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include <Eigen/Dense>

using Eigen::FullPivLU;
using Eigen::BDCSVD;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using namespace std;

// ./bin/RKA_converg.exe dense 4000 1000

int main(int argc, char *argv[]) {

	if(argc != 4) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_converg.exe <data_set> <M> <N>'" << endl;
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
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A_matrix, b_vector, x_vector);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_converg.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	MatrixXd m(M,N);
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++)
				m(i,j) = A_matrix[i][j];

	// VectorXd b(M);
	// 	for (int i = 0; i < M; i++)
	// 		b(i) = b_vector[i];

	// VectorXd x(N);
	// 	for (int i = 0; i < N; i++)
	// 		x(i) = x_vector[i];

	delete[] A_matrix[0];
	delete[] A_matrix;
	delete[] b_vector;
	delete[] x_vector;

	cout << "Sqr norm A: " << m.squaredNorm() << endl;

	MatrixXd A_t_A = m.transpose()*m;
	MatrixXd A_A_t = m*m.transpose();

	double norm = m.squaredNorm();

	MatrixXd i_n = MatrixXd::Identity(N, N);
	MatrixXd i_m = MatrixXd::Identity(M, M);

	MatrixXd temp1 = A_t_A/norm/norm;
	MatrixXd temp2 = A_A_t/norm/norm;

	double max_el = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (temp1(i,j) > max_el)
				max_el = temp1(i,j);
		}
	}

	cout << "max1: " << max_el;

	max_el = 0;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < M; j++) {
			if (temp2(i,j) > max_el)
				max_el = temp2(i,j);
		}
	}

	MatrixXd m1 = (i_n-temp1)*(i_n-temp1);
	MatrixXd m2 = m.transpose()/norm*(i_m-temp2)*m/norm;

	cout << " max2: " << max_el << endl;

	for (int q = 1; q < 20; q++) {

		MatrixXd full_matrix = m1 + 1/q*m2;

		BDCSVD<MatrixXd> svd(full_matrix);
	    VectorXd sigma = svd.singularValues();
	    cout << "max sing val(A): " << sigma(0) << endl;

	}

	return 0;

}