#!/bin/bash

# sbatch bash/omp/RKAB_single_uni_speedup.sh

#SBATCH --job-name="RKAB_single_uni_speedup"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKAB_single_uni_speedup.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_single_uni_speedup.txt

echo "--- Dense RKAB Single ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC.exe dense 10 1E-10 $m $n $t $n 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it.exe dense 10 $m $n $t $n $it >> outputs/omp/RKAB_single_uni_speedup.txt
				echo "seq $m $n $t $n $it"
				export OMP_NUM_THREADS=$t
				./bin/RKAB_single_uni_max_it.exe dense 10 $m $n $n $it >> outputs/omp/RKAB_single_uni_speedup.txt
				echo "par $m $n $t $n $it"
			done
		fi
	done
done