#include "aux_func.h"
#include "cg.h"
#include "csr.h"
#include "csc.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <random>
#include <algorithm>
using namespace std;

double sqrNorm(double * vec, int size) {
	double norm = 0;
	for (int i = 0; i < size; i++)
		norm += vec[i]*vec[i];
	return norm;
}

double sqrNormDiff(double * vec1, double * vec2, int size) {
	double norm = 0;
	double dif = 0;
	for (int i = 0; i < size; i++) {
		dif = vec1[i] - vec2[i];
		norm += dif*dif;
	}
	return norm;
}

double sqrNormMatrixCol(double ** matrix, int col, int size) {
	double norm = 0;
	for (int i = 0; i < size; i++)
		norm += matrix[i][col]*matrix[i][col];
	return norm;
}

double dotProduct(double * vec1, double * vec2, int size) {
	double dot_p = 0;
	for (int i = 0; i < size; i++)
		dot_p += vec1[i]*vec2[i];
	return dot_p;
}

double dotProductCol(double ** matrix, int col, double * vec2, int size) {
	double dot_p = 0;
	for (int i = 0; i < size; i++)
		dot_p += matrix[i][col]*vec2[i];
	return dot_p;
}

void importDenseSystemBIN(int M, int N, string A_filename, string b_filename, string x_filename, double**& A, double*& b, double*& x) {
	
	ifstream file_A;
	file_A.open(A_filename, ios::binary);
	if (!file_A.is_open()) {
		cout << "Error in opening the matrix file" << endl;
		exit(1);
	}

	double * aux;
	aux = new double[(long)M*(long)N];
	A = new double*[(long)M];
	for (long i = 0; i < M; i++)
		A[i] = &aux[i * N];

	for (int i = 0; i < M; i++)
		for (int j = 0; j < N; j++)
			file_A.read(reinterpret_cast<char *>(&A[i][j]), sizeof(A[i][j]));

	file_A.close();

	ifstream file_b;
	file_b.open(b_filename, ios::binary);
	if (!file_b.is_open()) {
		cout << "Error in opening the b vector file" << endl;
		delete[] A[0];
		delete[] A;
		exit(1);
	}

	b = new double[M];

	for (int i = 0; i < M; i++)
		file_b.read(reinterpret_cast<char *>(&b[i]), sizeof(b[i]));

	file_b.close();

	ifstream file_x;
	file_x.open(x_filename, ios::binary);
	if (!file_x.is_open()) {
		cout << "Error in opening the x vector file" << endl;
		delete[] A[0];
		delete[] A;
		delete[] b;
		exit(1);
	}

	x = new double[N];

	for (int i = 0; i < N; i++)
		file_x.read(reinterpret_cast<char *>(&x[i]), sizeof(x[i]));

	file_x.close();
}

void importDenseMatrixMTX(int M, int N, string A_filename, double**& A) {

	// Assuming that there are no zero rows

	ifstream file;
	file.open(A_filename);
	if (!file.is_open()) {
		cout << "Error in opening the MTX file" << endl;
		exit(1);
	}

	string header;
	getline(file, header);
	string object;
	string format;
	string field;
	string symmetry;
	stringstream(header) >> object >> object >> format >> field >> symmetry;

	if(object.compare("vector") == 0) {
		cout << "ERROR: Invalid file. This file contains a vector. Only matrices are allowed." << endl;
		exit(1);
	}
	else if (object.compare("matrix") != 0) {
		cout << "ERROR: Invalid file. Object field must be 'matrix'." << endl;
		exit(1);
	}

	if(format.compare("coordinate") != 0) {
		cout << "ERROR: Invalid file. Format field must be 'coodinate'." << endl;
		exit(1);
	}

	if(field.compare("complex") == 0) {
		cout << "ERROR: Invalid file. Complex matrices are not allowed." << endl;
		exit(1);
	}
	else if (field.compare("real") != 0 && field.compare("double") != 0 && field.compare("integer") != 0 && field.compare("pattern") != 0) {
		cout << "ERROR: Invalid file. Field must be 'real', 'double', 'integer' or 'pattern'." << endl;
		exit(1);
	}

	if (symmetry.compare("general") != 0 && symmetry.compare("symmetric") != 0 && symmetry.compare("skew-symmetric") != 0) {
		cout << "ERROR: Invalid file. Symmetry field must be 'general', 'symmetric' or 'skew-symmetric'." << endl;
		exit(1);
	}

	while(file.peek() == '%')
		file.ignore(2048, '\n');

	double * aux;
	aux = new double[(long)M*(long)N];
	A = new double*[(long)M];
	for (long i = 0; i < M; i++)
		A[i] = &aux[i * N];

	for (int i = 0; i < M; i++)
		for (int j = 0; j < N; j++)
			A[i][j] = 0;

	int col;
	int row;
	double val;

	int NNZ;
	if (symmetry.compare("general") == 0) {
		if (field.compare("pattern") == 0) {
			file >> NNZ >> NNZ >> NNZ;
			for(int l = 0; l < NNZ; l++) {
				file >> row >> col;
				row--;
				col--;
				A[row][col] = 1;
			}
			file.close();
			return;
		}
		else {
			file >> NNZ >> NNZ >> NNZ;
			for(int l = 0; l < NNZ; l++) {
				file >> row >> col >> val;
				row--;
				col--;
				A[row][col] = val;
			}
			file.close();
			return;
		}
	}
	else if (symmetry.compare("symmetric") == 0) {
		if (field.compare("pattern") == 0) {
			file >> NNZ >> NNZ >> NNZ;
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> row >> col;
				row--;
				col--;
				A[row][col] = 1;
				if (row != col) {
					true_NNZ++;
					A[col][row] = 1;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			return;
		}
		else {
			file >> NNZ >> NNZ >> NNZ;
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> row >> col >> val;
				row--;
				col--;
				A[row][col] = val;
				if (row != col) {
					true_NNZ++;
					A[col][row] = val;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			return;
		}
	}
	else {
		file >> NNZ >> NNZ >> NNZ;
		int l = 0;
		while(l < NNZ) {
			file >> row >> col >> val;
			row--;
			col--;
			A[row][col] = val;
			A[col][row] = -val;
			l++;
		}
		NNZ *= 2;
		return;
	}
}

void importDenseMatrixTXT(int M, int N, string A_filename, double**& A) {

	ifstream file_A;
	file_A.open(A_filename);
	if (!file_A.is_open()) {
		cout << "Error in opening the matrix file" << endl;
		exit(1);
	}

	double * aux = new double[M*N];
	A = new double*[M];
	for (int i = 0; i < M; i++)
		A[i] = &aux[i * N];

	for (int i = 0; i < M; i++)
		for (int j = 0; j < N; j++)
			file_A >> A[i][j];

	file_A.close();
}

void importDenseMatrixBIN(int M, int N, string A_filename, double**& A) {

	ifstream file_A;
	file_A.open(A_filename, ios::binary);
	if (!file_A.is_open()) {
		cout << "Error in opening the matrix file" << endl;
		exit(1);
	}

	double * aux;
	aux = new double[(long)M*(long)N];
	A = new double*[(long)M];
	for (long i = 0; i < M; i++)
		A[i] = &aux[i * N];

	for (int i = 0; i < M; i++)
		for (int j = 0; j < N; j++)
			file_A.read(reinterpret_cast<char *>(&A[i][j]), sizeof(A[i][j]));

	file_A.close();
}

void importDenseMatrixSparseBIN(int M, int N, string filename_row_idx, string filename_cols, string filename_values, double**& A) {

	int NNZ;

	int* row_idx = new int[M+1];
	ifstream file_row_idx;
	file_row_idx.open(filename_row_idx, ios::binary);
	if (file_row_idx.is_open())	{
		for (int i = 0; i < M+1; i++) {
			file_row_idx.read(reinterpret_cast<char *>(&row_idx[i]), sizeof(row_idx[i]));
		}
		file_row_idx.close();
	}
	else {
		cout << "ERROR: Invalid input file for CSR array with row indices." << endl;
		delete[] row_idx;
		exit(1);
	}

	int* cols;
	ifstream file_cols;
	file_cols.open(filename_cols, ios::binary);
	if (file_cols.is_open()) {
		file_cols.read(reinterpret_cast<char *>(&NNZ), sizeof(NNZ));
		cols = new int[NNZ];
		for (int i = 0; i < NNZ; i++) {
			file_cols.read(reinterpret_cast<char *>(&cols[i]), sizeof(cols[i]));
		}
		file_cols.close();
	}
	else {
		cout << "ERROR: Invalid input file for CSR array with column indices." << endl;
		delete[] row_idx;
		exit(1);
	}

	double* values;
	ifstream file_values;
	file_values.open(filename_values, ios::binary);
	if (file_values.is_open())	{
		file_values.read(reinterpret_cast<char *>(&NNZ), sizeof(NNZ));
		values = new double[NNZ];
		for (int i = 0; i < NNZ; i++) 
			file_values.read(reinterpret_cast<char *>(&values[i]), sizeof(values[i]));
		file_values.close();
	}
	else {
		cout << "ERROR: Invalid input file for CSR array with values." << endl;
		delete[] cols;
		delete[] row_idx;
		exit(1);
	}

	double * aux = new double[M*N];
	A = new double*[M];
	for (int i = 0; i < M; i++) {
		A[i] = &aux[i * N];
		for (int j = 0; j < N; j++)
			A[i][j] = 0;
	}

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < row_idx[i+1]-row_idx[i]; j++) {
			A[i][cols[row_idx[i]+j]] = values[row_idx[i]+j];
		}
	}

	return;
}

void importCSRMatrixSparseBIN(int M, int N, int& NNZ, string filename_row_idx, string filename_cols, string filename_values, int*& row_idx, int*& cols, double*& values) {

	row_idx = new int[M+1];

	ifstream file_row_idx;
	file_row_idx.open(filename_row_idx, ios::binary);
	if (file_row_idx.is_open())	{
		for (int i = 0; i < M+1; i++) {
			file_row_idx.read(reinterpret_cast<char *>(&row_idx[i]), sizeof(row_idx[i]));
		}
		file_row_idx.close();
	}
	else {
		cout << "ERROR: Invalid input file for CSR array with row indices." << endl;
		delete[] row_idx;
		exit(1);
	}

	ifstream file_cols;
	file_cols.open(filename_cols, ios::binary);
	if (file_cols.is_open()) {
		file_cols.read(reinterpret_cast<char *>(&NNZ), sizeof(NNZ));
		cols = new int[NNZ];
		for (int i = 0; i < NNZ; i++) {
			file_cols.read(reinterpret_cast<char *>(&cols[i]), sizeof(cols[i]));
		}
		file_cols.close();
	}
	else {
		cout << "ERROR: Invalid input file for CSR array with column indices." << endl;
		delete[] row_idx;
		exit(1);
	}

	ifstream file_values;
	file_values.open(filename_values, ios::binary);
	if (file_values.is_open())	{
		file_values.read(reinterpret_cast<char *>(&NNZ), sizeof(NNZ));
		values = new double[NNZ];
		for (int i = 0; i < NNZ; i++) 
			file_values.read(reinterpret_cast<char *>(&values[i]), sizeof(values[i]));
		file_values.close();
	}
	else {
		cout << "ERROR: Invalid input file for CSR array with values." << endl;
		delete[] cols;
		delete[] row_idx;
		exit(1);
	}

	return;
}

void importCSCMatrixSparseBIN(int M, int N, int& NNZ, string filename_col_idx, string filename_rows, string filename_values, int*& col_idx, int*& rows, double*& values) {

	col_idx = new int[N+1];

	ifstream file_col_idx;
	file_col_idx.open(filename_col_idx, ios::binary);
	if (file_col_idx.is_open())	{
		for (int i = 0; i < N+1; i++) {
			file_col_idx.read(reinterpret_cast<char *>(&col_idx[i]), sizeof(col_idx[i]));
		}
		file_col_idx.close();
	}
	else {
		cout << "ERROR: Invalid input file for CSC array with row indices." << endl;
		delete[] col_idx;
		exit(1);
	}

	ifstream file_rows;
	file_rows.open(filename_rows, ios::binary);
	if (file_rows.is_open()) {
		file_rows.read(reinterpret_cast<char *>(&NNZ), sizeof(NNZ));
		rows = new int[NNZ];
		for (int i = 0; i < NNZ; i++)
			file_rows.read(reinterpret_cast<char *>(&rows[i]), sizeof(rows[i]));
		file_rows.close();
	}
	else {
		cout << "ERROR: Invalid input file for CSC array with column indices." << endl;
		delete[] col_idx;
		exit(1);
	}

	ifstream file_values;
	file_values.open(filename_values, ios::binary);
	if (file_values.is_open())	{
		file_values.read(reinterpret_cast<char *>(&NNZ), sizeof(NNZ));
		values = new double[NNZ];
		for (int i = 0; i < NNZ; i++) 
			file_values.read(reinterpret_cast<char *>(&values[i]), sizeof(values[i]));
		file_values.close();
	}
	else {
		cout << "ERROR: Invalid output file for CSC array with non zero values." << endl;
		delete[] rows;
		delete[] col_idx;
		exit(1);
	}

	return;
}

void importCSRMatrixSparseMTX(std::string filename, int& M, int& N, int& NNZ, int*& row_idx, int*& cols, double*& values) {

	ifstream file;
	file.open(filename);
	if (!file.is_open()) {
		cout << "Error in opening the MTX file" << endl;
		exit(1);
	}

	string header;
	getline(file, header);
	string object;
	string format;
	string field;
	string symmetry;
	stringstream(header) >> object >> object >> format >> field >> symmetry;

	if(object.compare("vector") == 0) {
		cout << "ERROR: Invalid file. This file contains a vector. Only matrices are allowed." << endl;
		exit(1);
	}
	else if (object.compare("matrix") != 0) {
		cout << "ERROR: Invalid file. Object field must be 'matrix'." << endl;
		exit(1);
	}

	if(format.compare("coordinate") != 0) {
		cout << "ERROR: Invalid file. Format field must be 'coodinate'." << endl;
		exit(1);
	}

	if(field.compare("complex") == 0) {
		cout << "ERROR: Invalid file. Complex matrices are not allowed." << endl;
		exit(1);
	}
	else if (field.compare("real") != 0 && field.compare("double") != 0 && field.compare("integer") != 0 && field.compare("pattern") != 0) {
		cout << "ERROR: Invalid file. Field must be 'real', 'double', 'integer' or 'pattern'." << endl;
		exit(1);
	}

	if (symmetry.compare("general") != 0 && symmetry.compare("symmetric") != 0 && symmetry.compare("skew-symmetric") != 0) {
		cout << "ERROR: Invalid file. Symmetry field must be 'general', 'symmetric' or 'skew-symmetric'." << endl;
		exit(1);
	}

	while(file.peek() == '%')
		file.ignore(2048, '\n');

	if (symmetry.compare("general") == 0) {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSR> csr(NNZ);
			row_idx = new int[M+1];
			for(int l = 0; l < NNZ; l++) {
				file >> csr[l].row >> csr[l].col;
				csr[l].row -= 1;
				csr[l].col -= 1;
				csr[l].value = 1;
			}
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSR> csr(NNZ);
			row_idx = new int[M+1];
			for(int l = 0; l < NNZ; l++) {
				file >> csr[l].row >> csr[l].col >> csr[l].value;
				csr[l].row -= 1;
				csr[l].col -= 1;
			}
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			return;
		}
	}
	else if (symmetry.compare("symmetric") == 0) {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSR> csr(2*NNZ);
			row_idx = new int[M+1];
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> csr[true_NNZ].row >> csr[true_NNZ].col;
				csr[true_NNZ].row -= 1;
				csr[true_NNZ].col -= 1;
				csr[true_NNZ].value = 1;
				if (csr[true_NNZ].row != csr[true_NNZ].col) {
					true_NNZ++;
					csr[true_NNZ].row = csr[true_NNZ-1].col;
					csr[true_NNZ].col = csr[true_NNZ-1].row;
					csr[true_NNZ].value = 1;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			csr.resize(NNZ);
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSR> csr(2*NNZ);
			row_idx = new int[M+1];
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> csr[true_NNZ].row >> csr[true_NNZ].col >> csr[true_NNZ].value;
				csr[true_NNZ].row -= 1;
				csr[true_NNZ].col -= 1;
				if (csr[true_NNZ].row != csr[true_NNZ].col) {
					true_NNZ++;
					csr[true_NNZ].row = csr[true_NNZ-1].col;
					csr[true_NNZ].col = csr[true_NNZ-1].row;
					csr[true_NNZ].value = csr[true_NNZ-1].value;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			csr.resize(NNZ);
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			return;
		}
	}
	else {
		file >> M >> N >> NNZ;
		vector<CSR> csr(2*NNZ);
		row_idx = new int[M+1];
		int l = 0;
		while(l < NNZ) {
			file >> csr[l].row >> csr[l].col >> csr[l].value;
			csr[l].row -= 1;
			csr[l].col -= 1;
			csr[l].row = csr[l-1].col;
			csr[l].col = csr[l-1].row;
			csr[l].value = -csr[l-1].value;
			l++;
		}
		NNZ *= 2;
		sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
			return a.row < b.row || (a.row == b.row && a.col < b.col);
		});
		row_idx[0] = 0;
		for (int m = 1; m <= M; m++) {
			row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
		}
		cols = new int[NNZ];
		values = new double[NNZ];
		for(int l = 0; l < NNZ; l++) {
			cols[l] = csr[l].col;
			values[l] = csr[l].value;
		}
		deleteRowsZeros(M, row_idx);
		file.close();
		csr.clear();
		
		return;
	}
}

void importCSCMatrixSparseMTX(std::string filename, int& M, int& N, int& NNZ, int*& col_idx, int*& rows, double*& values) {

	ifstream file;
	file.open(filename);
	if (!file.is_open()) {
		cout << "Error in opening the MTX file" << endl;
		exit(1);
	}

	string header;
	getline(file, header);
	string object;
	string format;
	string field;
	string symmetry;
	stringstream(header) >> object >> object >> format >> field >> symmetry;

	if(object.compare("vector") == 0) {
		cout << "ERROR: Invalid file. This file contains a vector. Only matrices are allowed." << endl;
		exit(1);
	}
	else if (object.compare("matrix") != 0) {
		cout << "ERROR: Invalid file. Object field must be 'matrix'." << endl;
		exit(1);
	}

	if(format.compare("coordinate") != 0) {
		cout << "ERROR: Invalid file. Format field must be 'coodinate'." << endl;
		exit(1);
	}

	if(field.compare("complex") == 0) {
		cout << "ERROR: Invalid file. Complex matrices are not allowed." << endl;
		exit(1);
	}
	else if (field.compare("real") != 0 && field.compare("double") != 0 && field.compare("integer") != 0 && field.compare("pattern") != 0) {
		cout << "ERROR: Invalid file. Field must be 'real', 'double', 'integer' or 'pattern'." << endl;
		exit(1);
	}

	if (symmetry.compare("general") != 0 && symmetry.compare("symmetric") != 0 && symmetry.compare("skew-symmetric") != 0) {
		cout << "ERROR: Invalid file. Symmetry field must be 'general', 'symmetric' or 'skew-symmetric'." << endl;
		exit(1);
	}

	while(file.peek() == '%')
		file.ignore(2048, '\n');

	if (symmetry.compare("general") == 0) {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSC> csc(NNZ);
			col_idx = new int[N+1];
			for(int l = 0; l < NNZ; l++) {
				file >> csc[l].row >> csc[l].col;
				csc[l].row -= 1;
				csc[l].col -= 1;
				csc[l].value = 1;
			}
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();
			
			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSC> csc(NNZ);
			col_idx = new int[N+1];
			for(int l = 0; l < NNZ; l++) {
				file >> csc[l].row >> csc[l].col >> csc[l].value;
				csc[l].row -= 1;
				csc[l].col -= 1;
			}
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();
			
			return;
		}
	}
	else if (symmetry.compare("symmetric") == 0) {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSC> csc(2*NNZ);
			col_idx = new int[N+1];
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> csc[true_NNZ].row >> csc[true_NNZ].col;
				csc[true_NNZ].row -= 1;
				csc[true_NNZ].col -= 1;
				csc[true_NNZ].value = 1;
				if (csc[true_NNZ].row != csc[true_NNZ].col) {
					true_NNZ++;
					csc[true_NNZ].row = csc[true_NNZ-1].col;
					csc[true_NNZ].col = csc[true_NNZ-1].row;
					csc[true_NNZ].value = 1;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			csc.resize(NNZ);
			sort(csc.begin(), csc.end(), [](const CSC &a, const CSC &b){
				return a.col < b.col || (a.col == b.col && a.row < b.row);
			});
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();
			
			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSC> csc(2*NNZ);
			col_idx = new int[N+1];
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> csc[true_NNZ].row >> csc[true_NNZ].col >> csc[true_NNZ].value;
				csc[true_NNZ].row -= 1;
				csc[true_NNZ].col -= 1;
				if (csc[true_NNZ].row != csc[true_NNZ].col) {
					true_NNZ++;
					csc[true_NNZ].row = csc[true_NNZ-1].col;
					csc[true_NNZ].col = csc[true_NNZ-1].row;
					csc[true_NNZ].value = csc[true_NNZ-1].value;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			csc.resize(NNZ);
			sort(csc.begin(), csc.end(), [](const CSC &a, const CSC &b){
				return a.col < b.col || (a.col == b.col && a.row < b.row);
			});
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();
			
			return;
		}
	}
	else {

		file >> M >> N >> NNZ;
		vector<CSC> csc(2*NNZ);
		col_idx = new int[N+1];
		int l = 0;
		while(l < NNZ) {
			file >> csc[l].row >> csc[l].col >> csc[l].value;
			csc[l].row -= 1;
			csc[l].col -= 1;
			csc[l].row = csc[l-1].col;
			csc[l].col = csc[l-1].row;
			csc[l].value = -csc[l-1].value;
			l++;
		}
		NNZ *= 2;
		sort(csc.begin(), csc.end(), [](const CSC &a, const CSC &b){
			return a.col < b.col || (a.col == b.col && a.row < b.row);
		});
		col_idx[0] = 0;
		for (int n = 1; n <= N; n++) {
			col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
		}
		rows = new int[NNZ];
		values = new double[NNZ];
		for(int l = 0; l < NNZ; l++) {
			rows[l] = csc[l].row;
			values[l] = csc[l].value;
		}
		deleteColsZeros(N, col_idx);
		file.close();
		csc.clear();
		
		return;

	}
}

void importCSRMatrixDenseBIN(std::string filename, int& M, int& N, int& NNZ, int*& row_idx, int*& cols, double*& values) {

	// We are assuming that there are no rows of zeros

	ifstream file;
	file.open(filename, ios::binary);
	if (!file.is_open()) {
		cout << "Error in opening the binary matrix file" << endl;
		exit(1);
	}

	row_idx = new int[M+1];
	vector<CSR> csr(M*N);

	double val;
	int counter = 0;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			file.read(reinterpret_cast<char *>(&val), sizeof(val));
			if (val != 0) {
				csr[counter].row = i;
				csr[counter].col = j;
				csr[counter].value = val;
				counter++;
			}
		}
	}

	NNZ = counter;
	csr.resize(NNZ);

	row_idx[0] = 0;
	for (int m = 1; m <= M; m++) {
		row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
	}

	cols = new int[NNZ];
	values = new double[NNZ];
	for(int l = 0; l < NNZ; l++) {
		cols[l] = csr[l].col;
		values[l] = csr[l].value;
	}
	file.close();
	csr.clear();
	
	return;
}

void importCSCMatrixDenseBIN(std::string filename, int& M, int& N, int& NNZ, int*& col_idx, int*& rows, double*& values) {

	// We are assuming that there are no column of zeros

	ifstream file;
	file.open(filename, ios::binary);
	if (!file.is_open()) {
		cout << "Error in opening the binary matrix file" << endl;
		exit(1);
	}

	col_idx = new int[N+1];
	vector<CSC> csc(M*N);

	double val;
	int counter = 0;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			file.read(reinterpret_cast<char *>(&val), sizeof(val));
			if (val != 0) {
				csc[counter].row = i;
				csc[counter].col = j;
				csc[counter].value = val;
				counter++;
			}
		}
	}

	sort(csc.begin(), csc.end(), [](const CSC &a, const CSC &b){
		return a.col < b.col || (a.col == b.col && a.row < b.row);
	});

	NNZ = counter;
	csc.resize(NNZ);

	col_idx[0] = 0;
	for (int n = 1; n <= N; n++) {
		col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
	}

	rows = new int[NNZ];
	values = new double[NNZ];
	for(int l = 0; l < NNZ; l++) {
		rows[l] = csc[l].row;
		values[l] = csc[l].value;
	}
	file.close();
	csc.clear();
	
	return;
}

void convertMTXtoCSR_BIN(int& M, int& N, int& NNZ, std::string filename, std::string folder_out) {

	int* row_idx;
	int* cols;
	double* values;

	ifstream file;
	file.open(filename);
	if (!file.is_open()) {
		cout << "Error in opening the MTX file" << endl;
		exit(1);
	}

	string header;
	getline(file, header);
	string object;
	string format;
	string field;
	string symmetry;
	stringstream(header) >> object >> object >> format >> field >> symmetry;

	if(object.compare("vector") == 0) {
		cout << "ERROR: Invalid file. This file contains a vector. Only matrices are allowed." << endl;
		exit(1);
	}
	else if (object.compare("matrix") != 0) {
		cout << "ERROR: Invalid file. Object field must be 'matrix'." << endl;
		exit(1);
	}

	if(format.compare("coordinate") != 0) {
		cout << "ERROR: Invalid file. Format field must be 'coodinate'." << endl;
		exit(1);
	}

	if(field.compare("complex") == 0) {
		cout << "ERROR: Invalid file. Complex matrices are not allowed." << endl;
		exit(1);
	}
	else if (field.compare("real") != 0 && field.compare("double") != 0 && field.compare("integer") != 0 && field.compare("pattern") != 0) {
		cout << "ERROR: Invalid file. Field must be 'real', 'double', 'integer' or 'pattern'." << endl;
		exit(1);
	}

	if (symmetry.compare("general") != 0 && symmetry.compare("symmetric") != 0 && symmetry.compare("skew-symmetric") != 0) {
		cout << "ERROR: Invalid file. Symmetry field must be 'general', 'symmetric' or 'skew-symmetric'." << endl;
		exit(1);
	}

	while(file.peek() == '%')
		file.ignore(2048, '\n');

	if (symmetry.compare("general") == 0) {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSR> csr(NNZ);
			row_idx = new int[M+1];
			for(int l = 0; l < NNZ; l++) {
				file >> csr[l].row >> csr[l].col;
				csr[l].row -= 1;
				csr[l].col -= 1;
				csr[l].value = 1;
			}
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();

			string filename_row_idx = folder_out + "/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_cols = folder_out + "/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_row_idx(filename_row_idx, ios::binary);
			if(file_row_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_row_idx.write(reinterpret_cast<char*>(&row_idx[i]), sizeof(row_idx[i]));
				}
				file_row_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with row indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_cols(filename_cols, ios::binary);
			if(file_cols.is_open()) {
				file_cols.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_cols.write(reinterpret_cast<char*>(&cols[i]), sizeof(cols[i]));
				}
				file_cols.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with column indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with non zero values." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			delete[] row_idx;
			delete[] cols;
			delete[] values;

			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSR> csr(NNZ);
			row_idx = new int[M+1];
			for(int l = 0; l < NNZ; l++) {
				file >> csr[l].row >> csr[l].col >> csr[l].value;
				csr[l].row -= 1;
				csr[l].col -= 1;
			}
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			string filename_row_idx = folder_out + "/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_cols = folder_out + "/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_row_idx(filename_row_idx, ios::binary);
			if(file_row_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_row_idx.write(reinterpret_cast<char*>(&row_idx[i]), sizeof(row_idx[i]));
				}
				file_row_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with row indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_cols(filename_cols, ios::binary);
			if(file_cols.is_open()) {
				file_cols.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_cols.write(reinterpret_cast<char*>(&cols[i]), sizeof(cols[i]));
				}
				file_cols.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with column indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with non zero values." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			delete[] row_idx;
			delete[] cols;
			delete[] values;
				
			return;
		}
	}
	else if (symmetry.compare("symmetric") == 0) {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSR> csr(2*NNZ);
			row_idx = new int[M+1];
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> csr[true_NNZ].row >> csr[true_NNZ].col;
				csr[true_NNZ].row -= 1;
				csr[true_NNZ].col -= 1;
				csr[true_NNZ].value = 1;
				if (csr[true_NNZ].row != csr[true_NNZ].col) {
					true_NNZ++;
					csr[true_NNZ].row = csr[true_NNZ-1].col;
					csr[true_NNZ].col = csr[true_NNZ-1].row;
					csr[true_NNZ].value = 1;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			csr.resize(NNZ);
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			string filename_row_idx = folder_out + "/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_cols = folder_out + "/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_row_idx(filename_row_idx, ios::binary);
			if(file_row_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_row_idx.write(reinterpret_cast<char*>(&row_idx[i]), sizeof(row_idx[i]));
				}
				file_row_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with row indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_cols(filename_cols, ios::binary);
			if(file_cols.is_open()) {
				file_cols.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_cols.write(reinterpret_cast<char*>(&cols[i]), sizeof(cols[i]));
				}
				file_cols.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with column indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with non zero values." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			delete[] row_idx;
			delete[] cols;
			delete[] values;
				
			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSR> csr(2*NNZ);
			row_idx = new int[M+1];
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> csr[true_NNZ].row >> csr[true_NNZ].col >> csr[true_NNZ].value;
				csr[true_NNZ].row -= 1;
				csr[true_NNZ].col -= 1;
				if (csr[true_NNZ].row != csr[true_NNZ].col) {
					true_NNZ++;
					csr[true_NNZ].row = csr[true_NNZ-1].col;
					csr[true_NNZ].col = csr[true_NNZ-1].row;
					csr[true_NNZ].value = csr[true_NNZ-1].value;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			csr.resize(NNZ);
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			string filename_row_idx = folder_out + "/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_cols = folder_out + "/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_row_idx(filename_row_idx, ios::binary);
			if(file_row_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_row_idx.write(reinterpret_cast<char*>(&row_idx[i]), sizeof(row_idx[i]));
				}
				file_row_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with row indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_cols(filename_cols, ios::binary);
			if(file_cols.is_open()) {
				file_cols.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_cols.write(reinterpret_cast<char*>(&cols[i]), sizeof(cols[i]));
				}
				file_cols.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with column indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with non zero values." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			delete[] row_idx;
			delete[] cols;
			delete[] values;
				
			return;
		}
	}
	else {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSR> csr(2*NNZ);
			row_idx = new int[M+1];
			int l = 0;
			while(l < 2*NNZ) {
				file >> csr[l].row >> csr[l].col;
				csr[l].row -= 1;
				csr[l].col -= 1;
				csr[l].value = 1;
				l++;
				csr[l].row = csr[l-1].col;
				csr[l].col = csr[l-1].row;
				csr[l].value = 1;
				l++;
			}
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			string filename_row_idx = folder_out + "/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_cols = folder_out + "/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_row_idx(filename_row_idx, ios::binary);
			if(file_row_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_row_idx.write(reinterpret_cast<char*>(&row_idx[i]), sizeof(row_idx[i]));
				}
				file_row_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with row indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_cols(filename_cols, ios::binary);
			if(file_cols.is_open()) {
				file_cols.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_cols.write(reinterpret_cast<char*>(&cols[i]), sizeof(cols[i]));
				}
				file_cols.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with column indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with non zero values." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			delete[] row_idx;
			delete[] cols;
			delete[] values;
				
			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSR> csr(2*NNZ);
			row_idx = new int[M+1];
			int l = 0;
			while(l < 2*NNZ) {
				file >> csr[l].row >> csr[l].col >> csr[l].value;
				csr[l].row -= 1;
				csr[l].col -= 1;
				l++;
				csr[l].row = csr[l-1].col;
				csr[l].col = csr[l-1].row;
				csr[l].value = -csr[l-1].value;
				l++;
			}
			sort(csr.begin(), csr.end(), [](const CSR &a, const CSR &b){
				return a.row < b.row || (a.row == b.row && a.col < b.col);
			});
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + count_if(csr.begin(), csr.end(), row_equal(m-1));
			}
			cols = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				cols[l] = csr[l].col;
				values[l] = csr[l].value;
			}
			deleteRowsZeros(M, row_idx);
			file.close();
			csr.clear();
			
			string filename_row_idx = folder_out + "/row_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_cols = folder_out + "/cols_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csr_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_row_idx(filename_row_idx, ios::binary);
			if(file_row_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_row_idx.write(reinterpret_cast<char*>(&row_idx[i]), sizeof(row_idx[i]));
				}
				file_row_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with row indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_cols(filename_cols, ios::binary);
			if(file_cols.is_open()) {
				file_cols.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_cols.write(reinterpret_cast<char*>(&cols[i]), sizeof(cols[i]));
				}
				file_cols.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with column indices." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR array with non zero values." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				exit(1);
			}

			delete[] row_idx;
			delete[] cols;
			delete[] values;
				
			return;
		}
	}
}

void convertMTXtoCSC_BIN(int& M, int& N, int& NNZ, std::string filename, std::string folder_out) {

	int* col_idx;
	int* rows;
	double* values;

	ifstream file;
	file.open(filename);
	if (!file.is_open()) {
		cout << "Error in opening the MTX file" << endl;
		exit(1);
	}

	string header;
	getline(file, header);
	string object;
	string format;
	string field;
	string symmetry;
	stringstream(header) >> object >> object >> format >> field >> symmetry;

	if(object.compare("vector") == 0) {
		cout << "ERROR: Invalid file. This file contains a vector. Only matrices are allowed." << endl;
		exit(1);
	}
	else if (object.compare("matrix") != 0) {
		cout << "ERROR: Invalid file. Object field must be 'matrix'." << endl;
		exit(1);
	}

	if(format.compare("coordinate") != 0) {
		cout << "ERROR: Invalid file. Format field must be 'coodinate'." << endl;
		exit(1);
	}

	if(field.compare("complex") == 0) {
		cout << "ERROR: Invalid file. Complex matrices are not allowed." << endl;
		exit(1);
	}
	else if (field.compare("real") != 0 && field.compare("double") != 0 && field.compare("integer") != 0 && field.compare("pattern") != 0) {
		cout << "ERROR: Invalid file. Field must be 'real', 'double', 'integer' or 'pattern'." << endl;
		exit(1);
	}

	if (symmetry.compare("general") != 0 && symmetry.compare("symmetric") != 0 && symmetry.compare("skew-symmetric") != 0) {
		cout << "ERROR: Invalid file. Symmetry field must be 'general', 'symmetric' or 'skew-symmetric'." << endl;
		exit(1);
	}

	while(file.peek() == '%')
		file.ignore(2048, '\n');

	if (symmetry.compare("general") == 0) {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSC> csc(NNZ);
			col_idx = new int[N+1];
			for(int l = 0; l < NNZ; l++) {
				file >> csc[l].row >> csc[l].col;
				csc[l].row -= 1;
				csc[l].col -= 1;
				csc[l].value = 1;
			}
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();
		
			string filename_col_idx = folder_out + "/col_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_rows = folder_out + "/rows_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csc_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_col_idx(filename_col_idx, ios::binary);
			if(file_col_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_col_idx.write(reinterpret_cast<char*>(&col_idx[i]), sizeof(col_idx[i]));
				}
				file_col_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with row indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_rows(filename_rows, ios::binary);
			if(file_rows.is_open()) {
				file_rows.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_rows.write(reinterpret_cast<char*>(&rows[i]), sizeof(rows[i]));
				}
				file_rows.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with column indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with non zero values." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			delete[] col_idx;
			delete[] rows;
			delete[] values;

			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSC> csc(NNZ);
			col_idx = new int[N+1];
			for(int l = 0; l < NNZ; l++) {
				file >> csc[l].row >> csc[l].col >> csc[l].value;
				csc[l].row -= 1;
				csc[l].col -= 1;
			}
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();

			string filename_col_idx = folder_out + "/col_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_rows = folder_out + "/rows_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csc_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_col_idx(filename_col_idx, ios::binary);
			if(file_col_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_col_idx.write(reinterpret_cast<char*>(&col_idx[i]), sizeof(col_idx[i]));
				}
				file_col_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with row indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_rows(filename_rows, ios::binary);
			if(file_rows.is_open()) {
				file_rows.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_rows.write(reinterpret_cast<char*>(&rows[i]), sizeof(rows[i]));
				}
				file_rows.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with column indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with non zero values." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			delete[] col_idx;
			delete[] rows;
			delete[] values;

			return;
		}
	}
	else if (symmetry.compare("symmetric") == 0) {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSC> csc(2*NNZ);
			col_idx = new int[N+1];
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> csc[true_NNZ].row >> csc[true_NNZ].col;
				csc[true_NNZ].row -= 1;
				csc[true_NNZ].col -= 1;
				csc[true_NNZ].value = 1;
				if (csc[true_NNZ].row != csc[true_NNZ].col) {
					true_NNZ++;
					csc[true_NNZ].row = csc[true_NNZ-1].col;
					csc[true_NNZ].col = csc[true_NNZ-1].row;
					csc[true_NNZ].value = 1;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			csc.resize(NNZ);
			sort(csc.begin(), csc.end(), [](const CSC &a, const CSC &b){
				return a.col < b.col || (a.col == b.col && a.row < b.row);
			});
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();

			string filename_col_idx = folder_out + "/col_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_rows = folder_out + "/rows_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csc_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_col_idx(filename_col_idx, ios::binary);
			if(file_col_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_col_idx.write(reinterpret_cast<char*>(&col_idx[i]), sizeof(col_idx[i]));
				}
				file_col_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with row indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_rows(filename_rows, ios::binary);
			if(file_rows.is_open()) {
				file_rows.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_rows.write(reinterpret_cast<char*>(&rows[i]), sizeof(rows[i]));
				}
				file_rows.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with column indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with non zero values." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			delete[] col_idx;
			delete[] rows;
			delete[] values;

			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSC> csc(2*NNZ);
			col_idx = new int[N+1];
			int l = 0;
			int true_NNZ = 0;
			while(l < NNZ) {
				file >> csc[true_NNZ].row >> csc[true_NNZ].col >> csc[true_NNZ].value;
				csc[true_NNZ].row -= 1;
				csc[true_NNZ].col -= 1;
				if (csc[true_NNZ].row != csc[true_NNZ].col) {
					true_NNZ++;
					csc[true_NNZ].row = csc[true_NNZ-1].col;
					csc[true_NNZ].col = csc[true_NNZ-1].row;
					csc[true_NNZ].value = csc[true_NNZ-1].value;
				}
				true_NNZ++;
				l++;
			}
			NNZ = true_NNZ;
			csc.resize(NNZ);
			sort(csc.begin(), csc.end(), [](const CSC &a, const CSC &b){
				return a.col < b.col || (a.col == b.col && a.row < b.row);
			});
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();

			string filename_col_idx = folder_out + "/col_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_rows = folder_out + "/rows_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csc_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_col_idx(filename_col_idx, ios::binary);
			if(file_col_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_col_idx.write(reinterpret_cast<char*>(&col_idx[i]), sizeof(col_idx[i]));
				}
				file_col_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with row indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_rows(filename_rows, ios::binary);
			if(file_rows.is_open()) {
				file_rows.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_rows.write(reinterpret_cast<char*>(&rows[i]), sizeof(rows[i]));
				}
				file_rows.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with column indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with non zero values." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			delete[] col_idx;
			delete[] rows;
			delete[] values;

			return;
		}
	}
	else {
		if (field.compare("pattern") == 0) {
			file >> M >> N >> NNZ;
			vector<CSC> csc(2*NNZ);
			col_idx = new int[N+1];
			int l = 0;
			while(l < 2*NNZ) {
				file >> csc[l].row >> csc[l].col;
				csc[l].row -= 1;
				csc[l].col -= 1;
				csc[l].value = 1;
				l++;
				csc[l].row = csc[l-1].col;
				csc[l].col = csc[l-1].row;
				csc[l].value = 1;
				l++;
			}
			sort(csc.begin(), csc.end(), [](const CSC &a, const CSC &b){
				return a.col < b.col || (a.col == b.col && a.row < b.row);
			});
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();

			string filename_col_idx = folder_out + "/col_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_rows = folder_out + "/rows_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csc_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_col_idx(filename_col_idx, ios::binary);
			if(file_col_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_col_idx.write(reinterpret_cast<char*>(&col_idx[i]), sizeof(col_idx[i]));
				}
				file_col_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with row indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_rows(filename_rows, ios::binary);
			if(file_rows.is_open()) {
				file_rows.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_rows.write(reinterpret_cast<char*>(&rows[i]), sizeof(rows[i]));
				}
				file_rows.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with column indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with non zero values." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			delete[] col_idx;
			delete[] rows;
			delete[] values;

			return;
		}
		else {
			file >> M >> N >> NNZ;
			vector<CSC> csc(2*NNZ);
			col_idx = new int[N+1];
			int l = 0;
			while(l < 2*NNZ) {
				file >> csc[l].row >> csc[l].col >> csc[l].value;
				csc[l].row -= 1;
				csc[l].col -= 1;
				l++;
				csc[l].row = csc[l-1].col;
				csc[l].col = csc[l-1].row;
				csc[l].value = -csc[l-1].value;
				l++;
			}
			sort(csc.begin(), csc.end(), [](const CSC &a, const CSC &b){
				return a.col < b.col || (a.col == b.col && a.row < b.row);
			});
			col_idx[0] = 0;
			for (int n = 1; n <= N; n++) {
				col_idx[n] = col_idx[n-1] + count_if(csc.begin(), csc.end(), col_equal(n-1));
			}
			rows = new int[NNZ];
			values = new double[NNZ];
			for(int l = 0; l < NNZ; l++) {
				rows[l] = csc[l].row;
				values[l] = csc[l].value;
			}
			deleteColsZeros(N, col_idx);
			file.close();
			csc.clear();

			string filename_col_idx = folder_out + "/col_idx_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_rows = folder_out + "/rows_" + to_string(M) + "_" + to_string(N) + ".bin";
			string filename_values = folder_out + "/values_csc_" + to_string(M) + "_" + to_string(N) + ".bin";

			ofstream file_col_idx(filename_col_idx, ios::binary);
			if(file_col_idx.is_open()) {
				for(int i = 0; i < M+1; i++){
					file_col_idx.write(reinterpret_cast<char*>(&col_idx[i]), sizeof(col_idx[i]));
				}
				file_col_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with row indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_rows(filename_rows, ios::binary);
			if(file_rows.is_open()) {
				file_rows.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_rows.write(reinterpret_cast<char*>(&rows[i]), sizeof(rows[i]));
				}
				file_rows.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with column indices." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int i = 0; i < NNZ; i++){
					file_values.write(reinterpret_cast<char*>(&values[i]), sizeof(values[i]));
				}
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSC array with non zero values." << endl;
				delete[] col_idx;
				delete[] rows;
				delete[] values;
				exit(1);
			}

			delete[] col_idx;
			delete[] rows;
			delete[] values;
						
			return;
		}
	}
}

void importbVectorTXT(int M, string b_filename, double*& b) {
	ifstream file;
	file.open(b_filename);
	if (!file.is_open())
		exit(1);

	b = new double[M];

	for (int i = 0; i < M; i++)
		file >> b[i];
	file.close();
}

void importxVectorTXT(int N, string x_filename, double*& x) {
	ifstream file;
	file.open(x_filename);
	if (!file.is_open())
		exit(1);

	x = new double[N];

	for (int i = 0; i < N; i++)
		file >> x[i];
	file.close();
}

void importbVectorBIN(int M, string b_filename, double*& b) {

	b = new double[M];

	ifstream file;
	file.open(b_filename, ios::binary);
	if (file.is_open())	{
		for (int i = 0; i < M; i++) {
			file.read(reinterpret_cast<char *>(&b[i]), sizeof(b[i]));
		}
		file.close();
	}
	else {
		cout << "ERROR: Invalid input file for b vector." << endl;
		delete[] b;
		exit(1);
	}
}

void importxVectorBIN(int N, string x_filename, double*& x) {

	x = new double[N];

	ifstream file;
	file.open(x_filename, ios::binary);
	if (file.is_open())	{
		for (int i = 0; i < N; i++) {
			file.read(reinterpret_cast<char *>(&x[i]), sizeof(x[i]));
		}
		file.close();
	}
	else {
		cout << "ERROR: Invalid input file for x vector." << endl;
		delete[] x;
		exit(1);
	}
}

void convertMatrixBIN(int M, int N, string A_filename) {

	string input_etx = ".txt";
	string output_etx = ".bin";

	string input_name = A_filename;
	string output_name = input_name.substr(0, input_name.length() - input_etx.length());

	output_name = output_name + output_etx;

	ifstream file_in(input_name);
	ofstream file_out(output_name, ios::binary);
	if (file_in.is_open() && file_out.is_open()) {
		double num;
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				file_in >> num;
				file_out.write(reinterpret_cast<char*>(&num), sizeof(num));
			}
		}
		file_in.close();
		file_out.close();
	}	
	else {
		cout << "ERROR: Invalid input file for matrix." << endl;
		exit(1);
	}

	return;	
}

void convertxVectorBIN(int N, string x_filename) {

	string input_etx = ".txt";
	string output_etx = ".bin";

	string input_name = x_filename;
	string output_name = input_name.substr(0, input_name.length() - input_etx.length());

	output_name = output_name + output_etx;

	ifstream file_in(input_name);
	ofstream file_out(output_name, ios::binary);
	if (file_in.is_open() && file_out.is_open()) {
		double num;
		for (int i = 0; i < N; i++) {
			file_in >> num;
			file_out.write(reinterpret_cast<char*>(&num), sizeof(num));
		}
		file_in.close();
		file_out.close();
	}	
	else {
		cout << "ERROR: Invalid input file for x vector." << endl;
		exit(1);
	}

	return;
}

void convertbVectorBIN(int M, string b_filename) {

	string input_etx = ".txt";
	string output_etx = ".bin";

	string input_name = b_filename;
	string output_name = input_name.substr(0, input_name.length() - input_etx.length());

	output_name = output_name + output_etx;

	ifstream file_in(input_name);
	ofstream file_out(output_name, ios::binary);
	if (file_in.is_open() && file_out.is_open()) {
		double num;
		for (int i = 0; i < M; i++) {
			file_in >> num;
			file_out.write(reinterpret_cast<char*>(&num), sizeof(num));
		}
		file_in.close();
		file_out.close();
	}	
	else {
		cout << "ERROR: Invalid input file for b vector." << endl;
		exit(1);
	}

	return;
}

void genConsistSparseSystem(int M, int N) {

	default_random_engine gen_mu;
	gen_mu.seed(1);
	uniform_int_distribution<int> dist_mu(-5, 5);

	default_random_engine gen_sigma;
	gen_sigma.seed(2);
	uniform_int_distribution<int> dist_sigma(1, 20);

	int mu;
	int sigma;

	default_random_engine gen;
	gen.seed(3);

	string filename_A;
	string filename_x;
	string filename_b;

	string filename_row_idx;
	string filename_cols;
	string filename_values;
	
	vector<int> densities{1, 2, 5, 8, 10, 20, 30, 50};
	auto rng = default_random_engine {};

	for (int d = 0; d < densities.size(); d++) {

			double* aux = new double[(long)M*(long)N];
			double** A = new double*[(long)M];
			for (long i = 0; i < M; i++) {
				A[i] = &aux[i * N];	
				for (int j = 0; j < N; j++) {
					A[i][j] = 0;
				}
			}

			int NNZ = M*densities[d];

			int* cols = new int[NNZ];
			double* values = new double[NNZ];

			default_random_engine gen_entry;
			gen_entry.seed(4);
			uniform_int_distribution<int> dist_entry(0,N-1);

			int entry;
			for (int i = 0; i < M; i++) {
				mu = dist_mu(gen_mu);
				sigma = dist_sigma(gen_sigma);
				normal_distribution<double> dist(mu,sigma);
				for (int j = 0; j < densities[d]; j++) {
					entry = dist_entry(gen_entry);
					while (A[i][entry] != 0)
						entry = dist_entry(gen_entry);
					A[i][entry] = dist(gen);
					cols[i*densities[d]+j] = entry;
					values[i*densities[d]+j] = A[i][entry];
				}
			}

			int* row_idx = new int[M+1];
			row_idx[0] = 0;
			for (int m = 1; m <= M; m++) {
				row_idx[m] = row_idx[m-1] + densities[d];
			}

			mu = dist_mu(gen_mu);
			sigma = dist_sigma(gen_sigma);
			normal_distribution<double> dist(mu,sigma);
			double* x = new double[N];
			for (int i = 0; i < N; i++)
				x[i] = dist(gen);

			double* b = new double[M];
			for (int k = 0; k < M; k++) {
				b[k] = 0;
				for (int l = 0; l < N; l++)
					b[k] += A[k][l]*x[l];
			}

			filename_A = "../data/sparse/A_" + to_string(M) + "_" + to_string(N) + "_" + to_string(densities[d]) + ".bin";
			filename_x = "../data/sparse/x_" + to_string(M) + "_" + to_string(N) + "_" + to_string(densities[d]) + ".bin";
			filename_b = "../data/sparse/b_" + to_string(M) + "_" + to_string(N) + "_" + to_string(densities[d]) + ".bin";

			filename_row_idx = "../data/sparse/row_idx_" + to_string(M) + "_" + to_string(N) + "_" + to_string(densities[d]) + ".bin";
			filename_cols = "../data/sparse/cols_" + to_string(M) + "_" + to_string(N) + "_" + to_string(densities[d]) + ".bin";
			filename_values = "../data/sparse/values_" + to_string(M) + "_" + to_string(N) + "_" + to_string(densities[d]) + ".bin";

			ofstream file_values(filename_values, ios::binary);
			if(file_values.is_open()) {
				file_values.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int k = 0; k < NNZ; k++)
					file_values.write(reinterpret_cast<char*>(&values[k]), sizeof(values[k]));
				file_values.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR column indices vector." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				delete[] A[0];
				delete[] A;
				delete[] x;
				delete[] b;
				exit(1);
			}

			ofstream file_cols(filename_cols, ios::binary);
			if(file_cols.is_open()) {
				file_cols.write(reinterpret_cast<char*>(&NNZ), sizeof(NNZ));
				for(int k = 0; k < NNZ; k++)
					file_cols.write(reinterpret_cast<char*>(&cols[k]), sizeof(cols[k]));
				file_cols.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR column indices vector." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				delete[] A[0];
				delete[] A;
				delete[] x;
				delete[] b;
				exit(1);
			}

			ofstream file_row_idx(filename_row_idx, ios::binary);
			if(file_row_idx.is_open()) {
				for(int k = 0; k < M+1; k++)
					file_row_idx.write(reinterpret_cast<char*>(&row_idx[k]), sizeof(row_idx[k]));
				file_row_idx.close();
			}
			else {
				cout << "ERROR: Invalid output file for CSR row indices vector." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				delete[] A[0];
				delete[] A;
				delete[] x;
				delete[] b;
				exit(1);
			}

			ofstream file_A(filename_A, ios::binary);
			if(file_A.is_open()) {
				for(int k = 0; k < M; k++)
					for (int l = 0; l < N; l++)
						file_A.write(reinterpret_cast<char*>(&A[k][l]), sizeof(A[k][l]));
				file_A.close();
			}
			else {
				cout << "ERROR: Invalid output file for matrix A." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				delete[] A[0];
				delete[] A;
				delete[] x;
				delete[] b;
				exit(1);
			}

			ofstream file_x(filename_x, ios::binary);
			if(file_x.is_open()) {
				for (int l = 0; l < N; l++)
					file_x.write(reinterpret_cast<char*>(&x[l]), sizeof(x[l]));
				file_x.close();
			}
			else {
				cout << "ERROR: Invalid output file for vector x." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				delete[] A[0];
				delete[] A;
				delete[] x;
				delete[] b;
				exit(1);
			}

			ofstream file_b(filename_b, ios::binary);
			if(file_b.is_open()) {
				for(int k = 0; k < M; k++)
					file_b.write(reinterpret_cast<char*>(&b[k]), sizeof(b[k]));
				file_b.close();
			}
			else {
				cout << "ERROR: Invalid output file for vector b." << endl;
				delete[] row_idx;
				delete[] cols;
				delete[] values;
				delete[] A[0];
				delete[] A;
				delete[] x;
				delete[] b;
				exit(1);
			}

			cout << "M = " << M << " and N = " << N << " completed!" << endl;

			delete[] row_idx;
			delete[] cols;
			delete[] values;
			delete[] A[0];
			delete[] A;
			delete[] x;
			delete[] b;

		}

	return;

}

void genConsistDenseSystems() {

	int M_max = 80000;
	int N_max = 10000;

	vector<int> N_values{50, 100, 200, 500, 750, 1000, 2000, 4000, 10000};
	vector<int> M_values{2000, 4000, 20000, 40000, 80000};

	default_random_engine gen_mu;
	gen_mu.seed(1);
	uniform_int_distribution<int> dist_mu(-5, 5);

	default_random_engine gen_sigma;
	gen_sigma.seed(2);
	uniform_int_distribution<int> dist_sigma(1, 20);

	int mu;
	int sigma;

	double* aux = new double[(long)M_max*(long)N_max];
	double** A = new double*[(long)M_max];
	for (long i = 0; i < M_max; i++)
		A[i] = &aux[i * N_max];

	default_random_engine gen;
	gen.seed(3);

	for (int i = 0; i < M_max; i++) {
		mu = dist_mu(gen_mu);
		sigma = dist_sigma(gen_sigma);
		normal_distribution<double> dist(mu,sigma);
		for (int j = 0; j < N_max; j++) {
			A[i][j] = dist(gen);
		}
	}

	mu = dist_mu(gen_mu);
	sigma = dist_sigma(gen_sigma);
	normal_distribution<double> dist(mu,sigma);
	double* x = new double[N_max];
	for (int i = 0; i < N_max; i++)
		x[i] = dist(gen);

	cout << "Full matrix A and solution generated!" << endl;

	string filename_A;
	string filename_x;
	string filename_b;

	int M;
	int N;
	double* b = new double[M_max];
	for (int i = 0; i < M_values.size(); i++)
		for (int j = 0; j < N_values.size(); j++) {
			M = M_values[i];
			N = N_values[j];
			if (M/N >= 2) {

				for (int k = 0; k < M; k++) {
					b[k] = 0;
					for (int l = 0; l < N; l++)
						b[k] += A[k][l]*x[l];
				}

				filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
				filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
				filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";

				ofstream file_A(filename_A, ios::binary);
				if(file_A.is_open()) {
					for(int k = 0; k < M; k++)
						for (int l = 0; l < N; l++)
							file_A.write(reinterpret_cast<char*>(&A[k][l]), sizeof(A[k][l]));
					file_A.close();
				}
				else {
					cout << "ERROR: Invalid output file for matrix A." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_x(filename_x, ios::binary);
				if(file_x.is_open()) {
					for (int l = 0; l < N; l++)
						file_x.write(reinterpret_cast<char*>(&x[l]), sizeof(x[l]));
					file_x.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector x." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_b(filename_b, ios::binary);
				if(file_b.is_open()) {
					for(int k = 0; k < M; k++)
						file_b.write(reinterpret_cast<char*>(&b[k]), sizeof(b[k]));
					file_b.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector b." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				cout << "M = " << M << " and N = " << N << " completed!" << endl;

			}
		}

	delete[] A[0];
	delete[] A;
	delete[] x;
	delete[] b;

	return;
}

void genConsistDenseSystemsNorm() {

	int M_max = 80000;
	int N_max = 10000;

	vector<int> N_values{50, 100, 200, 500, 750, 1000, 2000, 4000, 10000};
	vector<int> M_values{2000, 4000, 20000, 40000, 80000};

	int mu = 0;
	int sigma = 1;

	default_random_engine gen;
	gen.seed(3);
	normal_distribution<double> dist(mu,sigma);

	double* aux = new double[(long)M_max*(long)N_max];
	double** A = new double*[(long)M_max];
	for (long i = 0; i < M_max; i++)
		A[i] = &aux[i * N_max];

	for (int i = 0; i < M_max; i++)
		for (int j = 0; j < N_max; j++) {
			A[i][j] = dist(gen);
		}

	double* x = new double[N_max];
	for (int i = 0; i < N_max; i++)
		x[i] = dist(gen);

	cout << "Full matrix A and solution generated!" << endl;

	string filename_A;
	string filename_x;
	string filename_b;

	int M;
	int N;
	double* b = new double[M_max];
	for (int i = 0; i < M_values.size(); i++)
		for (int j = 0; j < N_values.size(); j++) {
			M = M_values[i];
			N = N_values[j];
			if (M/N >= 2) {

				for (int k = 0; k < M; k++) {
					b[k] = 0;
					for (int l = 0; l < N; l++)
						b[k] += A[k][l]*x[l];
				}

				filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
				filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
				filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";

				ofstream file_A(filename_A, ios::binary);
				if(file_A.is_open()) {
					for(int k = 0; k < M; k++)
						for (int l = 0; l < N; l++)
							file_A.write(reinterpret_cast<char*>(&A[k][l]), sizeof(A[k][l]));
					file_A.close();
				}
				else {
					cout << "ERROR: Invalid output file for matrix A." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_x(filename_x, ios::binary);
				if(file_x.is_open()) {
					for (int l = 0; l < N; l++)
						file_x.write(reinterpret_cast<char*>(&x[l]), sizeof(x[l]));
					file_x.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector x." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_b(filename_b, ios::binary);
				if(file_b.is_open()) {
					for(int k = 0; k < M; k++)
						file_b.write(reinterpret_cast<char*>(&b[k]), sizeof(b[k]));
					file_b.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector b." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				cout << "M = " << M << " and N = " << N << " completed!" << endl;

			}
		}

	delete[] A[0];
	delete[] A;
	delete[] x;
	delete[] b;

	return;
}

void genConsistDenseSystemsRand() {

	int M_max = 80000;
	int N_max = 10000;

	vector<int> N_values{50, 100, 200, 500, 750, 1000, 2000, 4000, 10000};
	vector<int> M_values{2000, 4000, 20000, 40000, 80000};

	default_random_engine gen_mu;
	gen_mu.seed(1);
	uniform_int_distribution<int> dist_mu(-5, 5);

	default_random_engine gen_sigma;
	gen_sigma.seed(2);
	uniform_int_distribution<int> dist_sigma(1, 20);

	int mu;
	int sigma;

	double* aux = new double[(long)M_max*(long)N_max];
	double** A = new double*[(long)M_max];
	for (long i = 0; i < M_max; i++)
		A[i] = &aux[i * N_max];

	default_random_engine gen;
	gen.seed(3);

	for (int i = 0; i < M_max; i++) {
		mu = dist_mu(gen_mu);
		sigma = dist_sigma(gen_sigma);
		normal_distribution<double> dist(mu,sigma);
		for (int j = 0; j < N_max; j++) {
			A[i][j] = dist(gen);
		}
	}

	mu = dist_mu(gen_mu);
	sigma = dist_sigma(gen_sigma);
	normal_distribution<double> dist(mu,sigma);
	double* x = new double[N_max];
	for (int i = 0; i < N_max; i++)
		x[i] = dist(gen);

	cout << "Full matrix A generated!" << endl;

	string filename_A;
	string filename_x;
	string filename_b;

	vector<int> samp_line(M_max);
	for (int i = 0; i < M_max; i++)
		samp_line[i] = i;
	mt19937 rng(1);

	int M;
	int N;
	double* b = new double[M_max];
	for (int i = 0; i < M_values.size(); i++)
		for (int j = 0; j < N_values.size(); j++) {
			M = M_values[i];
			N = N_values[j];
			if (M/N >= 2) {

				double* aux_temp = new double[(long)M*(long)N];
				double** A_temp = new double*[(long)M];
				for (int k = 0; k < M; k++)
					A_temp[k] = &aux_temp[k * N];

				shuffle(begin(samp_line), end(samp_line), rng);

				for (int k = 0; k < M; k++) {
					for (int l = 0; l < N; l++)
						A_temp[k][l] = A[samp_line[k]][l];
				}

				for (int k = 0; k < M; k++) {
					b[k] = 0;
					for (int l = 0; l < N; l++)
						b[k] += A_temp[k][l]*x[l];
				}

				filename_A = "../data/dense_rand/A_" + to_string(M) + "_" + to_string(N) + ".bin";
				filename_x = "../data/dense_rand/x_" + to_string(M) + "_" + to_string(N) + ".bin";
				filename_b = "../data/dense_rand/b_" + to_string(M) + "_" + to_string(N) + ".bin";

				ofstream file_A(filename_A, ios::binary);
				if(file_A.is_open()) {
					for(int k = 0; k < M; k++)
						for (int l = 0; l < N; l++)
							file_A.write(reinterpret_cast<char*>(&A_temp[k][l]), sizeof(A_temp[k][l]));
					file_A.close();
				}
				else {
					cout << "ERROR: Invalid output file for matrix A." << endl;
					delete[] A[0];
					delete[] A;
					delete[] A_temp[0];
					delete[] A_temp;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_x(filename_x, ios::binary);
				if(file_x.is_open()) {
					for (int l = 0; l < N; l++)
						file_x.write(reinterpret_cast<char*>(&x[l]), sizeof(x[l]));
					file_x.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector x." << endl;
					delete[] A[0];
					delete[] A;
					delete[] A_temp[0];
					delete[] A_temp;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_b(filename_b, ios::binary);
				if(file_b.is_open()) {
					for(int k = 0; k < M; k++)
						file_b.write(reinterpret_cast<char*>(&b[k]), sizeof(b[k]));
					file_b.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector b." << endl;
					delete[] A[0];
					delete[] A;
					delete[] A_temp[0];
					delete[] A_temp;
					delete[] x;
					delete[] b;
					exit(1);
				}

				cout << "M = " << M << " and N = " << N << " completed!" << endl;

				delete[] A_temp[0];
				delete[] A_temp;

			}
		}

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;

	return;
}

void genLSDenseSystems() {

	int M_max = 80000;
	int N_max = 10000;

	vector<int> N_values{50, 100, 200, 500, 750, 1000, 2000, 4000, 10000};
	vector<int> M_values{2000, 4000, 20000, 40000, 80000};

	double* aux = new double[(long)M_max*(long)N_max];
	double** A = new double*[(long)M_max];
	for (long i = 0; i < M_max; i++)
		A[i] = &aux[i * N_max];

	default_random_engine gen_mu;
	gen_mu.seed(1);
	uniform_int_distribution<int> dist_mu(-5, 5);

	default_random_engine gen_sigma;
	gen_sigma.seed(2);
	uniform_int_distribution<int> dist_sigma(1, 20);

	int mu;
	int sigma;

	default_random_engine gen;
	gen.seed(3);

	for (int i = 0; i < M_max; i++) {
		mu = dist_mu(gen_mu);
		sigma = dist_sigma(gen_sigma);
		normal_distribution<double> dist(mu,sigma);
		for (int j = 0; j < N_max; j++) {
			A[i][j] = dist(gen);
		}
	}

	mu = dist_mu(gen_mu);
	sigma = dist_sigma(gen_sigma);
	normal_distribution<double> dist(mu,sigma);
	double* x_temp = new double[N_max];
	for (int i = 0; i < N_max; i++)
		x_temp[i] = dist(gen);

	double* b = new double[M_max];

	int M;
	int N;
	double* x = new double[N_max];
	for (int i = 0; i < M_values.size(); i++)
		for (int j = 0; j < N_values.size(); j++) {

			M = M_values[i];
			N = N_values[j];

			if (M/N > 2) {

				mu = 0;
				sigma = 1;
				normal_distribution<double> dist(mu,sigma);

				for (int k = 0; k < M; k++) {
					b[k] = 0;
					for (int l = 0; l < N; l++)
						b[k] += A[k][l]*x_temp[l];
					b[k] += dist(gen);
				}

				int it;
				double* x_sol = cglsSolve(M, N, it, A, b, 1E-15);

				for (int i = 0; i < N; i++)
					x[i] = x_sol[i];

				string filename_A = "../data/ls_dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
				string filename_x = "../data/ls_dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
				string filename_b = "../data/ls_dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";

				ofstream file_A(filename_A, ios::binary);
				if(file_A.is_open()) {
					for(int k = 0; k < M; k++)
						for (int l = 0; l < N; l++)
							file_A.write(reinterpret_cast<char*>(&A[k][l]), sizeof(A[k][l]));
					file_A.close();
				}
				else {
					cout << "ERROR: Invalid output file for matrix A." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_x(filename_x, ios::binary);
				if(file_x.is_open()) {
					for (int l = 0; l < N; l++)
						file_x.write(reinterpret_cast<char*>(&x[l]), sizeof(x[l]));
					file_x.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector x." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_b(filename_b, ios::binary);
				if(file_b.is_open()) {
					for(int k = 0; k < M; k++)
						file_b.write(reinterpret_cast<char*>(&b[k]), sizeof(b[k]));
					file_b.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector b." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				cout << "M = " << M << " and N = " << N << " compleated!" << endl;

				delete[] x_sol;

			}
		}

	delete[] x_temp;

	delete[] A[0];
	delete[] A;
	delete[] x;
	delete[] b;

	return;
}

void genLSDenseSystemsNorm() {

	int M_max = 80000;
	int N_max = 10000;

	vector<int> N_values{50, 100, 200, 500, 750, 1000, 2000, 4000, 10000};
	vector<int> M_values{2000, 4000, 20000, 40000, 80000};

	double* aux = new double[(long)M_max*(long)N_max];
	double** A = new double*[(long)M_max];
	for (long i = 0; i < M_max; i++)
		A[i] = &aux[i * N_max];

	default_random_engine gen;
	gen.seed(1);
	normal_distribution<double> dist(0,1);

	for (int i = 0; i < M_max; i++)
		for (int j = 0; j < N_max; j++) {
			A[i][j] = dist(gen);
		}

	double* x_temp = new double[N_max];
	for (int i = 0; i < N_max; i++)
		x_temp[i] = dist(gen);

	double* b = new double[M_max];

	int M;
	int N;
	double* x = new double[N_max];
	for (int i = 0; i < M_values.size(); i++)
		for (int j = 0; j < N_values.size(); j++) {

			M = M_values[i];
			N = N_values[j];

			if (M/N >= 2) {

				for (int k = 0; k < M; k++) {
					b[k] = 0;
					for (int l = 0; l < N; l++)
						b[k] += A[k][l]*x_temp[l];
					b[k] += dist(gen);
				}

				int it;
				double* x_sol = cglsSolve(M, N, it, A, b, 1E-18);

				for (int i = 0; i < N; i++)
					x[i] = x_sol[i];

				string filename_A = "../data/ls_dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
				string filename_x = "../data/ls_dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
				string filename_b = "../data/ls_dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";

				ofstream file_A(filename_A, ios::binary);
				if(file_A.is_open()) {
					for(int k = 0; k < M; k++)
						for (int l = 0; l < N; l++)
							file_A.write(reinterpret_cast<char*>(&A[k][l]), sizeof(A[k][l]));
					file_A.close();
				}
				else {
					cout << "ERROR: Invalid output file for matrix A." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_x(filename_x, ios::binary);
				if(file_x.is_open()) {
					for (int l = 0; l < N; l++)
						file_x.write(reinterpret_cast<char*>(&x[l]), sizeof(x[l]));
					file_x.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector x." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_b(filename_b, ios::binary);
				if(file_b.is_open()) {
					for(int k = 0; k < M; k++)
						file_b.write(reinterpret_cast<char*>(&b[k]), sizeof(b[k]));
					file_b.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector b." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				cout << "M = " << M << " and N = " << N << " compleated!" << endl;

				delete[] x_sol;

			}
		}

	delete[] x_temp;

	delete[] A[0];
	delete[] A;
	delete[] x;
	delete[] b;

	return;
}

void genCoherentDenseSystems() {

	int M_max = 80000;
	int N_max = 1000;

	vector<int> N_values{1000};
	vector<int> M_values{2000, 4000, 20000, 40000, 80000};

	default_random_engine gen_col_idx;
	gen_col_idx.seed(1);
	uniform_int_distribution<int> dist_col_idx(0, N_max-1);

	default_random_engine gen_col_val;
	gen_col_val.seed(2);
	uniform_int_distribution<int> dist_col_val(2, 20);

	double* aux = new double[(long)M_max*(long)N_max];
	double** A = new double*[(long)M_max];
	for (long i = 0; i < M_max; i++)
		A[i] = &aux[i * N_max];

	int mu = 0;
	int sigma = 1;
	default_random_engine gen;
	gen.seed(3);
	normal_distribution<double> dist(mu,sigma);

	for (int j = 0; j < N_max; j++) {
		A[0][j] = dist(gen);
	}

	for (int i = 1; i < M_max; i++) {
		for (int j = 0; j < N_max; j++) {
			A[i][j] = A[i-1][j];
		}
		for (int k = 0; k < 5; k++)
			A[i][dist_col_idx(gen_col_idx)] = dist_col_val(gen_col_val);
	}

	double* angles = new double[M_max-1];
	for (int i = 1; i < M_max; i++) {
		angles[i] = dotProduct(A[i], A[0], N_max)/sqrt(sqrNorm(A[i], N_max))/sqrt(sqrNorm(A[0], N_max));
		angles[i] = acos(angles[i]);
	}

	string filename_angles = "../data/dense_coherent/angles_" + to_string(M_max) + "_" + to_string(N_max) + ".bin";

	ofstream file_angles(filename_angles, ios::binary);
	if(file_angles.is_open()) {
		for (int l = 0; l < N_max; l++)
			file_angles.write(reinterpret_cast<char*>(&angles[l]), sizeof(angles[l]));
		file_angles.close();
	}
	else {
		cout << "ERROR: Invalid output file for angles." << endl;
		delete[] A[0];
		delete[] A;
		delete[] angles;
		exit(1);
	}

	delete[] angles;

	double* x = new double[N_max];
	for (int i = 0; i < N_max; i++)
		x[i] = dist(gen);

	cout << "Full matrix A and vector b generated!" << endl;

	string filename_A;
	string filename_x;
	string filename_b;

	int M;
	int N;
	double* b = new double[M_max];
	for (int i = 0; i < M_values.size(); i++)
		for (int j = 0; j < N_values.size(); j++) {
			M = M_values[i];
			N = N_values[j];
			if (M/N >= 2) {

				for (int k = 0; k < M; k++) {
					b[k] = 0;
					for (int l = 0; l < N; l++)
						b[k] += A[k][l]*x[l];
				}

				filename_A = "../data/dense_coherent/A_" + to_string(M) + "_" + to_string(N) + ".bin";
				filename_x = "../data/dense_coherent/x_" + to_string(M) + "_" + to_string(N) + ".bin";
				filename_b = "../data/dense_coherent/b_" + to_string(M) + "_" + to_string(N) + ".bin";

				ofstream file_A(filename_A, ios::binary);
				if(file_A.is_open()) {
					for(int k = 0; k < M; k++)
						for (int l = 0; l < N; l++)
							file_A.write(reinterpret_cast<char*>(&A[k][l]), sizeof(A[k][l]));
					file_A.close();
				}
				else {
					cout << "ERROR: Invalid output file for matrix A." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_x(filename_x, ios::binary);
				if(file_x.is_open()) {
					for (int l = 0; l < N; l++)
						file_x.write(reinterpret_cast<char*>(&x[l]), sizeof(x[l]));
					file_x.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector x." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				ofstream file_b(filename_b, ios::binary);
				if(file_b.is_open()) {
					for(int k = 0; k < M; k++)
						file_b.write(reinterpret_cast<char*>(&b[k]), sizeof(b[k]));
					file_b.close();
				}
				else {
					cout << "ERROR: Invalid output file for vector b." << endl;
					delete[] A[0];
					delete[] A;
					delete[] x;
					delete[] b;
					exit(1);
				}

				cout << "M = " << M << " and N = " << N << " completed!" << endl;

			}
		}

	delete[] A[0];
	delete[] A;
	delete[] x;
	delete[] b;

	return;
}