import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_single_uni_seq_N_options.py

filename = "outputs/omp/RK_seq_uni.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))

indices = (10, 16, 18, 24, 26, 27, 33, 35, 36)
time_seq_dim = [time_seq[i] for i in indices]

filename = "outputs/omp/RKAB_single_uni.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))

time_par_2_uni_1 = time[9::32]
time_par_2_uni_2 = time[11::32]
time_par_2_uni_3 = time[13::32]
time_par_2_uni_4 = time[15::32]

time_par_4_uni_1 = time[17::32]
time_par_4_uni_2 = time[19::32]
time_par_4_uni_3 = time[21::32]
time_par_4_uni_4 = time[23::32]

time_par_8_uni_1 = time[25::32]
time_par_8_uni_2 = time[27::32]
time_par_8_uni_3 = time[29::32]
time_par_8_uni_4 = time[31::32]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = [5, 10, 50, 100, 500, 1000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[6], linewidth=1.5, linestyle='--', color='gray', label=r'SRKWOR')
plt.scatter(x, time_par_2_uni_1, color='orange')
plt.plot(x, time_par_2_uni_1, linewidth=1.5, color='orange', label=r'2 Threads - Option 1')
plt.scatter(x, time_par_2_uni_2, color='orange')
plt.plot(x, time_par_2_uni_2, linewidth=1.5, color='orange', linestyle='--', label=r'2 Threads - Option 2')
plt.scatter(x, time_par_4_uni_1, color='red')
plt.plot(x, time_par_4_uni_1, linewidth=1.5, color='red', label=r'4 Threads - Option 1')
plt.scatter(x, time_par_4_uni_2, color='red')
plt.plot(x, time_par_4_uni_2, linewidth=1.5, color='red', linestyle='--', label=r'4 Threads - Option 2')
plt.scatter(x, time_par_8_uni_1, color='blue')
plt.plot(x, time_par_8_uni_1, linewidth=1.5, color='blue', label=r'8 Threads - Option 1')
plt.scatter(x, time_par_8_uni_2, color='blue')
plt.plot(x, time_par_8_uni_2, linewidth=1.5, color='blue', linestyle='--', label=r'8 Threads - Option 2')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_uni_seq_N_time_options_80000_1000"

fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

filename = "outputs/omp/RKAB_single_uni_extra.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))

time_par_2_uni_1 = time[9::32]
time_par_2_uni_2 = time[11::32]
time_par_2_uni_3 = time[13::32]
time_par_2_uni_4 = time[15::32]

time_par_4_uni_1 = time[17::32]
time_par_4_uni_2 = time[19::32]
time_par_4_uni_3 = time[21::32]
time_par_4_uni_4 = time[23::32]

time_par_8_uni_1 = time[25::32]
time_par_8_uni_2 = time[27::32]
time_par_8_uni_3 = time[29::32]
time_par_8_uni_4 = time[31::32]

time_seq_2_uni_1 = time[8::32]
time_seq_2_uni_2 = time[10::32]
time_seq_2_uni_3 = time[12::32]
time_seq_2_uni_4 = time[14::32]

time_seq_4_uni_1 = time[16::32]
time_seq_4_uni_2 = time[18::32]
time_seq_4_uni_3 = time[20::32]
time_seq_4_uni_4 = time[22::32]

time_seq_8_uni_1 = time[24::32]
time_seq_8_uni_2 = time[26::32]
time_seq_8_uni_3 = time[28::32]
time_seq_8_uni_4 = time[30::32]

x = [5, 10, 50, 100, 500, 1000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[7], linewidth=1.5, linestyle='--', color='gray', label=r'SRKWOR')
plt.scatter(x, time_par_2_uni_1, color='orange')
plt.plot(x, time_par_2_uni_1, linewidth=1.5, color='orange', label=r'2 Threads - Option 1')
plt.scatter(x, time_par_2_uni_2, color='orange')
plt.plot(x, time_par_2_uni_2, linewidth=1.5, color='orange', linestyle='--', label=r'2 Threads - Option 2')
plt.scatter(x, time_par_4_uni_1, color='red')
plt.plot(x, time_par_4_uni_1, linewidth=1.5, color='red', label=r'4 Threads - Option 1')
plt.scatter(x, time_par_4_uni_2, color='red')
plt.plot(x, time_par_4_uni_2, linewidth=1.5, color='red', linestyle='--', label=r'4 Threads - Option 2')
plt.scatter(x, time_par_8_uni_1, color='blue')
plt.plot(x, time_par_8_uni_1, linewidth=1.5, color='blue', label=r'8 Threads - Option 1')
plt.scatter(x, time_par_8_uni_2, color='blue')
plt.plot(x, time_par_8_uni_2, linewidth=1.5, color='blue', linestyle='--', label=r'8 Threads - Option 2')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_uni_seq_N_time_options_80000_4000"

fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')