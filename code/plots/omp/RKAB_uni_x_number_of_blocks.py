import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_uni_x_number_of_blocks.py 80000 4000

if (len(sys.argv) != 3):
	exit()

M = int(sys.argv[1])
N = int(sys.argv[2])

filename = "outputs/omp/RKAB_50.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_1_8_t2 = []
time_1_16_t2 = []
time_1_32_t2 = []
time_1_64_t2 = []
time_1_8_t4 = []
time_1_16_t4 = []
time_1_32_t4 = []
time_1_64_t4 = []
time_1_8_t8 = []
time_1_16_t8 = []
time_1_32_t8 = []
time_1_64_t8 = []
time_2_8_t2 = []
time_2_16_t2 = []
time_2_32_t2 = []
time_2_64_t2 = []
time_2_8_t4 = []
time_2_16_t4 = []
time_2_32_t4 = []
time_2_64_t4 = []
time_2_8_t8 = []
time_2_16_t8 = []
time_2_32_t8 = []
time_2_64_t8 = []
time_5_8_t2 = []
time_5_16_t2 = []
time_5_32_t2 = []
time_5_64_t2 = []
time_5_8_t4 = []
time_5_16_t4 = []
time_5_32_t4 = []
time_5_64_t4 = []
time_5_8_t8 = []
time_5_16_t8 = []
time_5_32_t8 = []
time_5_64_t8 = []
time_10_8_t2 = []
time_10_16_t2 = []
time_10_32_t2 = []
time_10_64_t2 = []
time_10_8_t4 = []
time_10_16_t4 = []
time_10_32_t4 = []
time_10_64_t4 = []
time_10_8_t8 = []
time_10_16_t8 = []
time_10_32_t8 = []
time_10_64_t8 = []
time_1_8_t2.append(float(lines[17].split()[2]))
time_1_16_t2.append(float(lines[22].split()[2]))
time_1_32_t2.append(float(lines[27].split()[2]))
time_1_64_t2.append(float(lines[32].split()[2]))
time_1_8_t4.append(float(lines[18].split()[2]))
time_1_16_t4.append(float(lines[23].split()[2]))
time_1_32_t4.append(float(lines[28].split()[2]))
time_1_64_t4.append(float(lines[33].split()[2]))
time_1_8_t8.append(float(lines[19].split()[2]))
time_1_16_t8.append(float(lines[24].split()[2]))
time_1_32_t8.append(float(lines[29].split()[2]))
time_1_64_t8.append(float(lines[34].split()[2]))
time_2_8_t2.append(float(lines[52].split()[2]))
time_2_16_t2.append(float(lines[57].split()[2]))
time_2_32_t2.append(float(lines[62].split()[2]))
time_2_64_t2.append(float(lines[67].split()[2]))
time_2_8_t4.append(float(lines[53].split()[2]))
time_2_16_t4.append(float(lines[58].split()[2]))
time_2_32_t4.append(float(lines[63].split()[2]))
time_2_64_t4.append(float(lines[68].split()[2]))
time_2_8_t8.append(float(lines[54].split()[2]))
time_2_16_t8.append(float(lines[59].split()[2]))
time_2_32_t8.append(float(lines[64].split()[2]))
time_2_64_t8.append(float(lines[69].split()[2]))
time_5_8_t2.append(float(lines[87].split()[2]))
time_5_16_t2.append(float(lines[92].split()[2]))
time_5_32_t2.append(float(lines[97].split()[2]))
time_5_64_t2.append(float(lines[102].split()[2]))
time_5_8_t4.append(float(lines[88].split()[2]))
time_5_16_t4.append(float(lines[93].split()[2]))
time_5_32_t4.append(float(lines[98].split()[2]))
time_5_64_t4.append(float(lines[103].split()[2]))
time_5_8_t8.append(float(lines[89].split()[2]))
time_5_16_t8.append(float(lines[94].split()[2]))
time_5_32_t8.append(float(lines[99].split()[2]))
time_5_64_t8.append(float(lines[104].split()[2]))
time_10_8_t2.append(float(lines[122].split()[2]))
time_10_16_t2.append(float(lines[127].split()[2]))
time_10_32_t2.append(float(lines[132].split()[2]))
time_10_64_t2.append(float(lines[137].split()[2]))
time_10_8_t4.append(float(lines[123].split()[2]))
time_10_16_t4.append(float(lines[128].split()[2]))
time_10_32_t4.append(float(lines[133].split()[2]))
time_10_64_t4.append(float(lines[138].split()[2]))
time_10_8_t8.append(float(lines[124].split()[2]))
time_10_16_t8.append(float(lines[129].split()[2]))
time_10_32_t8.append(float(lines[134].split()[2]))
time_10_64_t8.append(float(lines[139].split()[2]))

filename = "outputs/omp/RKAB_200.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_1_8_t2.append(float(lines[17].split()[2]))
time_1_16_t2.append(float(lines[22].split()[2]))
time_1_32_t2.append(float(lines[27].split()[2]))
time_1_64_t2.append(float(lines[32].split()[2]))
time_1_8_t4.append(float(lines[18].split()[2]))
time_1_16_t4.append(float(lines[23].split()[2]))
time_1_32_t4.append(float(lines[28].split()[2]))
time_1_64_t4.append(float(lines[33].split()[2]))
time_1_8_t8.append(float(lines[19].split()[2]))
time_1_16_t8.append(float(lines[24].split()[2]))
time_1_32_t8.append(float(lines[29].split()[2]))
time_1_64_t8.append(float(lines[34].split()[2]))
time_2_8_t2.append(float(lines[52].split()[2]))
time_2_16_t2.append(float(lines[57].split()[2]))
time_2_32_t2.append(float(lines[62].split()[2]))
time_2_64_t2.append(float(lines[67].split()[2]))
time_2_8_t4.append(float(lines[53].split()[2]))
time_2_16_t4.append(float(lines[58].split()[2]))
time_2_32_t4.append(float(lines[63].split()[2]))
time_2_64_t4.append(float(lines[68].split()[2]))
time_2_8_t8.append(float(lines[54].split()[2]))
time_2_16_t8.append(float(lines[59].split()[2]))
time_2_32_t8.append(float(lines[64].split()[2]))
time_2_64_t8.append(float(lines[69].split()[2]))
time_5_8_t2.append(float(lines[87].split()[2]))
time_5_16_t2.append(float(lines[92].split()[2]))
time_5_32_t2.append(float(lines[97].split()[2]))
time_5_64_t2.append(float(lines[102].split()[2]))
time_5_8_t4.append(float(lines[88].split()[2]))
time_5_16_t4.append(float(lines[93].split()[2]))
time_5_32_t4.append(float(lines[98].split()[2]))
time_5_64_t4.append(float(lines[103].split()[2]))
time_5_8_t8.append(float(lines[89].split()[2]))
time_5_16_t8.append(float(lines[94].split()[2]))
time_5_32_t8.append(float(lines[99].split()[2]))
time_5_64_t8.append(float(lines[104].split()[2]))
time_10_8_t2.append(float(lines[122].split()[2]))
time_10_16_t2.append(float(lines[127].split()[2]))
time_10_32_t2.append(float(lines[132].split()[2]))
time_10_64_t2.append(float(lines[137].split()[2]))
time_10_8_t4.append(float(lines[123].split()[2]))
time_10_16_t4.append(float(lines[128].split()[2]))
time_10_32_t4.append(float(lines[133].split()[2]))
time_10_64_t4.append(float(lines[138].split()[2]))
time_10_8_t8.append(float(lines[124].split()[2]))
time_10_16_t8.append(float(lines[129].split()[2]))
time_10_32_t8.append(float(lines[134].split()[2]))
time_10_64_t8.append(float(lines[139].split()[2]))

filename = "outputs/omp/RKAB_400.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_1_8_t2.append(float(lines[17].split()[2]))
time_1_16_t2.append(float(lines[22].split()[2]))
time_1_32_t2.append(float(lines[27].split()[2]))
time_1_64_t2.append(float(lines[32].split()[2]))
time_1_8_t4.append(float(lines[18].split()[2]))
time_1_16_t4.append(float(lines[23].split()[2]))
time_1_32_t4.append(float(lines[28].split()[2]))
time_1_64_t4.append(float(lines[33].split()[2]))
time_1_8_t8.append(float(lines[19].split()[2]))
time_1_16_t8.append(float(lines[24].split()[2]))
time_1_32_t8.append(float(lines[29].split()[2]))
time_1_64_t8.append(float(lines[34].split()[2]))
time_2_8_t2.append(float(lines[52].split()[2]))
time_2_16_t2.append(float(lines[57].split()[2]))
time_2_32_t2.append(float(lines[62].split()[2]))
time_2_64_t2.append(float(lines[67].split()[2]))
time_2_8_t4.append(float(lines[53].split()[2]))
time_2_16_t4.append(float(lines[58].split()[2]))
time_2_32_t4.append(float(lines[63].split()[2]))
time_2_64_t4.append(float(lines[68].split()[2]))
time_2_8_t8.append(float(lines[54].split()[2]))
time_2_16_t8.append(float(lines[59].split()[2]))
time_2_32_t8.append(float(lines[64].split()[2]))
time_2_64_t8.append(float(lines[69].split()[2]))
time_5_8_t2.append(float(lines[87].split()[2]))
time_5_16_t2.append(float(lines[92].split()[2]))
time_5_32_t2.append(float(lines[97].split()[2]))
time_5_64_t2.append(float(lines[102].split()[2]))
time_5_8_t4.append(float(lines[88].split()[2]))
time_5_16_t4.append(float(lines[93].split()[2]))
time_5_32_t4.append(float(lines[98].split()[2]))
time_5_64_t4.append(float(lines[103].split()[2]))
time_5_8_t8.append(float(lines[89].split()[2]))
time_5_16_t8.append(float(lines[94].split()[2]))
time_5_32_t8.append(float(lines[99].split()[2]))
time_5_64_t8.append(float(lines[104].split()[2]))
time_10_8_t2.append(float(lines[122].split()[2]))
time_10_16_t2.append(float(lines[127].split()[2]))
time_10_32_t2.append(float(lines[132].split()[2]))
time_10_64_t2.append(float(lines[137].split()[2]))
time_10_8_t4.append(float(lines[123].split()[2]))
time_10_16_t4.append(float(lines[128].split()[2]))
time_10_32_t4.append(float(lines[133].split()[2]))
time_10_64_t4.append(float(lines[138].split()[2]))
time_10_8_t8.append(float(lines[124].split()[2]))
time_10_16_t8.append(float(lines[129].split()[2]))
time_10_32_t8.append(float(lines[134].split()[2]))
time_10_64_t8.append(float(lines[139].split()[2]))

filename = "outputs/omp/RKAB_uni_1.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

# rep / number of blocks / threads

time_1_8_uni_opt1_t2 = []
time_1_16_uni_opt1_t2 = []
time_1_32_uni_opt1_t2 = []
time_1_64_uni_opt1_t2 = []
time_1_8_uni_opt2_t2 = []
time_1_16_uni_opt2_t2 = []
time_1_32_uni_opt2_t2 = []
time_1_64_uni_opt2_t2 = []
time_1_8_uni_opt1_copy_t2 = []
time_1_16_uni_opt1_copy_t2 = []
time_1_32_uni_opt1_copy_t2 = []
time_1_64_uni_opt1_copy_t2 = []
time_1_8_uni_opt2_copy_t2 = []
time_1_16_uni_opt2_copy_t2 = []
time_1_32_uni_opt2_copy_t2 = []
time_1_64_uni_opt2_copy_t2 = []
time_1_8_uni_opt1_t4 = []
time_1_16_uni_opt1_t4 = []
time_1_32_uni_opt1_t4 = []
time_1_64_uni_opt1_t4 = []
time_1_8_uni_opt2_t4 = []
time_1_16_uni_opt2_t4 = []
time_1_32_uni_opt2_t4 = []
time_1_64_uni_opt2_t4 = []
time_1_8_uni_opt1_copy_t4 = []
time_1_16_uni_opt1_copy_t4 = []
time_1_32_uni_opt1_copy_t4 = []
time_1_64_uni_opt1_copy_t4 = []
time_1_8_uni_opt2_copy_t4 = []
time_1_16_uni_opt2_copy_t4 = []
time_1_32_uni_opt2_copy_t4 = []
time_1_64_uni_opt2_copy_t4 = []
time_1_8_uni_opt1_t8 = []
time_1_16_uni_opt1_t8 = []
time_1_32_uni_opt1_t8 = []
time_1_64_uni_opt1_t8 = []
time_1_8_uni_opt2_t8 = []
time_1_16_uni_opt2_t8 = []
time_1_32_uni_opt2_t8 = []
time_1_64_uni_opt2_t8 = []
time_1_8_uni_opt1_copy_t8 = []
time_1_16_uni_opt1_copy_t8 = []
time_1_32_uni_opt1_copy_t8 = []
time_1_64_uni_opt1_copy_t8 = []
time_1_8_uni_opt2_copy_t8 = []
time_1_16_uni_opt2_copy_t8 = []
time_1_32_uni_opt2_copy_t8 = []
time_1_64_uni_opt2_copy_t8 = []
for i in range(3):
	time_1_8_uni_opt1_t2.append(float(lines[62+140*i].split()[2]))
	time_1_16_uni_opt1_t2.append(float(lines[82+140*i].split()[2]))
	time_1_32_uni_opt1_t2.append(float(lines[102+140*i].split()[2]))
	time_1_64_uni_opt1_t2.append(float(lines[122+140*i].split()[2]))
	time_1_8_uni_opt2_t2.append(float(lines[67+140*i].split()[2]))
	time_1_16_uni_opt2_t2.append(float(lines[87+140*i].split()[2]))
	time_1_32_uni_opt2_t2.append(float(lines[107+140*i].split()[2]))
	time_1_64_uni_opt2_t2.append(float(lines[127+140*i].split()[2]))
	time_1_8_uni_opt1_copy_t2.append(float(lines[72+140*i].split()[2]))
	time_1_16_uni_opt1_copy_t2.append(float(lines[92+140*i].split()[2]))
	time_1_32_uni_opt1_copy_t2.append(float(lines[112+140*i].split()[2]))
	time_1_64_uni_opt1_copy_t2.append(float(lines[132+140*i].split()[2]))
	time_1_8_uni_opt2_copy_t2.append(float(lines[77+140*i].split()[2]))
	time_1_16_uni_opt2_copy_t2.append(float(lines[97+140*i].split()[2]))
	time_1_32_uni_opt2_copy_t2.append(float(lines[117+140*i].split()[2]))
	time_1_64_uni_opt2_copy_t2.append(float(lines[137+140*i].split()[2]))
	time_1_8_uni_opt1_t4.append(float(lines[63+140*i].split()[2]))
	time_1_16_uni_opt1_t4.append(float(lines[83+140*i].split()[2]))
	time_1_32_uni_opt1_t4.append(float(lines[103+140*i].split()[2]))
	time_1_64_uni_opt1_t4.append(float(lines[123+140*i].split()[2]))
	time_1_8_uni_opt2_t4.append(float(lines[68+140*i].split()[2]))
	time_1_16_uni_opt2_t4.append(float(lines[88+140*i].split()[2]))
	time_1_32_uni_opt2_t4.append(float(lines[108+140*i].split()[2]))
	time_1_64_uni_opt2_t4.append(float(lines[128+140*i].split()[2]))
	time_1_8_uni_opt1_copy_t4.append(float(lines[73+140*i].split()[2]))
	time_1_16_uni_opt1_copy_t4.append(float(lines[93+140*i].split()[2]))
	time_1_32_uni_opt1_copy_t4.append(float(lines[113+140*i].split()[2]))
	time_1_64_uni_opt1_copy_t4.append(float(lines[133+140*i].split()[2]))
	time_1_8_uni_opt2_copy_t4.append(float(lines[78+140*i].split()[2]))
	time_1_16_uni_opt2_copy_t4.append(float(lines[98+140*i].split()[2]))
	time_1_32_uni_opt2_copy_t4.append(float(lines[118+140*i].split()[2]))
	time_1_64_uni_opt2_copy_t4.append(float(lines[138+140*i].split()[2]))
	time_1_8_uni_opt1_t8.append(float(lines[64+140*i].split()[2]))
	time_1_16_uni_opt1_t8.append(float(lines[84+140*i].split()[2]))
	time_1_32_uni_opt1_t8.append(float(lines[103+140*i].split()[2]))
	time_1_64_uni_opt1_t8.append(float(lines[124+140*i].split()[2]))
	time_1_8_uni_opt2_t8.append(float(lines[69+140*i].split()[2]))
	time_1_16_uni_opt2_t8.append(float(lines[89+140*i].split()[2]))
	time_1_32_uni_opt2_t8.append(float(lines[109+140*i].split()[2]))
	time_1_64_uni_opt2_t8.append(float(lines[129+140*i].split()[2]))
	time_1_8_uni_opt1_copy_t8.append(float(lines[74+140*i].split()[2]))
	time_1_16_uni_opt1_copy_t8.append(float(lines[94+140*i].split()[2]))
	time_1_32_uni_opt1_copy_t8.append(float(lines[114+140*i].split()[2]))
	time_1_64_uni_opt1_copy_t8.append(float(lines[134+140*i].split()[2]))
	time_1_8_uni_opt2_copy_t8.append(float(lines[79+140*i].split()[2]))
	time_1_16_uni_opt2_copy_t8.append(float(lines[99+140*i].split()[2]))
	time_1_32_uni_opt2_copy_t8.append(float(lines[119+140*i].split()[2]))
	time_1_64_uni_opt2_copy_t8.append(float(lines[139+140*i].split()[2]))

filename = "outputs/omp/RKAB_uni_2.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

# rep / number of blocks / threads

time_2_8_uni_opt1_t2 = []
time_2_16_uni_opt1_t2 = []
time_2_32_uni_opt1_t2 = []
time_2_64_uni_opt1_t2 = []
time_2_8_uni_opt2_t2 = []
time_2_16_uni_opt2_t2 = []
time_2_32_uni_opt2_t2 = []
time_2_64_uni_opt2_t2 = []
time_2_8_uni_opt1_copy_t2 = []
time_2_16_uni_opt1_copy_t2 = []
time_2_32_uni_opt1_copy_t2 = []
time_2_64_uni_opt1_copy_t2 = []
time_2_8_uni_opt2_copy_t2 = []
time_2_16_uni_opt2_copy_t2 = []
time_2_32_uni_opt2_copy_t2 = []
time_2_64_uni_opt2_copy_t2 = []
time_2_8_uni_opt1_t4 = []
time_2_16_uni_opt1_t4 = []
time_2_32_uni_opt1_t4 = []
time_2_64_uni_opt1_t4 = []
time_2_8_uni_opt2_t4 = []
time_2_16_uni_opt2_t4 = []
time_2_32_uni_opt2_t4 = []
time_2_64_uni_opt2_t4 = []
time_2_8_uni_opt1_copy_t4 = []
time_2_16_uni_opt1_copy_t4 = []
time_2_32_uni_opt1_copy_t4 = []
time_2_64_uni_opt1_copy_t4 = []
time_2_8_uni_opt2_copy_t4 = []
time_2_16_uni_opt2_copy_t4 = []
time_2_32_uni_opt2_copy_t4 = []
time_2_64_uni_opt2_copy_t4 = []
time_2_8_uni_opt1_t8 = []
time_2_16_uni_opt1_t8 = []
time_2_32_uni_opt1_t8 = []
time_2_64_uni_opt1_t8 = []
time_2_8_uni_opt2_t8 = []
time_2_16_uni_opt2_t8 = []
time_2_32_uni_opt2_t8 = []
time_2_64_uni_opt2_t8 = []
time_2_8_uni_opt1_copy_t8 = []
time_2_16_uni_opt1_copy_t8 = []
time_2_32_uni_opt1_copy_t8 = []
time_2_64_uni_opt1_copy_t8 = []
time_2_8_uni_opt2_copy_t8 = []
time_2_16_uni_opt2_copy_t8 = []
time_2_32_uni_opt2_copy_t8 = []
time_2_64_uni_opt2_copy_t8 = []
for i in range(3):
	time_2_8_uni_opt1_t2.append(float(lines[62+140*i].split()[2]))
	time_2_16_uni_opt1_t2.append(float(lines[82+140*i].split()[2]))
	time_2_32_uni_opt1_t2.append(float(lines[102+140*i].split()[2]))
	time_2_64_uni_opt1_t2.append(float(lines[122+140*i].split()[2]))
	time_2_8_uni_opt2_t2.append(float(lines[67+140*i].split()[2]))
	time_2_16_uni_opt2_t2.append(float(lines[87+140*i].split()[2]))
	time_2_32_uni_opt2_t2.append(float(lines[107+140*i].split()[2]))
	time_2_64_uni_opt2_t2.append(float(lines[127+140*i].split()[2]))
	time_2_8_uni_opt1_copy_t2.append(float(lines[72+140*i].split()[2]))
	time_2_16_uni_opt1_copy_t2.append(float(lines[92+140*i].split()[2]))
	time_2_32_uni_opt1_copy_t2.append(float(lines[112+140*i].split()[2]))
	time_2_64_uni_opt1_copy_t2.append(float(lines[132+140*i].split()[2]))
	time_2_8_uni_opt2_copy_t2.append(float(lines[77+140*i].split()[2]))
	time_2_16_uni_opt2_copy_t2.append(float(lines[97+140*i].split()[2]))
	time_2_32_uni_opt2_copy_t2.append(float(lines[117+140*i].split()[2]))
	time_2_64_uni_opt2_copy_t2.append(float(lines[137+140*i].split()[2]))
	time_2_8_uni_opt1_t4.append(float(lines[63+140*i].split()[2]))
	time_2_16_uni_opt1_t4.append(float(lines[83+140*i].split()[2]))
	time_2_32_uni_opt1_t4.append(float(lines[103+140*i].split()[2]))
	time_2_64_uni_opt1_t4.append(float(lines[123+140*i].split()[2]))
	time_2_8_uni_opt2_t4.append(float(lines[68+140*i].split()[2]))
	time_2_16_uni_opt2_t4.append(float(lines[88+140*i].split()[2]))
	time_2_32_uni_opt2_t4.append(float(lines[108+140*i].split()[2]))
	time_2_64_uni_opt2_t4.append(float(lines[128+140*i].split()[2]))
	time_2_8_uni_opt1_copy_t4.append(float(lines[73+140*i].split()[2]))
	time_2_16_uni_opt1_copy_t4.append(float(lines[93+140*i].split()[2]))
	time_2_32_uni_opt1_copy_t4.append(float(lines[113+140*i].split()[2]))
	time_2_64_uni_opt1_copy_t4.append(float(lines[133+140*i].split()[2]))
	time_2_8_uni_opt2_copy_t4.append(float(lines[78+140*i].split()[2]))
	time_2_16_uni_opt2_copy_t4.append(float(lines[98+140*i].split()[2]))
	time_2_32_uni_opt2_copy_t4.append(float(lines[118+140*i].split()[2]))
	time_2_64_uni_opt2_copy_t4.append(float(lines[138+140*i].split()[2]))
	time_2_8_uni_opt1_t8.append(float(lines[64+140*i].split()[2]))
	time_2_16_uni_opt1_t8.append(float(lines[84+140*i].split()[2]))
	time_2_32_uni_opt1_t8.append(float(lines[103+140*i].split()[2]))
	time_2_64_uni_opt1_t8.append(float(lines[124+140*i].split()[2]))
	time_2_8_uni_opt2_t8.append(float(lines[69+140*i].split()[2]))
	time_2_16_uni_opt2_t8.append(float(lines[89+140*i].split()[2]))
	time_2_32_uni_opt2_t8.append(float(lines[109+140*i].split()[2]))
	time_2_64_uni_opt2_t8.append(float(lines[129+140*i].split()[2]))
	time_2_8_uni_opt1_copy_t8.append(float(lines[74+140*i].split()[2]))
	time_2_16_uni_opt1_copy_t8.append(float(lines[94+140*i].split()[2]))
	time_2_32_uni_opt1_copy_t8.append(float(lines[114+140*i].split()[2]))
	time_2_64_uni_opt1_copy_t8.append(float(lines[134+140*i].split()[2]))
	time_2_8_uni_opt2_copy_t8.append(float(lines[79+140*i].split()[2]))
	time_2_16_uni_opt2_copy_t8.append(float(lines[99+140*i].split()[2]))
	time_2_32_uni_opt2_copy_t8.append(float(lines[119+140*i].split()[2]))
	time_2_64_uni_opt2_copy_t8.append(float(lines[139+140*i].split()[2]))

filename = "outputs/omp/RKAB_uni_5.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

# rep / number of blocks / threads

time_5_8_uni_opt1_t2 = []
time_5_16_uni_opt1_t2 = []
time_5_32_uni_opt1_t2 = []
time_5_64_uni_opt1_t2 = []
time_5_8_uni_opt2_t2 = []
time_5_16_uni_opt2_t2 = []
time_5_32_uni_opt2_t2 = []
time_5_64_uni_opt2_t2 = []
time_5_8_uni_opt1_copy_t2 = []
time_5_16_uni_opt1_copy_t2 = []
time_5_32_uni_opt1_copy_t2 = []
time_5_64_uni_opt1_copy_t2 = []
time_5_8_uni_opt2_copy_t2 = []
time_5_16_uni_opt2_copy_t2 = []
time_5_32_uni_opt2_copy_t2 = []
time_5_64_uni_opt2_copy_t2 = []
time_5_8_uni_opt1_t4 = []
time_5_16_uni_opt1_t4 = []
time_5_32_uni_opt1_t4 = []
time_5_64_uni_opt1_t4 = []
time_5_8_uni_opt2_t4 = []
time_5_16_uni_opt2_t4 = []
time_5_32_uni_opt2_t4 = []
time_5_64_uni_opt2_t4 = []
time_5_8_uni_opt1_copy_t4 = []
time_5_16_uni_opt1_copy_t4 = []
time_5_32_uni_opt1_copy_t4 = []
time_5_64_uni_opt1_copy_t4 = []
time_5_8_uni_opt2_copy_t4 = []
time_5_16_uni_opt2_copy_t4 = []
time_5_32_uni_opt2_copy_t4 = []
time_5_64_uni_opt2_copy_t4 = []
time_5_8_uni_opt1_t8 = []
time_5_16_uni_opt1_t8 = []
time_5_32_uni_opt1_t8 = []
time_5_64_uni_opt1_t8 = []
time_5_8_uni_opt2_t8 = []
time_5_16_uni_opt2_t8 = []
time_5_32_uni_opt2_t8 = []
time_5_64_uni_opt2_t8 = []
time_5_8_uni_opt1_copy_t8 = []
time_5_16_uni_opt1_copy_t8 = []
time_5_32_uni_opt1_copy_t8 = []
time_5_64_uni_opt1_copy_t8 = []
time_5_8_uni_opt2_copy_t8 = []
time_5_16_uni_opt2_copy_t8 = []
time_5_32_uni_opt2_copy_t8 = []
time_5_64_uni_opt2_copy_t8 = []
for i in range(3):
	time_5_8_uni_opt1_t2.append(float(lines[62+140*i].split()[2]))
	time_5_16_uni_opt1_t2.append(float(lines[82+140*i].split()[2]))
	time_5_32_uni_opt1_t2.append(float(lines[102+140*i].split()[2]))
	time_5_64_uni_opt1_t2.append(float(lines[122+140*i].split()[2]))
	time_5_8_uni_opt2_t2.append(float(lines[67+140*i].split()[2]))
	time_5_16_uni_opt2_t2.append(float(lines[87+140*i].split()[2]))
	time_5_32_uni_opt2_t2.append(float(lines[107+140*i].split()[2]))
	time_5_64_uni_opt2_t2.append(float(lines[127+140*i].split()[2]))
	time_5_8_uni_opt1_copy_t2.append(float(lines[72+140*i].split()[2]))
	time_5_16_uni_opt1_copy_t2.append(float(lines[92+140*i].split()[2]))
	time_5_32_uni_opt1_copy_t2.append(float(lines[112+140*i].split()[2]))
	time_5_64_uni_opt1_copy_t2.append(float(lines[132+140*i].split()[2]))
	time_5_8_uni_opt2_copy_t2.append(float(lines[77+140*i].split()[2]))
	time_5_16_uni_opt2_copy_t2.append(float(lines[97+140*i].split()[2]))
	time_5_32_uni_opt2_copy_t2.append(float(lines[117+140*i].split()[2]))
	time_5_64_uni_opt2_copy_t2.append(float(lines[137+140*i].split()[2]))
	time_5_8_uni_opt1_t4.append(float(lines[63+140*i].split()[2]))
	time_5_16_uni_opt1_t4.append(float(lines[83+140*i].split()[2]))
	time_5_32_uni_opt1_t4.append(float(lines[103+140*i].split()[2]))
	time_5_64_uni_opt1_t4.append(float(lines[123+140*i].split()[2]))
	time_5_8_uni_opt2_t4.append(float(lines[68+140*i].split()[2]))
	time_5_16_uni_opt2_t4.append(float(lines[88+140*i].split()[2]))
	time_5_32_uni_opt2_t4.append(float(lines[108+140*i].split()[2]))
	time_5_64_uni_opt2_t4.append(float(lines[128+140*i].split()[2]))
	time_5_8_uni_opt1_copy_t4.append(float(lines[73+140*i].split()[2]))
	time_5_16_uni_opt1_copy_t4.append(float(lines[93+140*i].split()[2]))
	time_5_32_uni_opt1_copy_t4.append(float(lines[113+140*i].split()[2]))
	time_5_64_uni_opt1_copy_t4.append(float(lines[133+140*i].split()[2]))
	time_5_8_uni_opt2_copy_t4.append(float(lines[78+140*i].split()[2]))
	time_5_16_uni_opt2_copy_t4.append(float(lines[98+140*i].split()[2]))
	time_5_32_uni_opt2_copy_t4.append(float(lines[118+140*i].split()[2]))
	time_5_64_uni_opt2_copy_t4.append(float(lines[138+140*i].split()[2]))
	time_5_8_uni_opt1_t8.append(float(lines[64+140*i].split()[2]))
	time_5_16_uni_opt1_t8.append(float(lines[84+140*i].split()[2]))
	time_5_32_uni_opt1_t8.append(float(lines[103+140*i].split()[2]))
	time_5_64_uni_opt1_t8.append(float(lines[124+140*i].split()[2]))
	time_5_8_uni_opt2_t8.append(float(lines[69+140*i].split()[2]))
	time_5_16_uni_opt2_t8.append(float(lines[89+140*i].split()[2]))
	time_5_32_uni_opt2_t8.append(float(lines[109+140*i].split()[2]))
	time_5_64_uni_opt2_t8.append(float(lines[129+140*i].split()[2]))
	time_5_8_uni_opt1_copy_t8.append(float(lines[74+140*i].split()[2]))
	time_5_16_uni_opt1_copy_t8.append(float(lines[94+140*i].split()[2]))
	time_5_32_uni_opt1_copy_t8.append(float(lines[114+140*i].split()[2]))
	time_5_64_uni_opt1_copy_t8.append(float(lines[134+140*i].split()[2]))
	time_5_8_uni_opt2_copy_t8.append(float(lines[79+140*i].split()[2]))
	time_5_16_uni_opt2_copy_t8.append(float(lines[99+140*i].split()[2]))
	time_5_32_uni_opt2_copy_t8.append(float(lines[119+140*i].split()[2]))
	time_5_64_uni_opt2_copy_t8.append(float(lines[139+140*i].split()[2]))

filename = "outputs/omp/RKAB_uni_10.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

# rep / number of blocks / threads

time_10_8_uni_opt1_t2 = []
time_10_16_uni_opt1_t2 = []
time_10_32_uni_opt1_t2 = []
time_10_64_uni_opt1_t2 = []
time_10_8_uni_opt2_t2 = []
time_10_16_uni_opt2_t2 = []
time_10_32_uni_opt2_t2 = []
time_10_64_uni_opt2_t2 = []
time_10_8_uni_opt1_copy_t2 = []
time_10_16_uni_opt1_copy_t2 = []
time_10_32_uni_opt1_copy_t2 = []
time_10_64_uni_opt1_copy_t2 = []
time_10_8_uni_opt2_copy_t2 = []
time_10_16_uni_opt2_copy_t2 = []
time_10_32_uni_opt2_copy_t2 = []
time_10_64_uni_opt2_copy_t2 = []
time_10_8_uni_opt1_t4 = []
time_10_16_uni_opt1_t4 = []
time_10_32_uni_opt1_t4 = []
time_10_64_uni_opt1_t4 = []
time_10_8_uni_opt2_t4 = []
time_10_16_uni_opt2_t4 = []
time_10_32_uni_opt2_t4 = []
time_10_64_uni_opt2_t4 = []
time_10_8_uni_opt1_copy_t4 = []
time_10_16_uni_opt1_copy_t4 = []
time_10_32_uni_opt1_copy_t4 = []
time_10_64_uni_opt1_copy_t4 = []
time_10_8_uni_opt2_copy_t4 = []
time_10_16_uni_opt2_copy_t4 = []
time_10_32_uni_opt2_copy_t4 = []
time_10_64_uni_opt2_copy_t4 = []
time_10_8_uni_opt1_t8 = []
time_10_16_uni_opt1_t8 = []
time_10_32_uni_opt1_t8 = []
time_10_64_uni_opt1_t8 = []
time_10_8_uni_opt2_t8 = []
time_10_16_uni_opt2_t8 = []
time_10_32_uni_opt2_t8 = []
time_10_64_uni_opt2_t8 = []
time_10_8_uni_opt1_copy_t8 = []
time_10_16_uni_opt1_copy_t8 = []
time_10_32_uni_opt1_copy_t8 = []
time_10_64_uni_opt1_copy_t8 = []
time_10_8_uni_opt2_copy_t8 = []
time_10_16_uni_opt2_copy_t8 = []
time_10_32_uni_opt2_copy_t8 = []
time_10_64_uni_opt2_copy_t8 = []
for i in range(3):
	time_10_8_uni_opt1_t2.append(float(lines[62+140*i].split()[2]))
	time_10_16_uni_opt1_t2.append(float(lines[82+140*i].split()[2]))
	time_10_32_uni_opt1_t2.append(float(lines[102+140*i].split()[2]))
	time_10_64_uni_opt1_t2.append(float(lines[122+140*i].split()[2]))
	time_10_8_uni_opt2_t2.append(float(lines[67+140*i].split()[2]))
	time_10_16_uni_opt2_t2.append(float(lines[87+140*i].split()[2]))
	time_10_32_uni_opt2_t2.append(float(lines[107+140*i].split()[2]))
	time_10_64_uni_opt2_t2.append(float(lines[127+140*i].split()[2]))
	time_10_8_uni_opt1_copy_t2.append(float(lines[72+140*i].split()[2]))
	time_10_16_uni_opt1_copy_t2.append(float(lines[92+140*i].split()[2]))
	time_10_32_uni_opt1_copy_t2.append(float(lines[112+140*i].split()[2]))
	time_10_64_uni_opt1_copy_t2.append(float(lines[132+140*i].split()[2]))
	time_10_8_uni_opt2_copy_t2.append(float(lines[77+140*i].split()[2]))
	time_10_16_uni_opt2_copy_t2.append(float(lines[97+140*i].split()[2]))
	time_10_32_uni_opt2_copy_t2.append(float(lines[117+140*i].split()[2]))
	time_10_64_uni_opt2_copy_t2.append(float(lines[137+140*i].split()[2]))
	time_10_8_uni_opt1_t4.append(float(lines[63+140*i].split()[2]))
	time_10_16_uni_opt1_t4.append(float(lines[83+140*i].split()[2]))
	time_10_32_uni_opt1_t4.append(float(lines[103+140*i].split()[2]))
	time_10_64_uni_opt1_t4.append(float(lines[123+140*i].split()[2]))
	time_10_8_uni_opt2_t4.append(float(lines[68+140*i].split()[2]))
	time_10_16_uni_opt2_t4.append(float(lines[88+140*i].split()[2]))
	time_10_32_uni_opt2_t4.append(float(lines[108+140*i].split()[2]))
	time_10_64_uni_opt2_t4.append(float(lines[128+140*i].split()[2]))
	time_10_8_uni_opt1_copy_t4.append(float(lines[73+140*i].split()[2]))
	time_10_16_uni_opt1_copy_t4.append(float(lines[93+140*i].split()[2]))
	time_10_32_uni_opt1_copy_t4.append(float(lines[113+140*i].split()[2]))
	time_10_64_uni_opt1_copy_t4.append(float(lines[133+140*i].split()[2]))
	time_10_8_uni_opt2_copy_t4.append(float(lines[78+140*i].split()[2]))
	time_10_16_uni_opt2_copy_t4.append(float(lines[98+140*i].split()[2]))
	time_10_32_uni_opt2_copy_t4.append(float(lines[118+140*i].split()[2]))
	time_10_64_uni_opt2_copy_t4.append(float(lines[138+140*i].split()[2]))
	time_10_8_uni_opt1_t8.append(float(lines[64+140*i].split()[2]))
	time_10_16_uni_opt1_t8.append(float(lines[84+140*i].split()[2]))
	time_10_32_uni_opt1_t8.append(float(lines[103+140*i].split()[2]))
	time_10_64_uni_opt1_t8.append(float(lines[124+140*i].split()[2]))
	time_10_8_uni_opt2_t8.append(float(lines[69+140*i].split()[2]))
	time_10_16_uni_opt2_t8.append(float(lines[89+140*i].split()[2]))
	time_10_32_uni_opt2_t8.append(float(lines[109+140*i].split()[2]))
	time_10_64_uni_opt2_t8.append(float(lines[129+140*i].split()[2]))
	time_10_8_uni_opt1_copy_t8.append(float(lines[74+140*i].split()[2]))
	time_10_16_uni_opt1_copy_t8.append(float(lines[94+140*i].split()[2]))
	time_10_32_uni_opt1_copy_t8.append(float(lines[114+140*i].split()[2]))
	time_10_64_uni_opt1_copy_t8.append(float(lines[134+140*i].split()[2]))
	time_10_8_uni_opt2_copy_t8.append(float(lines[79+140*i].split()[2]))
	time_10_16_uni_opt2_copy_t8.append(float(lines[99+140*i].split()[2]))
	time_10_32_uni_opt2_copy_t8.append(float(lines[119+140*i].split()[2]))
	time_10_64_uni_opt2_copy_t8.append(float(lines[139+140*i].split()[2]))

time_1_50_uni_opt1_t2 = []
time_1_200_uni_opt1_t2 = []
time_1_400_uni_opt1_t2 = []
time_1_50_uni_opt2_t2 = []
time_1_200_uni_opt2_t2 = []
time_1_400_uni_opt2_t2 = []
time_1_50_uni_opt1_copy_t2 = []
time_1_200_uni_opt1_copy_t2 = []
time_1_400_uni_opt1_copy_t2 = []
time_1_50_uni_opt2_copy_t2 = []
time_1_200_uni_opt2_copy_t2 = []
time_1_400_uni_opt2_copy_t2 = []
time_1_50_uni_opt1_t4 = []
time_1_200_uni_opt1_t4 = []
time_1_400_uni_opt1_t4 = []
time_1_50_uni_opt2_t4 = []
time_1_200_uni_opt2_t4 = []
time_1_400_uni_opt2_t4 = []
time_1_50_uni_opt1_copy_t4 = []
time_1_200_uni_opt1_copy_t4 = []
time_1_400_uni_opt1_copy_t4 = []
time_1_50_uni_opt2_copy_t4 = []
time_1_200_uni_opt2_copy_t4 = []
time_1_400_uni_opt2_copy_t4 = []
time_1_50_uni_opt1_t8 = []
time_1_200_uni_opt1_t8 = []
time_1_400_uni_opt1_t8 = []
time_1_50_uni_opt2_t8 = []
time_1_200_uni_opt2_t8 = []
time_1_400_uni_opt2_t8 = []
time_1_50_uni_opt1_copy_t8 = []
time_1_200_uni_opt1_copy_t8 = []
time_1_400_uni_opt1_copy_t8 = []
time_1_50_uni_opt2_copy_t8 = []
time_1_200_uni_opt2_copy_t8 = []
time_1_400_uni_opt2_copy_t8 = []
time_2_50_uni_opt1_t2 = []
time_2_200_uni_opt1_t2 = []
time_2_400_uni_opt1_t2 = []
time_2_50_uni_opt2_t2 = []
time_2_200_uni_opt2_t2 = []
time_2_400_uni_opt2_t2 = []
time_2_50_uni_opt1_copy_t2 = []
time_2_200_uni_opt1_copy_t2 = []
time_2_400_uni_opt1_copy_t2 = []
time_2_50_uni_opt2_copy_t2 = []
time_2_200_uni_opt2_copy_t2 = []
time_2_400_uni_opt2_copy_t2 = []
time_2_50_uni_opt1_t4 = []
time_2_200_uni_opt1_t4 = []
time_2_400_uni_opt1_t4 = []
time_2_50_uni_opt2_t4 = []
time_2_200_uni_opt2_t4 = []
time_2_400_uni_opt2_t4 = []
time_2_50_uni_opt1_copy_t4 = []
time_2_200_uni_opt1_copy_t4 = []
time_2_400_uni_opt1_copy_t4 = []
time_2_50_uni_opt2_copy_t4 = []
time_2_200_uni_opt2_copy_t4 = []
time_2_400_uni_opt2_copy_t4 = []
time_2_50_uni_opt1_t8 = []
time_2_200_uni_opt1_t8 = []
time_2_400_uni_opt1_t8 = []
time_2_50_uni_opt2_t8 = []
time_2_200_uni_opt2_t8 = []
time_2_400_uni_opt2_t8 = []
time_2_50_uni_opt1_copy_t8 = []
time_2_200_uni_opt1_copy_t8 = []
time_2_400_uni_opt1_copy_t8 = []
time_2_50_uni_opt2_copy_t8 = []
time_2_200_uni_opt2_copy_t8 = []
time_2_400_uni_opt2_copy_t8 = []
time_5_50_uni_opt1_t2 = []
time_5_200_uni_opt1_t2 = []
time_5_400_uni_opt1_t2 = []
time_5_50_uni_opt2_t2 = []
time_5_200_uni_opt2_t2 = []
time_5_400_uni_opt2_t2 = []
time_5_50_uni_opt1_copy_t2 = []
time_5_200_uni_opt1_copy_t2 = []
time_5_400_uni_opt1_copy_t2 = []
time_5_50_uni_opt2_copy_t2 = []
time_5_200_uni_opt2_copy_t2 = []
time_5_400_uni_opt2_copy_t2 = []
time_5_50_uni_opt1_t4 = []
time_5_200_uni_opt1_t4 = []
time_5_400_uni_opt1_t4 = []
time_5_50_uni_opt2_t4 = []
time_5_200_uni_opt2_t4 = []
time_5_400_uni_opt2_t4 = []
time_5_50_uni_opt1_copy_t4 = []
time_5_200_uni_opt1_copy_t4 = []
time_5_400_uni_opt1_copy_t4 = []
time_5_50_uni_opt2_copy_t4 = []
time_5_200_uni_opt2_copy_t4 = []
time_5_400_uni_opt2_copy_t4 = []
time_5_50_uni_opt1_t8 = []
time_5_200_uni_opt1_t8 = []
time_5_400_uni_opt1_t8 = []
time_5_50_uni_opt2_t8 = []
time_5_200_uni_opt2_t8 = []
time_5_400_uni_opt2_t8 = []
time_5_50_uni_opt1_copy_t8 = []
time_5_200_uni_opt1_copy_t8 = []
time_5_400_uni_opt1_copy_t8 = []
time_5_50_uni_opt2_copy_t8 = []
time_5_200_uni_opt2_copy_t8 = []
time_5_400_uni_opt2_copy_t8 = []
time_10_50_uni_opt1_t2 = []
time_10_200_uni_opt1_t2 = []
time_10_400_uni_opt1_t2 = []
time_10_50_uni_opt2_t2 = []
time_10_200_uni_opt2_t2 = []
time_10_400_uni_opt2_t2 = []
time_10_50_uni_opt1_copy_t2 = []
time_10_200_uni_opt1_copy_t2 = []
time_10_400_uni_opt1_copy_t2 = []
time_10_50_uni_opt2_copy_t2 = []
time_10_200_uni_opt2_copy_t2 = []
time_10_400_uni_opt2_copy_t2 = []
time_10_50_uni_opt1_t4 = []
time_10_200_uni_opt1_t4 = []
time_10_400_uni_opt1_t4 = []
time_10_50_uni_opt2_t4 = []
time_10_200_uni_opt2_t4 = []
time_10_400_uni_opt2_t4 = []
time_10_50_uni_opt1_copy_t4 = []
time_10_200_uni_opt1_copy_t4 = []
time_10_400_uni_opt1_copy_t4 = []
time_10_50_uni_opt2_copy_t4 = []
time_10_200_uni_opt2_copy_t4 = []
time_10_400_uni_opt2_copy_t4 = []
time_10_50_uni_opt1_t8 = []
time_10_200_uni_opt1_t8 = []
time_10_400_uni_opt1_t8 = []
time_10_50_uni_opt2_t8 = []
time_10_200_uni_opt2_t8 = []
time_10_400_uni_opt2_t8 = []
time_10_50_uni_opt1_copy_t8 = []
time_10_200_uni_opt1_copy_t8 = []
time_10_400_uni_opt1_copy_t8 = []
time_10_50_uni_opt2_copy_t8 = []
time_10_200_uni_opt2_copy_t8 = []
time_10_400_uni_opt2_copy_t8 = []
time_1_50_uni_opt1_t2 = [time_1_8_uni_opt1_t2[0], time_1_16_uni_opt1_t2[0], time_1_32_uni_opt1_t2[0], time_1_64_uni_opt1_t2[0]]
time_1_200_uni_opt1_t2 = [time_1_8_uni_opt1_t2[1], time_1_16_uni_opt1_t2[1], time_1_32_uni_opt1_t2[1], time_1_64_uni_opt1_t2[1]]
time_1_400_uni_opt1_t2 = [time_1_8_uni_opt1_t2[2], time_1_16_uni_opt1_t2[2], time_1_32_uni_opt1_t2[2], time_1_64_uni_opt1_t2[2]]
time_1_50_uni_opt2_t2 = [time_1_8_uni_opt2_t2[0], time_1_16_uni_opt2_t2[0], time_1_32_uni_opt2_t2[0], time_1_64_uni_opt2_t2[0]]
time_1_200_uni_opt2_t2 = [time_1_8_uni_opt2_t2[1], time_1_16_uni_opt2_t2[1], time_1_32_uni_opt2_t2[1], time_1_64_uni_opt2_t2[1]]
time_1_400_uni_opt2_t2 = [time_1_8_uni_opt2_t2[2], time_1_16_uni_opt2_t2[2], time_1_32_uni_opt2_t2[2], time_1_64_uni_opt2_t2[2]]
time_1_50_uni_opt1_copy_t2 = [time_1_8_uni_opt1_copy_t2[0], time_1_16_uni_opt1_copy_t2[0], time_1_32_uni_opt1_copy_t2[0], time_1_64_uni_opt1_copy_t2[0]]
time_1_200_uni_opt1_copy_t2 = [time_1_8_uni_opt1_copy_t2[1], time_1_16_uni_opt1_copy_t2[1], time_1_32_uni_opt1_copy_t2[1], time_1_64_uni_opt1_copy_t2[1]]
time_1_400_uni_opt1_copy_t2 = [time_1_8_uni_opt1_copy_t2[2], time_1_16_uni_opt1_copy_t2[2], time_1_32_uni_opt1_copy_t2[2], time_1_64_uni_opt1_copy_t2[2]]
time_1_50_uni_opt2_copy_t2 = [time_1_8_uni_opt2_copy_t2[0], time_1_16_uni_opt2_copy_t2[0], time_1_32_uni_opt2_copy_t2[0], time_1_64_uni_opt2_copy_t2[0]]
time_1_200_uni_opt2_copy_t2 = [time_1_8_uni_opt2_copy_t2[1], time_1_16_uni_opt2_copy_t2[1], time_1_32_uni_opt2_copy_t2[1], time_1_64_uni_opt2_copy_t2[1]]
time_1_400_uni_opt2_copy_t2 = [time_1_8_uni_opt2_copy_t2[2], time_1_16_uni_opt2_copy_t2[2], time_1_32_uni_opt2_copy_t2[2], time_1_64_uni_opt2_copy_t2[2]]
time_1_50_uni_opt1_t4 = [time_1_8_uni_opt1_t4[0], time_1_16_uni_opt1_t4[0], time_1_32_uni_opt1_t4[0], time_1_64_uni_opt1_t4[0]]
time_1_200_uni_opt1_t4 = [time_1_8_uni_opt1_t4[1], time_1_16_uni_opt1_t4[1], time_1_32_uni_opt1_t4[1], time_1_64_uni_opt1_t4[1]]
time_1_400_uni_opt1_t4 = [time_1_8_uni_opt1_t4[2], time_1_16_uni_opt1_t4[2], time_1_32_uni_opt1_t4[2], time_1_64_uni_opt1_t4[2]]
time_1_50_uni_opt2_t4 = [time_1_8_uni_opt2_t4[0], time_1_16_uni_opt2_t4[0], time_1_32_uni_opt2_t4[0], time_1_64_uni_opt2_t4[0]]
time_1_200_uni_opt2_t4 = [time_1_8_uni_opt2_t4[1], time_1_16_uni_opt2_t4[1], time_1_32_uni_opt2_t4[1], time_1_64_uni_opt2_t4[1]]
time_1_400_uni_opt2_t4 = [time_1_8_uni_opt2_t4[2], time_1_16_uni_opt2_t4[2], time_1_32_uni_opt2_t4[2], time_1_64_uni_opt2_t4[2]]
time_1_50_uni_opt1_copy_t4 = [time_1_8_uni_opt1_copy_t4[0], time_1_16_uni_opt1_copy_t4[0], time_1_32_uni_opt1_copy_t4[0], time_1_64_uni_opt1_copy_t4[0]]
time_1_200_uni_opt1_copy_t4 = [time_1_8_uni_opt1_copy_t4[1], time_1_16_uni_opt1_copy_t4[1], time_1_32_uni_opt1_copy_t4[1], time_1_64_uni_opt1_copy_t4[1]]
time_1_400_uni_opt1_copy_t4 = [time_1_8_uni_opt1_copy_t4[2], time_1_16_uni_opt1_copy_t4[2], time_1_32_uni_opt1_copy_t4[2], time_1_64_uni_opt1_copy_t4[2]]
time_1_50_uni_opt2_copy_t4 = [time_1_8_uni_opt2_copy_t4[0], time_1_16_uni_opt2_copy_t4[0], time_1_32_uni_opt2_copy_t4[0], time_1_64_uni_opt2_copy_t4[0]]
time_1_200_uni_opt2_copy_t4 = [time_1_8_uni_opt2_copy_t4[1], time_1_16_uni_opt2_copy_t4[1], time_1_32_uni_opt2_copy_t4[1], time_1_64_uni_opt2_copy_t4[1]]
time_1_400_uni_opt2_copy_t4 = [time_1_8_uni_opt2_copy_t4[2], time_1_16_uni_opt2_copy_t4[2], time_1_32_uni_opt2_copy_t4[2], time_1_64_uni_opt2_copy_t4[2]]
time_1_50_uni_opt1_t8 = [time_1_8_uni_opt1_t8[0], time_1_16_uni_opt1_t8[0], time_1_32_uni_opt1_t8[0], time_1_64_uni_opt1_t8[0]]
time_1_200_uni_opt1_t8 = [time_1_8_uni_opt1_t8[1], time_1_16_uni_opt1_t8[1], time_1_32_uni_opt1_t8[1], time_1_64_uni_opt1_t8[1]]
time_1_400_uni_opt1_t8 = [time_1_8_uni_opt1_t8[2], time_1_16_uni_opt1_t8[2], time_1_32_uni_opt1_t8[2], time_1_64_uni_opt1_t8[2]]
time_1_50_uni_opt2_t8 = [time_1_8_uni_opt2_t8[0], time_1_16_uni_opt2_t8[0], time_1_32_uni_opt2_t8[0], time_1_64_uni_opt2_t8[0]]
time_1_200_uni_opt2_t8 = [time_1_8_uni_opt2_t8[1], time_1_16_uni_opt2_t8[1], time_1_32_uni_opt2_t8[1], time_1_64_uni_opt2_t8[1]]
time_1_400_uni_opt2_t8 = [time_1_8_uni_opt2_t8[2], time_1_16_uni_opt2_t8[2], time_1_32_uni_opt2_t8[2], time_1_64_uni_opt2_t8[2]]
time_1_50_uni_opt1_copy_t8 = [time_1_8_uni_opt1_copy_t8[0], time_1_16_uni_opt1_copy_t8[0], time_1_32_uni_opt1_copy_t8[0], time_1_64_uni_opt1_copy_t8[0]]
time_1_200_uni_opt1_copy_t8 = [time_1_8_uni_opt1_copy_t8[1], time_1_16_uni_opt1_copy_t8[1], time_1_32_uni_opt1_copy_t8[1], time_1_64_uni_opt1_copy_t8[1]]
time_1_400_uni_opt1_copy_t8 = [time_1_8_uni_opt1_copy_t8[2], time_1_16_uni_opt1_copy_t8[2], time_1_32_uni_opt1_copy_t8[2], time_1_64_uni_opt1_copy_t8[2]]
time_1_50_uni_opt2_copy_t8 = [time_1_8_uni_opt2_copy_t8[0], time_1_16_uni_opt2_copy_t8[0], time_1_32_uni_opt2_copy_t8[0], time_1_64_uni_opt2_copy_t8[0]]
time_1_200_uni_opt2_copy_t8 = [time_1_8_uni_opt2_copy_t8[1], time_1_16_uni_opt2_copy_t8[1], time_1_32_uni_opt2_copy_t8[1], time_1_64_uni_opt2_copy_t8[1]]
time_1_400_uni_opt2_copy_t8 = [time_1_8_uni_opt2_copy_t8[2], time_1_16_uni_opt2_copy_t8[2], time_1_32_uni_opt2_copy_t8[2], time_1_64_uni_opt2_copy_t8[2]]
time_2_50_uni_opt1_t2 = [time_2_8_uni_opt1_t2[0], time_2_16_uni_opt1_t2[0], time_2_32_uni_opt1_t2[0], time_2_64_uni_opt1_t2[0]]
time_2_200_uni_opt1_t2 = [time_2_8_uni_opt1_t2[1], time_2_16_uni_opt1_t2[1], time_2_32_uni_opt1_t2[1], time_2_64_uni_opt1_t2[1]]
time_2_400_uni_opt1_t2 = [time_2_8_uni_opt1_t2[2], time_2_16_uni_opt1_t2[2], time_2_32_uni_opt1_t2[2], time_2_64_uni_opt1_t2[2]]
time_2_50_uni_opt2_t2 = [time_2_8_uni_opt2_t2[0], time_2_16_uni_opt2_t2[0], time_2_32_uni_opt2_t2[0], time_2_64_uni_opt2_t2[0]]
time_2_200_uni_opt2_t2 = [time_2_8_uni_opt2_t2[1], time_2_16_uni_opt2_t2[1], time_2_32_uni_opt2_t2[1], time_2_64_uni_opt2_t2[1]]
time_2_400_uni_opt2_t2 = [time_2_8_uni_opt2_t2[2], time_2_16_uni_opt2_t2[2], time_2_32_uni_opt2_t2[2], time_2_64_uni_opt2_t2[2]]
time_2_50_uni_opt1_copy_t2 = [time_2_8_uni_opt1_copy_t2[0], time_2_16_uni_opt1_copy_t2[0], time_2_32_uni_opt1_copy_t2[0], time_2_64_uni_opt1_copy_t2[0]]
time_2_200_uni_opt1_copy_t2 = [time_2_8_uni_opt1_copy_t2[1], time_2_16_uni_opt1_copy_t2[1], time_2_32_uni_opt1_copy_t2[1], time_2_64_uni_opt1_copy_t2[1]]
time_2_400_uni_opt1_copy_t2 = [time_2_8_uni_opt1_copy_t2[2], time_2_16_uni_opt1_copy_t2[2], time_2_32_uni_opt1_copy_t2[2], time_2_64_uni_opt1_copy_t2[2]]
time_2_50_uni_opt2_copy_t2 = [time_2_8_uni_opt2_copy_t2[0], time_2_16_uni_opt2_copy_t2[0], time_2_32_uni_opt2_copy_t2[0], time_2_64_uni_opt2_copy_t2[0]]
time_2_200_uni_opt2_copy_t2 = [time_2_8_uni_opt2_copy_t2[1], time_2_16_uni_opt2_copy_t2[1], time_2_32_uni_opt2_copy_t2[1], time_2_64_uni_opt2_copy_t2[1]]
time_2_400_uni_opt2_copy_t2 = [time_2_8_uni_opt2_copy_t2[2], time_2_16_uni_opt2_copy_t2[2], time_2_32_uni_opt2_copy_t2[2], time_2_64_uni_opt2_copy_t2[2]]
time_2_50_uni_opt1_t4 = [time_2_8_uni_opt1_t4[0], time_2_16_uni_opt1_t4[0], time_2_32_uni_opt1_t4[0], time_2_64_uni_opt1_t4[0]]
time_2_200_uni_opt1_t4 = [time_2_8_uni_opt1_t4[1], time_2_16_uni_opt1_t4[1], time_2_32_uni_opt1_t4[1], time_2_64_uni_opt1_t4[1]]
time_2_400_uni_opt1_t4 = [time_2_8_uni_opt1_t4[2], time_2_16_uni_opt1_t4[2], time_2_32_uni_opt1_t4[2], time_2_64_uni_opt1_t4[2]]
time_2_50_uni_opt2_t4 = [time_2_8_uni_opt2_t4[0], time_2_16_uni_opt2_t4[0], time_2_32_uni_opt2_t4[0], time_2_64_uni_opt2_t4[0]]
time_2_200_uni_opt2_t4 = [time_2_8_uni_opt2_t4[1], time_2_16_uni_opt2_t4[1], time_2_32_uni_opt2_t4[1], time_2_64_uni_opt2_t4[1]]
time_2_400_uni_opt2_t4 = [time_2_8_uni_opt2_t4[2], time_2_16_uni_opt2_t4[2], time_2_32_uni_opt2_t4[2], time_2_64_uni_opt2_t4[2]]
time_2_50_uni_opt1_copy_t4 = [time_2_8_uni_opt1_copy_t4[0], time_2_16_uni_opt1_copy_t4[0], time_2_32_uni_opt1_copy_t4[0], time_2_64_uni_opt1_copy_t4[0]]
time_2_200_uni_opt1_copy_t4 = [time_2_8_uni_opt1_copy_t4[1], time_2_16_uni_opt1_copy_t4[1], time_2_32_uni_opt1_copy_t4[1], time_2_64_uni_opt1_copy_t4[1]]
time_2_400_uni_opt1_copy_t4 = [time_2_8_uni_opt1_copy_t4[2], time_2_16_uni_opt1_copy_t4[2], time_2_32_uni_opt1_copy_t4[2], time_2_64_uni_opt1_copy_t4[2]]
time_2_50_uni_opt2_copy_t4 = [time_2_8_uni_opt2_copy_t4[0], time_2_16_uni_opt2_copy_t4[0], time_2_32_uni_opt2_copy_t4[0], time_2_64_uni_opt2_copy_t4[0]]
time_2_200_uni_opt2_copy_t4 = [time_2_8_uni_opt2_copy_t4[1], time_2_16_uni_opt2_copy_t4[1], time_2_32_uni_opt2_copy_t4[1], time_2_64_uni_opt2_copy_t4[1]]
time_2_400_uni_opt2_copy_t4 = [time_2_8_uni_opt2_copy_t4[2], time_2_16_uni_opt2_copy_t4[2], time_2_32_uni_opt2_copy_t4[2], time_2_64_uni_opt2_copy_t4[2]]
time_2_50_uni_opt1_t8 = [time_2_8_uni_opt1_t8[0], time_2_16_uni_opt1_t8[0], time_2_32_uni_opt1_t8[0], time_2_64_uni_opt1_t8[0]]
time_2_200_uni_opt1_t8 = [time_2_8_uni_opt1_t8[1], time_2_16_uni_opt1_t8[1], time_2_32_uni_opt1_t8[1], time_2_64_uni_opt1_t8[1]]
time_2_400_uni_opt1_t8 = [time_2_8_uni_opt1_t8[2], time_2_16_uni_opt1_t8[2], time_2_32_uni_opt1_t8[2], time_2_64_uni_opt1_t8[2]]
time_2_50_uni_opt2_t8 = [time_2_8_uni_opt2_t8[0], time_2_16_uni_opt2_t8[0], time_2_32_uni_opt2_t8[0], time_2_64_uni_opt2_t8[0]]
time_2_200_uni_opt2_t8 = [time_2_8_uni_opt2_t8[1], time_2_16_uni_opt2_t8[1], time_2_32_uni_opt2_t8[1], time_2_64_uni_opt2_t8[1]]
time_2_400_uni_opt2_t8 = [time_2_8_uni_opt2_t8[2], time_2_16_uni_opt2_t8[2], time_2_32_uni_opt2_t8[2], time_2_64_uni_opt2_t8[2]]
time_2_50_uni_opt1_copy_t8 = [time_2_8_uni_opt1_copy_t8[0], time_2_16_uni_opt1_copy_t8[0], time_2_32_uni_opt1_copy_t8[0], time_2_64_uni_opt1_copy_t8[0]]
time_2_200_uni_opt1_copy_t8 = [time_2_8_uni_opt1_copy_t8[1], time_2_16_uni_opt1_copy_t8[1], time_2_32_uni_opt1_copy_t8[1], time_2_64_uni_opt1_copy_t8[1]]
time_2_400_uni_opt1_copy_t8 = [time_2_8_uni_opt1_copy_t8[2], time_2_16_uni_opt1_copy_t8[2], time_2_32_uni_opt1_copy_t8[2], time_2_64_uni_opt1_copy_t8[2]]
time_2_50_uni_opt2_copy_t8 = [time_2_8_uni_opt2_copy_t8[0], time_2_16_uni_opt2_copy_t8[0], time_2_32_uni_opt2_copy_t8[0], time_2_64_uni_opt2_copy_t8[0]]
time_2_200_uni_opt2_copy_t8 = [time_2_8_uni_opt2_copy_t8[1], time_2_16_uni_opt2_copy_t8[1], time_2_32_uni_opt2_copy_t8[1], time_2_64_uni_opt2_copy_t8[1]]
time_2_400_uni_opt2_copy_t8 = [time_2_8_uni_opt2_copy_t8[2], time_2_16_uni_opt2_copy_t8[2], time_2_32_uni_opt2_copy_t8[2], time_2_64_uni_opt2_copy_t8[2]]
time_5_50_uni_opt1_t2 = [time_5_8_uni_opt1_t2[0], time_5_16_uni_opt1_t2[0], time_5_32_uni_opt1_t2[0], time_5_64_uni_opt1_t2[0]]
time_5_200_uni_opt1_t2 = [time_5_8_uni_opt1_t2[1], time_5_16_uni_opt1_t2[1], time_5_32_uni_opt1_t2[1], time_5_64_uni_opt1_t2[1]]
time_5_400_uni_opt1_t2 = [time_5_8_uni_opt1_t2[2], time_5_16_uni_opt1_t2[2], time_5_32_uni_opt1_t2[2], time_5_64_uni_opt1_t2[2]]
time_5_50_uni_opt2_t2 = [time_5_8_uni_opt2_t2[0], time_5_16_uni_opt2_t2[0], time_5_32_uni_opt2_t2[0], time_5_64_uni_opt2_t2[0]]
time_5_200_uni_opt2_t2 = [time_5_8_uni_opt2_t2[1], time_5_16_uni_opt2_t2[1], time_5_32_uni_opt2_t2[1], time_5_64_uni_opt2_t2[1]]
time_5_400_uni_opt2_t2 = [time_5_8_uni_opt2_t2[2], time_5_16_uni_opt2_t2[2], time_5_32_uni_opt2_t2[2], time_5_64_uni_opt2_t2[2]]
time_5_50_uni_opt1_copy_t2 = [time_5_8_uni_opt1_copy_t2[0], time_5_16_uni_opt1_copy_t2[0], time_5_32_uni_opt1_copy_t2[0], time_5_64_uni_opt1_copy_t2[0]]
time_5_200_uni_opt1_copy_t2 = [time_5_8_uni_opt1_copy_t2[1], time_5_16_uni_opt1_copy_t2[1], time_5_32_uni_opt1_copy_t2[1], time_5_64_uni_opt1_copy_t2[1]]
time_5_400_uni_opt1_copy_t2 = [time_5_8_uni_opt1_copy_t2[2], time_5_16_uni_opt1_copy_t2[2], time_5_32_uni_opt1_copy_t2[2], time_5_64_uni_opt1_copy_t2[2]]
time_5_50_uni_opt2_copy_t2 = [time_5_8_uni_opt2_copy_t2[0], time_5_16_uni_opt2_copy_t2[0], time_5_32_uni_opt2_copy_t2[0], time_5_64_uni_opt2_copy_t2[0]]
time_5_200_uni_opt2_copy_t2 = [time_5_8_uni_opt2_copy_t2[1], time_5_16_uni_opt2_copy_t2[1], time_5_32_uni_opt2_copy_t2[1], time_5_64_uni_opt2_copy_t2[1]]
time_5_400_uni_opt2_copy_t2 = [time_5_8_uni_opt2_copy_t2[2], time_5_16_uni_opt2_copy_t2[2], time_5_32_uni_opt2_copy_t2[2], time_5_64_uni_opt2_copy_t2[2]]
time_5_50_uni_opt1_t4 = [time_5_8_uni_opt1_t4[0], time_5_16_uni_opt1_t4[0], time_5_32_uni_opt1_t4[0], time_5_64_uni_opt1_t4[0]]
time_5_200_uni_opt1_t4 = [time_5_8_uni_opt1_t4[1], time_5_16_uni_opt1_t4[1], time_5_32_uni_opt1_t4[1], time_5_64_uni_opt1_t4[1]]
time_5_400_uni_opt1_t4 = [time_5_8_uni_opt1_t4[2], time_5_16_uni_opt1_t4[2], time_5_32_uni_opt1_t4[2], time_5_64_uni_opt1_t4[2]]
time_5_50_uni_opt2_t4 = [time_5_8_uni_opt2_t4[0], time_5_16_uni_opt2_t4[0], time_5_32_uni_opt2_t4[0], time_5_64_uni_opt2_t4[0]]
time_5_200_uni_opt2_t4 = [time_5_8_uni_opt2_t4[1], time_5_16_uni_opt2_t4[1], time_5_32_uni_opt2_t4[1], time_5_64_uni_opt2_t4[1]]
time_5_400_uni_opt2_t4 = [time_5_8_uni_opt2_t4[2], time_5_16_uni_opt2_t4[2], time_5_32_uni_opt2_t4[2], time_5_64_uni_opt2_t4[2]]
time_5_50_uni_opt1_copy_t4 = [time_5_8_uni_opt1_copy_t4[0], time_5_16_uni_opt1_copy_t4[0], time_5_32_uni_opt1_copy_t4[0], time_5_64_uni_opt1_copy_t4[0]]
time_5_200_uni_opt1_copy_t4 = [time_5_8_uni_opt1_copy_t4[1], time_5_16_uni_opt1_copy_t4[1], time_5_32_uni_opt1_copy_t4[1], time_5_64_uni_opt1_copy_t4[1]]
time_5_400_uni_opt1_copy_t4 = [time_5_8_uni_opt1_copy_t4[2], time_5_16_uni_opt1_copy_t4[2], time_5_32_uni_opt1_copy_t4[2], time_5_64_uni_opt1_copy_t4[2]]
time_5_50_uni_opt2_copy_t4 = [time_5_8_uni_opt2_copy_t4[0], time_5_16_uni_opt2_copy_t4[0], time_5_32_uni_opt2_copy_t4[0], time_5_64_uni_opt2_copy_t4[0]]
time_5_200_uni_opt2_copy_t4 = [time_5_8_uni_opt2_copy_t4[1], time_5_16_uni_opt2_copy_t4[1], time_5_32_uni_opt2_copy_t4[1], time_5_64_uni_opt2_copy_t4[1]]
time_5_400_uni_opt2_copy_t4 = [time_5_8_uni_opt2_copy_t4[2], time_5_16_uni_opt2_copy_t4[2], time_5_32_uni_opt2_copy_t4[2], time_5_64_uni_opt2_copy_t4[2]]
time_5_50_uni_opt1_t8 = [time_5_8_uni_opt1_t8[0], time_5_16_uni_opt1_t8[0], time_5_32_uni_opt1_t8[0], time_5_64_uni_opt1_t8[0]]
time_5_200_uni_opt1_t8 = [time_5_8_uni_opt1_t8[1], time_5_16_uni_opt1_t8[1], time_5_32_uni_opt1_t8[1], time_5_64_uni_opt1_t8[1]]
time_5_400_uni_opt1_t8 = [time_5_8_uni_opt1_t8[2], time_5_16_uni_opt1_t8[2], time_5_32_uni_opt1_t8[2], time_5_64_uni_opt1_t8[2]]
time_5_50_uni_opt2_t8 = [time_5_8_uni_opt2_t8[0], time_5_16_uni_opt2_t8[0], time_5_32_uni_opt2_t8[0], time_5_64_uni_opt2_t8[0]]
time_5_200_uni_opt2_t8 = [time_5_8_uni_opt2_t8[1], time_5_16_uni_opt2_t8[1], time_5_32_uni_opt2_t8[1], time_5_64_uni_opt2_t8[1]]
time_5_400_uni_opt2_t8 = [time_5_8_uni_opt2_t8[2], time_5_16_uni_opt2_t8[2], time_5_32_uni_opt2_t8[2], time_5_64_uni_opt2_t8[2]]
time_5_50_uni_opt1_copy_t8 = [time_5_8_uni_opt1_copy_t8[0], time_5_16_uni_opt1_copy_t8[0], time_5_32_uni_opt1_copy_t8[0], time_5_64_uni_opt1_copy_t8[0]]
time_5_200_uni_opt1_copy_t8 = [time_5_8_uni_opt1_copy_t8[1], time_5_16_uni_opt1_copy_t8[1], time_5_32_uni_opt1_copy_t8[1], time_5_64_uni_opt1_copy_t8[1]]
time_5_400_uni_opt1_copy_t8 = [time_5_8_uni_opt1_copy_t8[2], time_5_16_uni_opt1_copy_t8[2], time_5_32_uni_opt1_copy_t8[2], time_5_64_uni_opt1_copy_t8[2]]
time_5_50_uni_opt2_copy_t8 = [time_5_8_uni_opt2_copy_t8[0], time_5_16_uni_opt2_copy_t8[0], time_5_32_uni_opt2_copy_t8[0], time_5_64_uni_opt2_copy_t8[0]]
time_5_200_uni_opt2_copy_t8 = [time_5_8_uni_opt2_copy_t8[1], time_5_16_uni_opt2_copy_t8[1], time_5_32_uni_opt2_copy_t8[1], time_5_64_uni_opt2_copy_t8[1]]
time_5_400_uni_opt2_copy_t8 = [time_5_8_uni_opt2_copy_t8[2], time_5_16_uni_opt2_copy_t8[2], time_5_32_uni_opt2_copy_t8[2], time_5_64_uni_opt2_copy_t8[2]]
time_10_50_uni_opt1_t2 = [time_10_8_uni_opt1_t2[0], time_10_16_uni_opt1_t2[0], time_10_32_uni_opt1_t2[0], time_10_64_uni_opt1_t2[0]]
time_10_200_uni_opt1_t2 = [time_10_8_uni_opt1_t2[1], time_10_16_uni_opt1_t2[1], time_10_32_uni_opt1_t2[1], time_10_64_uni_opt1_t2[1]]
time_10_400_uni_opt1_t2 = [time_10_8_uni_opt1_t2[2], time_10_16_uni_opt1_t2[2], time_10_32_uni_opt1_t2[2], time_10_64_uni_opt1_t2[2]]
time_10_50_uni_opt2_t2 = [time_10_8_uni_opt2_t2[0], time_10_16_uni_opt2_t2[0], time_10_32_uni_opt2_t2[0], time_10_64_uni_opt2_t2[0]]
time_10_200_uni_opt2_t2 = [time_10_8_uni_opt2_t2[1], time_10_16_uni_opt2_t2[1], time_10_32_uni_opt2_t2[1], time_10_64_uni_opt2_t2[1]]
time_10_400_uni_opt2_t2 = [time_10_8_uni_opt2_t2[2], time_10_16_uni_opt2_t2[2], time_10_32_uni_opt2_t2[2], time_10_64_uni_opt2_t2[2]]
time_10_50_uni_opt1_copy_t2 = [time_10_8_uni_opt1_copy_t2[0], time_10_16_uni_opt1_copy_t2[0], time_10_32_uni_opt1_copy_t2[0], time_10_64_uni_opt1_copy_t2[0]]
time_10_200_uni_opt1_copy_t2 = [time_10_8_uni_opt1_copy_t2[1], time_10_16_uni_opt1_copy_t2[1], time_10_32_uni_opt1_copy_t2[1], time_10_64_uni_opt1_copy_t2[1]]
time_10_400_uni_opt1_copy_t2 = [time_10_8_uni_opt1_copy_t2[2], time_10_16_uni_opt1_copy_t2[2], time_10_32_uni_opt1_copy_t2[2], time_10_64_uni_opt1_copy_t2[2]]
time_10_50_uni_opt2_copy_t2 = [time_10_8_uni_opt2_copy_t2[0], time_10_16_uni_opt2_copy_t2[0], time_10_32_uni_opt2_copy_t2[0], time_10_64_uni_opt2_copy_t2[0]]
time_10_200_uni_opt2_copy_t2 = [time_10_8_uni_opt2_copy_t2[1], time_10_16_uni_opt2_copy_t2[1], time_10_32_uni_opt2_copy_t2[1], time_10_64_uni_opt2_copy_t2[1]]
time_10_400_uni_opt2_copy_t2 = [time_10_8_uni_opt2_copy_t2[2], time_10_16_uni_opt2_copy_t2[2], time_10_32_uni_opt2_copy_t2[2], time_10_64_uni_opt2_copy_t2[2]]
time_10_50_uni_opt1_t4 = [time_10_8_uni_opt1_t4[0], time_10_16_uni_opt1_t4[0], time_10_32_uni_opt1_t4[0], time_10_64_uni_opt1_t4[0]]
time_10_200_uni_opt1_t4 = [time_10_8_uni_opt1_t4[1], time_10_16_uni_opt1_t4[1], time_10_32_uni_opt1_t4[1], time_10_64_uni_opt1_t4[1]]
time_10_400_uni_opt1_t4 = [time_10_8_uni_opt1_t4[2], time_10_16_uni_opt1_t4[2], time_10_32_uni_opt1_t4[2], time_10_64_uni_opt1_t4[2]]
time_10_50_uni_opt2_t4 = [time_10_8_uni_opt2_t4[0], time_10_16_uni_opt2_t4[0], time_10_32_uni_opt2_t4[0], time_10_64_uni_opt2_t4[0]]
time_10_200_uni_opt2_t4 = [time_10_8_uni_opt2_t4[1], time_10_16_uni_opt2_t4[1], time_10_32_uni_opt2_t4[1], time_10_64_uni_opt2_t4[1]]
time_10_400_uni_opt2_t4 = [time_10_8_uni_opt2_t4[2], time_10_16_uni_opt2_t4[2], time_10_32_uni_opt2_t4[2], time_10_64_uni_opt2_t4[2]]
time_10_50_uni_opt1_copy_t4 = [time_10_8_uni_opt1_copy_t4[0], time_10_16_uni_opt1_copy_t4[0], time_10_32_uni_opt1_copy_t4[0], time_10_64_uni_opt1_copy_t4[0]]
time_10_200_uni_opt1_copy_t4 = [time_10_8_uni_opt1_copy_t4[1], time_10_16_uni_opt1_copy_t4[1], time_10_32_uni_opt1_copy_t4[1], time_10_64_uni_opt1_copy_t4[1]]
time_10_400_uni_opt1_copy_t4 = [time_10_8_uni_opt1_copy_t4[2], time_10_16_uni_opt1_copy_t4[2], time_10_32_uni_opt1_copy_t4[2], time_10_64_uni_opt1_copy_t4[2]]
time_10_50_uni_opt2_copy_t4 = [time_10_8_uni_opt2_copy_t4[0], time_10_16_uni_opt2_copy_t4[0], time_10_32_uni_opt2_copy_t4[0], time_10_64_uni_opt2_copy_t4[0]]
time_10_200_uni_opt2_copy_t4 = [time_10_8_uni_opt2_copy_t4[1], time_10_16_uni_opt2_copy_t4[1], time_10_32_uni_opt2_copy_t4[1], time_10_64_uni_opt2_copy_t4[1]]
time_10_400_uni_opt2_copy_t4 = [time_10_8_uni_opt2_copy_t4[2], time_10_16_uni_opt2_copy_t4[2], time_10_32_uni_opt2_copy_t4[2], time_10_64_uni_opt2_copy_t4[2]]
time_10_50_uni_opt1_t8 = [time_10_8_uni_opt1_t8[0], time_10_16_uni_opt1_t8[0], time_10_32_uni_opt1_t8[0], time_10_64_uni_opt1_t8[0]]
time_10_200_uni_opt1_t8 = [time_10_8_uni_opt1_t8[1], time_10_16_uni_opt1_t8[1], time_10_32_uni_opt1_t8[1], time_10_64_uni_opt1_t8[1]]
time_10_400_uni_opt1_t8 = [time_10_8_uni_opt1_t8[2], time_10_16_uni_opt1_t8[2], time_10_32_uni_opt1_t8[2], time_10_64_uni_opt1_t8[2]]
time_10_50_uni_opt2_t8 = [time_10_8_uni_opt2_t8[0], time_10_16_uni_opt2_t8[0], time_10_32_uni_opt2_t8[0], time_10_64_uni_opt2_t8[0]]
time_10_200_uni_opt2_t8 = [time_10_8_uni_opt2_t8[1], time_10_16_uni_opt2_t8[1], time_10_32_uni_opt2_t8[1], time_10_64_uni_opt2_t8[1]]
time_10_400_uni_opt2_t8 = [time_10_8_uni_opt2_t8[2], time_10_16_uni_opt2_t8[2], time_10_32_uni_opt2_t8[2], time_10_64_uni_opt2_t8[2]]
time_10_50_uni_opt1_copy_t8 = [time_10_8_uni_opt1_copy_t8[0], time_10_16_uni_opt1_copy_t8[0], time_10_32_uni_opt1_copy_t8[0], time_10_64_uni_opt1_copy_t8[0]]
time_10_200_uni_opt1_copy_t8 = [time_10_8_uni_opt1_copy_t8[1], time_10_16_uni_opt1_copy_t8[1], time_10_32_uni_opt1_copy_t8[1], time_10_64_uni_opt1_copy_t8[1]]
time_10_400_uni_opt1_copy_t8 = [time_10_8_uni_opt1_copy_t8[2], time_10_16_uni_opt1_copy_t8[2], time_10_32_uni_opt1_copy_t8[2], time_10_64_uni_opt1_copy_t8[2]]
time_10_50_uni_opt2_copy_t8 = [time_10_8_uni_opt2_copy_t8[0], time_10_16_uni_opt2_copy_t8[0], time_10_32_uni_opt2_copy_t8[0], time_10_64_uni_opt2_copy_t8[0]]
time_10_200_uni_opt2_copy_t8 = [time_10_8_uni_opt2_copy_t8[1], time_10_16_uni_opt2_copy_t8[1], time_10_32_uni_opt2_copy_t8[1], time_10_64_uni_opt2_copy_t8[1]]
time_10_400_uni_opt2_copy_t8 = [time_10_8_uni_opt2_copy_t8[2], time_10_16_uni_opt2_copy_t8[2], time_10_32_uni_opt2_copy_t8[2], time_10_64_uni_opt2_copy_t8[2]]

time_1_50_t2 = []
time_1_200_t2 = []
time_1_400_t2 = []
time_1_50_t4 = []
time_1_200_t4 = []
time_1_400_t4 = []
time_1_50_t8 = []
time_1_200_t8 = []
time_1_400_t8 = []
time_2_50_t2 = []
time_2_200_t2 = []
time_2_400_t2 = []
time_2_50_t4 = []
time_2_200_t4 = []
time_2_400_t4 = []
time_2_50_t8 = []
time_2_200_t8 = []
time_2_400_t8 = []
time_5_50_t2 = []
time_5_200_t2 = []
time_5_400_t2 = []
time_5_50_t4 = []
time_5_200_t4 = []
time_5_400_t4 = []
time_5_50_t8 = []
time_5_200_t8 = []
time_5_400_t8 = []
time_10_50_t2 = []
time_10_200_t2 = []
time_10_400_t2 = []
time_10_50_t4 = []
time_10_200_t4 = []
time_10_400_t4 = []
time_10_50_t8 = []
time_10_200_t8 = []
time_10_400_t8 = []
time_1_50_t2 = [time_1_8_t2[0], time_1_16_t2[0], time_1_32_t2[0], time_1_64_t2[0]]
time_1_200_t2 = [time_1_8_t2[1], time_1_16_t2[1], time_1_32_t2[1], time_1_64_t2[1]]
time_1_400_t2 = [time_1_8_t2[2], time_1_16_t2[2], time_1_32_t2[2], time_1_64_t2[2]]
time_1_50_t4 = [time_1_8_t4[0], time_1_16_t4[0], time_1_32_t4[0], time_1_64_t4[0]]
time_1_200_t4 = [time_1_8_t4[1], time_1_16_t4[1], time_1_32_t4[1], time_1_64_t4[1]]
time_1_400_t4 = [time_1_8_t4[2], time_1_16_t4[2], time_1_32_t4[2], time_1_64_t4[2]]
time_1_50_t8 = [time_1_8_t8[0], time_1_16_t8[0], time_1_32_t8[0], time_1_64_t8[0]]
time_1_200_t8 = [time_1_8_t8[1], time_1_16_t8[1], time_1_32_t8[1], time_1_64_t8[1]]
time_1_400_t8 = [time_1_8_t8[2], time_1_16_t8[2], time_1_32_t8[2], time_1_64_t8[2]]
time_2_50_t2 = [time_2_8_t2[0], time_2_16_t2[0], time_2_32_t2[0], time_2_64_t2[0]]
time_2_200_t2 = [time_2_8_t2[1], time_2_16_t2[1], time_2_32_t2[1], time_2_64_t2[1]]
time_2_400_t2 = [time_2_8_t2[2], time_2_16_t2[2], time_2_32_t2[2], time_2_64_t2[2]]
time_2_50_t4 = [time_2_8_t4[0], time_2_16_t4[0], time_2_32_t4[0], time_2_64_t4[0]]
time_2_200_t4 = [time_2_8_t4[1], time_2_16_t4[1], time_2_32_t4[1], time_2_64_t4[1]]
time_2_400_t4 = [time_2_8_t4[2], time_2_16_t4[2], time_2_32_t4[2], time_2_64_t4[2]]
time_2_50_t8 = [time_2_8_t8[0], time_2_16_t8[0], time_2_32_t8[0], time_2_64_t8[0]]
time_2_200_t8 = [time_2_8_t8[1], time_2_16_t8[1], time_2_32_t8[1], time_2_64_t8[1]]
time_2_400_t8 = [time_2_8_t8[2], time_2_16_t8[2], time_2_32_t8[2], time_2_64_t8[2]]
time_5_50_t2 = [time_5_8_t2[0], time_5_16_t2[0], time_5_32_t2[0], time_5_64_t2[0]]
time_5_200_t2 = [time_5_8_t2[1], time_5_16_t2[1], time_5_32_t2[1], time_5_64_t2[1]]
time_5_400_t2 = [time_5_8_t2[2], time_5_16_t2[2], time_5_32_t2[2], time_5_64_t2[2]]
time_5_50_t4 = [time_5_8_t4[0], time_5_16_t4[0], time_5_32_t4[0], time_5_64_t4[0]]
time_5_200_t4 = [time_5_8_t4[1], time_5_16_t4[1], time_5_32_t4[1], time_5_64_t4[1]]
time_5_400_t4 = [time_5_8_t4[2], time_5_16_t4[2], time_5_32_t4[2], time_5_64_t4[2]]
time_5_50_t8 = [time_5_8_t8[0], time_5_16_t8[0], time_5_32_t8[0], time_5_64_t8[0]]
time_5_200_t8 = [time_5_8_t8[1], time_5_16_t8[1], time_5_32_t8[1], time_5_64_t8[1]]
time_5_400_t8 = [time_5_8_t8[2], time_5_16_t8[2], time_5_32_t8[2], time_5_64_t8[2]]
time_10_50_t2 = [time_10_8_t2[0], time_10_16_t2[0], time_10_32_t2[0], time_10_64_t2[0]]
time_10_200_t2 = [time_10_8_t2[1], time_10_16_t2[1], time_10_32_t2[1], time_10_64_t2[1]]
time_10_400_t2 = [time_10_8_t2[2], time_10_16_t2[2], time_10_32_t2[2], time_10_64_t2[2]]
time_10_50_t4 = [time_10_8_t4[0], time_10_16_t4[0], time_10_32_t4[0], time_10_64_t4[0]]
time_10_200_t4 = [time_10_8_t4[1], time_10_16_t4[1], time_10_32_t4[1], time_10_64_t4[1]]
time_10_400_t4 = [time_10_8_t4[2], time_10_16_t4[2], time_10_32_t4[2], time_10_64_t4[2]]
time_10_50_t8 = [time_10_8_t8[0], time_10_16_t8[0], time_10_32_t8[0], time_10_64_t8[0]]
time_10_200_t8 = [time_10_8_t8[1], time_10_16_t8[1], time_10_32_t8[1], time_10_64_t8[1]]
time_10_400_t8 = [time_10_8_t8[2], time_10_16_t8[2], time_10_32_t8[2], time_10_64_t8[2]]

x = [8, 16, 32, 64]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"Block size = 50 - No repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_50_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_50_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_50_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_50_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_50_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_1_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - No repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_200_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_200_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_200_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_200_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_200_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_1_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - No repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_400_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_400_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_400_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_400_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_400_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_1_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - No repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_50_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_50_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_50_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_50_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_50_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_1_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - No repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_200_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_200_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_200_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_200_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_200_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_1_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - No repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_400_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_400_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_400_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_400_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_400_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_1_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - No repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_50_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_50_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_50_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_50_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_50_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_1_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - No repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_200_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_200_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_200_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_200_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_200_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_1_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - No repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_1_400_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_1_400_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_1_400_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_1_400_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_1_400_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_1_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 2 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_50_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_50_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_50_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_50_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_50_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_2_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 2 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_200_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_200_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_200_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_200_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_200_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_2_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 2 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_400_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_400_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_400_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_400_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_400_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_2_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 2 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_50_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_50_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_50_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_50_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_50_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_2_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 2 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_200_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_200_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_200_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_200_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_200_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_2_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 2 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_400_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_400_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_400_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_400_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_400_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_2_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 2 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_50_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_50_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_50_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_50_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_50_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_2_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 2 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_200_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_200_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_200_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_200_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_200_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_2_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 2 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_2_400_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_2_400_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_2_400_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_2_400_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_2_400_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_2_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 5 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_50_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_50_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_50_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_50_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_50_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_5_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 5 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_200_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_200_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_200_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_200_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_200_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_5_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 5 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_400_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_400_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_400_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_400_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_400_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_5_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 5 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_50_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_50_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_50_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_50_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_50_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_5_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 5 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_200_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_200_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_200_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_200_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_200_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_5_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 5 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_400_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_400_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_400_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_400_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_400_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_5_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 5 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_50_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_50_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_50_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_50_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_50_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_5_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 5 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_200_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_200_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_200_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_200_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_200_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_5_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 5 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_5_400_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_5_400_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_5_400_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_5_400_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_5_400_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_5_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 10 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_50_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_50_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_50_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_50_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_50_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_10_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 10 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_200_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_200_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_200_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_200_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_200_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_10_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 10 repetitions and 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_400_uni_opt1_t2, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_400_uni_opt2_t2, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_400_uni_opt1_copy_t2, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_400_uni_opt2_copy_t2, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_400_t2, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_10_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 10 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_50_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_50_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_50_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_50_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_50_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_10_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 10 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_200_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_200_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_200_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_200_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_200_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_10_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 10 repetitions and 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_400_uni_opt1_t4, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_400_uni_opt2_t4, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_400_uni_opt1_copy_t4, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_400_uni_opt2_copy_t4, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_400_t4, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_10_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 50 - 10 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_50_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_50_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_50_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_50_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_50_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_50_10_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 200 - 10 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_200_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_200_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_200_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_200_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_200_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_200_10_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"Block size = 400 - 10 repetitions and 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_10_400_uni_opt1_t8, color='green', label=r'Uniform - Option 1 - No Copy')
plt.plot(x, time_10_400_uni_opt2_t8, color='yellow', label=r'Uniform - Option 2 - No Copy')
plt.plot(x, time_10_400_uni_opt1_copy_t8, color='orange', label=r'Uniform - Option 1 - With Copy')
plt.plot(x, time_10_400_uni_opt2_copy_t8, color='red', label=r'Uniform - Option 2 - With Copy')
plt.plot(x, time_10_400_t8, color='blue', label=r'Row Norms')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_uni_x_number_of_blocks_time_400_10_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)