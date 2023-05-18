#!/bin/bash

# sbatch bash/omp/RKAB_single_uni_alpha.sh

#SBATCH --job-name="RKAB_single_uni_alpha"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKAB_single_uni_alpha.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(1000)
M=(80000)
K=(5 10 50 100 500 1000 10000)
T=(1 2 4 8)

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_single_uni_alpha.txt

echo "--- Dense RKAB Single Uni ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				alpha=1
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC_alpha.exe dense 10 1E-10 $m $n 1 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it_alpha.exe dense 10 $m $n 1 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 1 $k $it"
				export OMP_NUM_THREADS=1
				./bin/RKAB_single_uni_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 1 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC2_alpha.exe dense 10 1E-10 $m $n 1 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it2_alpha.exe dense 10 $m $n 1 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 1 $k $it"
				export OMP_NUM_THREADS=1
				./bin/RKAB_single_uni_max_it2_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 1 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC3_alpha.exe dense 10 1E-10 $m $n 1 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it3_alpha.exe dense 10 $m $n 1 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 1 $k $it"
				export OMP_NUM_THREADS=1
				./bin/RKAB_single_uni_max_it3_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 1 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC4_alpha.exe dense 10 1E-10 $m $n 1 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it4_alpha.exe dense 10 $m $n 1 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 1 $k $it"
				export OMP_NUM_THREADS=1
				./bin/RKAB_single_uni_max_it4_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 1 $k $it"
				alpha=1.99864
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC_alpha.exe dense 10 1E-10 $m $n 2 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it_alpha.exe dense 10 $m $n 2 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 2 $k $it"
				export OMP_NUM_THREADS=2
				./bin/RKAB_single_uni_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 2 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC2_alpha.exe dense 10 1E-10 $m $n 2 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it2_alpha.exe dense 10 $m $n 2 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 2 $k $it"
				export OMP_NUM_THREADS=2
				./bin/RKAB_single_uni_max_it2_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 2 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC3_alpha.exe dense 10 1E-10 $m $n 2 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it3_alpha.exe dense 10 $m $n 2 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 2 $k $it"
				export OMP_NUM_THREADS=2
				./bin/RKAB_single_uni_max_it3_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 2 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC4_alpha.exe dense 10 1E-10 $m $n 2 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it4_alpha.exe dense 10 $m $n 2 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 2 $k $it"
				export OMP_NUM_THREADS=2
				./bin/RKAB_single_uni_max_it4_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 2 $k $it"
				alpha=3.99183
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC_alpha.exe dense 10 1E-10 $m $n 4 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it_alpha.exe dense 10 $m $n 4 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 4 $k $it"
				export OMP_NUM_THREADS=4
				./bin/RKAB_single_uni_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 4 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC2_alpha.exe dense 10 1E-10 $m $n 4 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it2_alpha.exe dense 10 $m $n 4 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 4 $k $it"
				export OMP_NUM_THREADS=4
				./bin/RKAB_single_uni_max_it2_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 4 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC3_alpha.exe dense 10 1E-10 $m $n 4 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it3_alpha.exe dense 10 $m $n 4 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 4 $k $it"
				export OMP_NUM_THREADS=4
				./bin/RKAB_single_uni_max_it3_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 4 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC4_alpha.exe dense 10 1E-10 $m $n 4 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it4_alpha.exe dense 10 $m $n 4 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 4 $k $it"
				export OMP_NUM_THREADS=4
				./bin/RKAB_single_uni_max_it4_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 4 $k $it"
				alpha=7.96199
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC_alpha.exe dense 10 1E-10 $m $n 8 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it_alpha.exe dense 10 $m $n 8 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 8 $k $it"
				export OMP_NUM_THREADS=8
				./bin/RKAB_single_uni_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 8 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC2_alpha.exe dense 10 1E-10 $m $n 8 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it2_alpha.exe dense 10 $m $n 8 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 8 $k $it"
				export OMP_NUM_THREADS=8
				./bin/RKAB_single_uni_max_it2_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 8 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC3_alpha.exe dense 10 1E-10 $m $n 8 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it3_alpha.exe dense 10 $m $n 8 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 8 $k $it"
				export OMP_NUM_THREADS=8
				./bin/RKAB_single_uni_max_it3_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 8 $k $it"
				export OMP_NUM_THREADS=1
				str=$(./bin/RKAB_single_seq_uni_newSC4_alpha.exe dense 10 1E-10 $m $n 8 $k $alpha 1)
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				./bin/RKAB_single_seq_uni_max_it4_alpha.exe dense 10 $m $n 8 $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "seq $m $n 8 $k $it"
				export OMP_NUM_THREADS=8
				./bin/RKAB_single_uni_max_it4_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_uni_alpha.txt
				echo "par $m $n 8 $k $it"
			done
		fi
	done
done