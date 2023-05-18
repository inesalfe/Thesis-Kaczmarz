#!/bin/bash

# sbatch bash/omp/RKAB_single_alpha_dim.sh

#SBATCH --job-name="RKAB_single_alpha_dim"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKAB_single_alpha_dim.txt

#SBATCH --nodes=1
#SBATCH --exclusive

echo "--- Remove Old Files ---"

rm outputs/omp/RKAB_single_alpha_dim.txt

echo "--- Dense RKAB Single ---"

N=(1000)
M=(80000)
K=(50 500 1000)
T=(2)
A=(1.0 1.2 1.3 1.5 1.8 1.99864)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_single_seq_newSC_alpha.exe dense 10 1E-10 $m $n 2 $k $alpha 1)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_single_seq_max_it_alpha.exe dense 10 $m $n 2 $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "seq $m $n 2 $k $it"
					export OMP_NUM_THREADS=2
					./bin/RKAB_single_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "par $m $n 2 $k $it"
				done
			done
		fi
	done
done

# 3.0 e 3.99183 para K = 500 não deu
# 3.0 e 3.99183 para K = 1000 não deu

N=(1000)
M=(80000)
K=(50 500 1000)
T=(4)
A=(1.0 1.5 2.0 2.5 3.0 3.99183)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_single_seq_newSC_alpha.exe dense 10 1E-10 $m $n 4 $k $alpha 1)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_single_seq_max_it_alpha.exe dense 10 $m $n 4 $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "seq $m $n 4 $k $it"
					export OMP_NUM_THREADS=4
					./bin/RKAB_single_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "par $m $n 4 $k $it"
				done
			done
		fi
	done
done

# 7.96199 para K = 50 não deu
# 5.0 e 7.96199 para K = 500 não deu
# 3.0 e 5.0 e 7.96199 para K = 1000 não deu

N=(1000)
M=(80000)
K=(50 500 1000)
T=(8)
A=(1.0 2.0 2.5 3.0 5.0 7.96199)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_single_seq_newSC_alpha.exe dense 10 1E-10 $m $n 8 $k $alpha 1)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_single_seq_max_it_alpha.exe dense 10 $m $n 8 $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "seq $m $n 8 $k $it"
					export OMP_NUM_THREADS=8
					./bin/RKAB_single_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "par $m $n 8 $k $it"
				done
			done
		fi
	done
done

N=(4000)
M=(80000)
K=(500 1000 4000)
T=(2)
A=(1.0 1.2 1.3 1.5 1.8 1.99994)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_single_seq_newSC_alpha.exe dense 10 1E-10 $m $n 2 $k $alpha 1)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_single_seq_max_it_alpha.exe dense 10 $m $n 2 $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "seq $m $n 2 $k $it"
					export OMP_NUM_THREADS=2
					./bin/RKAB_single_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "par $m $n 2 $k $it"
				done
			done
		fi
	done
done

# 3.99965 para K = 500 não deu
# 3.99965 para K = 1000 não deu
# 3.0 e 3.99965 para K = 4000 não deu

N=(4000)
M=(80000)
K=(500 1000 4000)
T=(4)
A=(1.0 1.5 2.0 2.5 3.0 3.99965)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_single_seq_newSC_alpha.exe dense 10 1E-10 $m $n 4 $k $alpha 1)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_single_seq_max_it_alpha.exe dense 10 $m $n 4 $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "seq $m $n 4 $k $it"
					export OMP_NUM_THREADS=4
					./bin/RKAB_single_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "par $m $n 4 $k $it"
				done
			done
		fi
	done
done

# 5.0 e 7.99839 para K = 500 não deu
# 5.0 e 7.99839 para K = 500 não deu
# 3.0, 5.0 e 7.99839 para K = 500 não deu

N=(4000)
M=(80000)
K=(500 1000 4000)
T=(8)
A=(1.0 2.0 2.5 3.0 5.0 7.99839)

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for alpha in ${A[@]}; do
					export OMP_NUM_THREADS=1
					str=$(./bin/RKAB_single_seq_newSC_alpha.exe dense 10 1E-10 $m $n 8 $k $alpha 1)
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					./bin/RKAB_single_seq_max_it_alpha.exe dense 10 $m $n 8 $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "seq $m $n 8 $k $it"
					export OMP_NUM_THREADS=8
					./bin/RKAB_single_max_it_alpha.exe dense 10 $m $n $k $alpha $it >> outputs/omp/RKAB_single_alpha_dim.txt
					echo "par $m $n 8 $k $it"
				done
			done
		fi
	done
done