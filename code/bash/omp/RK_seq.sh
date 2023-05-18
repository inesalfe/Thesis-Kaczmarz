#!/bin/bash

# sbatch bash/omp/RK_seq.sh

#SBATCH --job-name="RK_seq"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_seq.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)

echo "--- Remove Old Files ---"

rm outputs/omp/RK_seq.txt
rm outputs/omp/RK_seq_uni.txt
rm outputs/omp/RK_seq_uni_copy.txt

echo "--- Dense RK ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			str=$(./bin/RK_seq_newSC.exe dense 10 1E-10 $m $n 1)
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			./bin/RK_seq_max_it.exe dense 10 $m $n $it >> outputs/omp/RK_seq.txt
			echo "seq $m $n $it"
		fi
	done
done

echo "--- Dense RK Uni ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			str=$(./bin/RK_seq_uni_newSC.exe dense 10 1E-10 $m $n 1)
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			./bin/RK_seq_uni_max_it.exe dense 10 $m $n $it >> outputs/omp/RK_seq_uni.txt
			echo "seq $m $n $it"
		fi
	done
done

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			str=$(./bin/RK_seq_uni_newSC2.exe dense 10 1E-10 $m $n 1)
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			./bin/RK_seq_uni_max_it2.exe dense 10 $m $n $it >> outputs/omp/RK_seq_uni_copy.txt
			echo "seq $m $n $it"
		fi
	done
done