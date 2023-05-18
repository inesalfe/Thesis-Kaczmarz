#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int main (int argc, char *argv[]) {

	if(argc != 7) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RK_csr_partial_block_max_it.exe <data_set> <n_runs> <M> <N> <it_per_thread> <max_it_stop>'" << endl;
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
	int it_per_thread = atoi(argv[5]);
	long long max_it_stop = atoll(argv[6]);

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
		cout << "'./bin/RK_csr_partial_block_max_it.exe <data_set> <n_runs> <M> <N> <it_per_thread>'" << endl;
		exit(1);
	}

	vector<double> sqrNorm_line(M);
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
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

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

	long long avg_it = 0;

	int t_id;
	int num_threads;

	#pragma omp parallel
	{
		#pragma omp single
			num_threads = omp_get_num_threads();
	}

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		it = 0;
		start = omp_get_wtime();
		#pragma omp parallel private(line, scale, t_id) firstprivate(it)
		{
			t_id = omp_get_thread_num();
			mt19937 generator(run*num_threads+t_id+1);
			while(it < max_it_stop) {
				it++;
				for (int i = 0; i < it_per_thread; i++) {
					line = dist(generator);
					scale = (b[line]-dotProductCSR(line, row_idx, cols, values_csr, x_k))/sqrNorm_line[line];
					scaleVecLinePartial(line, BLOCK_LOW(t_id, num_threads, N), BLOCK_HIGH(t_id, num_threads, N), row_idx, cols, values_csr, scale, x_k);
				}
			}
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

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}
