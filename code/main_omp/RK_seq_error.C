#include "aux_func.h"
#include <iostream>
#include <iterator>
#include <fstream>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RK_seq_error.exe <data_set> <n_runs> <eps> <M> <N> <max_it_stop>'" << endl;
		exit(1);
	}

	double* b;
	double* x;
	double* x_sol;
	double** A;

	int n_runs = atoi(argv[2]);
	double eps = atof(argv[3]);

	int M = atoi(argv[4]);
	int N = atoi(argv[5]);
	long long max_it_stop = atoll(argv[6]);

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else if (matrix_type.compare("dense_rand") == 0) {
		filename_A = "../data/dense_rand/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_rand/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_rand/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RK_seq_error.exe <data_set> <n_runs> <eps> <M> <N> <max_it_stop>'" << endl;
		exit(1);
	}

	double start_total = omp_get_wtime();

	importDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);

	vector<double> sqrNorm_line(M);
	double sqr_matrixNorm = 0;
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
		sqr_matrixNorm += sqrNorm_line[i];
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
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
	
	long long avg_it = 0;
	int max_it = 0;

	bool solution_found;
	double norm_dif;
	double sqr_norm_res;
	double dif;
	double dot_p;

	vector<vector<double>> error;
	vector<double> error_curr;
	for(int run = 0; run < n_runs; run++) {
		error_curr.clear();
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		mt19937 generator(run+1);
		it = 0;
		solution_found = false;
		start = omp_get_wtime();
		while(!solution_found) {
			it++;
			line = dist(generator);
			dot_p = 0;
			for (int i = 0; i < N; i++)
				dot_p += A[line][i]*x_k[i];
			scale = (b[line]-dot_p)/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%max_it_stop == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			// error_curr.push_back(sqrt(sqrNormDiff(x_k, x, N))/sqrt(sqrNorm(x, N)));
			error_curr.push_back(sqrt(sqrNormDiff(x_k, x, N)));
			if (it%max_it_stop == 0) {
				norm_dif = 0;
				for (int i = 0; i < N; i++) {
					dif = x_k[i] - x_prev[i];
					norm_dif += dif*dif;
				}
				if (norm_dif < 1E-25) {
					for (int i = 0; i < M; i++) {
						res[i] = b[i] - dotProduct(A[i], x_k, N);
					}
					sqr_norm_res = 0;
					for (int i = 0; i < M; i++)
						sqr_norm_res += res[i]*res[i];
					if (sqr_norm_res < eps) {
						solution_found = true;

					}
				}
			}
		}
		stop = omp_get_wtime();
		duration += stop - start;
		if (it > max_it)
			max_it = it;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it;
		error.push_back(error_curr);
	} 
	avg_it /= n_runs;
	cout << M << " " << N << " " << duration << " " << avg_it << " ";

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}

	for (int i = 0; i < n_runs; i++) {
		error[i].resize(max_it,-1);
	}
	error_curr.clear();
	error_curr.resize(max_it,0);
	int el;
	for (int i = 0; i < max_it; i++) {
		el = 0;
		for (int j = 0; j < n_runs; j++) {
			if(error[j][i] != -1) {
				error_curr[i] += error[j][i];
				el++;
			}
		}
		error_curr[i] /= el;
	}
	string filename_error = "errors/RK_converg_" + to_string(M) + "_" + to_string(N) + ".txt";
	ofstream output_file(filename_error);
	ostream_iterator<double> output_iterator(output_file, "\n");
	copy(error_curr.begin(), error_curr.end(), output_iterator);
	for (int i = 0; i < error.size(); i++)
		error[i].clear();
	error.clear();
	error_curr.clear();

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration_total << endl;

	delete[] x_k;
	delete[] x_prev;
	delete[] res;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}