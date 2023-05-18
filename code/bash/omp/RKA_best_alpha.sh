#!/bin/bash

# sbatch bash/omp/RKA_best_alpha.sh

#SBATCH --job-name="RKA_best_alpha"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKA_best_alpha.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA_best_alpha.txt
# rm outputs/omp/RKA_best_alpha_RT.txt

echo "--- Dense RKA ---"

export OMP_NUM_THREADS=1

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			./bin/best_alpha.exe dense $m $n >> outputs/omp/RKA_best_alpha.txt
		fi
	done
done

# for m in ${M[@]}; do
# 	for n in ${N[@]}; do
# 		if [ "$m" -gt "$(( 2*n ))" ]
# 		then
# 			./bin/alpha_RT.exe dense $m $n >> outputs/omp/RKA_best_alpha_RT.txt
# 		fi
# 	done
# done