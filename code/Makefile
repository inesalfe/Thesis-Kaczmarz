all: seq eigen omp omp_csr tomo

seq:
	make -f makefile.seq

eigen:
	make -f makefile.eigen

omp:
	make -f makefile.omp

omp_csr:
	make -f makefile.omp_csr

tomo:
	make -f makefile.tomo

mpi:
	make -f makefile.mpi

mpi_omp:
	make -f makefile.mpi_omp

clean:
	rm -fv bin/*.o bin/*.exe
