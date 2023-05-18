#!/bin/bash

# sbatch bash/seq/GSSRK_N_1000.sh

#SBATCH --job-name="GSSRK_N_1000"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/GSSRK_N_1000.txt

#SBATCH --nodes=1
#SBATCH --exclusive

export OMP_NUM_THREADS=1

N=(1000)
M=(2000 4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/seq/GSSRK_N_1000.txt
rm outputs/seq/GSSRK_N_1000_it.txt

echo "--- GSSRK Dense Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			./bin/rand_full.exe GSSRK dense 10 1E-10 $m $n 1000 >> outputs/seq/GSSRK_N_1000.txt
			echo "GSSRK dense $m $n"
		fi
	done
done

echo "--- GSSRK Dense Full ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$n" ]
			then
			./bin/rand_full.exe GSSRK dense 5 1E-10 $m $n 20 >> outputs/seq/GSSRK_N_1000_it.txt
			echo "GSSRK dense $m $n"
		fi
	done
done