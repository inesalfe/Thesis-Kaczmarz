#!/bin/bash

# sbatch bash/omp/RKA_dist.sh

#SBATCH --job-name="RKA_dist"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKA_dist.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA_dist.txt

echo "--- Dense RKA ---"

for n in ${N[@]}; do
	for m in ${M[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_newSC.exe dense 10 1E-10 $m $n $t 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				export OMP_NUM_THREADS=$t
				./bin/RKA_max_it.exe dense 10 $m $n $it >> outputs/omp/RKA_dist.txt
				echo "par $m $n $t $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_newSC_dist.exe dense 10 1E-10 $m $n $t 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				export OMP_NUM_THREADS=$t
				./bin/RKA_max_it_dist.exe dense 10 $m $n $it >> outputs/omp/RKA_dist.txt
				echo "par $m $n $t $it"
			done
		fi
	done
done