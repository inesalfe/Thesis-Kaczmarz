#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <Eigen/Sparse>
#include <Eigen/IterativeLinearSolvers>

using Eigen::VectorXd;
using Eigen::LeastSquaresConjugateGradient;
using namespace std;

// https://eigen.tuxfamily.org/dox/classEigen_1_1ConjugateGradient.html

int main(int argc, char *argv[]) {

	if(argc != 5) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/cgls_eigen_find_it_newSC_csr.exe <data_set> <M> <N> <eps>'" << endl;
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

	double eps = atof(argv[4]);

	string matrix_type = argv[1];
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
	else if (matrix_type.compare("ls_sparse_csr") == 0) {
		string filename_row_idx = "../data/ls_sparse_csr/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_cols = "../data/ls_sparse_csr/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csr = "../data/ls_sparse_csr/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ls_sparse_csr/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ls_sparse_csr/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b_vector);
		importxVectorBIN(N, filename_x, x_vector);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/cgls_eigen_find_it_newSC_csr.exe <data_set> <M> <N> <eps>'" << endl;
		exit(1);
	}

	VectorXd b(M);
		for (int i = 0; i < M; i++)
			b(i) = b_vector[i];

	VectorXd x(N);
		for (int i = 0; i < N; i++)
			x(i) = x_vector[i];

	Eigen::SparseMatrix<double> m(M,N);
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

	LeastSquaresConjugateGradient<Eigen::SparseMatrix<double>> cgls;

	cgls.compute(m);

    VectorXd x_sol;
    int maxIt = 0;
    int error_code;
    double tol_init = cgls.tolerance();

    while(1) {

    	cgls.setMaxIterations(maxIt);

    	cgls.setTolerance(tol_init);
		x_sol = cgls.solve(b);

		error_code = cgls.info();

		if (error_code != 0) {
    		cgls.setTolerance(cgls.error());
			x_sol = cgls.solve(b);
			error_code = cgls.info();
		}

		if (error_code != 0) {
			maxIt++;
		}
		else {

			auto diff = x_sol - x;

			if(diff.squaredNorm() < eps)
				break;
			else
				maxIt++;

		}

    }

	auto diff = x_sol - x;
	auto res = m*x_sol-b;

	cout << M << " " << N << " " << maxIt << " " << diff.norm() << " " << res.norm() << endl;

	return 0;

}