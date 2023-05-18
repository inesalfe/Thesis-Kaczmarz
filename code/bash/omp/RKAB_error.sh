#!/bin/bash

# sbatch bash/omp/RKAB_error.sh

#SBATCH --job-name="RKAB_error"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKAB_error.txt

#SBATCH --nodes=1
#SBATCH --exclusive

echo "--- Dense RKAB ---"

export OMP_NUM_THREADS=1
./bin/RKAB_single_seq_error.exe ls_dense 80000 1000 1 1000 50 1
echo "80000 1000 1 1000 50 1"
./bin/RKAB_single_seq_error.exe ls_dense 80000 1000 2 1000 50 1
echo "80000 1000 2 1000 50 1"
./bin/RKAB_single_seq_error.exe ls_dense 80000 1000 4 1000 50 1
echo "80000 1000 4 1000 50 1"
./bin/RKAB_single_seq_error.exe ls_dense 80000 1000 8 1000 50 1
echo "80000 1000 8 1000 50 1"
./bin/RKAB_single_seq_error.exe ls_dense 80000 1000 20 1000 50 1
echo "80000 1000 20 1000 50 1"
./bin/RKAB_single_seq_error.exe ls_dense 80000 1000 50 1000 50 1
echo "80000 1000 50 1000 50 1"
./bin/RKAB_single_seq_error.exe ls_dense 80000 1000 100 1000 50 1
echo "80000 1000 100 1000 50 1"