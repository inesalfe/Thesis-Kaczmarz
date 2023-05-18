#!/bin/bash

# sbatch bash/seq_coherent/RK_quasirand_coherent.sh

#SBATCH --job-name="RK_quasirand_coherent"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_quasirand_coherent.txt

#SBATCH --nodes=1
#SBATCH --exclusive

export OMP_NUM_THREADS=1

N=(1000)
M=(2000 4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/seq_coherent/RK_quasirand_coherent.txt
rm outputs/seq_coherent/RK_quasirand_coherent_it.txt

echo "--- RK_quasirand_coherent Dense Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			./bin/rand_full.exe RK_quasirand dense_coherent 10 1E-10 $m $n 1000 >> outputs/seq_coherent/RK_quasirand_coherent.txt
			echo "RK_quasirand_coherent dense_coherent $m $n"
		fi
	done
done

echo "--- RK_quasirand_coherent Dense Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			./bin/rand_full.exe RK_quasirand dense_coherent 5 1E-10 $m $n 20 >> outputs/seq_coherent/RK_quasirand_coherent_it.txt
			echo "RK_quasirand_coherent dense_coherent $m $n"
		fi
	done
done