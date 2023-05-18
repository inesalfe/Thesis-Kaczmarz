#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <Eigen/Dense>

using Eigen::FullPivLU;
using Eigen::BDCSVD;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using namespace std;

int main(int argc, char *argv[]) {

	if(argc != 4) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/params_ct.exe <data_set> <M> <N>'" << endl;
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
	if (matrix_type.compare("ct") == 0) {
		filename_A = "../data/ct/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/ct/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/ct/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A_matrix, b_vector, x_vector);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/params_ct.exe <M> <N>'" << endl;
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

	FullPivLU<MatrixXd> lu_decomp(m);
	auto rank = lu_decomp.rank();
	cout << "Rank: " << rank << endl;
	lu_decomp.setThreshold(1e-20);
	rank = lu_decomp.rank();
	cout << "Rank w/ tolerance 1E-20: " << rank << endl;

	BDCSVD<MatrixXd> svd(m);
    auto sigma = svd.singularValues();
    auto min_sing_val = sigma(sigma.size()-1);
    auto max_sing_val = sigma(0);
    cout << "min sing val(A): " << min_sing_val << endl;
    cout << "max sing val(A): " << max_sing_val << endl;

    cout << "cond(A): " << max_sing_val/min_sing_val << endl;
    cout << "cond(A, 'fro'): " << m.norm()/min_sing_val << endl;

    cout << "norm(b): " << b.norm() << endl;

    auto res = m*x-b;
    cout << "norm(r): " << res.norm() << endl;
    cout << "norm(r)/norm(b): " << res.norm()/b.norm() << endl;

    auto horizon = res.norm()/min_sing_val;

    cout << "Horizon: " << horizon << endl;

	return 0;

}