#!/bin/bash

# sbatch bash/omp/RK_partial_block.sh

#SBATCH --job-name="RK_partial_block"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_partial_block.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
K=(5 10 50 100 500)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RK_partial_block.txt

echo "--- Dense RK_partial_block ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for t in ${T[@]}; do
					export OMP_NUM_THREADS=$t
					./bin/RK_partial_block_newSC.exe dense 10 1E-10 $m $n $k 1000 >> outputs/omp/RK_partial_block.txt
					echo "par $m $n $t $k"
				done
			done
		fi
	done
done