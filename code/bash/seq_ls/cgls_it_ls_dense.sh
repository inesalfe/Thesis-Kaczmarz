#!/bin/bash

# sbatch bash/seq_ls/cgls_it_ls_dense.sh

#SBATCH --job-name="cgls_it_ls_dense"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/cgls_it_ls_dense.txt

#SBATCH --nodes=1
#SBATCH --exclusive

echo "--- Remove Old Files ---"

rm outputs/seq_ls/cgls_it_ls_dense.txt

echo "--- Dense CGLS ---"

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			str=$(./bin/cgls_eigen_find_it_newSC.exe ls_dense $m $n 1E-10)
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[2]}
			wait
			echo "$m $n $it" >> outputs/seq_ls/cgls_it_ls_dense.txt
		fi
	done
done