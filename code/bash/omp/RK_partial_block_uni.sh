#!/bin/bash

# sbatch bash/omp/RK_partial_block_uni.sh

#SBATCH --job-name="RK_partial_block_uni"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_partial_block_uni.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
K=(5 10 50 100 500)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RK_partial_block_uni.txt
rm outputs/omp/RK_partial_block_uni2.txt

echo "--- Dense RK_partial_block Uni ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				if [ "$m" -ge "$(( 8*k ))" ]
				then
					for t in ${T[@]}; do
						export OMP_NUM_THREADS=$t
						./bin/RK_partial_block_uni_newSC.exe dense 10 1E-10 $m $n $k 1000 >> outputs/omp/RK_partial_block_uni.txt
						echo "par $m $n $t $k"
					done
				fi
			done
		fi
	done
done

echo "--- Dense RK_partial_block Uni 2 ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				if [ "$m" -ge "$(( 8*k ))" ]
				then
					for t in ${T[@]}; do
						export OMP_NUM_THREADS=$t
						./bin/RK_partial_block_uni_newSC2.exe dense 10 1E-10 $m $n $k 1000 >> outputs/omp/RK_partial_block_uni2.txt
						echo "par $m $n $t $k"
					done
				fi
			done
		fi
	done
done