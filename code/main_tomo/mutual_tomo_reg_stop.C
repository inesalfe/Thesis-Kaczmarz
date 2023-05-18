#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

// ./bin/mutual_tomo_reg_stop.exe ct_gaussian 19558 16384 3 200
// ?

// ./bin/mutual_tomo_reg_stop.exe ct_poisson 19558 16384 3 200
// ?

int main (int argc, char *argv[]) {

	if(argc != 6) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/mutual_tomo_reg_stop.exe <data_set> <M> <M> <seed> <max_it_stop>'" << endl;
		exit(1);
	}

	int NNZ;
	double* b;
	double* x;
	int* row_idx;
	int* cols;
	double* values_csr;

	int M = atoi(argv[2]);
	int N = atoi(argv[3]);
	int seed = atoi(argv[4]);
	long long max_it_stop = atoll(argv[5]);

	double start_total = omp_get_wtime();
	string matrix_type = argv[1];
	if (matrix_type.compare("ct_poisson") == 0) {
		string filename_row_idx = "../data/ct_poisson/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_cols = "../data/ct_poisson/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_values_csr = "../data/ct_poisson/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_b = "../data/ct_poisson/b_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_x = "../data/ct_poisson/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else if (matrix_type.compare("ct_gaussian") == 0) {
		string filename_row_idx = "../data/ct_gaussian/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_cols = "../data/ct_gaussian/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_values_csr = "../data/ct_gaussian/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_b = "../data/ct_gaussian/b_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_x = "../data/ct_gaussian/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/mutual_tomo_reg_stop.exe <data_set> <M> <M> <seed> <max_it_stop> <step_save>'" << endl;
		exit(1);
	}

	vector<double> sqrNorm_line(M);
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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_down = new double[N];
	double* x_up = new double[N];
	double* kacz_down = new double[N];
	double* kacz_up = new double[N];
	double* s_down = new double[N];
	double* s_up = new double[N];
	double scale;
	int line;
	long long it;
	double eps1 = 1E-4;
	double eps2 = 1E-4;
	double alpha;
	double beta;
	double M11;
	double M12;
	double M21;
	double M22;
	double B1;
	double B2;
	double det;
	double norm_x_down;
	double norm_x_up;
	double norm_x_diff;
	double cond11;
	double cond12;
	double cond2;
	
	for (int i = 0; i < N; i++) {
		x_down[i] = 0;
		x_up[i] = 0;
		kacz_down[i] = 0;
		kacz_up[i] = 0;
	}
	it = 0;
	double start = omp_get_wtime();
	for (int i = 0; i < M; i++) {
		line = i;
		scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_down))/sqrNorm_line[line];
		scaleVecLine(line, row_idx, cols, values_csr, scale, x_down);		
	}
	for (int i = 0; i < N; i++) {
		if (x_down[i] < 0)
			x_down[i] = 0;
	}
	for (int i = N-1; i >= 0; i--) {
		if (x_up[i] < 0)
			x_up[i] = 0;
	}
	for (int i = M; i >= 0; i--) {
		line = i;
		scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_up))/sqrNorm_line[line];
		scaleVecLine(line, row_idx, cols, values_csr, scale, x_up);		
	}
	for (int i = 0; i < N; i++) {
		kacz_down[i] = x_down[i];
		kacz_up[i] = x_up[i];
	}
	while(it < max_it_stop) {
		it++;
		for (int i = 0; i < M; i++) {
			line = i;
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_down))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values_csr, scale, x_down);		
		}
		for (int i = 0; i < N; i++) {
			if (x_down[i] < 0)
				x_down[i] = 0;
		}
		for (int i = N-1; i >= 0; i--) {
			if (x_up[i] < 0)
				x_up[i] = 0;
		}
		for (int i = M; i >= 0; i--) {
			line = i;
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_up))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values_csr, scale, x_up);		
		}
		for (int i = 0; i < N; i++) {
			s_down[i] = kacz_down[i]-x_down[i];
			s_up[i] = kacz_up[i]-x_up[i];
		}
		M11 = 0;
		M12 = 0;
		M22 = 0;
		B1 = 0;
		B2 = 0;
		norm_x_down = 0;
		norm_x_up = 0;
		norm_x_diff = 0;
		for (int i = 0; i < N; i++) {
			M11 += s_down[i]*s_down[i];
			M22 += s_up[i]*s_up[i];
			M12 += s_down[i]*s_up[i];
			B1 += s_down[i]*(x_down[i]-x_up[i]);
			B2 += s_up[i]*(x_down[i]-x_up[i]);
			norm_x_down += x_down[i]*x_down[i];
			norm_x_up += x_up[i]*x_up[i];
			norm_x_diff += (x_down[i]-x_up[i])*(x_down[i]-x_up[i]);
		}
		norm_x_down = sqrt(norm_x_down);
		norm_x_up = sqrt(norm_x_up);
		norm_x_diff = sqrt(norm_x_diff);
		B1 = -B1;
		M12 = -M12;
		M21 = M12;
		det = M11*M22-M12*M21;
		alpha = 1/det*(M22*B1-M12*B2);
		beta = 1/det*(-M21*B1+M11*B2);
		cond11 = abs(B1)/sqrt(M11)/norm_x_diff;
		cond12 = abs(B2)/sqrt(M22)/norm_x_diff;
		if (cond11 < eps1 && cond12 < eps1)
			break;
		cond2 = abs(alpha)*sqrt(M11)/norm_x_down + abs(beta)*sqrt(M22)/norm_x_up;
		if (cond2 < eps2)
			break;
		for (int i = 0; i < N; i++) {
			x_down[i] += alpha*s_down[i];
			x_up[i] += beta*s_up[i];
		}
	}
	double end = omp_get_wtime();

	double* x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0.5*(x_down[i]+x_up[i]);
	}
	cout << M << " " << N << " " << it << " " << end - start << " " << sqrt(sqrNormDiff(x_sol, x, N)) << endl;
	delete[] x_sol;

	delete[] x_down;
	delete[] x_up;
	delete[] kacz_down;
	delete[] kacz_up;
	delete[] s_down;
	delete[] s_up;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;

	return 0;
}