#!/bin/bash

# sbatch bash/omp/RKA_error.sh

#SBATCH --job-name="RKA_error"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKA_error.txt

#SBATCH --nodes=1
#SBATCH --exclusive

echo "--- Dense RKA ---"

export OMP_NUM_THREADS=1
./bin/RKA_seq_error.exe ls_dense 80000 1000 1 500000 100
echo "80000 1000 1 500000 100"
./bin/RKA_seq_error.exe ls_dense 80000 1000 2 500000 100
echo "80000 1000 2 500000 100"
./bin/RKA_seq_error.exe ls_dense 80000 1000 4 500000 100
echo "80000 1000 4 500000 100"
./bin/RKA_seq_error.exe ls_dense 80000 1000 8 500000 100
echo "80000 1000 8 500000 100"
./bin/RKA_seq_error.exe ls_dense 80000 1000 20 500000 100
echo "80000 1000 20 500000 100"
./bin/RKA_seq_error.exe ls_dense 80000 1000 50 500000 100
echo "80000 1000 50 500000 100"
./bin/RKA_seq_error.exe ls_dense 80000 1000 100 500000 100
echo "80000 1000 100 500000 100"