#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

// ./bin/mutual_tomo_reg.exe ct_gaussian 19558 16384 1 50 1
// ./bin/mutual_tomo_reg.exe ct_gaussian 19558 16384 2 50 1
// ./bin/mutual_tomo_reg.exe ct_gaussian 19558 16384 3 50 1
// ./bin/mutual_tomo_reg.exe ct_gaussian 19558 16384 4 50 1

// ./bin/mutual_tomo_reg.exe ct_poisson 19558 16384 1 50 1
// ./bin/mutual_tomo_reg.exe ct_poisson 19558 16384 2 50 1
// ./bin/mutual_tomo_reg.exe ct_poisson 19558 16384 3 50 1
// ./bin/mutual_tomo_reg.exe ct_poisson 19558 16384 4 50 1

// ./bin/mutual_tomo_reg.exe ct_gaussian 19558 16384 1 200 1
// ./bin/mutual_tomo_reg.exe ct_gaussian 19558 16384 2 200 1
// ./bin/mutual_tomo_reg.exe ct_gaussian 19558 16384 3 200 1
// ./bin/mutual_tomo_reg.exe ct_gaussian 19558 16384 4 200 1

// ./bin/mutual_tomo_reg.exe ct_poisson 19558 16384 1 200 1
// ./bin/mutual_tomo_reg.exe ct_poisson 19558 16384 2 200 1
// ./bin/mutual_tomo_reg.exe ct_poisson 19558 16384 3 200 1
// ./bin/mutual_tomo_reg.exe ct_poisson 19558 16384 4 200 1

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/mutual_tomo_reg.exe <data_set> <M> <M> <seed> <max_it_stop> <step_save>'" << endl;
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
	int step_save = atoi(argv[6]);

	double start_total = omp_get_wtime();
	string matrix_type = argv[1];
	string output_foler;
	if (matrix_type.compare("ct_poisson") == 0) {
		string filename_row_idx = "../data/ct_poisson/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_cols = "../data/ct_poisson/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_values_csr = "../data/ct_poisson/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_b = "../data/ct_poisson/b_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		string filename_x = "../data/ct_poisson/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + ".bin";
		output_foler = "errors/tomo_poisson_reg/";
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
		output_foler = "errors/tomo_gauss_reg/";
		importCSRMatrixSparseBIN(M, N, NNZ, filename_row_idx, filename_cols, filename_values_csr, row_idx, cols, values_csr);
		importbVectorBIN(M, filename_b, b);
		importxVectorBIN(N, filename_x, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/mutual_tomo_reg.exe <data_set> <M> <M> <seed> <max_it_stop> <step_save>'" << endl;
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
	double* x_sol = new double[N];
	double* res = new double[M+N];
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

	string filename_error = output_foler + "mutual_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_error(filename_error);
	if (!file_error.is_open()) {
		cout << "ERROR: Invalid input file for error output file." << endl;
		exit(1);
	}

	string filename_res = output_foler + "mutual_res_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_res(filename_res);
	if (!file_res.is_open()) {
		cout << "ERROR: Invalid input file for residual output file." << endl;
		exit(1);
	}

	string filename_cond11 = output_foler + "mutual_cond11_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_cond11(filename_cond11);
	if (!file_cond11.is_open()) {
		cout << "ERROR: Invalid input file for error gauge output file." << endl;
		exit(1);
	}

	string filename_cond12 = output_foler + "mutual_cond12_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_cond12(filename_cond12);
	if (!file_cond12.is_open()) {
		cout << "ERROR: Invalid input file for error gauge output file." << endl;
		exit(1);
	}

	string filename_cond2 = output_foler + "mutual_cond2_" + to_string(M) + "_" + to_string(N) + "_" + to_string(seed) + "_" + to_string(max_it_stop) + ".txt";
	ofstream file_cond2(filename_cond2);
	if (!file_cond2.is_open()) {
		cout << "ERROR: Invalid input file for error gauge output file." << endl;
		exit(1);
	}
	
	for (int i = 0; i < N; i++) {
		x_down[i] = 0;
		x_up[i] = 0;
		kacz_down[i] = 0;
		kacz_up[i] = 0;
	}
	it = 0;
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
		file_cond11 << it << " " << cond11 << endl;
		file_cond12 << it << " " << cond12 << endl;
		cond2 = abs(alpha)*sqrt(M11)/norm_x_down + abs(beta)*sqrt(M22)/norm_x_up;
		file_cond2 << it << " " << cond2 << endl;
		for (int i = 0; i < N; i++) {
			x_down[i] += alpha*s_down[i];
			x_up[i] += beta*s_up[i];
		}
		if (it%step_save == 0) {
			for (int i = 0; i < N; i++) {
				x_sol[i] = 0.5*(x_up[i]+x_down[i]);
			}
			for (int i = 0; i < M; i++) {
				res[i] = b[i] - dotProductCSR(i, row_idx, cols, values_csr, x_sol);
			}
			for (int i = 0; i < N; i++) {
				if (x_sol[i] < 0)
					res[M+i] = x_sol[i];
				else
					res[M+i] = 0;
			}
			file_res << it << " " << sqrt(sqrNorm(res, M+N)) << endl;
			file_error << it << " " << sqrt(sqrNormDiff(x_sol, x, N)) << endl;
		}
	}
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0.5*(x_up[i]+x_down[i]);
	}
	file_res.close();
	file_error.close();

	delete[] x_down;
	delete[] x_up;
	delete[] kacz_down;
	delete[] kacz_up;
	delete[] s_down;
	delete[] s_up;
	delete[] x_sol;
	delete[] res;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;

	return 0;
}