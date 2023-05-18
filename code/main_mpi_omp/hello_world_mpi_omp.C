#include <iostream>
#include <mpi.h>
#include <omp.h>
#include <sched.h>
using namespace std;

int np;
int id;
int num_threads;
int t_id;
int len;
char name[MPI_MAX_PROCESSOR_NAME];

int main (int argc, char *argv[]) {

	MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &id);
    MPI_Comm_size(MPI_COMM_WORLD, &np);
    MPI_Get_processor_name(name, &len);

    if (!id) {
    	printf("MPI tasks: %d.\n", np); fflush(stdout);
    }

	#pragma omp parallel
	{
		num_threads = omp_get_num_threads();
		#pragma omp single
			if (!id) {
				printf("OpenMP Threads: %d.\n", num_threads); fflush(stdout);
			}
		t_id = omp_get_thread_num();
		printf("Machine name: %s, CPU ID: %d, Process id: %d, Thread id: %d.\n", name, sched_getcpu(), id, t_id); fflush(stdout);
	}

	MPI_Finalize();

}