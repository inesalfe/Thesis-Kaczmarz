#!/bin/bash

# sbatch bash/mpi_omp/RKAB_mpi_omp_extra.sh

#SBATCH --job-name="RKAB_mpi_omp_extra"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKAB_mpi_omp_extra.txt

#SBATCH --nodes=20
#SBATCH --exclusive

# N=(10000 4000 100000)
# M=(4000 20000 40000 80000)
# N=(10000)
# M=(80000)
# P=(4 8 20)
# T=(10 5 2)

# echo "--- Remove Old Files ---"

# rm outputs/mpi_omp/RKAB_mpi_omp_extra.txt

# echo "--- Dense RKAB ---"

# for m in ${M[@]}; do
# 	for n in ${N[@]}; do
# 		if [ "$m" -gt "$(( 2*n ))" ]
# 		then
# 			for (( i=0; i<3; i++ )) do
# 				nproc=${P[i]}
# 				t=${T[i]}
# 				# str=$(srun --nodes=1 --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_omp_seq.exe dense 10 1E-10 $m $n $nproc $t $n 1)
# 				str=$(srun --nodes=$nproc --ntasks=$nproc --ntasks-per-node=1 --cpus-per-task=$t ./bin/RKAB_mpi_omp.exe dense 10 1E-10 80000 10000 1000 1)
# 				wait
# 				IFS=' ' read -r -a arr <<< "$str"
# 				it=${arr[3]}
# 				srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_omp_seq_max_it.exe dense 10 80000 10000 $nproc $t 1000 $it >> outputs/mpi_omp/RKAB_mpi_omp_extra.txt
# 				wait
# 				echo "seq 80000 10000 $nproc $t $it"
# 				srun --nodes=$nproc --exclusive --ntasks=$nproc --ntasks-per-node=1 --cpus-per-task=$t ./bin/RKAB_mpi_omp_max_it.exe dense 10 80000 10000 1000 $it >> outputs/mpi_omp/RKAB_mpi_omp_extra.txt
# 				wait
# 				echo "par1 80000 10000 $nproc $t $it"
# 				srun --nodes=$((nproc/2)) --exclusive --ntasks=$nproc --ntasks-per-node=2 --cpus-per-task=$t ./bin/RKAB_mpi_omp_max_it.exe dense 10 80000 10000 1000 $it >> outputs/mpi_omp/RKAB_mpi_omp_extra.txt
# 				wait
# 				echo "par2 80000 10000 $nproc $t $it"
# 			done
# 		fi
# 	done
# done