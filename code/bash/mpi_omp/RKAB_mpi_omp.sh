#!/bin/bash

# sbatch bash/mpi_omp/RKAB_mpi_omp.sh

#SBATCH --job-name="RKAB_mpi_omp"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKAB_mpi_omp.txt

#SBATCH --nodes=8
#SBATCH --cpus-per-task=10
#SBATCH --ntasks-per-node=2
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)
P=(1 2 4 8)
T=(2 10)

echo "--- Remove Old Files ---"

rm outputs/mpi_omp/RKAB_mpi_omp.txt

echo "--- Dense RKAB ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for nproc in ${P[@]}; do
				for t in ${T[@]}; do
					str=$(srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_omp_seq.exe dense 10 1E-10 $m $n $nproc $t $n 1)
					wait
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_omp_seq_max_it.exe dense 10 $m $n $nproc $t $n $it >> outputs/mpi_omp/RKAB_mpi_omp.txt
					wait
					echo "seq $m $n $nproc $t $it"
					srun --nodes=$nproc --ntasks=$nproc --ntasks-per-node=1 --cpus-per-task=$t ./bin/RKAB_mpi_omp_max_it.exe dense 10 $m $n $n $it >> outputs/mpi_omp/RKAB_mpi_omp.txt
					wait
					echo "par1 $m $n $nproc $t $it"
					srun --nodes=$(((nproc+2-1)/2)) --ntasks=$nproc --ntasks-per-node=2 --cpus-per-task=$t ./bin/RKAB_mpi_omp_max_it.exe dense 10 $m $n $n $it >> outputs/mpi_omp/RKAB_mpi_omp.txt
					wait
					echo "par2 $m $n $nproc $t $it"
				done
			done
		fi
	done
done