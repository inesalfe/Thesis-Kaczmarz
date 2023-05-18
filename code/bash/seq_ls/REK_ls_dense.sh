#!/bin/bash

# sbatch bash/seq_ls/REK_ls_dense.sh

#SBATCH --job-name="REK_ls_dense"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/REK_ls_dense.txt

#SBATCH --nodes=1
#SBATCH --exclusive

echo "--- Remove Old Files ---"

rm outputs/seq_ls/REK_ls_dense.txt

echo "--- REK_errorSC Dense Full ---"

export OMP_NUM_THREADS=1

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
			then
			./bin/ls_full.exe REK_errorSC ls_dense 10 1E-10 $m $n >> outputs/seq_ls/REK_ls_dense.txt
			echo "REK_errorSC ls_dense $m $n $it"
		fi
	done
done