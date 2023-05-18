#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <Eigen/Dense>

using Eigen::FullPivLU;
using Eigen::BDCSVD;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using namespace std;

// ./bin/params_dense.exe dense 4000 1000

// 1 1
// 2 3.75524
// 4 6.69156
// 8 10.9871
// 20 17.8699
// 50 23.845

int main(int argc, char *argv[]) {

	if(argc != 4) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/params_dense.exe <data_set> <M> <N>'" << endl;
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
		cout << "'./bin/params_dense.exe <M> <N>'" << endl;
		exit(1);
	}

	MatrixXd m(M,N);
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++)
				m(i,j) = A_matrix[i][j];

	delete[] A_matrix[0];
	delete[] A_matrix;
	delete[] b_vector;
	delete[] x_vector;

	BDCSVD<MatrixXd> svd(m);
    auto sigma = svd.singularValues();
    auto min_sing_val = sigma(sigma.size()-1);
    auto max_sing_val = sigma(0);
    cout << "min sing val(A): " << min_sing_val << endl;
    cout << "max sing val(A): " << max_sing_val << endl;
    auto norm = m.norm();
    cout << "norm(A): " << norm << endl;

    double s_min = (min_sing_val/norm)*(min_sing_val/norm);
    double s_max = (max_sing_val/norm)*(max_sing_val/norm);

    vector<int> q_values{1, 2, 4, 8, 20, 50};

    double q;
    double best_alpha;
    for (int q_idx = 0; q_idx < q_values.size(); q_idx++) {
    	q = q_values[q_idx];
    	if (s_max-s_min <= (1/(1-q))) {
    		best_alpha = q/(1+(q-1)*s_min);
    	}
    	else {
    		best_alpha = 2*q/(1+(q-1)*(s_min+s_max));
    	}
    	cout << q << " " << best_alpha << endl;
    }

	return 0;

}