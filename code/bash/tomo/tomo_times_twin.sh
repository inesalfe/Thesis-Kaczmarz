#!/bin/bash

# sbatch bash/tomo/tomo_times_twin.sh

#SBATCH --job-name="tomo_times_twin"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/tomo_times_twin.txt

#SBATCH --nodes=1
#SBATCH --exclusive

loop_variable=10

echo "--- Remove Old Files ---"

rm outputs/tomo/times_twin.txt

echo "--- twin ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/twin_tomo_stop.exe ct_gaussian 19558 16384 3 50)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times_twin.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/twin_tomo_stop.exe ct_poisson 19558 16384 3 50)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times_twin.txt

echo "--- twin REG ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/twin_tomo_reg_stop.exe ct_gaussian 19558 16384 3 50)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times_twin.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/twin_tomo_reg_stop.exe ct_poisson 19558 16384 3 50)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times_twin.txt

echo "--- mutual ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/mutual_tomo_stop.exe ct_gaussian 19558 16384 3 50)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times_twin.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/mutual_tomo_stop.exe ct_poisson 19558 16384 3 50)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times_twin.txt