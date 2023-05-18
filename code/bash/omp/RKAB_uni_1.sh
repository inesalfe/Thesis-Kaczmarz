#!/bin/bash

# sbatch bash/omp/RKAB_uni_1.sh

#SBATCH --job-name="RKAB_uni_1"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKAB_uni_1.txt

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

N=(4000)
M=(80000)
K=(50 200 400)
B=(1 2 4 8 16 32 64)
T=(1 2 4 8)
R=(1)

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_uni_1.txt

echo "--- Dense RKAB Uni ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for r in ${R[@]}; do
				for k in ${K[@]}; do
					for b in ${B[@]}; do
						export OMP_NUM_THREADS=1
						str=$(./bin/RKAB_seq_uni_newSC.exe dense 10 1E-10 $m $n $b $k 1 $r)
						IFS=' ' read -r -a arr <<< "$str"
						it=${arr[3]}
						./bin/RKAB_seq_uni_max_it.exe dense 10 $m $n $b $k $it $r >> outputs/omp/RKAB_uni_1.txt
						echo "seq $m $n $b $k $it $r"
						for t in ${T[@]}; do
							export OMP_NUM_THREADS=$t
							./bin/RKAB_uni_max_it.exe dense 10 $m $n $k $it $b $r >> outputs/omp/RKAB_uni_1.txt
							echo "par $m $n $t $k $it $b $r"
						done
						export OMP_NUM_THREADS=1
						str=$(./bin/RKAB_seq_uni_newSC2.exe dense 10 1E-10 $m $n $b $k 1 $r)
						IFS=' ' read -r -a arr <<< "$str"
						it=${arr[3]}
						./bin/RKAB_seq_uni_max_it2.exe dense 10 $m $n $b $k $it $r >> outputs/omp/RKAB_uni_1.txt
						echo "seq $m $n $b $k $it $r"
						for t in ${T[@]}; do
							export OMP_NUM_THREADS=$t
							./bin/RKAB_uni_max_it2.exe dense 10 $m $n $k $it $b $r >> outputs/omp/RKAB_uni_1.txt
							echo "par $m $n $t $k $it $b $r"
						done
						export OMP_NUM_THREADS=1
						str=$(./bin/RKAB_seq_uni_newSC3.exe dense 10 1E-10 $m $n $b $k 1 $r)
						IFS=' ' read -r -a arr <<< "$str"
						it=${arr[3]}
						./bin/RKAB_seq_uni_max_it3.exe dense 10 $m $n $b $k $it $r >> outputs/omp/RKAB_uni_1.txt
						echo "seq $m $n $b $k $it $r"
						for t in ${T[@]}; do
							export OMP_NUM_THREADS=$t
							./bin/RKAB_uni_max_it3.exe dense 10 $m $n $k $it $b $r >> outputs/omp/RKAB_uni_1.txt
							echo "par $m $n $t $k $it $b $r"
						done
						export OMP_NUM_THREADS=1
						str=$(./bin/RKAB_seq_uni_newSC4.exe dense 10 1E-10 $m $n $b $k 1 $r)
						IFS=' ' read -r -a arr <<< "$str"
						it=${arr[3]}
						./bin/RKAB_seq_uni_max_it4.exe dense 10 $m $n $b $k $it $r >> outputs/omp/RKAB_uni_1.txt
						echo "seq $m $n $b $k $it $r"
						for t in ${T[@]}; do
							export OMP_NUM_THREADS=$t
							./bin/RKAB_uni_max_it4.exe dense 10 $m $n $k $it $b $r >> outputs/omp/RKAB_uni_1.txt
							echo "par $m $n $t $k $it $b $r"
						done
					done
				done
			done
		fi
	done
done