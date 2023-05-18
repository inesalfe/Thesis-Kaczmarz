#include "cg.h"
#include <iostream>
using namespace std;

double* cgSolve(int dim, double**& A, double*& b, double eps) {

	double* x = new double[dim];
	double* r = new double[dim];
	double* p = new double[dim];
	double* A_mult_p = new double[dim];

	double num1; // r_k^T * r_k
	double num2; // r_k+1^T * r_k+1
	double denom1; // p_k^T * A * p_k
	double alpha; // num1 / denom1
	double beta; // num2 / num1

	int it = 0;
		
	num1 = 0;
	for (int i = 0; i < dim; i++) {
		x[i] = 0;
		r[i] = b[i];
		num1 += r[i]*r[i];
	}
	if (num1 >= eps) {
		for (int i = 0; i < dim; i++) {
			p[i] = r[i];
		}
		while (1) {

			denom1 = 0;
			for (int i = 0; i < dim; i++) {
				A_mult_p[i] = 0;
				for (int j = 0; j < dim; j++)
					A_mult_p[i] += A[i][j]*p[j];
				denom1 += p[i]*A_mult_p[i];
			}
			alpha = num1/denom1;

			num2 = 0;
			for (int i = 0; i < dim; i++) {
				x[i] += alpha*p[i];
				r[i] -= alpha*A_mult_p[i];
				num2 += r[i]*r[i];
			}

			if (num2 < eps)
				break;

			beta = num2/num1;

			for (int i = 0; i < dim; i++) {
				p[i] = r[i] + beta*p[i];
			}
			it++;

			num1 = num2;

		}
	}

	delete[] r;
	delete[] p;
	delete[] A_mult_p;

	return x;

}

double* cglsSolve(int M, int N, int& it, double**& A, double*& b, double eps) {

	double* x = new double[N];
	double* r = new double[M];
	double* g = new double[N];
	double* p = new double[N];
	double* A_mult_p = new double[M];

	double num1;
	double num2;
	double denom1;
	double denom2;
	double alpha;
	double beta;

	it = 0;
		
	for (int i = 0; i < N; i++) {
		x[i] = 0;
	}

	for (int i = 0; i < M; i++) {
		r[i] = b[i];
	}

	num1 = 0;
	for (int i = 0; i < N; i++) {
		g[i] = 0;
		for (int j = 0; j < M; j++)
			g[i] += A[j][i]*r[j];
		p[i] = g[i];
		num1 += g[i]*g[i];
	}

	denom2 = 0;
	for (int i = 0; i < M; i++) {
		A_mult_p[i] = 0;
		for (int j = 0; j < N; j++)
			A_mult_p[i] += A[i][j]*p[j];
		denom2 += A_mult_p[i]*A_mult_p[i];
	}

	alpha = num1 / denom2;

	for (int i = 0; i < N; i++) {
		x[i] += alpha*p[i];
	}

	for (int i = 0; i < M; i++) {
		r[i] -= alpha*A_mult_p[i];
	}

	denom1 = num1;
	num1 = 0;
	for (int i = 0; i < N; i++) {
		g[i] = 0;
		for (int j = 0; j < M; j++) {
			g[i] += A[j][i]*r[j];
		}
		num1 += g[i]*g[i];
	}

	it++;

	while (num1 > eps) {

		beta = - num1 / denom1;

		for (int i = 0; i < N; i++) {
			p[i] = g[i] - beta*p[i];
		}

		denom2 = 0;
		for (int i = 0; i < M; i++) {
			A_mult_p[i] = 0;
			for (int j = 0; j < N; j++)
				A_mult_p[i] += A[i][j]*p[j];
			denom2 += A_mult_p[i]*A_mult_p[i];
		}

		alpha = num1 / denom2;

		for (int i = 0; i < N; i++) {
			x[i] += alpha*p[i];
		}

		for (int i = 0; i < M; i++) {
			r[i] -= alpha*A_mult_p[i];
		}

		denom1 = num1;
		num1 = 0;
		for (int i = 0; i < N; i++) {
			g[i] = 0;
			for (int j = 0; j < M; j++) {
				g[i] += A[j][i]*r[j];
			}
			num1 += g[i]*g[i];
		}

		it++;

	}

	delete[] r;
	delete[] p;
	delete[] g;
	delete[] A_mult_p;

	return x;

}