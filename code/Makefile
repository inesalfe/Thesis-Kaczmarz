all: seq eigen omp omp_csr sc ct ct_csr mpi mpi_omp tomo

seq:
	make -f makefile.seq

eigen:
	make -f makefile.eigen

omp:
	make -f makefile.omp

omp_csr:
	make -f makefile.omp_csr

sc:
	make -f makefile.sc

ct:
	make -f makefile.ct

ct_csr:
	make -f makefile.ct_csr

mpi:
	make -f makefile.mpi

mpi_omp:
	make -f makefile.mpi_omp

tomo:
	make -f makefile.tomo

clean:
	rm -fv bin/*.o bin/*.exe
