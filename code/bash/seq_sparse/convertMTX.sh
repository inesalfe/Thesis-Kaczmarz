#!/bin/bash

# sbatch bash/seq_sparse/convertMTX.sh

#SBATCH --job-name="convertMTX"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/convertMTX.txt

#SBATCH --nodes=1
#SBATCH --exclusive

./bin/convertMTX.exe 1260 378
./bin/convertMTX.exe 4200 630
./bin/convertMTX.exe 10160 1740
./bin/convertMTX.exe 12600 4200
./bin/convertMTX.exe 16728 7176
./bin/convertMTX.exe 20058 5970
./bin/convertMTX.exe 71952 2704
./bin/convertMTX.exe 171369 47271
./bin/convertMTX.exe 477976 1600
./bin/convertMTX.exe 1748122 62729
./bin/convertMTX.exe 5921786 274669
./bin/convertMTX.exe 9746232 549336
./bin/convertMTX.exe 2111154 801374
./bin/convertMTX.exe 1548649 955128