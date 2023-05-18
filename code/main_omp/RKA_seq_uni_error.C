#include "aux_func.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

// ./bin/RKA_seq_uni_error.exe ls_dense 4000 1000 1 30000 1000
// ./bin/RKA_seq_uni_error.exe ls_dense 4000 1000 2 30000 1000
// ./bin/RKA_seq_uni_error.exe ls_dense 4000 1000 4 30000 1000
// ./bin/RKA_seq_uni_error.exe ls_dense 4000 1000 8 30000 1000
// ./bin/RKA_seq_uni_error.exe ls_dense 4000 1000 20 30000 1000
// ./bin/RKA_seq_uni_error.exe ls_dense 4000 1000 50 30000 1000
// ./bin/RKA_seq_uni_error.exe ls_dense 4000 1000 100 30000 1000
// ./bin/RKA_seq_uni_error.exe ls_dense 4000 1000 1000 30000 1000

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_seq_uni_error.exe <data_set> <M> <N> <threads> <max_it_stop> <step_save>'" << endl;
		exit(1);
	}

	double* b;
	double* x;
	double* x_sol;
	double** A;

	int M = atoi(argv[2]);
	int N = atoi(argv[3]);
	int threads = atoi(argv[4]);
	long long max_it_stop = atoll(argv[5]);
	int step_save = atoi(argv[6]);

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("ls_dense") == 0) {
		filename_A = "../data/ls_dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/ls_dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/ls_dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKA_seq_uni_error.exe <data_set> <M> <N> <threads> <max_it_stop> <step_save>'" << endl;
		exit(1);
	}

	double start_total = omp_get_wtime();

	importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);

	vector<double> sqrNorm_line(M);
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNorm(A[i], N);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] A[0];
			delete[] A;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	double* x_k = new double[N];
	double* x_prev = new double[N];
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

	vector<double> error;
	vector<double> res;
	vector<int> error_it;
	vector<int> res_it;
	double* res_vec = new double[M];
	double sqr_norm_res;

	shuffle(begin(samp_line), end(samp_line), rng);
	for (int i = 0; i < N; i++) {
		x_k[i] = 0;
	}
	it = -1;
	start = omp_get_wtime();
	while(it < max_it_stop) {
		it++;
		for (int i = 0; i < N; i++) {
			x_prev[i] = x_k[i];
		}
		for (int i = 0; i < threads; i++) {
			line = samp_line[(threads*it+i)%M];
			scale = (b[line]-dotProduct(A[line], x_prev, N))/sqrNorm_line[line];
			for (int j = 0; j < N; j++) {
				x_k[j] += (scale * A[line][j])/threads;
			}
		}
		if (it%step_save == 0) {
			error_it.push_back(it);
			error.push_back(sqrt(sqrNormDiff(x_k, x, N)));
			for (int i = 0; i < M; i++) {
				res_vec[i] = b[i] - dotProduct(A[i], x_k, N);
			}
			sqr_norm_res = 0;
			for (int i = 0; i < M; i++)
				sqr_norm_res += res_vec[i]*res_vec[i];
			res_it.push_back(it);
			res.push_back(sqrt(sqr_norm_res));
		}
	}
	stop = omp_get_wtime();
	duration += stop - start;
	for (int i = 0; i < N; i++) {
		x_sol[i] += x_k[i];
	}

	cout << M << " " << N << " " << duration << " " << max_it_stop << " ";

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	string filename_error = "errors/seq/RKA_uni_ls_error_" + to_string(M) + "_" + to_string(N) + "_" + to_string(threads) + ".txt";
	string filename_res = "errors/seq/RKA_uni_ls_res_" + to_string(M) + "_" + to_string(N) + "_" + to_string(threads) + ".txt";

	ofstream file_error(filename_error);
	ofstream file_res(filename_res);
	if (file_error.is_open() && file_res.is_open()) {
		for (int i = 0; i < error.size(); i++) {
			file_error << error_it[i] << " " << error[i] << endl;
			file_res << res_it[i] << " " << res[i] << endl;
		}
		file_error.close();
		file_res.close();
	}
	else {
		cout << "ERROR: Invalid input file for error or residual output file." << endl;
		exit(1);
	}

	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration_total << endl;

	delete[] x_k;
	delete[] x_prev;
	delete[] res_vec;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}
