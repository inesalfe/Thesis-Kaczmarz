#include "aux_func.h"
#include "csr.h"
#include <iostream>
#include <algorithm>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int main (int argc, char *argv[]) {

	if(argc != 10) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_csr_uni_newSC.exe <data_set> <n_runs> <eps> <M> <N> <it_per_thread> <max_it_stop> <blocks> <block_repeat>'" << endl;
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
	double eps = atof(argv[3]);

	int M = atoi(argv[4]);
	int N = atoi(argv[5]);
	int it_per_thread = atoi(argv[6]);
	long long max_it_stop = atoll(argv[7]);
	int blocks = atoi(argv[8]);
	int block_repeat = atoi(argv[9]);

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
		cout << "'./bin/RKAB_csr_uni_newSC.exe <data_set> <n_runs> <eps> <M> <N> <it_per_thread> <max_it_stop> <blocks> <block_repeat>'" << endl;
		exit(1);
	}

	double* sqrNorm_line = new double[M];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	double* x_k = new double[N];
	double* x_k_thread;
	double* x_k_block;
	x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	long long it;
	double norm_dif;
	double dif;

	double start; 
	double stop;
	double duration = 0;

	int t_id;
	int num_threads;

	long long avg_it = 0;
	long long it_final;
	bool solution_found;

	#pragma omp parallel
	{
		#pragma omp single
			num_threads = omp_get_num_threads();
	}

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
		it = -1;
		solution_found = false;
		start = omp_get_wtime();
		#pragma omp parallel private(line, scale, t_id, x_k_thread, x_k_block) firstprivate(it)
		{
			x_k_thread = new double[N];
			x_k_block = new double[N];
			t_id = omp_get_thread_num();
			int low_block_id = BLOCK_LOW(t_id, num_threads, blocks);
			int size_blocks = BLOCK_SIZE(t_id, num_threads, blocks);
			while(!solution_found) {
				it++;
				#pragma omp barrier
				for (int block_it = 0; block_it < size_blocks; block_it++) {
					line = BLOCK_LOW(low_block_id+block_it, blocks, M) + (it*it_per_thread)%BLOCK_SIZE(low_block_id+block_it, blocks, M);
					scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k))/sqrNorm_line_shuffle[line];
					scaleNewVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k, x_k_block);
					for (int i = 1; i < it_per_thread; i++) {
						line = BLOCK_LOW(low_block_id+block_it, blocks, M) + (it*it_per_thread+i)%BLOCK_SIZE(low_block_id+block_it, blocks, M);
						scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k_block))/sqrNorm_line_shuffle[line];
						scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k_block);
					}
					for (int n = 0; n < block_repeat-1; n++) {
						for (int i = 0; i < it_per_thread; i++) {
							line = BLOCK_LOW(low_block_id+block_it, blocks, M) + (it*it_per_thread+i)%BLOCK_SIZE(low_block_id+block_it, blocks, M);
							scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k_block))/sqrNorm_line_shuffle[line];
							scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k_block);
						}
					}
					if (block_it == 0)
						for (int i = 0; i < N; i++) {
							x_k_thread[i] = (x_k_block[i] - x_k[i])/blocks;
						}
					else
						for (int i = 0; i < N; i++) {
							x_k_thread[i] += (x_k_block[i] - x_k[i])/blocks;
						}
				}
				#pragma omp barrier
				#pragma omp critical
			    	for (int i = 0; i < N; i++)
			            x_k[i] += x_k_thread[i];
				if (it%max_it_stop == 0) {
					#pragma omp single
						norm_dif = 0;
					#pragma omp for reduction(+:norm_dif)
						for (int i = 0; i < N; i++) {
							dif = x_k[i] - x[i];
							norm_dif += dif*dif;
						}
					#pragma omp single
						if (norm_dif < eps) {
							it_final = it;
							solution_found = true;
						}
				}
			}
			delete[] x_k_thread;
			delete[] x_k_block;
		}	
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it_final;
	}
	avg_it /= n_runs;
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration_total << endl;

	delete[] row_idx_shuffle;
	delete[] cols_shuffle;
	delete[] values_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;

	delete[] row_idx;
	delete[] cols;
	delete[] values_csr;
	delete[] b;
	delete[] x;
	delete[] x_sol;
	delete[] sqrNorm_line;

	return 0;
}
