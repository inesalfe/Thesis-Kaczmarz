#!/bin/bash

# sbatch bash/seq/genSystems.sh

#SBATCH --job-name="genSystems"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/genSystems.txt

#SBATCH --nodes=1
#SBATCH --exclusive

# ./bin/genConsistDataSets.exe
# ./bin/genConsistSparseSystems.exe
./bin/genLSDataSets.exe
# ./bin/genCoherentDenseDataSets.exe