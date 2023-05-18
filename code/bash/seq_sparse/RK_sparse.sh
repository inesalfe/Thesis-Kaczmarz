#!/bin/bash

# sbatch bash/seq_sparse/RK_sparse.sh

#SBATCH --job-name="RK_sparse"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_sparse.txt

#SBATCH --nodes=1
#SBATCH --exclusive

export OMP_NUM_THREADS=1

N=(1000)
M=(80000)
D=(1 2 5 8 10 20 30 50)

echo "--- Remove Old Files ---"

rm outputs/seq_sparse/RK_sparse.txt

echo "--- RK Dense Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			for d in ${D[@]}; do
				./bin/sparse_full.exe RK sparse 100 1E-10 $m $n $d >> outputs/seq_sparse/RK_sparse.txt
				echo "RK sparse_full $m $n $d"
				./bin/sparse_csr.exe RK sparse 100 1E-10 $m $n $d >> outputs/seq_sparse/RK_sparse.txt
				echo "RK sparse_csr $m $n $d"
			done
		fi
	done
done