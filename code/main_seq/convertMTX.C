#include "kacz.h"
#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
using namespace std;

int main (int argc, char *argv[]) {

	if(argc != 3) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/convertMTX.exe <M> <N>'" << endl;
		exit(1);
	}

	int M = atoi(argv[1]);
	int N = atoi(argv[2]);

	string filename = "../data/sparse_real/A_" + to_string(M) + "_" + to_string(N) + ".mtx";
	string folder_out = "../data/sparse_real";

	int NNZ;
	// convertMTXtoCSC_BIN(M, N, NNZ, filename, folder_out);
	convertMTXtoCSR_BIN(M, N, NNZ, filename, folder_out);

	filename = "../data/sparse_real/x_" + to_string(M) + "_" + to_string(N) + ".txt";
	convertxVectorBIN(N, filename);
	filename = "../data/sparse_real/b_" + to_string(M) + "_" + to_string(N) + ".txt";
	convertbVectorBIN(M, filename);

	return 0;
}