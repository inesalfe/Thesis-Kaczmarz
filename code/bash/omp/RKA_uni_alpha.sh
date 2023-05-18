#!/bin/bash

# sbatch bash/omp/RKA_uni_alpha.sh

#SBATCH --job-name="RKA_uni_alpha"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKA_uni_alpha.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(50 100 200 500 750 1000 2000 4000 10000)
M=(2000 4000 20000 40000 80000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RKA_uni_alpha.txt

echo "--- Dense RKA Uni ---"

line=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			for t in ${T[@]}; do
				export OMP_NUM_THREADS=1
				str="$(sed "${line}q;d" outputs/omp/RKA_best_alpha.txt)"
				IFS=' ' read -r -a arr <<< "$str"
				alpha=${arr[3]}
				str=$(./bin/RKA_seq_uni_newSC_alpha.exe dense 10 1E-10 $m $n $t $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_seq_uni_max_it_alpha.exe dense 10 $m $n $t $alpha $it >> outputs/omp/RKA_uni_alpha.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_uni_max_it_alpha.exe dense 10 $m $n $alpha $it >> outputs/omp/RKA_uni_alpha.txt
				echo "par $m $n $t $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_uni_newSC2_alpha.exe dense 10 1E-10 $m $n $t $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_seq_uni_max_it2_alpha.exe dense 10 $m $n $t $alpha $it >> outputs/omp/RKA_uni_alpha.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_uni_max_it2_alpha.exe dense 10 $m $n $alpha $it >> outputs/omp/RKA_uni_alpha.txt
				echo "par $m $n $t $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_uni_newSC3_alpha.exe dense 10 1E-10 $m $n $t $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_seq_uni_max_it3_alpha.exe dense 10 $m $n $t $alpha $it >> outputs/omp/RKA_uni_alpha.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_uni_max_it3_alpha.exe dense 10 $m $n $alpha $it >> outputs/omp/RKA_uni_alpha.txt
				echo "par $m $n $t $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKA_seq_uni_newSC4_alpha.exe dense 10 1E-10 $m $n $t $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKA_seq_uni_max_it4_alpha.exe dense 10 $m $n $t $alpha $it >> outputs/omp/RKA_uni_alpha.txt
				echo "seq $m $n $t $it"
				export OMP_NUM_THREADS=$t
				./bin/RKA_uni_max_it4_alpha.exe dense 10 $m $n $alpha $it >> outputs/omp/RKA_uni_alpha.txt
				echo "par $m $n $t $it"
				((line++))
			done
			((line++))
			((line++))
			((line++))
		fi
	done
done