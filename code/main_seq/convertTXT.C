#include "kacz.h"
#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <omp.h>
#include <iomanip>
using namespace std;

// ./bin/convertTXT.exe 2000 100

int main (int argc, char *argv[]) {

	if(argc != 3) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'./bin/convertTXT.exe <M> <N>'" << endl;
		exit(1);
	}

	int M = atoi(argv[1]);
	int N = atoi(argv[2]);

	string filename_A_bin = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
	string filename_b_bin = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
	string filename_x_bin = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";

	convertMatrixTXT(M, N, filename_A_bin);
	convertbVectorTXT(M, filename_b_bin);
	convertxVectorTXT(N, filename_x_bin);

	// string filename_A_txt = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".txt";
	// string filename_b_txt = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".txt";
	// string filename_x_txt = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".txt";

	// double** A_bin;
	// double* b_bin;
	// double* x_bin;

	// importDenseSystemBIN(M, N, filename_A_bin, filename_b_bin, filename_x_bin, A_bin, b_bin, x_bin);

	// double** A_txt;
	// double* b_txt;
	// double* x_txt;

	// importDenseSystemTXT(M, N, filename_A_txt, filename_b_txt, filename_x_txt, A_txt, b_txt, x_txt);

	// cout << std::setprecision(std::numeric_limits<double>::digits10+1);

	// cout << A_txt[2][99] << " " << A_bin[2][99] << endl;
	// cout << A_txt[1500][0] << " " << A_bin[1500][0] << endl;
	// cout << A_txt[0][50] << " " << A_bin[0][50] << endl;
	// cout << A_txt[1999][49] << " " << A_bin[1999][49] << endl;

	// cout << x_txt[99] << " " << x_bin[99] << endl;
	// cout << x_txt[0] << " " << x_bin[0] << endl;
	// cout << x_txt[50] << " " << x_bin[50] << endl;
	// cout << x_txt[49] << " " << x_bin[49] << endl;

	// cout << b_txt[2] << " " << b_bin[2] << endl;
	// cout << b_txt[1500] << " " << b_bin[1500] << endl;
	// cout << b_txt[0] << " " << b_bin[0] << endl;
	// cout << b_txt[1999] << " " << b_bin[1999] << endl;

	// delete[] A_bin[0];
	// delete[] A_bin;
	// delete[] b_bin;
	// delete[] x_bin;

	// delete[] A_txt[0];
	// delete[] A_txt;
	// delete[] b_txt;
	// delete[] x_txt;

	return 0;
}