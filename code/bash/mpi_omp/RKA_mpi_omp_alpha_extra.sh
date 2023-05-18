#!/bin/bash

# sbatch bash/mpi_omp/RKA_mpi_omp_alpha_extra.sh

#SBATCH --job-name="RKA_mpi_omp_alpha_extra"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/RKA_mpi_omp_alpha_extra.txt

#SBATCH --nodes=20
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)
P=(4 8 20)
T=(10 5 2)

echo "--- Remove Old Files ---"

rm outputs/mpi_omp/RKA_mpi_omp_alpha_extra.txt

echo "--- Dense RKA ---"

line=1
for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for (( i=0; i<3; i++ )) do
				nproc=${P[i]}
				t=${T[i]}
				str="$(sed "${line}q;d" outputs/mpi_omp/RKA_alpha_params.txt)"
				IFS=' ' read -r -a arr <<< "$str"
				alpha=${arr[3]}
				it=${arr[2]}
				srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_omp_seq_max_it_alpha.exe dense 10 $m $n $nproc $t $alpha $it >> outputs/mpi_omp/RKA_mpi_omp_alpha_extra.txt
				wait
				echo "seq $m $n $nproc $t $alpha $it"
				srun --nodes=$nproc --exclusive --ntasks=$nproc --ntasks-per-node=1 --cpus-per-task=$t ./bin/RKA_mpi_omp_max_it_alpha.exe dense 10 $m $n $alpha $it >> outputs/mpi_omp/RKA_mpi_omp_alpha_extra.txt
				wait
				echo "par1 $m $n $nproc $t $alpha $it"
				srun --nodes=$(((nproc+1)/2)) --exclusive --ntasks=$nproc --ntasks-per-node=2 --cpus-per-task=$t ./bin/RKA_mpi_omp_max_it_alpha.exe dense 10 $m $n $alpha $it >> outputs/mpi_omp/RKA_mpi_omp_alpha_extra.txt
				wait
				echo "par2 $m $n $nproc $t $alpha $it"
				((line++))
			done
		fi
	done
done