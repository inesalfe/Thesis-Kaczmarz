#!/bin/bash

# sbatch bash/omp/RK_partial.sh

#SBATCH --job-name="RK_partial"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_partial.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RK_partial.txt

echo "--- Dense RK_partial ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=$t
				./bin/RK_partial_newSC.exe dense 10 1E-10 $m $n 1000 >> outputs/omp/RK_partial.txt
				echo "par $m $n $t"
			done
		fi
	done
done