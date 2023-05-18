#!/bin/bash

# sbatch bash/mpi/RKA_mpi_alpha_40.sh

#SBATCH --job-name="RKA_mpi_alpha_40"
#SBATCH --mem-per-cpu=32GB
#SBATCH --open-mode=append
#SBATCH --output=outputs/progress/RKA_mpi_alpha_40.txt

#SBATCH --nodes=40
#SBATCH --exclusive

# echo "--- Remove Old Files ---"

# rm outputs/mpi/RKA_mpi_alpha_40.txt

# echo "--- Dense RKAB ---"

# srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_seq_max_it_alpha.exe dense 10 4000 1000 40 22.5863 3931 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "seq 4000 1000 40 22.5863 3931"
# srun --nodes=40 --exclusive --ntasks=40 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_max_it_alpha.exe dense 10 4000 1000 22.5863 3931 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "par1 4000 1000 40 22.5863 3931"
# srun --nodes=20 --exclusive --ntasks=40 --ntasks-per-node=2 --cpus-per-task=1 ./bin/RKA_mpi_max_it_alpha.exe dense 10 4000 1000 22.5863 3931 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "par2 4000 1000 40 22.5863 3931"

# srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_omp_seq_max_it_alpha.exe dense 10 4000 1000 40 1 22.5863 3895 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "seq 4000 1000 40 1 22.5863 3895"
# srun --nodes=40 --exclusive --ntasks=40 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_omp_max_it_alpha.exe dense 10 4000 1000 22.5863 3895 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "par1 4000 1000 40 1 22.5863 3895"
# srun --nodes=20 --exclusive --ntasks=40 --ntasks-per-node=2 --cpus-per-task=1 ./bin/RKA_mpi_omp_max_it_alpha.exe dense 10 4000 1000 22.5863 3895 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "par2 4000 1000 40 1 22.5863 3895"

# srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_seq_max_it_alpha.exe dense 10 40000 10000 40 22.6029 43025 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "seq 40000 10000 40 22.6029 43025"
# srun --nodes=40 --exclusive --ntasks=40 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_max_it_alpha.exe dense 10 40000 10000 22.6029 43025 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "par1 40000 10000 40 22.6029 43025"
# srun --nodes=20 --exclusive --ntasks=40 --ntasks-per-node=2 --cpus-per-task=1 ./bin/RKA_mpi_max_it_alpha.exe dense 10 40000 10000 22.6029 43025 >> outputs/mpi/RKA_mpi_alpha_40.txt
# wait
# echo "par2 40000 10000 40 22.6029 43025"

srun --nodes=1 --exclusive --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_omp_seq_max_it_alpha.exe dense 10 40000 10000 40 1 22.6029 43019 >> outputs/mpi/RKA_mpi_alpha_40.txt
wait
echo "seq 40000 10000 40 1 22.6029 43019"
srun --nodes=40 --exclusive --ntasks=40 --ntasks-per-node=1 --cpus-per-task=1 ./bin/RKA_mpi_omp_max_it_alpha.exe dense 10 40000 10000 22.6029 43019 >> outputs/mpi/RKA_mpi_alpha_40.txt
wait
echo "par1 40000 10000 40 1 22.6029 43019"
srun --nodes=20 --exclusive --ntasks=40 --ntasks-per-node=2 --cpus-per-task=1 ./bin/RKA_mpi_omp_max_it_alpha.exe dense 10 40000 10000 22.6029 43019 >> outputs/mpi/RKA_mpi_alpha_40.txt
wait
echo "par2 40000 10000 40 1 22.6029 43019"