#!/bin/bash

# sbatch bash/seq/RK_quasirand.sh

#SBATCH --job-name="RK_quasirand"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_quasirand.txt

#SBATCH --nodes=1
#SBATCH --exclusive

export OMP_NUM_THREADS=1

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/seq/RK_quasirand.txt
rm outputs/seq/RK_quasirand_it.txt

echo "--- RK_quasirand Dense Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			./bin/rand_full.exe RK_quasirand dense 10 1E-10 $m $n 1000 >> outputs/seq/RK_quasirand.txt
			echo "RK_quasirand dense $m $n"
		fi
	done
done

echo "--- RK_quasirand Dense Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			./bin/rand_full.exe RK_quasirand dense 5 1E-10 $m $n 20 >> outputs/seq/RK_quasirand_it.txt
			echo "RK_quasirand dense $m $n"
		fi
	done
done