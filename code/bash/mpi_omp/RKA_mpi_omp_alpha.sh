#!/bin/bash

# sbatch bash/mpi_omp/RKA_mpi_omp_alpha.sh

#SBATCH --job-name="RKA_mpi_omp_alpha"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKA_mpi_omp_alpha.txt

#SBATCH --nodes=8
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)
P=(1 2 4 8)
T=(2 10)

echo "--- Remove Old Files ---"

rm outputs/mpi_omp/RKA_mpi_omp_alpha.txt

echo "--- Dense RKA ---"

l1=1
l2=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			for nproc in ${P[@]}; do
				for t in ${T[@]}; do
					str="$(sed "${l1}q;d" outputs/mpi/RKA_alpha.txt)"
					IFS=' ' read -r -a arr <<< "$str"
					alpha=${arr[3]}
					str="$(sed "${l2}q;d" outputs/mpi_omp/RKA_mpi_omp_alpha_it.txt)"
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_omp_seq_max_it_alpha.exe dense 10 $m $n $nproc $t $alpha $it >> outputs/mpi_omp/RKA_mpi_omp_alpha.txt
					wait
					echo "seq $m $n $nproc $t $alpha $it"
					srun --nodes=$nproc --exclusive --ntasks=$nproc --ntasks-per-node=1 --cpus-per-task=$t ./bin/RKA_mpi_omp_max_it_alpha.exe dense 10 $m $n $alpha $it >> outputs/mpi_omp/RKA_mpi_omp_alpha.txt
					wait
					echo "par1 $m $n $nproc $t $alpha $it"
					srun --nodes=$(((nproc+1)/2)) --exclusive --ntasks=$nproc --ntasks-per-node=2 --cpus-per-task=$t ./bin/RKA_mpi_omp_max_it_alpha.exe dense 10 $m $n $alpha $it >> outputs/mpi_omp/RKA_mpi_omp_alpha.txt
					wait
					echo "par2 $m $n $nproc $t $alpha $it"
					((l1++))
					((l2++))
					((l2++))
					((l2++))
				done
			done
		fi
	done
done