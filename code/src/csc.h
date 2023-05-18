#ifndef _CSC_
#define _CSC_
#include <string>
#include <vector>
using namespace std;

typedef struct 
{
	int col;
	int row;
	double value;
} CSC;

struct col_equal
{
	explicit col_equal(const int s) : col(s) {}

	bool operator () (const CSC& csc) const
	{
		return csc.col == col;
	}

	int col;
};

double sqrNormCol(int& n, int*& col_idx, int*& rows, double*& values);

double dotProductCSC(int& n, int*& col_idx, int*& rows, double*& values, double*& vector);

void scaleVecCol(int& n, int*& col_idx, int*& rows, double*& values, double& scale, double*& vector);

void deleteColsZeros(int& N, int*& col_idx);

#endif