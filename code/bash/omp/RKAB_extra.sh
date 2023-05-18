#!/bin/bash

# sbatch bash/omp/RKAB_extra.sh

#SBATCH --job-name="RKAB_extra"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKAB_extra.txt

#SBATCH --nodes=1
#SBATCH --exclusive

N=(4000)
M=(80000)
K=(500 1000 4000 10000)
B=(8)
T=(8)
R=(1 2 5 10)

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_extra.txt

echo "--- Dense RKAB ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for r in ${R[@]}; do
				for k in ${K[@]}; do
					for b in ${B[@]}; do
						export OMP_NUM_THREADS=1
						str=$(./bin/RKAB_seq_newSC.exe dense 10 1E-10 $m $n $b $k 1 $r)
						IFS=' ' read -r -a arr <<< "$str"
						it=${arr[3]}
						./bin/RKAB_seq_max_it.exe dense 10 $m $n $b $k $it $r >> outputs/omp/RKAB_extra.txt
						echo "seq $m $n $b $k $it $r"
						for t in ${T[@]}; do
							export OMP_NUM_THREADS=$t
							./bin/RKAB_max_it.exe dense 10 $m $n $k $it $b $r >> outputs/omp/RKAB_extra.txt
							echo "par $m $n $t $k $it $b $r"
						done
						export OMP_NUM_THREADS=1
						str=$(./bin/RKAB_seq_uni_newSC.exe dense 10 1E-10 $m $n $b $k 1 $r)
						IFS=' ' read -r -a arr <<< "$str"
						it=${arr[3]}
						./bin/RKAB_seq_uni_max_it.exe dense 10 $m $n $b $k $it $r >> outputs/omp/RKAB_extra.txt
						echo "seq $m $n $b $k $it $r"
						for t in ${T[@]}; do
							export OMP_NUM_THREADS=$t
							./bin/RKAB_uni_max_it.exe dense 10 $m $n $k $it $b $r >> outputs/omp/RKAB_extra.txt
							echo "par $m $n $t $k $it $b $r"
						done
						export OMP_NUM_THREADS=1
						str=$(./bin/RKAB_seq_uni_newSC2.exe dense 10 1E-10 $m $n $b $k 1 $r)
						IFS=' ' read -r -a arr <<< "$str"
						it=${arr[3]}
						./bin/RKAB_seq_uni_max_it2.exe dense 10 $m $n $b $k $it $r >> outputs/omp/RKAB_extra.txt
						echo "seq $m $n $b $k $it $r"
						for t in ${T[@]}; do
							export OMP_NUM_THREADS=$t
							./bin/RKAB_uni_max_it2.exe dense 10 $m $n $k $it $b $r >> outputs/omp/RKAB_extra.txt
							echo "par $m $n $t $k $it $b $r"
						done
					done
				done
			done
		fi
	done
done