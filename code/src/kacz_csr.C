#include "kacz_csr.h"
#include "aux_func.h"
#include "csr.h"
#include "csc.h"
#include "sobol.h"
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <random>
#include <omp.h>
using namespace std;

double* RK_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	vector<double> sqrNorm_line(M);
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = dist(generator);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* NSSRK_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	vector<double> sqrNorm_line(M);
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	int old_line;
	long long it;

	double start;
	double stop;
	double duration = 0;		
	long long avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		old_line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			old_line = line;
			line = dist(generator);
			while (line == old_line) {
				line = dist(generator);
			}
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* GSSRK_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	vector<double> sqrNorm_line(M);
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double** G = new double*[M];
	int index_1;
	int index_2;
	for (size_t i = 0; i < M; i++) {
		G[i] = new double[M];
		for (int j = 0; j < M; j++) {
			G[i][j] = 0;
			index_1 = row_idx[i];
			index_2 = row_idx[j];
			while(index_1 < row_idx[i+1] && index_2 < row_idx[j+1]) {
				if (cols[index_1] < cols[index_2])
					index_1++;
				else if (cols[index_1] > cols[index_2])
					index_2++;
				else {
					G[i][j] += values[index_1]*values[index_2];
					index_1++;
					index_2++;
				}
			}
		}
	}

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	unordered_set<int> select_set;
	for (int i = 0; i < M; i++)
		select_set.insert(i);

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = dist(generator);
			while(select_set.count(line) == 0)
				line = dist(generator);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
			}
			select_set.erase(line);
			for (int j = 0; j < M; j++)
				if(G[line][j] != 0 && select_set.count(j) == 0)
					select_set.insert(j);
		}
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it;
	}
	avg_it /= n_runs;
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	for (int i = 0; i < M; i++) {
		delete[] G[i];
	}
	delete[] G;
	return x_sol;
}

double* GRK_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	double sqr_matrixNorm = 0;
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
		sqr_matrixNorm += sqrNorm_line[i];
	}

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	long long it;

	double* res = new double[M];
	double* res_samp = new double[M];
	double normRes;
	double maxVal;
	double eps_k;
	double temp;
	vector<double> probs(M);
	discrete_distribution<> dist;

	double start;
	double stop;
	double duration = 0;
	long long avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			normRes = 0;
			maxVal = 0;
			for (int i = 0; i < M; i++) {
				res_samp[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
				temp = res_samp[i]*res_samp[i];
				if (temp/sqrNorm_line[i] > maxVal)
					maxVal = temp/sqrNorm_line[i];
				normRes += temp;
			}
			if (normRes < eps2)
				break;
			eps_k = 0.5*(maxVal/normRes + 1/sqr_matrixNorm);
			maxVal = 0;
			for (int i = 0; i < M; i++) {
				if (res_samp[i]*res_samp[i] < eps_k*normRes*sqrNorm_line[i])
					res_samp[i] = 0;
				maxVal += res_samp[i]*res_samp[i];
			}

			for (int i = 0; i < M; i++)
				probs[i] = res_samp[i]*res_samp[i]/maxVal;
			dist = discrete_distribution<>(probs.begin(), probs.end());
			line = dist(generator);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] res_samp;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* REK_csr_csc(int M, int N, int*& row_idx, int*& cols, double*& values_csr, int*& col_idx, int*& rows, double*& values_csc, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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
			delete[] col_idx;
			delete[] rows;
			delete[] values_csc;
			exit(1);
		}
	}

	discrete_distribution<> dist_lines(sqrNorm_line.begin(), sqrNorm_line.end());

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormCol(i, col_idx, rows, values_csc);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
	double* z_k = new double[M];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	int col;
	long long it;
	int counter;

	double start;
	double stop;
	double duration = 0;		
	long long avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		for (int i = 0; i < M; i++) {
			z_k[i] = b[i];
		}
		line = 0;
		col = 0;
		it = 0;
		counter = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			col = dist_cols(generator);
			scale = -dotProductCSC(col, col_idx, rows, values_csc, z_k)/sqrNorm_col[col];
			scaleVecCol(col, col_idx, rows, values_csc, scale, z_k);
			line = dist_lines(generator);
			scale = (b[line]-z_k[line]-dotProductCSR(line, row_idx, cols, values_csr, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values_csr, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					counter++;
					if (counter >= 10)
						break;
				}			
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] z_k;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RGS_csr_csc(int M, int N, int*& row_idx, int*& cols, double*& values_csr, int*& col_idx, int*& rows, double*& values_csc, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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
			delete[] col_idx;
			delete[] rows;
			delete[] values_csc;
			exit(1);
		}
	}

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormCol(i, col_idx, rows, values_csc);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_k = new double[N];
	double* r_k = new double[M];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	long long it;
	int col;
	int counter;

	double start;
	double stop;
	double duration = 0;		
	long long avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		for (int i = 0; i < M; i++) {
			r_k[i] = b[i];
		}
		it = 0;
		col = 0;
		counter = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			col = dist_cols(generator);
			scale = -dotProductCSC(col, col_idx, rows, values_csc, r_k)/sqrNorm_col[col];
			if (it%step_sc == 0)	
				x_prev[col] = x_k[col];
			x_k[col] -= scale;
			scaleVecCol(col, col_idx, rows, values_csc, scale, r_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					counter++;
					if (counter >= 10)
						break;
				}			
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] r_k;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_cyclic_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_rand_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	mt19937_64 gen(0);
	uniform_int_distribution<> dis(0, M-1);

	for(int run = 0; run < n_runs; run++) {
		gen.seed(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = dis(gen);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			if (line == 1)
				shuffle(begin(samp_line), end(samp_line), rng);
			line = samp_line[line];
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_csr_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	int* row_idx_shuffle = new int[M+1];
	int* cols_shuffle = new int[row_idx[M]];
	double* values_shuffle = new double[row_idx[M]];

	double* b_shuffle = new double[M];
	double* sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			if (line == 1) {
				shuffle(begin(samp_line), end(samp_line), rng);
				reorderRows(M, N, samp_line, row_idx, cols, values, row_idx_shuffle, cols_shuffle, values_shuffle);
				for (int i = 0; i < M; i++) {
					b_shuffle[i] = b[samp_line[i]];
					sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
				}
			}
			scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k))/sqrNorm_line_shuffle[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b_shuffle[i] - dotProductCSR(i, row_idx_shuffle, cols_shuffle, values_shuffle, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] row_idx_shuffle;
	delete[] cols_shuffle;
	delete[] values_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_noshuffle_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	for(int run = 0; run < n_runs; run++) {
		shuffle(begin(samp_line), end(samp_line), rng);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = samp_line[it%M];
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_noshuffle_csr_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	int* row_idx_shuffle = new int[M+1];
	int* cols_shuffle = new int[row_idx[M]];
	double* values_shuffle = new double[row_idx[M]];

	double* b_shuffle = new double[M];
	double* sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		shuffle(begin(samp_line), end(samp_line), rng);
		reorderRows(M, N, samp_line, row_idx, cols, values, row_idx_shuffle, cols_shuffle, values_shuffle);
		for (int i = 0; i < M; i++) {
			b_shuffle[i] = b[samp_line[i]];
			sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
		}
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k))/sqrNorm_line_shuffle[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b_shuffle[i] - dotProductCSR(i, row_idx_shuffle, cols_shuffle, values_shuffle, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] row_idx_shuffle;
	delete[] cols_shuffle;
	delete[] values_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_quasirand_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double phi = 1.6180339887498948482;
	double alpha = 1.0/phi;
	double seed;
	mt19937_64 gen(0);
	uniform_real_distribution<> dist(0.0, 1.0);
	double integral;

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	for(int run = 0; run < n_runs; run++) {
		gen.seed(run);
		seed = dist(gen);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = (int)(modf(seed+alpha*it, &integral)*M);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";
	
	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_quasirand_sobol_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = (int)(sobol::sample(it, run)*M);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";
	
	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_quasirand_sobol_noshuffle_csr(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	unsigned dim = 0;

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);

	int* count_sobol = new int[M];
	int temp_line;
	int counter_line_sobol;
	
	for(int run = 0; run < n_runs; run++) {
		counter_line_sobol = 0;
		for (int i = 0; i < M; i++) {
			count_sobol[i] = 0;
		}
		for (int i = 0; i < M; i++) {
			temp_line = (int)(sobol::sample(counter_line_sobol, run)*M);
			count_sobol[temp_line]++;
			counter_line_sobol++;
			while (count_sobol[temp_line] > 1) {
				count_sobol[temp_line]--;
				temp_line = (int)(sobol::sample(counter_line_sobol, run)*M);
				count_sobol[temp_line]++;
				counter_line_sobol++;
			}
			samp_line[i] = temp_line;
		}
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = samp_line[it%M];
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] count_sobol;
	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_quasirand_sobol_noshuffle_csr_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	unsigned dim = 0;

	double* res = new double[M];
	double* x_prev = new double[N];
	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	
	int* count_sobol = new int[M];
	int temp_line;
	int counter_line_sobol;

	int* row_idx_shuffle = new int[M+1];
	int* cols_shuffle = new int[row_idx[M]];
	double* values_shuffle = new double[row_idx[M]];

	double* b_shuffle = new double[M];
	double* sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		counter_line_sobol = 0;
		for (int i = 0; i < M; i++) {
			count_sobol[i] = 0;
		}
		for (int i = 0; i < M; i++) {
			temp_line = (int)(sobol::sample(counter_line_sobol, run)*M);
			count_sobol[temp_line]++;
			counter_line_sobol++;
			while (count_sobol[temp_line] > 1) {
				count_sobol[temp_line]--;
				temp_line = (int)(sobol::sample(counter_line_sobol, run)*M);
				count_sobol[temp_line]++;
				counter_line_sobol++;
			}
			samp_line[i] = temp_line;
		}
		reorderRows(M, N, samp_line, row_idx, cols, values, row_idx_shuffle, cols_shuffle, values_shuffle);
		for (int i = 0; i < M; i++) {
			b_shuffle[i] = b[samp_line[i]];
			sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
		}
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k))/sqrNorm_line_shuffle[line];
			if (it%step_sc == 0)
				for (int i = 0; i < N; i++)
					x_prev[i] = x_k[i];
			scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b_shuffle[i] - dotProductCSR(i, row_idx_shuffle, cols_shuffle, values_shuffle, x_k);
					if (sqrNorm(res, M) < eps2)
						break;
				}
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] count_sobol;

	delete[] row_idx_shuffle;
	delete[] cols_shuffle;
	delete[] values_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;
	delete[] x_prev;
	delete[] res;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	vector<double> sqrNorm_line(M);
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = dist(generator);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* NSSRK_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	vector<double> sqrNorm_line(M);
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_sol = new double[N];
	double* x_k = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	int old_line;
	long long it;

	double start;
	double stop;
	double duration = 0;		
	long long avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		old_line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			old_line = line;
			line = dist(generator);
			while (line == old_line) {
				line = dist(generator);
			}
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* GSSRK_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	vector<double> sqrNorm_line(M);
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double** G = new double*[M];
	int index_1;
	int index_2;
	for (size_t i = 0; i < M; i++) {
		G[i] = new double[M];
		for (int j = 0; j < M; j++) {
			G[i][j] = 0;
			index_1 = row_idx[i];
			index_2 = row_idx[j];
			while(index_1 < row_idx[i+1] && index_2 < row_idx[j+1]) {
				if (cols[index_1] < cols[index_2])
					index_1++;
				else if (cols[index_1] > cols[index_2])
					index_2++;
				else {
					G[i][j] += values[index_1]*values[index_2];
					index_1++;
					index_2++;
				}
			}
		}
	}

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	unordered_set<int> select_set;
	for (int i = 0; i < M; i++)
		select_set.insert(i);

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = dist(generator);
			while(select_set.count(line) == 0)
				line = dist(generator);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
			}
			select_set.erase(line);
			for (int j = 0; j < M; j++)
				if(G[line][j] != 0 && select_set.count(j) == 0)
					select_set.insert(j);
		}
		stop = omp_get_wtime();
		duration += stop - start;
		for (int i = 0; i < N; i++) {
			x_sol[i] += x_k[i];
		}
		avg_it += it;
	}
	avg_it /= n_runs;
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	for (int i = 0; i < M; i++) {
		delete[] G[i];
	}
	delete[] G;
	return x_sol;
}

double* GRK_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	double sqr_matrixNorm = 0;
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
		sqr_matrixNorm += sqrNorm_line[i];
	}

	double* x_k = new double[N];
	double* x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	long long it;

	double* res_samp = new double[M];
	double normRes;
	double maxVal;
	double eps_k;
	double temp;
	vector<double> probs(M);
	discrete_distribution<> dist;

	double start;
	double stop;
	double duration = 0;
	long long avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			normRes = 0;
			maxVal = 0;
			for (int i = 0; i < M; i++) {
				res_samp[i] = b[i] - dotProductCSR(i, row_idx, cols, values, x_k);
				temp = res_samp[i]*res_samp[i];
				if (temp/sqrNorm_line[i] > maxVal)
					maxVal = temp/sqrNorm_line[i];
				normRes += temp;
			}
			if (normRes < eps2)
				break;
			eps_k = 0.5*(maxVal/normRes + 1/sqr_matrixNorm);
			maxVal = 0;
			for (int i = 0; i < M; i++) {
				if (res_samp[i]*res_samp[i] < eps_k*normRes*sqrNorm_line[i])
					res_samp[i] = 0;
				maxVal += res_samp[i]*res_samp[i];
			}

			for (int i = 0; i < M; i++)
				probs[i] = res_samp[i]*res_samp[i]/maxVal;
			dist = discrete_distribution<>(probs.begin(), probs.end());
			line = dist(generator);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] res_samp;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* REK_csr_csc_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values_csr, int*& col_idx, int*& rows, double*& values_csc, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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
			delete[] col_idx;
			delete[] rows;
			delete[] values_csc;
			exit(1);
		}
	}

	discrete_distribution<> dist_lines(sqrNorm_line.begin(), sqrNorm_line.end());

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormCol(i, col_idx, rows, values_csc);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_sol = new double[N];
	double* x_k = new double[N];
	double* z_k = new double[M];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	int col;
	long long it;
	int counter;

	double start;
	double stop;
	double duration = 0;		
	long long avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		for (int i = 0; i < M; i++) {
			z_k[i] = b[i];
		}
		line = 0;
		col = 0;
		it = 0;
		counter = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			col = dist_cols(generator);
			scale = -dotProductCSC(col, col_idx, rows, values_csc, z_k)/sqrNorm_col[col];
			scaleVecCol(col, col_idx, rows, values_csc, scale, z_k);
			line = dist_lines(generator);
			scale = (b[line]-z_k[line]-dotProductCSR(line, row_idx, cols, values_csr, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values_csr, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] z_k;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RGS_csr_csc_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values_csr, int*& col_idx, int*& rows, double*& values_csc, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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
			delete[] col_idx;
			delete[] rows;
			delete[] values_csc;
			exit(1);
		}
	}

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormCol(i, col_idx, rows, values_csc);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_k = new double[N];
	double* r_k = new double[M];
	double* x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	long long it;
	int col;
	int counter;

	double start;
	double stop;
	double duration = 0;		
	long long avg_it = 0;

	for(int run = 0; run < n_runs; run++) {
		mt19937 generator(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		for (int i = 0; i < M; i++) {
			r_k[i] = b[i];
		}
		it = 0;
		col = 0;
		counter = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			col = dist_cols(generator);
			scale = -dotProductCSC(col, col_idx, rows, values_csc, r_k)/sqrNorm_col[col];
			x_k[col] -= scale;
			scaleVecCol(col, col_idx, rows, values_csc, scale, r_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] r_k;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_cyclic_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_rand_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	mt19937_64 gen(0);
	uniform_int_distribution<> dis(0, M-1);

	for(int run = 0; run < n_runs; run++) {
		gen.seed(run+1);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = dis(gen);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			if (line == 1)
				shuffle(begin(samp_line), end(samp_line), rng);
			line = samp_line[line];
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_csr_errorSC_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	int* row_idx_shuffle = new int[M+1];
	int* cols_shuffle = new int[row_idx[M]];
	double* values_shuffle = new double[row_idx[M]];

	double* b_shuffle = new double[M];
	double* sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			if (line == 1) {
				shuffle(begin(samp_line), end(samp_line), rng);
				reorderRows(M, N, samp_line, row_idx, cols, values, row_idx_shuffle, cols_shuffle, values_shuffle);
				for (int i = 0; i < M; i++) {
					b_shuffle[i] = b[samp_line[i]];
					sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
				}
			}
			scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k))/sqrNorm_line_shuffle[line];
			scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] row_idx_shuffle;
	delete[] cols_shuffle;
	delete[] values_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_noshuffle_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	for(int run = 0; run < n_runs; run++) {
		shuffle(begin(samp_line), end(samp_line), rng);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = samp_line[it%M];
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_noshuffle_csr_errorSC_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	int* row_idx_shuffle = new int[M+1];
	int* cols_shuffle = new int[row_idx[M]];
	double* values_shuffle = new double[row_idx[M]];

	double* b_shuffle = new double[M];
	double* sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		shuffle(begin(samp_line), end(samp_line), rng);
		reorderRows(M, N, samp_line, row_idx, cols, values, row_idx_shuffle, cols_shuffle, values_shuffle);
		for (int i = 0; i < M; i++) {
			b_shuffle[i] = b[samp_line[i]];
			sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
		}
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k))/sqrNorm_line_shuffle[line];
			scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] row_idx_shuffle;
	delete[] cols_shuffle;
	delete[] values_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_quasirand_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double phi = 1.6180339887498948482;
	double alpha = 1.0/phi;
	double seed;
	mt19937_64 gen(0);
	uniform_real_distribution<> dist(0.0, 1.0);
	double integral;

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	for(int run = 0; run < n_runs; run++) {
		gen.seed(run);
		seed = dist(gen);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = (int)(modf(seed+alpha*it, &integral)*M);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";
	
	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_quasirand_sobol_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = (int)(sobol::sample(it, run)*M);
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";
	
	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_quasirand_sobol_noshuffle_csr_errorSC(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	unsigned dim = 0;

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);
	
	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < M; i++)
			samp_line[i] = (int)(sobol::sample(i, run)*M);
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = samp_line[it%M];
			scale = (b[line]-dotProductCSR(line, row_idx, cols, values, x_k))/sqrNorm_line[line];
			scaleVecLine(line, row_idx, cols, values, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_quasirand_sobol_noshuffle_csr_errorSC_copy(int M, int N, int*& row_idx, int*& cols, double*& values, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
	for (int i = 0; i < M; i++) {
		sqrNorm_line[i] = sqrNormRow(i, row_idx, cols, values);
		if (sqrNorm_line[i] == 0) {
			cout << "Invalid input: matrix with zero norm line" << endl;
			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] b;
			delete[] x;
			exit(1);
		}
	}

	unsigned dim = 0;

	double* x_sol = new double[N];
	double* x_k = new double[N];
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

	vector<int> samp_line(M);

	int* row_idx_shuffle = new int[M+1];
	int* cols_shuffle = new int[row_idx[M]];
	double* values_shuffle = new double[row_idx[M]];

	double* b_shuffle = new double[M];
	double* sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < M; i++)
			samp_line[i] = (int)(sobol::sample(i, run)*M);
		reorderRows(M, N, samp_line, row_idx, cols, values, row_idx_shuffle, cols_shuffle, values_shuffle);
		for (int i = 0; i < M; i++) {
			b_shuffle[i] = b[samp_line[i]];
			sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
		}
		for (int i = 0; i < N; i++) {
			x_k[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = it%M;
			scale = (b_shuffle[line]-dotProductCSR(line, row_idx_shuffle, cols_shuffle, values_shuffle, x_k))/sqrNorm_line_shuffle[line];
			scaleVecLine(line, row_idx_shuffle, cols_shuffle, values_shuffle, scale, x_k);
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x, N) < eps2)
					break;
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
	cout << M << " " << N << " " << duration << " ";
	cout << avg_it << " ";

	delete[] row_idx_shuffle;
	delete[] cols_shuffle;
	delete[] values_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}