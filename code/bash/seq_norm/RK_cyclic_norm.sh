#!/bin/bash

# sbatch bash/seq_norm/RK_cyclic_norm.sh

#SBATCH --job-name="RK_cyclic_norm"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_cyclic_norm.txt

#SBATCH --nodes=1
#SBATCH --exclusive

export OMP_NUM_THREADS=1

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/seq_norm/RK_cyclic_norm.txt
rm outputs/seq_norm/RK_cyclic_norm_it.txt

echo "--- RK_cyclic Dense Norm Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			./bin/rand_full.exe RK_cyclic dense_norm 10 1E-10 $m $n 1000 >> outputs/seq_norm/RK_cyclic_norm.txt
			echo "RK_cyclic dense_norm $m $n"
		fi
	done
done

echo "--- RK_cyclic Dense Norm Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			./bin/rand_full.exe RK_cyclic dense_norm 5 1E-10 $m $n 20 >> outputs/seq_norm/RK_cyclic_norm_it.txt
			echo "RK_cyclic dense_norm $m $n"
		fi
	done
done