#!/bin/bash

# sbatch bash/mpi/RKAB_mpi.sh

#SBATCH --job-name="RKAB_mpi"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKAB_mpi.txt

#SBATCH --nodes=20
#SBATCH --exclusive

N=(1000 4000 10000)
M=(4000 20000 40000 80000)
T=(1 2 4 8 20)
K=(500 1000 10000)

echo "--- Remove Old Files ---"

rm outputs/mpi/RKAB_mpi.txt

echo "--- Dense RKAB ---"

for m in ${M[@]}; do
	for n in ${N[@]}; do
		if [ "$m" -gt "$(( 2*n ))" ]
		then
			for k in ${K[@]}; do
				for nproc in ${T[@]}; do
					str=$(srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_seq.exe dense 10 1E-10 $m $n $nproc $k 1)
					wait
					IFS=' ' read -r -a arr <<< "$str"
					it=${arr[3]}
					srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_seq_max_it.exe dense 10 $m $n $nproc $k $it >> outputs/mpi/RKAB_mpi.txt
					wait
					echo "seq $m $n $nproc $it"
					srun --nodes=$nproc --ntasks=$nproc --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_max_it.exe dense 10 $m $n $k $it >> outputs/mpi/RKAB_mpi.txt
					wait
					echo "par1 $m $n $nproc $it"
					srun --nodes=$(((nproc+2-1)/2)) --ntasks=$nproc --ntasks-per-node=2 --cpus-per-task=1 ./bin/RKAB_mpi_max_it.exe dense 10 $m $n $k $it >> outputs/mpi/RKAB_mpi.txt
					wait
					echo "par2 $m $n $nproc $it"
					srun --nodes=1 --ntasks=$nproc --ntasks-per-node=$nproc --cpus-per-task=1 ./bin/RKAB_mpi_max_it.exe dense 10 $m $n $k $it >> outputs/mpi/RKAB_mpi.txt
					wait
					echo "par3 $m $n $nproc $it"
				done
			done
		fi
	done
done