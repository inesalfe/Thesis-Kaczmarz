#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <math.h>
#include <omp.h>
#include <random>
#include <algorithm>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 6) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RK_csr_seq_uni_max_it.exe <data_set> <n_runs> <M> <N> <max_it_stop>'" << endl;
		exit(1);
	}

	int NNZ;
	double* b;
	double* x;
	double* x_sol;
	int* row_idx;
	int* cols;
	double* values_csr;

	int n_runs = atoi(argv[2]);

	int M = atoi(argv[3]);
	int N = atoi(argv[4]);
	long long max_it_stop = atoll(argv[5]);

	double start_total = omp_get_wtime();

	string matrix_type = argv[1];
	if (matrix_type.compare("dense") == 0) {
		string filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixDenseBIN(filename_A, M, N, NNZ, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		string filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixDenseBIN(filename_A, M, N, NNZ, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else if (matrix_type.compare("ct") == 0) {
		string filename_row_idx = "../data/ct/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_cols = "../data/ct/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_values_csr = "../data/ct/values_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_b = "../data/ct/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		string filename_x = "../data/ct/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RK_csr_uni_max_it.exe <data_set> <n_runs> <M> <N> <max_it_stop>'" << endl;
		exit(1);
	}

	double* sqrNorm_line = new double[M];
	double sqr_matrixNorm = 0;
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values_csr);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values_csr;
			delete[] b;
			delete[] x;
			exit(1);
		}
		sqr_matrixNorm += sqrNorm_line[i];
	}

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	double* x_k = new double[N];
	x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	long long it;

	double start; 
	double stop;
	double duration = 0;
	
	double dot_p;

	int* row_idx_shuffle = new int[M+1];
	int* cols_shuffle = new int[row_idx[M]];
	double* values_shuffle = new double[row_idx[M]];

	double* b_shuffle = new double[M];
	double* sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		shuffle(begin(samp_line), end(samp_line), rng);
		reorderRows(M, N, samp_line, row_idx, cols, values_csr, row_idx_shuffle, cols_shuffle, values_shuffle);
		for (int i = 0; i < M; i++) {
			b_shuffle[i] = b[samp_line[i]];
			sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
		}
		it = 0;
		start = omp_get_wtime();
		while(it < max_it_stop) {
			it++;
			line = it%M;
			scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k))/sqrNorm_line_shuffle[line];
			scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k);
		}
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
	} 
	cout << M << " " << N << " " << duration << " " << max_it_stop << " ";

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration_total << endl;

	delete[] x_k;

	delete[] row_idx_shuffle;
	delete[] cols_shuffle;
	delete[] values_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] b;
	delete[] x;
	delete[] x_sol;
	delete[] sqrNorm_line;

	return 0;
}
