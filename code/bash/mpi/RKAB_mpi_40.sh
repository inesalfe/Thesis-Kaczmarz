#!/bin/bash

# sbatch bash/mpi/RKAB_mpi_40.sh

#SBATCH --job-name="RKAB_mpi_40"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKAB_mpi_40.txt

#SBATCH --nodes=40
#SBATCH --exclusive

echo "--- Remove Old Files ---"

rm outputs/mpi/RKAB_mpi_40.txt

echo "--- Dense RKAB ---"

str=$(srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_seq.exe dense 10 1E-10 80000 10000 40 1000 1)
wait
IFS=' ' read -r -a arr <<< "$str"
it=${arr[3]}
srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_seq_max_it.exe dense 10 80000 10000 40 1000 $it >> outputs/mpi/RKAB_mpi_40.txt
wait
echo "seq 80000 10000 40 $it"
srun --nodes=40 --exclusive --ntasks=40 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_max_it.exe dense 10 80000 10000 1000 $it >> outputs/mpi/RKAB_mpi_40.txt
wait
echo "par1 80000 10000 40 $it"
srun --nodes=20 --exclusive --ntasks=40 --ntasks-per-node=2 --cpus-per-task=1 ./bin/RKAB_mpi_max_it.exe dense 10 80000 10000 1000 $it >> outputs/mpi/RKAB_mpi_40.txt
wait
echo "par2 80000 10000 40 $it"

str=$(srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_omp_seq.exe dense 10 1E-10 80000 10000 40 1 1000 1)
wait
IFS=' ' read -r -a arr <<< "$str"
it=${arr[3]}
srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_omp_seq_max_it.exe dense 10 80000 10000 40 1 1000 $it >> outputs/mpi/RKAB_mpi_40.txt
wait
echo "seq 80000 10000 40 1 $it"
srun --nodes=40 --exclusive --ntasks=40 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKAB_mpi_omp_max_it.exe dense 10 80000 10000 1000 $it >> outputs/mpi/RKAB_mpi_40.txt
wait
echo "par1 80000 10000 40 1 $it"
srun --nodes=20 --exclusive --ntasks=40 --ntasks-per-node=2 --cpus-per-task=1 ./bin/RKAB_mpi_omp_max_it.exe dense 10 80000 10000 1000 $it >> outputs/mpi/RKAB_mpi_40.txt
wait
echo "par2 80000 10000 40 1 $it"