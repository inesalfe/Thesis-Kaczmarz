#!/bin/bash

# sbatch bash/mpi/RKA_mpi_alpha.sh

#SBATCH --job-name="RKA_mpi_alpha"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKA_mpi_alpha.txt

#SBATCH --nodes=20
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)
T=(1 2 4 8 20)

echo "--- Remove Old Files ---"

rm outputs/mpi/RKA_mpi_alpha.txt

echo "--- Dense RKA ---"

line=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then	
			for nproc in ${T[@]}; do
				str="$(sed "${line}q;d" outputs/omp/RKAB_single_best_alpha.txt)"
				IFS=' ' read -r -a arr <<< "$str"
				alpha=${arr[3]}
				str=$(srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_seq_alpha.exe dense 10 1E-10 $m $n $nproc $alpha 1)
				wait
				IFS=' ' read -r -a arr <<< "$str"
				it=${arr[3]}
				srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_seq_max_it_alpha.exe dense 10 $m $n $nproc $alpha $it >> outputs/mpi/RKA_mpi_alpha.txt
				wait
				echo "seq $m $n $nproc $alpha $it"
				srun --nodes=$nproc --ntasks=$nproc --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_max_it_alpha.exe dense 10 $m $n $alpha $it >> outputs/mpi/RKA_mpi_alpha.txt
				wait
				echo "par1 $m $n $nproc $alpha $it"
				srun --nodes=$(((nproc+2-1)/2)) --ntasks=$nproc --ntasks-per-node=2 --cpus-per-task=1 ./bin/RKA_mpi_max_it_alpha.exe dense 10 $m $n $alpha $it >> outputs/mpi/RKA_mpi_alpha.txt
				wait
				echo "par2 $m $n $nproc $alpha $it"
				srun --nodes=1 --ntasks=$nproc --ntasks-per-node=$nproc --cpus-per-task=1 ./bin/RKA_mpi_max_it_alpha.exe dense 10 $m $n $alpha $it >> outputs/mpi/RKA_mpi_alpha.txt
				wait
				echo "par3 $m $n $nproc $alpha $it"
				((line++))
			done
			((line++))
			((line++))
		fi
	done
done