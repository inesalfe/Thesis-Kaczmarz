#!/bin/bash

# sbatch bash/seq_norm/RK_norm_CG.sh

#SBATCH --job-name="RK_norm_CG"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_norm_CG.txt

#SBATCH --nodes=1
#SBATCH --exclusive

export OMP_NUM_THREADS=1

echo "--- Remove Old Files ---"

rm outputs/seq_norm/RK_norm_CG_N_1000.txt
rm outputs/seq_norm/RK_norm_CG_M_20000.txt

echo "--- RK Dense Norm Full CG ---"

N=(1000)
M=(2000 4000 20000 40000 80000)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			str=$(./bin/RK_seq.exe dense_norm 10 1E-10 $m $n 1)
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			./bin/RK_seq_max_it.exe dense_norm 10 $m $n $it >> outputs/seq_norm/RK_norm_CG_N_1000.txt
			echo "RK dense_norm $m $n $it"
		fi
	done
done

N=(50 100 200 500 750 1000 2000 4000)
M=(20000)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			str=$(./bin/RK_seq.exe dense_norm 10 1E-10 $m $n 1)
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			./bin/RK_seq_max_it.exe dense_norm 10 $m $n $it >> outputs/seq_norm/RK_norm_CG_M_20000.txt
			echo "RK dense_norm $m $n $it"
		fi
	done
done