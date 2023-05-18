#!/bin/bash

# sbatch bash/omp/RK_parallel.sh

#SBATCH --job-name="RK_parallel"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RK_parallel.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RK_parallel.txt
rm outputs/omp/RK_parallel_uni.txt
rm outputs/omp/RK_parallel_uni_copy.txt

echo "--- Dense RK parallel ---"

line=0
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			((line++))
			str="$(sed "${line}q;d" outputs/omp/RK_seq.txt)"
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=$t
				./bin/RK_parallel_max_it.exe dense 10 $m $n $it >> outputs/omp/RK_parallel.txt
				echo "par $m $n $it"
			done
		fi
	done
done

echo "--- Dense RK parallel Uni ---"

line=0
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			((line++))
			str="$(sed "${line}q;d" outputs/omp/RK_seq_uni.txt)"
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=$t
				./bin/RK_parallel_uni_max_it.exe dense 10 $m $n $it >> outputs/omp/RK_parallel_uni.txt
				echo "par $m $n $it"
			done
		fi
	done
done

echo "--- Dense RK parallel Uni Copy ---"

line=0
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			export OMP_NUM_THREADS=1
			((line++))
			str="$(sed "${line}q;d" outputs/omp/RK_seq_uni_copy.txt)"
			IFS=' ' read -r -a arr <<< "$str"
			it=${arr[3]}
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=$t
				./bin/RK_parallel_uni_max_it2.exe dense 10 $m $n $it >> outputs/omp/RK_parallel_uni_copy.txt
				echo "par $m $n $it"
			done
		fi
	done
done