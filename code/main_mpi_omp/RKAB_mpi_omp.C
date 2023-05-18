#include "aux_func.h"
#include <iostream>
#include <math.h>
#include <mpi.h>
#include <omp.h>
#include <random>
#include <fstream>
#include <sstream>
using namespace std;

// mpic++ -o bin/RKAB_mpi_omp_max_it.exe main/RKAB_mpi_omp_max_it.C
// mpirun -np 2 ./bin/RKAB_mpi_omp_max_it.exe dense 1 1E-10 2000 100 20

#define BLOCK_LOW(id, p, np) ((id) * (np) / (p))
#define BLOCK_HIGH(id, p, np) (BLOCK_LOW((id) + 1, p, np) - 1)
#define BLOCK_SIZE(id, p, np) (BLOCK_HIGH(id, p, np) - BLOCK_LOW(id, p, np) + 1)

int np;
int id;
int t_id;
int M_size;
int* M_size_vector;

int M;
int N;

double* b;
double* x;
double* x_sol;
double** A;
double* x_k;
double* x_k_thread;

int n_runs;
double eps;
int num_threads;
int block_size;
long long max_it_stop;

double start_total;
double stop_total;
double duration_total;
double start; 
double stop;
double duration;

vector<double> sqrNorm_line;
discrete_distribution<> dist;

double dif;
double norm_dif;
double scale;
int line;
long long it;
long long avg_it;
long long it_final;
bool solution_found;

void importMPIDenseSystemBIN(int M, int N, string A_filename, string b_filename, string x_filename, double**& A, double*& b, double*& x) {

	ifstream file_A;
	file_A.open(A_filename, ios::binary);
	if (!file_A.is_open()) {
		cout << "Error in opening the matrix file" << endl;
		exit(1);
	}

	double * aux = new double[(long)M_size*(long)N];
	A = new double*[(long)M_size];
	for (long i = 0; i < M_size; i++)
		A[i] = &aux[i * N];

	double temp;
	for (long i = 0; i < M; i++) {
		if (i >= BLOCK_LOW(id, np, M) && i <= BLOCK_HIGH(id, np, M))
			for (long j = 0; j < N; j++) 
				file_A.read(reinterpret_cast<char *>(&A[i-BLOCK_LOW(id, np, M)][j]), sizeof(A[i-BLOCK_LOW(id, np, M)][j]));
		else
			for (long j = 0; j < N; j++) 
				file_A.read(reinterpret_cast<char *>(&temp), sizeof(temp));
	}

	file_A.close();

	ifstream file_b;
	file_b.open(b_filename, ios::binary);
	if (!file_b.is_open()) {
		cout << "Error in opening the b vector file" << endl;
		delete[] A[0];
		delete[] A;
		exit(1);
	}

	b = new double[M_size];

	for (long i = 0; i < M; i++) {
		if (i >= BLOCK_LOW(id, np, M) && i <= BLOCK_HIGH(id, np, M))
			file_b.read(reinterpret_cast<char *>(&b[i-BLOCK_LOW(id, np, M)]), sizeof(b[i-BLOCK_LOW(id, np, M)]));
		else
			file_b.read(reinterpret_cast<char *>(&temp), sizeof(temp));
	}

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

	for (long i = 0; i < N; i++)
		file_x.read(reinterpret_cast<char *>(&x[i]), sizeof(x[i]));

	file_x.close();
}

int main (int argc, char *argv[]) {

	MPI_Init(&argc, &argv);

	MPI_Barrier(MPI_COMM_WORLD);
	start_total = MPI_Wtime();

    MPI_Comm_rank(MPI_COMM_WORLD, &id);
    MPI_Comm_size(MPI_COMM_WORLD, &np);

	if(argc != 8) {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'mpirun -np <nproc> ./bin/RKAB_mpi_omp.exe <data_set> <n_runs> <eps> <M> <N> <block_size> <max_it_stop>'" << endl;
		exit(1);
	}

	n_runs = atoi(argv[2]);
	eps = atof(argv[3]);

	M = atoi(argv[4]);
	N = atoi(argv[5]);
	block_size = atoi(argv[6]);
	max_it_stop = atoll(argv[7]);

	M_size = BLOCK_SIZE(id, np, M);

	M_size_vector = new int[np];
	for (int i = 0; i < np; i++)
		M_size_vector[i] = 0;
	M_size_vector[id] = M_size;

	string matrix_type = argv[1];
	string filename_A;
	string filename_b;
	string filename_x;
	if (matrix_type.compare("dense") == 0) {
		filename_A = "../data/dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importMPIDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("dense_norm") == 0) {
		filename_A = "../data/dense_norm/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/dense_norm/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/dense_norm/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importMPIDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else if (matrix_type.compare("ls_dense") == 0) {
		filename_A = "../data/ls_dense/A_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_b = "../data/ls_dense/b_" + to_string(M) + "_" + to_string(N) + ".bin";
		filename_x = "../data/ls_dense/x_" + to_string(M) + "_" + to_string(N) + ".bin";
		importMPIDenseSystemBIN(M, N, filename_A, filename_b, filename_x, A, b, x);
	}
	else {
		cout << "Incorrect number of arguments: Corret usage is ";
		cout << "'mpirun -np <nproc> ./bin/RKAB_mpi_omp.exe <data_set> <n_runs> <eps> <M> <N> <block_size> <max_it_stop>'" << endl;
		exit(1);
	}

	sqrNorm_line = vector<double>(M_size);
	for (int i = 0; i < M_size; i++) {
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

	dist = discrete_distribution<>(sqrNorm_line.begin(), sqrNorm_line.end());

	x_k = new double[N];
	x_sol = new double[N];
	for (int i = 0; i < N; i++) {
		x_sol[i] = 0;
	}
	duration = 0;
	avg_it = 0;

	#pragma omp parallel private(line, scale, t_id, it, x_k_thread)
	{
		x_k_thread = new double[N];
		num_threads = omp_get_num_threads();
		t_id = omp_get_thread_num();
		for(int run = 0; run < n_runs; run++) {
			mt19937 generator(np*run*num_threads+id*np+t_id+1);
			#pragma omp for
				for (int i = 0; i < N; i++) {
					x_k[i] = 0;
				}
			it = 0;
			#pragma omp single
			{
				solution_found = false;
				MPI_Barrier(MPI_COMM_WORLD);
				start = MPI_Wtime();			
			}
			while(!solution_found) {
				it++;
				line = dist(generator);
				scale = (b[line]-dotProduct(A[line], x_k, N))/sqrNorm_line[line];
				for (int i = 0; i < N; i++) {
					x_k_thread[i] = x_k[i] + scale * A[line][i];
				}
				for (int k = 0; k < block_size-1; k++) {
					line = dist(generator);
					scale = (b[line]-dotProduct(A[line], x_k_thread, N))/sqrNorm_line[line];
					for (int i = 0; i < N; i++) {
						x_k_thread[i] += scale * A[line][i];
					}
				}
				for (int i = 0; i < N; i++) {
					x_k_thread[i] -= x_k[i];
				}
				#pragma omp barrier
				#pragma omp critical
					for (int i = 0; i < N; i++) {
			            x_k[i] += x_k_thread[i]/num_threads;
					}
				#pragma omp barrier
				#pragma omp for
					for (int i = 0; i < N; i++) {
			            x_k[i] /= np;
					}
				#pragma omp single
					MPI_Allreduce(MPI_IN_PLACE, x_k, N, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD);
				if (it%max_it_stop == 0) {
					#pragma omp single
						norm_dif = 0;
					#pragma omp for reduction(+:norm_dif)
						for (int i = 0; i < N; i++) {
							dif = x_k[i] - x[i];
							norm_dif += dif*dif;
						}
					#pragma omp single
						if (norm_dif < eps) {
							it_final = it;
							solution_found = true;
						}
				}
			}
			#pragma omp single
			{
				stop = MPI_Wtime();
				MPI_Barrier(MPI_COMM_WORLD);
				if (!id) {
					duration += stop - start;
					for (int i = 0; i < N; i++) {
						x_sol[i] += x_k[i];
					}
					avg_it += it_final;
				}
			}
		}
		delete[] x_k_thread;
	}

	if (!id) {

		avg_it /= n_runs;

		cout << M << " " << N << " " << duration << " " << avg_it << " ";

		for (int i = 0; i < N; i++) {
			x_sol[i] /= n_runs;
		}

		stop_total = MPI_Wtime();
		duration_total = stop_total - start_total;

		cout << sqrt(sqrNormDiff(x_sol, x, N)) << " " << duration_total << endl;

	}

	delete[] x_k;

	delete[] A[0];
	delete[] A;
	delete[] b;
	delete[] x;
	delete[] x_sol;

	delete[] M_size_vector;

	MPI_Finalize();

}