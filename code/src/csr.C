#include "csr.h"
#include <fstream>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;

double sqrNormRow(int& m, int*& row_idx, int*& cols, double*& values) {
	int index = row_idx[m];
	double sqr_norm = 0;
	while (index < row_idx[m+1]) {
		sqr_norm += values[index]*values[index];
		index++;
	}
	return sqr_norm;
}

double dotProductCSR(int& m, int*& row_idx, int*& cols, double*& values, double*& vector) {
	int index = row_idx[m];
	double dp = 0;
	while (index < row_idx[m+1]) {
		dp += values[index] * vector[cols[index]];
		index++;
	}
	return dp;
}

void scaleVecLine(int& m, int*& row_idx, int*& cols, double*& values, double& scale, double*& vector) {
	int index = row_idx[m];
	int col;
	while (index < row_idx[m+1]) {
		col = cols[index];
		vector[col] += scale*values[index];
		index++;
	}
	return;
}

void scaleDivideVecLine(int& m, int div, int*& row_idx, int*& cols, double*& values, double& scale, double*& vector) {
	int index = row_idx[m];
	int col;
	while (index < row_idx[m+1]) {
		col = cols[index];
		vector[col] += scale*values[index] / div;
		index++;
	}
	return;
}

void scaleVecLinePartial(int& m, int i, int j, int*& row_idx, int*& cols, double*& values, double& scale, double*& vector) {
	int index = row_idx[m];
	int col;
	while (index < row_idx[m+1]) {
		col = cols[index];
		if (col >= i && col <= j)
			vector[col] += scale*values[index];
		index++;
	}
	return;
}

void scaleNewVecLine(int& m, int*& row_idx, int*& cols, double*& values, double& scale, double*& vector, double*& vector_out) {
	int index = row_idx[m];
	int col;
	while (index < row_idx[m+1]) {
		col = cols[index];
		vector_out[col] = vector[col]+scale*values[index];
		index++;
	}
	return;
}

void deleteRowsZeros(int& M, int*& row_idx) {

	int i = 0;
	int j = 1;
	int k = 0;

	while(i < M+1) {
		row_idx[k] = row_idx[i];
		while(j < M+1 && row_idx[i] == row_idx[j]) {
			i++;
			j++;
		}
		i++;
		j++;
		k++;
	}

	M = k-1;

	return;
}

void reorderRows(int M, int N, vector<int> row_order, int* row_idx_in, int* cols_in, double* values_in, int*& row_idx_out, int*& cols_out, double*& values_out) {

	row_idx_out[0] = 0;
	int row_el;
	int offset_in;
	for (int i = 0; i < M; i++) {
		offset_in = row_idx_in[row_order[i]];
		row_el = row_idx_in[row_order[i]+1] - offset_in;
		row_idx_out[i+1] = row_idx_out[i] + row_el;
		for (int j = 0; j < row_el; j++) {
			cols_out[row_idx_out[i]+j] = cols_in[offset_in+j];
			values_out[row_idx_out[i]+j] = values_in[offset_in+j];
		}
	}

	return;
}