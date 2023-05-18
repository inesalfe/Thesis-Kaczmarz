#!/bin/bash

# sbatch bash/omp/RKA_error_alpha.sh

#SBATCH --job-name="RKA_error_alpha"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKA_error_alpha.txt

#SBATCH --nodes=1
#SBATCH --exclusive

echo "--- Dense RKA ---"

export OMP_NUM_THREADS=1
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 1 30000 1 100
echo "80000 1000 1 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 2 30000 1.99864 100
echo "80000 1000 2 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 4 30000 3.99183 100
echo "80000 1000 4 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 8 30000 7.96199 100
echo "80000 1000 8 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 20 30000 17.6439 100
echo "80000 1000 20 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 50 30000 23.4318 100
echo "80000 1000 50 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 100 30000 26.3085 100
echo "80000 1000 100 30000 100"

export OMP_NUM_THREADS=1
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 1 30000 1 100
echo "80000 1000 1 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 2 30000 1 100
echo "80000 1000 2 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 4 30000 2 100
echo "80000 1000 4 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 8 30000 4 100
echo "80000 1000 8 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 20 30000 10 100
echo "80000 1000 20 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 50 30000 25 100
echo "80000 1000 50 30000 100"
./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 100 30000 50 100
echo "80000 1000 100 30000 100"