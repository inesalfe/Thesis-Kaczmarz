#!/bin/bash

# sbatch bash/seq_sparse/params_sparse_real.sh

#SBATCH --job-name="params_sparse_real"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/params_sparse_real.txt

#SBATCH --nodes=1
#SBATCH --exclusive

echo "--- Remove Old Files ---"

rm outputs/seq_sparse/params_sparse_real.txt

echo "SPARSE REAL"

./bin/params_sparse_real.exe 4200 630 >> outputs/seq_sparse/params_sparse_real.txt
echo "4200 630"
./bin/params_sparse_real.exe 1260 378 >> outputs/seq_sparse/params_sparse_real.txt
echo "1260 378"
./bin/params_sparse_real.exe 10160 1740 >> outputs/seq_sparse/params_sparse_real.txt
echo "10160 1740"
./bin/params_sparse_real.exe 12600 4200 >> outputs/seq_sparse/params_sparse_real.txt
echo "12600 4200"
./bin/params_sparse_real.exe 16728 7176 >> outputs/seq_sparse/params_sparse_real.txt
echo "16728 7176"
./bin/params_sparse_real.exe 71952 2704 >> outputs/seq_sparse/params_sparse_real.txt
echo "71952 2704"
./bin/params_sparse_real.exe 20058 5970 >> outputs/seq_sparse/params_sparse_real.txt
echo "20058 5970"
./bin/params_sparse_real.exe 171369 47271 >> outputs/seq_sparse/params_sparse_real.txt
echo "171369 47271"
./bin/params_sparse_real.exe 477976 1600 >> outputs/seq_sparse/params_sparse_real.txt
echo "477976 1600"
./bin/params_sparse_real.exe 2111154 801374 >> outputs/seq_sparse/params_sparse_real.txt
echo "2111154 801374"
./bin/params_sparse_real.exe 1548649 955128 >> outputs/seq_sparse/params_sparse_real.txt
echo "1548649 955128"
./bin/params_sparse_real.exe 9746232 549336 >> outputs/seq_sparse/params_sparse_real.txt
echo "9746232 549336"
./bin/params_sparse_real.exe 5921786 274669 >> outputs/seq_sparse/params_sparse_real.txt
echo "5921786 274669"
./bin/params_sparse_real.exe 1748122 62729 >> outputs/seq_sparse/params_sparse_real.txt
echo "1748122 62729"