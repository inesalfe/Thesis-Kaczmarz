#!/bin/bash

# sbatch bash/omp/RKA_uni.sh

#SBATCH --job-name="RKA_uni"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKA_uni.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA_uni.txt

echo "--- Dense RKA Uni ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_uni_newSC.exe dense 10 1E-10 $m $n $t 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_seq_uni_max_it.exe dense 10 $m $n $t $it >> outputs/omp/RKA_uni.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_uni_max_it.exe dense 10 $m $n $it >> outputs/omp/RKA_uni.txt
				echo "par $m $n $t $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_uni_newSC2.exe dense 10 1E-10 $m $n $t 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_seq_uni_max_it2.exe dense 10 $m $n $t $it >> outputs/omp/RKA_uni.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_uni_max_it2.exe dense 10 $m $n $it >> outputs/omp/RKA_uni.txt
				echo "par $m $n $t $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_uni_newSC3.exe dense 10 1E-10 $m $n $t 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_seq_uni_max_it3.exe dense 10 $m $n $t $it >> outputs/omp/RKA_uni.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_uni_max_it3.exe dense 10 $m $n $it >> outputs/omp/RKA_uni.txt
				echo "par $m $n $t $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_uni_newSC4.exe dense 10 1E-10 $m $n $t 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_seq_uni_max_it4.exe dense 10 $m $n $t $it >> outputs/omp/RKA_uni.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_uni_max_it4.exe dense 10 $m $n $it >> outputs/omp/RKA_uni.txt
				echo "par $m $n $t $it"
			done
		fi
	done
done