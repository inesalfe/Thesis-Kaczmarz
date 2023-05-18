#!/bin/bash

# sbatch bash/seq_ls/REK_ls_dense_max_it.sh

#SBATCH --job-name="REK_ls_dense_max_it"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/REK_ls_dense_max_it.txt

#SBATCH --nodes=1
#SBATCH --exclusive

loop_variable=10
N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/seq_ls/REK_ls_dense_max_it.txt

echo "--- Dense CGLS ---"

line=0
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			((line++))
			str="$(sed "${line}q;d" outputs/seq_ls/REK_ls_dense.txt)"
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			wait
			./bin/ls_full_max_it.exe REK_max_it ls_dense 10 $m $n $it >> outputs/seq_ls/REK_ls_dense_max_it.txt
			echo "REK_max_it ls_dense $m $n $it"
		fi
	done
done