#!/bin/bash

# sbatch bash/seq/cgls_it_M_20000.sh

#SBATCH --job-name="cgls_it_M_20000"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/cgls_it_M_20000.txt

#SBATCH --nodes=1
#SBATCH --exclusive

echo "--- Remove Old Files ---"

rm outputs/seq/cgls_it_M_20000.txt

echo "--- Dense CGLS ---"

N=(50 100 200 500 750 1000 2000 4000)
M=(20000)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
		then	
			export OMP_NUM_THREADS=1
			str=$(./bin/cgls_eigen_find_it.exe dense $m $n 1E-10)
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[2]}
			wait
			echo "$m $n $it" >> outputs/seq/cgls_it_M_20000.txt
		fi
	done
done