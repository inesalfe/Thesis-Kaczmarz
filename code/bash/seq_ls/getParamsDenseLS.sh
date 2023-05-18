#!/bin/bash

# sbatch bash/seq_ls/getParamsDenseLS.sh

#SBATCH --job-name="getParamsDenseLS"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/getParamsDenseLS.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/seq_ls/ParamsDenseLS.txt

echo "--- Params LS Dense ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -ge "$n" ]
		then	
			export OMP_NUM_THREADS=1
			echo "$m $n" >> outputs/seq_ls/ParamsDenseLS.txt
			./bin/params_ls_dense.exe ls_dense $m $n >> outputs/seq_ls/ParamsDenseLS.txt
			echo "" >> outputs/seq_ls/ParamsDenseLS.txt
			echo "ls_dense $m $n"
		fi
	done
done