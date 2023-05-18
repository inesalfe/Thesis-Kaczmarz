#ifndef _CG_
#define _CG_

#include <vector>

double* cgSolve(int dim, double**& A, double*& b, double eps);

double* cglsSolve(int M, int N, int& it, double**& A, double*& b, double eps);

#endif
