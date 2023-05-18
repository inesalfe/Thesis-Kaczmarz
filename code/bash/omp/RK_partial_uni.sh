#!/bin/bash

# sbatch bash/omp/RK_partial_uni.sh

#SBATCH --job-name="RK_partial_uni"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_partial_uni.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

# rm outputs/omp/RK_partial_uni.txt
rm outputs/omp/RK_partial_uni2.txt

# echo "--- Dense RK_partial Uni ---"

# for m in ${M[@]}; do
# 	for n in ${N[@]}; do
# 		if [ "$m" -gt "$(( 2*n ))" ]
# 		then
# 			for t in ${T[@]}; do
# 				export OMP_NUM_THREADS=$t
# 				./bin/RK_partial_uni_newSC.exe dense 10 1E-10 $m $n 1000 >> outputs/omp/RK_partial_uni.txt
# 				echo "par $m $n $t"
# 			done
# 		fi
# 	done
# done

echo "--- Dense RK_partial Uni 2 ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=$t
				./bin/RK_partial_uni_newSC2.exe dense 10 1E-10 $m $n 1000 >> outputs/omp/RK_partial_uni2.txt
				echo "par $m $n $t"
			done
		fi
	done
done