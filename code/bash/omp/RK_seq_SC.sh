#!/bin/bash

# sbatch bash/omp/RK_seq_SC.sh

#SBATCH --job-name="RK_seq_SC"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_seq_SC.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/seq/RK_seq_SC.txt

echo "--- Dense RK ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			str=$(./bin/RK_seq.exe dense 10 1E-10 $m $n 1000)
			echo "$str" >> outputs/seq/RK_seq_SC.txt
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			./bin/RK_seq_max_it.exe dense 10 $m $n $it >> outputs/seq/RK_seq_SC.txt
			echo "seq $m $n $it"
		fi
	done
done