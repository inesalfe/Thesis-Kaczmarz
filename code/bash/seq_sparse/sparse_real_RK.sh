#!/bin/bash

# sbatch bash/seq_sparse/sparse_real_RK.sh

#SBATCH --job-name="sparse_real_RK"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/sparse_real_RK.txt

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

export OMP_NUM_THREADS=1

echo "--- Remove Old Files ---"

rm outputs/seq_sparse/sparse_real_RK.txt

echo "RK"

./bin/real_csr.exe RK 5 1E-2 4200 630 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 4200 630"
./bin/real_csr.exe RK 5 1E-2 1260 378 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 1260 378"
./bin/real_csr.exe RK 5 1E-2 10160 1740 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 10160 1740"
./bin/real_csr.exe RK 5 1E-2 12600 4200 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 12600 4200"
./bin/real_csr.exe RK 5 1E-2 16728 7176 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 16728 7176"
./bin/real_csr.exe RK 5 1E-2 71952 2704 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 71952 2704"
./bin/real_csr.exe RK 5 1E-2 20058 5970 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 20058 5970"
./bin/real_csr.exe RK 5 1E-2 171369 47271 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 171369 47271"
./bin/real_csr.exe RK 5 1E-2 477976 1600 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 477976 1600"
./bin/real_csr.exe RK 5 1E-2 1748122 62729 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 1748122 62729"
./bin/real_csr.exe RK 5 1E-2 5921786 274669 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 5921786 274669"
./bin/real_csr.exe RK 5 1E-2 1548649 955128 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 1548649 955128"
./bin/real_csr.exe RK 5 1E-2 9746232 549336 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 9746232 549336"
./bin/real_csr.exe RK 5 1E-2 2111154 801374 >> outputs/seq_sparse/sparse_real_RK.txt
echo "RK 2111154 801374"