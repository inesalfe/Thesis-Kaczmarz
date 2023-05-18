#include "kacz.h"
#include "aux_func.h"
#include "sobol.h"
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <random>
#include <omp.h>
using namespace std;

double* RK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* NSSRK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* GSSRK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double * aux = new double[(long)M*(long)M];
	double ** G = new double*[(long)M];
	for (long i = 0; i < M; i++) {
		G[i] = &aux[i * M];
		for (long j = 0; j < M; j++)
			G[i][j] = dotProduct(A[i], A[j], N);
	}

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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
	
	delete[] G[0];
	delete[] G;
	return x_sol;
}

double* GRK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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
				res_samp[i] = b[i] - dotProduct(A[i], x_k, N);
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* REK(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	discrete_distribution<> dist_lines(sqrNorm_line.begin(), sqrNorm_line.end());

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormMatrixCol(A, i, M);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_k = new double[N];
	double z_k[M];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = dotProductCol(A, col, z_k, M)/sqrNorm_col[col];
			for (int i = 0; i < M; i++) {
				z_k[i] -= scale * A[i][col];
			}
			line = dist_lines(generator);
			scale = (b[line]-z_k[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
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
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RGS(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormMatrixCol(A, i, M);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_k = new double[N];
	double r_k[M];
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
			scale = dotProductCol(A, col, r_k, M)/sqrNorm_col[col];
			if (it%step_sc == 0)	
				x_prev[col] = x_k[col];
			x_k[col] += scale;
			for (int i = 0; i < M; i++) {
				r_k[i] -= scale * A[i][col];
			}
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
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_cyclic(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* RK_rand(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* RK_norep_rand(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* RK_norep_rand_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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

	double * aux = new double[(long)M*(long)N];
	double** A_shuffle = new double*[M];
	for (long i = 0; i < M; i++)
		A_shuffle[i] = &aux[i * N];
	double * b_shuffle = new double[M];
	double * sqrNorm_line_shuffle = new double[M];
	
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
				for (int i = 0; i < M; i++) {
					for (int j = 0; j < N; j++) {
						A_shuffle[i][j] = A[samp_line[i]][j];
					}
					b_shuffle[i] = b[samp_line[i]];
					sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
				}
			}
			scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k, N))/sqrNorm_line_shuffle[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A_shuffle[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b_shuffle[i] - dotProduct(A_shuffle[i], x_k, N);
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

	delete[] A_shuffle[0];
	delete[] A_shuffle;
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

double* RK_norep_rand_noshuffle(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	long long it;

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	double start;
	double stop;
	double duration = 0;		
	long long avg_it = 0;

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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* RK_norep_rand_noshuffle_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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

	double * aux = new double[(long)M*(long)N];
	double** A_shuffle = new double*[M];
	for (long i = 0; i < M; i++)
		A_shuffle[i] = &aux[i * N];
	double * b_shuffle = new double[M];
	double * sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		shuffle(begin(samp_line), end(samp_line), rng);
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				A_shuffle[i][j] = A[samp_line[i]][j];
			}
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
			scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k, N))/sqrNorm_line_shuffle[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A_shuffle[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b_shuffle[i] - dotProduct(A_shuffle[i], x_k, N);
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

	delete[] A_shuffle[0];
	delete[] A_shuffle;
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

double* RK_quasirand(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double phi = 1.6180339887498948482;
	double alpha = 1.0/phi;
	double seed;
	mt19937_64 gen(0);
	uniform_real_distribution<> dist(0.0, 1.0);
	double integral;

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* RK_quasirand_sobol(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* RK_norep_quasirand_sobol_noshuffle(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	unsigned dim = 0;

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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
			x_prev[i] = 0;
		}
		line = 0;
		it = 0;
		start = omp_get_wtime();
		while(1) {
			it++;
			line = samp_line[it%M];
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b[i] - dotProduct(A[i], x_k, N);
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

double* RK_norep_quasirand_sobol_noshuffle_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	unsigned dim = 0;

	double* x_k = new double[N];
	double* x_prev = new double[N];
	double* res = new double[M];
	double* x_sol = new double[N];
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

	double * aux = new double[(long)M*(long)N];
	double** A_shuffle = new double*[M];
	for (long i = 0; i < M; i++)
		A_shuffle[i] = &aux[i * N];
	double * b_shuffle = new double[M];
	double * sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < M; i++) {
			samp_line[i] = (int)(sobol::sample(i, run)*M);
			for (int j = 0; j < N; j++) {
				A_shuffle[i][j] = A[samp_line[i]][j];
			}
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
			scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k, N))/sqrNorm_line_shuffle[line];
			for (int i = 0; i < N; i++) {
				if (it%step_sc == 0)
					x_prev[i] = x_k[i];
				x_k[i] += scale * A_shuffle[line][i];
			}
			if (it%step_sc == 0) {
				if (sqrNormDiff(x_k, x_prev, N) < eps1) {
					for (int i = 0; i < M; i++)
						res[i] = b_shuffle[i] - dotProduct(A_shuffle[i], x_k, N);
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

	delete[] A_shuffle[0];
	delete[] A_shuffle;
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

double* RK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* NSSRK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* GSSRK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	discrete_distribution<> dist(sqrNorm_line.begin(), sqrNorm_line.end());

	double ** G = new double*[M];
	for (size_t i = 0; i < M; i++) {
		G[i] = new double[M];
		for (int j = 0; j < M; j++)
			G[i][j] = dotProduct(A[i], A[j], N);
	}

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* GRK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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
				res_samp[i] = b[i] - dotProduct(A[i], x_k, N);
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* REK_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	discrete_distribution<> dist_lines(sqrNorm_line.begin(), sqrNorm_line.end());

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormMatrixCol(A, i, M);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_k = new double[N];
	double z_k[M];
	double* x_sol = new double[N];
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
			scale = dotProductCol(A, col, z_k, M)/sqrNorm_col[col];
			for (int i = 0; i < M; i++) {
				z_k[i] -= scale * A[i][col];
			}
			line = dist_lines(generator);
			scale = (b[line]-z_k[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* RGS_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

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

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormMatrixCol(A, i, M);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_k = new double[N];
	double r_k[M];
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
			scale = dotProductCol(A, col, r_k, M)/sqrNorm_col[col];
			x_k[col] += scale;
			for (int i = 0; i < M; i++) {
				r_k[i] -= scale * A[i][col];
			}
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

double* REK_max_it(int M, int N, double**& A, double*& b, double*& x, int max_it, int n_runs) {

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

	discrete_distribution<> dist_lines(sqrNorm_line.begin(), sqrNorm_line.end());

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormMatrixCol(A, i, M);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_k = new double[N];
	double z_k[M];
	double* x_sol = new double[N];
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
		while(it < max_it) {
			it++;
			col = dist_cols(generator);
			scale = dotProductCol(A, col, z_k, M)/sqrNorm_col[col];
			for (int i = 0; i < M; i++) {
				z_k[i] -= scale * A[i][col];
			}
			line = dist_lines(generator);
			scale = (b[line]-z_k[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
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

double* RGS_max_it(int M, int N, double**& A, double*& b, double*& x, int max_it, int n_runs) {

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

	vector<double> sqrNorm_col(N);
	for (int i = 0; i < N; i++) {
		sqrNorm_col[i] = sqrNormMatrixCol(A, i, M);
	}

	discrete_distribution<> dist_cols(sqrNorm_col.begin(), sqrNorm_col.end());

	double* x_k = new double[N];
	double r_k[M];
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
		while(it < max_it) {
			it++;
			col = dist_cols(generator);
			scale = dotProductCol(A, col, r_k, M)/sqrNorm_col[col];
			x_k[col] += scale;
			for (int i = 0; i < M; i++) {
				r_k[i] -= scale * A[i][col];
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

double* RK_cyclic_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* RK_rand_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* RK_norep_rand_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* RK_norep_rand_errorSC_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_sol = new double[N];
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

	double * aux = new double[(long)M*(long)N];
	double** A_shuffle = new double*[M];
	for (long i = 0; i < M; i++)
		A_shuffle[i] = &aux[i * N];
	double * b_shuffle = new double[M];
	double * sqrNorm_line_shuffle = new double[M];
	
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
				for (int i = 0; i < M; i++) {
					for (int j = 0; j < N; j++) {
						A_shuffle[i][j] = A[samp_line[i]][j];
					}
					b_shuffle[i] = b[samp_line[i]];
					sqrNorm_line_shuffle[i] = sqrNorm_line[samp_line[i]];
				}
			}
			scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k, N))/sqrNorm_line_shuffle[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A_shuffle[line][i];
			}
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

	delete[] A_shuffle[0];
	delete[] A_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_norep_rand_noshuffle_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	double scale;
	int line;
	long long it;

	vector<int> samp_line(M);
	for (int i = 0; i < M; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	double start;
	double stop;
	double duration = 0;		
	long long avg_it = 0;

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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* RK_norep_rand_noshuffle_errorSC_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_sol = new double[N];
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

	double * aux = new double[(long)M*(long)N];
	double** A_shuffle = new double*[M];
	for (long i = 0; i < M; i++)
		A_shuffle[i] = &aux[i * N];
	double * b_shuffle = new double[M];
	double * sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		shuffle(begin(samp_line), end(samp_line), rng);
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				A_shuffle[i][j] = A[samp_line[i]][j];
			}
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
			scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k, N))/sqrNorm_line_shuffle[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A_shuffle[line][i];
			}
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

	delete[] A_shuffle[0];
	delete[] A_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;

	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}

double* RK_quasirand_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double phi = 1.6180339887498948482;
	double alpha = 1.0/phi;
	double seed;
	mt19937_64 gen(0);
	uniform_real_distribution<> dist(0.0, 1.0);
	double integral;

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* RK_quasirand_sobol_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* RK_norep_quasirand_sobol_noshuffle_errorSC(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	unsigned dim = 0;

	double* x_k = new double[N];
	double* x_sol = new double[N];
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
			scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A[line][i];
			}
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

double* RK_norep_quasirand_sobol_noshuffle_errorSC_copy(int M, int N, double**& A, double*& b, double*& x, double eps1, double eps2, int step_sc, int n_runs) {

	double* sqrNorm_line = new double[M];
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

	unsigned dim = 0;

	double* x_k = new double[N];
	double* x_sol = new double[N];
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

	double * aux = new double[(long)M*(long)N];
	double** A_shuffle = new double*[M];
	for (long i = 0; i < M; i++)
		A_shuffle[i] = &aux[i * N];
	double * b_shuffle = new double[M];
	double * sqrNorm_line_shuffle = new double[M];

	for(int run = 0; run < n_runs; run++) {
		for (int i = 0; i < M; i++) {
			samp_line[i] = (int)(sobol::sample(i, run)*M);
			for (int j = 0; j < N; j++) {
				A_shuffle[i][j] = A[samp_line[i]][j];
			}
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
			scale = (b_shuffle[line]-dotProduct(A_shuffle[line], x_k, N))/sqrNorm_line_shuffle[line];
			for (int i = 0; i < N; i++) {
				x_k[i] += scale * A_shuffle[line][i];
			}
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

	delete[] A_shuffle[0];
	delete[] A_shuffle;
	delete[] b_shuffle;
	delete[] sqrNorm_line_shuffle;
	
	delete[] x_k;
	delete[] sqrNorm_line;
	for (int i = 0; i < N; i++) {
		x_sol[i] /= n_runs;
	}
	return x_sol;
}