#!/bin/bash

# sbatch bash/omp/RKAB_single.sh

#SBATCH --job-name="RKAB_single"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKAB_single.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)
K=(5 10 50 100 500 1000 10000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_single.txt

echo "--- Dense RKAB Single ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				# if [ "$m" -ge "$(( 8*k ))" ]
				# then
					for t in ${T[@]}; do
						export OMP_NUM_THREADS=1
						str=$(./bin/RKAB_single_seq_newSC.exe dense 10 1E-10 $m $n $t $k 1)
						IFS=' ' read -r -a arr <<< "$str"
						it=${arr[3]}
						./bin/RKAB_single_seq_max_it.exe dense 10 $m $n $t $k $it >> outputs/omp/RKAB_single.txt
						echo "seq $m $n $t $k $it"
						export OMP_NUM_THREADS=$t
						./bin/RKAB_single_max_it.exe dense 10 $m $n $k $it >> outputs/omp/RKAB_single.txt
						echo "par $m $n $t $k $it"
					done
				# fi
			done
		fi
	done
done