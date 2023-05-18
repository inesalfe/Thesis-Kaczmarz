#!/bin/bash

# sbatch bash/mpi/best_alpha.sh

#SBATCH --job-name="best_alpha"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/best_alpha.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/mpi/RKA_alpha.txt

echo "--- Dense RKA ---"

export OMP_NUM_THREADS=1

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			./bin/best_alpha_mpi.exe dense $m $n >> outputs/mpi/RKA_alpha.txt
		fi
	done
done