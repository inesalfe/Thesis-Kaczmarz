#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
#include <random>
using namespace std;

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int main (int argc, char *argv[]) {

	if(argc != 9) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/RKAB_single_seq_newSC_dist.exe <data_set> <n_runs> <eps> <M> <N> <threads> <it_per_thread> <max_it_stop>'" << endl;
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
	int threads = atoi(argv[6]);
	int it_per_thread = atoi(argv[7]);
	long long max_it_stop = atoll(argv[8]);

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
		cout << "'./bin/RKAB_single_seq_newSC_dist.exe <data_set> <n_runs> <eps> <M> <N> <it_per_thread>'" << endl;
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

	vector<discrete_distribution<>> dist(threads);
	vector<mt19937> gen(threads);

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* x_k_thread = new double[N];
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
	bool solution_found;

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		it = 0;
		solution_found = false;
        gen.clear();
        for (int i = 0; i < threads; i++) {
            gen[i] = mt19937(run*threads+i+1);
        }
        dist.clear();
        for (int i = 0; i < threads; i++) {
            dist[i] = discrete_distribution<>(sqrNorm_line.begin()+BLOCK_LOW(i, threads, M), sqrNorm_line.begin()+BLOCK_LOW(i, threads, M)+BLOCK_SIZE(i, threads, M));
        }
		start = omp_get_wtime();
		while(!solution_found) {
			it++;
			for (int i = 0; i < N; i++) {
				x_prev[i] = x_k[i];
				x_k[i] = 0;
			}
			for (int i = 0; i < threads; i++) {
				for (int j = 0; j < N; j++)
					x_k_thread[j] = x_prev[j];
				for (int k = 0; k < it_per_thread; k++) {
					line = BLOCK_LOW(i, it_per_thread, M)+dist[i](gen[i]);
					scale = (b[line]-dotProduct(A[line], x_k_thread, N))/sqrNorm_line[line];
					for (int j = 0; j < N; j++) {
						x_k_thread[j] += scale * A[line][j];
					}
				}
				for (int j = 0; j < N; j++) {
					x_k[j] += x_k_thread[j]/threads;
				}
			}
			if (it%max_it_stop == 0) {
				if (sqrNormDiff(x_k, x, N) < eps)
					solution_found = true;	
			}
		}	
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it;
	}
	avg_it /= n_runs;
	cout << M << " " << N << " " << duration << " " << avg_it << " ";

	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}

	double stop_total = omp_get_wtime();
	double duration_total = stop_total - start_total;

	cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration_total << endl;

	delete[] x_k;
	delete[] x_k_thread;
	delete[] x_prev;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	return 0;
}