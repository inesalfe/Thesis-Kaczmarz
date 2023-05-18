#!/bin/bash

# sbatch bash/omp/RKAB_single_alpha.sh

#SBATCH --job-name="RKAB_single_alpha"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKAB_single_alpha.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)
K=(5 10 50 100 500 1000 10000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_single_alpha.txt

echo "--- Dense RKAB Single ---"

line=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for t in ${T[@]}; do
					export OMP_NUM_THREADS=1
					str="$(sed "${line}q;d" outputs/omp/RKAB_single_best_alpha.txt)"
					IFS=' ' read -r -a arr <<< "$str"
					alpha=${arr[3]}
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_single_seq_newSC_alpha.exe dense 10 1E-10 $m $n $t $k $alpha 1)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_single_seq_max_it_alpha.exe dense 10 $m $n $t $k $alpha $it >> outputs/omp/RKAB_single_alpha.txt
					echo "seq $m $n $t $k $it"
					export OMP_NUM_THREADS=$t
					./bin/RKAB_single_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_alpha.txt
					echo "par $m $n $t $k $it"
					((line++))
				done
				((line--))
				((line--))
				((line--))
				((line--))
			done
			((line++))
			((line++))
			((line++))
			((line++))
			((line++))
			((line++))
			((line++))
		fi
	done
done