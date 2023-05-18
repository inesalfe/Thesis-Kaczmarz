#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <Eigen/Dense>
#include <Eigen/Sparse>

using Eigen::SparseQR;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using Eigen::SparseMatrix;
using namespace std;

int main(int argc, char *argv[]) {

	if(argc != 4) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/params_ct_error.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	int M;
	int N;
	int NNZ;
	int* row_idx;
	int* cols;
	double* values_csr;

	int it_max;
	double* b_vector;
	double* x_vector;

	M = atoi(argv[2]);
	N = atoi(argv[3]);

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("ct") == 0) {
		string filename_row_idx = "../data/ct/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_cols = "../data/ct/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csr = "../data/ct/values_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ct/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ct/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b_vector);
		importxVectorBIN(N, filename_x, x_vector);
	}
	else if (matrix_type.compare("ct_error") == 0) {
		string filename_row_idx = "../data/ct_error/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_cols = "../data/ct_error/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csr = "../data/ct_error/values_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ct_error/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ct_error/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b_vector);
		importxVectorBIN(N, filename_x, x_vector);
	}
	else if (matrix_type.compare("ct_gaussian") == 0) {
		string filename_row_idx = "../data/ct_gaussian/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_cols = "../data/ct_gaussian/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csr = "../data/ct_gaussian/values_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ct_gaussian/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ct_gaussian/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b_vector);
		importxVectorBIN(N, filename_x, x_vector);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/params_ct_error.exe <data_set> <M> <N>'" << endl;
		exit(1);
	}

	VectorXd b(M);
		for (int i = 0; i < M; i++)
			b(i) = b_vector[i];

	VectorXd x(N);
		for (int i = 0; i < N; i++)
			x(i) = x_vector[i];

	SparseMatrix<double> m(M,N);
	m.reserve(NNZ);
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < row_idx[i+1]-row_idx[i]; j++) {
			m.insert(i,cols[row_idx[i]+j]) = values_csr[row_idx[i]+j];
		}
	}
	m.makeCompressed();

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b_vector;
	delete[] x_vector;

	SparseQR<SparseMatrix<double>, Eigen::COLAMDOrdering<int> > qr_decomp(m);
	auto rank = qr_decomp.rank();
	cout << "Rank: " << rank << endl;
	qr_decomp.setPivotThreshold(1E-20);
	rank = qr_decomp.rank();
	cout << "Rank w/ tolerance 1E-20: " << rank << endl;

	return 0;

}