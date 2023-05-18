#include "csc.h"
#include <fstream>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;

double sqrNormCol(int& n, int*& col_idx, int*& rows, double*& values) {
	int index = col_idx[n];
	double sqr_norm = 0;
	while (index < col_idx[n+1]) {
		sqr_norm += values[index]*values[index];
		index++;
	}
	return sqr_norm;
}

double dotProductCSC(int& n, int*& col_idx, int*& rows, double*& values, double*& vector) {
	int index = col_idx[n];
	double dp = 0;
	while (index < col_idx[n+1]) {
		dp += values[index] * vector[rows[index]];
		index++;
	}
	return dp;
}

void scaleVecCol(int& n, int*& col_idx, int*& rows, double*& values, double& scale, double*& vector) {
	int index = col_idx[n];
	int col;
	while (index < col_idx[n+1]) {
		col = rows[index];
		vector[col] += scale*values[index];
		index++;
	}
	return;
}

void deleteColsZeros(int& N, int*& col_idx) {

	int i = 0;
	int j = 1;
	int k = 0;

	while(i < N+1) {
		col_idx[k] = col_idx[i];
		while(j < N+1 && col_idx[i] == col_idx[j]) {
			i++;
			j++;
		}
		i++;
		j++;
		k++;
	}

	N = k-1;

	return;
}