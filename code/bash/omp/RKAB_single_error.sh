#!/bin/bash

# sbatch bash/omp/RKAB_single_error.sh

#SBATCH --job-name="RKAB_single_error"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKAB_single_error.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(1000)
M=(80000)
K=(5 10 50 100 500 1000 10000)
T=(1 2 4 8)
S=(50 20 10 5 1 1)

echo "--- Dense RKAB Single Error ---"

export OMP_NUM_THREADS=1

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for (( i=0; i<6; i++ )) do
				for t in ${T[@]}; do
					str=$(./bin/RKAB_single_seq_newSC.exe dense 1 1E-10 $m $n $t ${K[i]} ${S[i]})
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_single_seq_error.exe dense $m $n $t ${K[i]} $it ${S[i]}
					echo "seq $m $n $t ${K[i]} $it ${S[i]}"
				done
			done
		fi
	done
done