#!/bin/bash

# sbatch bash/tomo/tomo_times.sh

#SBATCH --job-name="tomo_times"
#SBATCH --mem-per-cpu=32GB
#SBATCH --output=outputs/progress/tomo_times.txt

#SBATCH --nodes=1
#SBATCH --exclusive

loop_variable=10

echo "--- Remove Old Files ---"

rm outputs/tomo/times.txt

echo "--- CK ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/CK_tomo_stop.exe ct_gaussian 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/CK_tomo_stop.exe ct_poisson 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

echo "--- CK REG ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/CK_tomo_reg_stop.exe ct_gaussian 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/CK_tomo_reg_stop.exe ct_poisson 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

echo "--- RK ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/RK_tomo_stop.exe ct_gaussian 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/RK_tomo_stop.exe ct_poisson 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

echo "--- RK REG ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/RK_tomo_reg_stop.exe ct_gaussian 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/RK_tomo_reg_stop.exe ct_poisson 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

echo "--- SRKWOR ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/SRKWOR_tomo_stop.exe ct_gaussian 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/SRKWOR_tomo_stop.exe ct_poisson 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

echo "--- SRKWOR REG ---"

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/SRKWOR_tomo_reg_stop.exe ct_gaussian 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt

sum=0.0
for (( i=0; i<loop_variable; i++ )) do
	export OMP_NUM_THREADS=1
	str=$(./bin/SRKWOR_tomo_reg_stop.exe ct_poisson 19558 16384 3 10000000 10000 50 0.1)
	IFS=' ' read -r -a arr <<< "$str"
	it=${arr[2]}
	time=${arr[3]}
	error=${arr[4]}
	wait
	sum=$(awk "BEGIN {print $sum+$time; exit}")
done
echo "$it $sum $error" >> outputs/tomo/times.txt