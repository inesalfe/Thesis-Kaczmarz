import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKA_uni_options_N.py

filename = "outputs/omp/RKA.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(float(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

time_seq_2 = time[2::8]
time_seq_4 = time[4::8]
time_seq_8 = time[6::8]

time_par_2 = time[3::8]
time_par_4 = time[5::8]
time_par_8 = time[7::8]

it_par_2 = it[3::8]
it_par_4 = it[5::8]
it_par_8 = it[7::8]

indices = (10, 16, 24, 33)
it_par_2_1000 = [it_par_2[i] for i in indices]
it_par_4_1000 = [it_par_4[i] for i in indices]
it_par_8_1000 = [it_par_8[i] for i in indices]
time_seq_2_1000 = [time_seq_2[i] for i in indices]
time_seq_4_1000 = [time_seq_4[i] for i in indices]
time_seq_8_1000 = [time_seq_8[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
speedup_2_1000 = [time_seq_2[i]/time_par_2[i] for i in indices]
speedup_4_1000 = [time_seq_4[i]/time_par_4[i] for i in indices]
speedup_8_1000 = [time_seq_8[i]/time_par_8[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (18, 26, 35)
it_par_2_4000 = [it_par_2[i] for i in indices]
it_par_4_4000 = [it_par_4[i] for i in indices]
it_par_8_4000 = [it_par_8[i] for i in indices]
time_seq_2_4000 = [time_seq_2[i] for i in indices]
time_seq_4_4000 = [time_seq_4[i] for i in indices]
time_seq_8_4000 = [time_seq_8[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
speedup_2_4000 = [time_seq_2[i]/time_par_2[i] for i in indices]
speedup_4_4000 = [time_seq_4[i]/time_par_4[i] for i in indices]
speedup_8_4000 = [time_seq_8[i]/time_par_8[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (27, 36)
it_par_2_10000 = [it_par_2[i] for i in indices]
it_par_4_10000 = [it_par_4[i] for i in indices]
it_par_8_10000 = [it_par_8[i] for i in indices]
time_seq_2_10000 = [time_seq_2[i] for i in indices]
time_seq_4_10000 = [time_seq_4[i] for i in indices]
time_seq_8_10000 = [time_seq_8[i] for i in indices]
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
speedup_2_10000 = [time_seq_2[i]/time_par_2[i] for i in indices]
speedup_4_10000 = [time_seq_4[i]/time_par_4[i] for i in indices]
speedup_8_10000 = [time_seq_8[i]/time_par_8[i] for i in indices]
x_10000 = [40000, 80000]

filename = "outputs/omp/RKA_uni.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(float(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

it_par_2_uni1 = it[9::32]
it_par_2_uni2 = it[11::32]
it_par_2_uni3 = it[13::32]
it_par_2_uni4 = it[15::32]

it_par_4_uni1 = it[17::32]
it_par_4_uni2 = it[19::32]
it_par_4_uni3 = it[21::32]
it_par_4_uni4 = it[23::32]

it_par_8_uni1 = it[25::32]
it_par_8_uni2 = it[27::32]
it_par_8_uni3 = it[29::32]
it_par_8_uni4 = it[31::32]

time_seq_2_uni1 = time[8::32]
time_seq_2_uni2 = time[10::32]
time_seq_2_uni3 = time[12::32]
time_seq_2_uni4 = time[14::32]

time_seq_4_uni1 = time[16::32]
time_seq_4_uni2 = time[18::32]
time_seq_4_uni3 = time[20::32]
time_seq_4_uni4 = time[22::32]

time_seq_8_uni1 = time[24::32]
time_seq_8_uni2 = time[26::32]
time_seq_8_uni3 = time[28::32]
time_seq_8_uni4 = time[30::32]

time_par_2_uni1 = time[9::32]
time_par_2_uni2 = time[11::32]
time_par_2_uni3 = time[13::32]
time_par_2_uni4 = time[15::32]

time_par_4_uni1 = time[17::32]
time_par_4_uni2 = time[19::32]
time_par_4_uni3 = time[21::32]
time_par_4_uni4 = time[23::32]

time_par_8_uni1 = time[25::32]
time_par_8_uni2 = time[27::32]
time_par_8_uni3 = time[29::32]
time_par_8_uni4 = time[31::32]

indices = (10, 16, 24, 33)
it_par_2_1000_uni1 = [it_par_2_uni1[i] for i in indices]
it_par_4_1000_uni1 = [it_par_4_uni1[i] for i in indices]
it_par_8_1000_uni1 = [it_par_8_uni1[i] for i in indices]
it_par_2_1000_uni2 = [it_par_2_uni2[i] for i in indices]
it_par_4_1000_uni2 = [it_par_4_uni2[i] for i in indices]
it_par_8_1000_uni2 = [it_par_8_uni2[i] for i in indices]
it_par_2_1000_uni3 = [it_par_2_uni3[i] for i in indices]
it_par_4_1000_uni3 = [it_par_4_uni3[i] for i in indices]
it_par_8_1000_uni3 = [it_par_8_uni3[i] for i in indices]
it_par_2_1000_uni4 = [it_par_2_uni4[i] for i in indices]
it_par_4_1000_uni4 = [it_par_4_uni4[i] for i in indices]
it_par_8_1000_uni4 = [it_par_8_uni4[i] for i in indices]
time_par_2_1000_uni1 = [time_par_2_uni1[i] for i in indices]
time_par_4_1000_uni1 = [time_par_4_uni1[i] for i in indices]
time_par_8_1000_uni1 = [time_par_8_uni1[i] for i in indices]
time_par_2_1000_uni2 = [time_par_2_uni2[i] for i in indices]
time_par_4_1000_uni2 = [time_par_4_uni2[i] for i in indices]
time_par_8_1000_uni2 = [time_par_8_uni2[i] for i in indices]
time_par_2_1000_uni3 = [time_par_2_uni3[i] for i in indices]
time_par_4_1000_uni3 = [time_par_4_uni3[i] for i in indices]
time_par_8_1000_uni3 = [time_par_8_uni3[i] for i in indices]
time_par_2_1000_uni4 = [time_par_2_uni4[i] for i in indices]
time_par_4_1000_uni4 = [time_par_4_uni4[i] for i in indices]
time_par_8_1000_uni4 = [time_par_8_uni4[i] for i in indices]
time_seq_2_1000_uni1 = [time_seq_2_uni1[i] for i in indices]
time_seq_4_1000_uni1 = [time_seq_4_uni1[i] for i in indices]
time_seq_8_1000_uni1 = [time_seq_8_uni1[i] for i in indices]
time_seq_2_1000_uni2 = [time_seq_2_uni2[i] for i in indices]
time_seq_4_1000_uni2 = [time_seq_4_uni2[i] for i in indices]
time_seq_8_1000_uni2 = [time_seq_8_uni2[i] for i in indices]
time_seq_2_1000_uni3 = [time_seq_2_uni3[i] for i in indices]
time_seq_4_1000_uni3 = [time_seq_4_uni3[i] for i in indices]
time_seq_8_1000_uni3 = [time_seq_8_uni3[i] for i in indices]
time_seq_2_1000_uni4 = [time_seq_2_uni4[i] for i in indices]
time_seq_4_1000_uni4 = [time_seq_4_uni4[i] for i in indices]
time_seq_8_1000_uni4 = [time_seq_8_uni4[i] for i in indices]
speedup_2_1000_uni1 = [time_seq_2_uni1[i]/time_par_2_uni1[i] for i in indices]
speedup_4_1000_uni1 = [time_seq_4_uni1[i]/time_par_4_uni1[i] for i in indices]
speedup_8_1000_uni1 = [time_seq_8_uni1[i]/time_par_8_uni1[i] for i in indices]
speedup_2_1000_uni2 = [time_seq_2_uni2[i]/time_par_2_uni2[i] for i in indices]
speedup_4_1000_uni2 = [time_seq_4_uni2[i]/time_par_4_uni2[i] for i in indices]
speedup_8_1000_uni2 = [time_seq_8_uni2[i]/time_par_8_uni2[i] for i in indices]
speedup_2_1000_uni3 = [time_seq_2_uni3[i]/time_par_2_uni3[i] for i in indices]
speedup_4_1000_uni3 = [time_seq_4_uni3[i]/time_par_4_uni3[i] for i in indices]
speedup_8_1000_uni3 = [time_seq_8_uni3[i]/time_par_8_uni3[i] for i in indices]
speedup_2_1000_uni4 = [time_seq_2_uni4[i]/time_par_2_uni4[i] for i in indices]
speedup_4_1000_uni4 = [time_seq_4_uni4[i]/time_par_4_uni4[i] for i in indices]
speedup_8_1000_uni4 = [time_seq_8_uni4[i]/time_par_8_uni4[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (18, 26, 35)
it_par_2_4000_uni1 = [it_par_2_uni1[i] for i in indices]
it_par_4_4000_uni1 = [it_par_4_uni1[i] for i in indices]
it_par_8_4000_uni1 = [it_par_8_uni1[i] for i in indices]
it_par_2_4000_uni2 = [it_par_2_uni2[i] for i in indices]
it_par_4_4000_uni2 = [it_par_4_uni2[i] for i in indices]
it_par_8_4000_uni2 = [it_par_8_uni2[i] for i in indices]
it_par_2_4000_uni3 = [it_par_2_uni3[i] for i in indices]
it_par_4_4000_uni3 = [it_par_4_uni3[i] for i in indices]
it_par_8_4000_uni3 = [it_par_8_uni3[i] for i in indices]
it_par_2_4000_uni4 = [it_par_2_uni4[i] for i in indices]
it_par_4_4000_uni4 = [it_par_4_uni4[i] for i in indices]
it_par_8_4000_uni4 = [it_par_8_uni4[i] for i in indices]
time_par_2_4000_uni1 = [time_par_2_uni1[i] for i in indices]
time_par_4_4000_uni1 = [time_par_4_uni1[i] for i in indices]
time_par_8_4000_uni1 = [time_par_8_uni1[i] for i in indices]
time_par_2_4000_uni2 = [time_par_2_uni2[i] for i in indices]
time_par_4_4000_uni2 = [time_par_4_uni2[i] for i in indices]
time_par_8_4000_uni2 = [time_par_8_uni2[i] for i in indices]
time_par_2_4000_uni3 = [time_par_2_uni3[i] for i in indices]
time_par_4_4000_uni3 = [time_par_4_uni3[i] for i in indices]
time_par_8_4000_uni3 = [time_par_8_uni3[i] for i in indices]
time_par_2_4000_uni4 = [time_par_2_uni4[i] for i in indices]
time_par_4_4000_uni4 = [time_par_4_uni4[i] for i in indices]
time_par_8_4000_uni4 = [time_par_8_uni4[i] for i in indices]
time_seq_2_4000_uni1 = [time_seq_2_uni1[i] for i in indices]
time_seq_4_4000_uni1 = [time_seq_4_uni1[i] for i in indices]
time_seq_8_4000_uni1 = [time_seq_8_uni1[i] for i in indices]
time_seq_2_4000_uni2 = [time_seq_2_uni2[i] for i in indices]
time_seq_4_4000_uni2 = [time_seq_4_uni2[i] for i in indices]
time_seq_8_4000_uni2 = [time_seq_8_uni2[i] for i in indices]
time_seq_2_4000_uni3 = [time_seq_2_uni3[i] for i in indices]
time_seq_4_4000_uni3 = [time_seq_4_uni3[i] for i in indices]
time_seq_8_4000_uni3 = [time_seq_8_uni3[i] for i in indices]
time_seq_2_4000_uni4 = [time_seq_2_uni4[i] for i in indices]
time_seq_4_4000_uni4 = [time_seq_4_uni4[i] for i in indices]
time_seq_8_4000_uni4 = [time_seq_8_uni4[i] for i in indices]
speedup_2_4000_uni1 = [time_seq_2_uni1[i]/time_par_2_uni1[i] for i in indices]
speedup_4_4000_uni1 = [time_seq_4_uni1[i]/time_par_4_uni1[i] for i in indices]
speedup_8_4000_uni1 = [time_seq_8_uni1[i]/time_par_8_uni1[i] for i in indices]
speedup_2_4000_uni2 = [time_seq_2_uni2[i]/time_par_2_uni2[i] for i in indices]
speedup_4_4000_uni2 = [time_seq_4_uni2[i]/time_par_4_uni2[i] for i in indices]
speedup_8_4000_uni2 = [time_seq_8_uni2[i]/time_par_8_uni2[i] for i in indices]
speedup_2_4000_uni3 = [time_seq_2_uni3[i]/time_par_2_uni3[i] for i in indices]
speedup_4_4000_uni3 = [time_seq_4_uni3[i]/time_par_4_uni3[i] for i in indices]
speedup_8_4000_uni3 = [time_seq_8_uni3[i]/time_par_8_uni3[i] for i in indices]
speedup_2_4000_uni4 = [time_seq_2_uni4[i]/time_par_2_uni4[i] for i in indices]
speedup_4_4000_uni4 = [time_seq_4_uni4[i]/time_par_4_uni4[i] for i in indices]
speedup_8_4000_uni4 = [time_seq_8_uni4[i]/time_par_8_uni4[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (27, 36)
it_par_2_10000_uni1 = [it_par_2_uni1[i] for i in indices]
it_par_4_10000_uni1 = [it_par_4_uni1[i] for i in indices]
it_par_8_10000_uni1 = [it_par_8_uni1[i] for i in indices]
it_par_2_10000_uni2 = [it_par_2_uni2[i] for i in indices]
it_par_4_10000_uni2 = [it_par_4_uni2[i] for i in indices]
it_par_8_10000_uni2 = [it_par_8_uni2[i] for i in indices]
it_par_2_10000_uni3 = [it_par_2_uni3[i] for i in indices]
it_par_4_10000_uni3 = [it_par_4_uni3[i] for i in indices]
it_par_8_10000_uni3 = [it_par_8_uni3[i] for i in indices]
it_par_2_10000_uni4 = [it_par_2_uni4[i] for i in indices]
it_par_4_10000_uni4 = [it_par_4_uni4[i] for i in indices]
it_par_8_10000_uni4 = [it_par_8_uni4[i] for i in indices]
time_par_2_10000_uni1 = [time_par_2_uni1[i] for i in indices]
time_par_4_10000_uni1 = [time_par_4_uni1[i] for i in indices]
time_par_8_10000_uni1 = [time_par_8_uni1[i] for i in indices]
time_par_2_10000_uni2 = [time_par_2_uni2[i] for i in indices]
time_par_4_10000_uni2 = [time_par_4_uni2[i] for i in indices]
time_par_8_10000_uni2 = [time_par_8_uni2[i] for i in indices]
time_par_2_10000_uni3 = [time_par_2_uni3[i] for i in indices]
time_par_4_10000_uni3 = [time_par_4_uni3[i] for i in indices]
time_par_8_10000_uni3 = [time_par_8_uni3[i] for i in indices]
time_par_2_10000_uni4 = [time_par_2_uni4[i] for i in indices]
time_par_4_10000_uni4 = [time_par_4_uni4[i] for i in indices]
time_par_8_10000_uni4 = [time_par_8_uni4[i] for i in indices]
time_seq_2_10000_uni1 = [time_seq_2_uni1[i] for i in indices]
time_seq_4_10000_uni1 = [time_seq_4_uni1[i] for i in indices]
time_seq_8_10000_uni1 = [time_seq_8_uni1[i] for i in indices]
time_seq_2_10000_uni2 = [time_seq_2_uni2[i] for i in indices]
time_seq_4_10000_uni2 = [time_seq_4_uni2[i] for i in indices]
time_seq_8_10000_uni2 = [time_seq_8_uni2[i] for i in indices]
time_seq_2_10000_uni3 = [time_seq_2_uni3[i] for i in indices]
time_seq_4_10000_uni3 = [time_seq_4_uni3[i] for i in indices]
time_seq_8_10000_uni3 = [time_seq_8_uni3[i] for i in indices]
time_seq_2_10000_uni4 = [time_seq_2_uni4[i] for i in indices]
time_seq_4_10000_uni4 = [time_seq_4_uni4[i] for i in indices]
time_seq_8_10000_uni4 = [time_seq_8_uni4[i] for i in indices]
speedup_2_10000_uni1 = [time_seq_2_uni1[i]/time_par_2_uni1[i] for i in indices]
speedup_4_10000_uni1 = [time_seq_4_uni1[i]/time_par_4_uni1[i] for i in indices]
speedup_8_10000_uni1 = [time_seq_8_uni1[i]/time_par_8_uni1[i] for i in indices]
speedup_2_10000_uni2 = [time_seq_2_uni2[i]/time_par_2_uni2[i] for i in indices]
speedup_4_10000_uni2 = [time_seq_4_uni2[i]/time_par_4_uni2[i] for i in indices]
speedup_8_10000_uni2 = [time_seq_8_uni2[i]/time_par_8_uni2[i] for i in indices]
speedup_2_10000_uni3 = [time_seq_2_uni3[i]/time_par_2_uni3[i] for i in indices]
speedup_4_10000_uni3 = [time_seq_4_uni3[i]/time_par_4_uni3[i] for i in indices]
speedup_8_10000_uni3 = [time_seq_8_uni3[i]/time_par_8_uni3[i] for i in indices]
speedup_2_10000_uni4 = [time_seq_2_uni4[i]/time_par_2_uni4[i] for i in indices]
speedup_4_10000_uni4 = [time_seq_4_uni4[i]/time_par_4_uni4[i] for i in indices]
speedup_8_10000_uni4 = [time_seq_8_uni4[i]/time_par_8_uni4[i] for i in indices]
x_10000 = [40000, 80000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"$n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, it_par_2_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - 2 Threads')
plt.plot(x_1000, it_par_2_1000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - 2 Threads')
plt.scatter(x_1000, it_par_2_1000_uni1, color='orange')
plt.scatter(x_1000, it_par_2_1000_uni2, color='orange')
plt.plot(x_1000, it_par_4_1000_uni1, linewidth=1.5, color='red', label=r'Option 1 - 4 Threads')
plt.plot(x_1000, it_par_4_1000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - 4 Threads')
plt.scatter(x_1000, it_par_4_1000_uni1, color='red')
plt.scatter(x_1000, it_par_4_1000_uni2, color='red')
plt.plot(x_1000, it_par_8_1000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - 8 Threads')
plt.plot(x_1000, it_par_8_1000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - 8 Threads')
plt.scatter(x_1000, it_par_8_1000_uni1, color='blue')
plt.scatter(x_1000, it_par_8_1000_uni2, color='blue')

plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, it_par_2_4000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - 2 Threads')
plt.plot(x_4000, it_par_2_4000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - 2 Threads')
plt.scatter(x_4000, it_par_2_4000_uni1, color='orange')
plt.scatter(x_4000, it_par_2_4000_uni2, color='orange')
plt.plot(x_4000, it_par_4_4000_uni1, linewidth=1.5, color='red', label=r'Option 1 - 4 Threads')
plt.plot(x_4000, it_par_4_4000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - 4 Threads')
plt.scatter(x_4000, it_par_4_4000_uni1, color='red')
plt.scatter(x_4000, it_par_4_4000_uni2, color='red')
plt.plot(x_4000, it_par_8_4000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - 8 Threads')
plt.plot(x_4000, it_par_8_4000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - 8 Threads')
plt.scatter(x_4000, it_par_8_4000_uni1, color='blue')
plt.scatter(x_4000, it_par_8_4000_uni2, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_10000, it_par_2_10000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - 2 Threads')
plt.plot(x_10000, it_par_2_10000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - 2 Threads')
plt.scatter(x_10000, it_par_2_10000_uni1, color='orange')
plt.scatter(x_10000, it_par_2_10000_uni2, color='orange')
plt.plot(x_10000, it_par_4_10000_uni1, linewidth=1.5, color='red', label=r'Option 1 - 4 Threads')
plt.plot(x_10000, it_par_4_10000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - 4 Threads')
plt.scatter(x_10000, it_par_4_10000_uni1, color='red')
plt.scatter(x_10000, it_par_4_10000_uni2, color='red')
plt.plot(x_10000, it_par_8_10000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - 8 Threads')
plt.plot(x_10000, it_par_8_10000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - 8 Threads')
plt.scatter(x_10000, it_par_8_10000_uni1, color='blue')
plt.scatter(x_10000, it_par_8_10000_uni2, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 2 projections"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, it_par_2_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - $n=1000$')
plt.plot(x_1000, it_par_2_1000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - $n=1000$')
plt.scatter(x_1000, it_par_2_1000_uni1, color='orange')
plt.scatter(x_1000, it_par_2_1000_uni2, color='orange')
plt.plot(x_4000, it_par_2_4000_uni1, linewidth=1.5, color='red', label=r'Option 1 - $n=4000$')
plt.plot(x_4000, it_par_2_4000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - $n=4000$')
plt.scatter(x_4000, it_par_2_4000_uni1, color='red')
plt.scatter(x_4000, it_par_2_4000_uni2, color='red')
plt.plot(x_10000, it_par_2_10000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - $n=10000$')
plt.plot(x_10000, it_par_2_10000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - $n=10000$')
plt.scatter(x_10000, it_par_2_10000_uni1, color='blue')
plt.scatter(x_10000, it_par_2_10000_uni2, color='blue')

plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 4 projections"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, it_par_4_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - $n=1000$')
plt.plot(x_1000, it_par_4_1000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - $n=1000$')
plt.scatter(x_1000, it_par_4_1000_uni1, color='orange')
plt.scatter(x_1000, it_par_4_1000_uni2, color='orange')
plt.plot(x_4000, it_par_4_4000_uni1, linewidth=1.5, color='red', label=r'Option 1 - $n=4000$')
plt.plot(x_4000, it_par_4_4000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - $n=4000$')
plt.scatter(x_4000, it_par_4_4000_uni1, color='red')
plt.scatter(x_4000, it_par_4_4000_uni2, color='red')
plt.plot(x_10000, it_par_4_10000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - $n=10000$')
plt.plot(x_10000, it_par_4_10000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - $n=10000$')
plt.scatter(x_10000, it_par_4_10000_uni1, color='blue')
plt.scatter(x_10000, it_par_4_10000_uni2, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 8 projections"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, it_par_8_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - $n=1000$')
plt.plot(x_1000, it_par_8_1000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - $n=1000$')
plt.scatter(x_1000, it_par_8_1000_uni1, color='orange')
plt.scatter(x_1000, it_par_8_1000_uni2, color='orange')
plt.plot(x_4000, it_par_8_4000_uni1, linewidth=1.5, color='red', label=r'Option 1 - $n=4000$')
plt.plot(x_4000, it_par_8_4000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - $n=4000$')
plt.scatter(x_4000, it_par_8_4000_uni1, color='red')
plt.scatter(x_4000, it_par_8_4000_uni2, color='red')
plt.plot(x_10000, it_par_8_10000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - $n=10000$')
plt.plot(x_10000, it_par_8_10000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - $n=10000$')
plt.scatter(x_10000, it_par_8_10000_uni1, color='blue')
plt.scatter(x_10000, it_par_8_10000_uni2, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, time_par_2_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - 2 Threads')
plt.plot(x_1000, time_par_2_1000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - 2 Threads')
plt.scatter(x_1000, time_par_2_1000_uni1, color='orange')
plt.scatter(x_1000, time_par_2_1000_uni2, color='orange')
plt.plot(x_1000, time_par_4_1000_uni1, linewidth=1.5, color='red', label=r'Option 1 - 4 Threads')
plt.plot(x_1000, time_par_4_1000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - 4 Threads')
plt.scatter(x_1000, time_par_4_1000_uni1, color='red')
plt.scatter(x_1000, time_par_4_1000_uni2, color='red')
plt.plot(x_1000, time_par_8_1000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - 8 Threads')
plt.plot(x_1000, time_par_8_1000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - 8 Threads')
plt.scatter(x_1000, time_par_8_1000_uni1, color='blue')
plt.scatter(x_1000, time_par_8_1000_uni2, color='blue')

plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, time_par_2_4000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - 2 Threads')
plt.plot(x_4000, time_par_2_4000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - 2 Threads')
plt.scatter(x_4000, time_par_2_4000_uni1, color='orange')
plt.scatter(x_4000, time_par_2_4000_uni2, color='orange')
plt.plot(x_4000, time_par_4_4000_uni1, linewidth=1.5, color='red', label=r'Option 1 - 4 Threads')
plt.plot(x_4000, time_par_4_4000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - 4 Threads')
plt.scatter(x_4000, time_par_4_4000_uni1, color='red')
plt.scatter(x_4000, time_par_4_4000_uni2, color='red')
plt.plot(x_4000, time_par_8_4000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - 8 Threads')
plt.plot(x_4000, time_par_8_4000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - 8 Threads')
plt.scatter(x_4000, time_par_8_4000_uni1, color='blue')
plt.scatter(x_4000, time_par_8_4000_uni2, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_10000, time_par_2_10000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - 2 Threads')
plt.plot(x_10000, time_par_2_10000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - 2 Threads')
plt.scatter(x_10000, time_par_2_10000_uni1, color='orange')
plt.scatter(x_10000, time_par_2_10000_uni2, color='orange')
plt.plot(x_10000, time_par_4_10000_uni1, linewidth=1.5, color='red', label=r'Option 1 - 4 Threads')
plt.plot(x_10000, time_par_4_10000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - 4 Threads')
plt.scatter(x_10000, time_par_4_10000_uni1, color='red')
plt.scatter(x_10000, time_par_4_10000_uni2, color='red')
plt.plot(x_10000, time_par_8_10000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - 8 Threads')
plt.plot(x_10000, time_par_8_10000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - 8 Threads')
plt.scatter(x_10000, time_par_8_10000_uni1, color='blue')
plt.scatter(x_10000, time_par_8_10000_uni2, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 2 projections"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, time_par_2_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - $n=1000$')
plt.plot(x_1000, time_par_2_1000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - $n=1000$')
plt.scatter(x_1000, time_par_2_1000_uni1, color='orange')
plt.scatter(x_1000, time_par_2_1000_uni2, color='orange')
plt.plot(x_4000, time_par_2_4000_uni1, linewidth=1.5, color='red', label=r'Option 1 - $n=4000$')
plt.plot(x_4000, time_par_2_4000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - $n=4000$')
plt.scatter(x_4000, time_par_2_4000_uni1, color='red')
plt.scatter(x_4000, time_par_2_4000_uni2, color='red')
plt.plot(x_10000, time_par_2_10000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - $n=10000$')
plt.plot(x_10000, time_par_2_10000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - $n=10000$')
plt.scatter(x_10000, time_par_2_10000_uni1, color='blue')
plt.scatter(x_10000, time_par_2_10000_uni2, color='blue')

plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 4 projections"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, time_par_4_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - $n=1000$')
plt.plot(x_1000, time_par_4_1000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - $n=1000$')
plt.scatter(x_1000, time_par_4_1000_uni1, color='orange')
plt.scatter(x_1000, time_par_4_1000_uni2, color='orange')
plt.plot(x_4000, time_par_4_4000_uni1, linewidth=1.5, color='red', label=r'Option 1 - $n=4000$')
plt.plot(x_4000, time_par_4_4000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - $n=4000$')
plt.scatter(x_4000, time_par_4_4000_uni1, color='red')
plt.scatter(x_4000, time_par_4_4000_uni2, color='red')
plt.plot(x_10000, time_par_4_10000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - $n=10000$')
plt.plot(x_10000, time_par_4_10000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - $n=10000$')
plt.scatter(x_10000, time_par_4_10000_uni1, color='blue')
plt.scatter(x_10000, time_par_4_10000_uni2, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 8 projections"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, time_par_8_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1 - $n=1000$')
plt.plot(x_1000, time_par_8_1000_uni2, linewidth=1.5, color='orange', linestyle='--', label=r'Option 2 - $n=1000$')
plt.scatter(x_1000, time_par_8_1000_uni1, color='orange')
plt.scatter(x_1000, time_par_8_1000_uni2, color='orange')
plt.plot(x_4000, time_par_8_4000_uni1, linewidth=1.5, color='red', label=r'Option 1 - $n=4000$')
plt.plot(x_4000, time_par_8_4000_uni2, linewidth=1.5, color='red', linestyle='--', label=r'Option 2 - $n=4000$')
plt.scatter(x_4000, time_par_8_4000_uni1, color='red')
plt.scatter(x_4000, time_par_8_4000_uni2, color='red')
plt.plot(x_10000, time_par_8_10000_uni1, linewidth=1.5, color='blue', label=r'Option 1 - $n=10000$')
plt.plot(x_10000, time_par_8_10000_uni2, linewidth=1.5, color='blue', linestyle='--', label=r'Option 2 - $n=10000$')
plt.scatter(x_10000, time_par_8_10000_uni1, color='blue')
plt.scatter(x_10000, time_par_8_10000_uni2, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 2 projections using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, time_par_2_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_1000, time_par_2_1000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_1000, time_par_2_1000_uni1, color='orange')
plt.scatter(x_1000, time_par_2_1000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_1000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 4 projections using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, time_par_4_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_1000, time_par_4_1000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_1000, time_par_4_1000_uni1, color='orange')
plt.scatter(x_1000, time_par_4_1000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_1000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 8 projections using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, time_par_8_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_1000, time_par_8_1000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_1000, time_par_8_1000_uni1, color='orange')
plt.scatter(x_1000, time_par_8_1000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_1000_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 2 projections using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, time_par_2_4000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_4000, time_par_2_4000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_4000, time_par_2_4000_uni1, color='orange')
plt.scatter(x_4000, time_par_2_4000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_4000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 4 projections using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, time_par_4_4000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_4000, time_par_4_4000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_4000, time_par_4_4000_uni1, color='orange')
plt.scatter(x_4000, time_par_4_4000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_4000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 8 projections using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, time_par_8_4000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_4000, time_par_8_4000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_4000, time_par_8_4000_uni1, color='orange')
plt.scatter(x_4000, time_par_8_4000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_4000_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 2 projections using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_10000, time_par_2_10000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_10000, time_par_2_10000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_10000, time_par_2_10000_uni1, color='orange')
plt.scatter(x_10000, time_par_2_10000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_10000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 4 projections using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_10000, time_par_4_10000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_10000, time_par_4_10000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_10000, time_par_4_10000_uni1, color='orange')
plt.scatter(x_10000, time_par_4_10000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_10000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 8 projections using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_10000, time_par_8_10000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_10000, time_par_8_10000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_10000, time_par_8_10000_uni1, color='orange')
plt.scatter(x_10000, time_par_8_10000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_uni_options_N_time_10000_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 2 projections using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, it_par_2_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_1000, it_par_2_1000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_1000, it_par_2_1000_uni1, color='orange')
plt.scatter(x_1000, it_par_2_1000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_1000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 4 projections using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, it_par_4_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_1000, it_par_4_1000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_1000, it_par_4_1000_uni1, color='orange')
plt.scatter(x_1000, it_par_4_1000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_1000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 8 projections using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, it_par_8_1000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_1000, it_par_8_1000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_1000, it_par_8_1000_uni1, color='orange')
plt.scatter(x_1000, it_par_8_1000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_1000_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 2 projections using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, it_par_2_4000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_4000, it_par_2_4000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_4000, it_par_2_4000_uni1, color='orange')
plt.scatter(x_4000, it_par_2_4000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_4000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 4 projections using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, it_par_4_4000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_4000, it_par_4_4000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_4000, it_par_4_4000_uni1, color='orange')
plt.scatter(x_4000, it_par_4_4000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_4000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 8 projections using $n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, it_par_8_4000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_4000, it_par_8_4000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_4000, it_par_8_4000_uni1, color='orange')
plt.scatter(x_4000, it_par_8_4000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_4000_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 2 projections using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_10000, it_par_2_10000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_10000, it_par_2_10000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_10000, it_par_2_10000_uni1, color='orange')
plt.scatter(x_10000, it_par_2_10000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_10000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 4 projections using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_10000, it_par_4_10000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_10000, it_par_4_10000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_10000, it_par_4_10000_uni1, color='orange')
plt.scatter(x_10000, it_par_4_10000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_10000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of 8 projections using $n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.plot(x_10000, it_par_8_10000_uni1, linewidth=1.5, color='orange', label=r'Option 1')
plt.plot(x_10000, it_par_8_10000_uni2, linewidth=1.5, color='red', label=r'Option 2')
plt.scatter(x_10000, it_par_8_10000_uni1, color='orange')
plt.scatter(x_10000, it_par_8_10000_uni2, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_uni_options_N_it_10000_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()