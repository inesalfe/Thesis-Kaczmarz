import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi/RKA_alpha_options.py

filename = "outputs/mpi/RKA_mpi_alpha.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(float(lines[i].split()[3]))

it_seq_1 = it[0::20]
it_seq_2 = it[4::20]
it_seq_4 = it[8::20]
it_seq_8 = it[12::20]
it_seq_20 = it[16::20]

it_par_op1_1 = it[1::20]
it_par_op1_2 = it[5::20]
it_par_op1_4 = it[9::20]
it_par_op1_8 = it[13::20]
it_par_op1_20 = it[17::20]

it_par_op2_1 = it[2::20]
it_par_op2_2 = it[6::20]
it_par_op2_4 = it[10::20]
it_par_op2_8 = it[14::20]
it_par_op2_20 = it[18::20]

it_par_op3_1 = it[3::20]
it_par_op3_2 = it[7::20]
it_par_op3_4 = it[11::20]
it_par_op3_8 = it[15::20]
it_par_op3_20 = it[19::20]

time_seq_1 = time[0::20]
time_seq_2 = time[4::20]
time_seq_4 = time[8::20]
time_seq_8 = time[12::20]
time_seq_20 = time[16::20]

time_par_op1_1 = time[1::20]
time_par_op1_2 = time[5::20]
time_par_op1_4 = time[9::20]
time_par_op1_8 = time[13::20]
time_par_op1_20 = time[17::20]

time_par_op2_1 = time[2::20]
time_par_op2_2 = time[6::20]
time_par_op2_4 = time[10::20]
time_par_op2_8 = time[14::20]
time_par_op2_20 = time[18::20]

time_par_op3_1 = time[3::20]
time_par_op3_2 = time[7::20]
time_par_op3_4 = time[11::20]
time_par_op3_8 = time[15::20]
time_par_op3_20 = time[19::20]

indices = (0, 1, 3, 6)
it_seq_1_1000 = [it_seq_1[i] for i in indices]
it_seq_2_1000 = [it_seq_2[i] for i in indices]
it_seq_4_1000 = [it_seq_4[i] for i in indices]
it_seq_8_1000 = [it_seq_8[i] for i in indices]
it_seq_20_1000 = [it_seq_20[i] for i in indices]
it_par_op1_1_1000 = [it_par_op1_1[i] for i in indices]
it_par_op1_2_1000 = [it_par_op1_2[i] for i in indices]
it_par_op1_4_1000 = [it_par_op1_4[i] for i in indices]
it_par_op1_8_1000 = [it_par_op1_8[i] for i in indices]
it_par_op1_20_1000 = [it_par_op1_20[i] for i in indices]
it_par_op2_1_1000 = [it_par_op2_1[i] for i in indices]
it_par_op2_2_1000 = [it_par_op2_2[i] for i in indices]
it_par_op2_4_1000 = [it_par_op2_4[i] for i in indices]
it_par_op2_8_1000 = [it_par_op2_8[i] for i in indices]
it_par_op2_20_1000 = [it_par_op2_20[i] for i in indices]
it_par_op3_1_1000 = [it_par_op3_1[i] for i in indices]
it_par_op3_2_1000 = [it_par_op3_2[i] for i in indices]
it_par_op3_4_1000 = [it_par_op3_4[i] for i in indices]
it_par_op3_8_1000 = [it_par_op3_8[i] for i in indices]
it_par_op3_20_1000 = [it_par_op3_20[i] for i in indices]
time_seq_1_1000 = [time_seq_1[i] for i in indices]
time_seq_2_1000 = [time_seq_2[i] for i in indices]
time_seq_4_1000 = [time_seq_4[i] for i in indices]
time_seq_8_1000 = [time_seq_8[i] for i in indices]
time_seq_20_1000 = [time_seq_20[i] for i in indices]
time_par_op1_1_1000 = [time_par_op1_1[i] for i in indices]
time_par_op1_2_1000 = [time_par_op1_2[i] for i in indices]
time_par_op1_4_1000 = [time_par_op1_4[i] for i in indices]
time_par_op1_8_1000 = [time_par_op1_8[i] for i in indices]
time_par_op1_20_1000 = [time_par_op1_20[i] for i in indices]
time_par_op2_1_1000 = [time_par_op2_1[i] for i in indices]
time_par_op2_2_1000 = [time_par_op2_2[i] for i in indices]
time_par_op2_4_1000 = [time_par_op2_4[i] for i in indices]
time_par_op2_8_1000 = [time_par_op2_8[i] for i in indices]
time_par_op2_20_1000 = [time_par_op2_20[i] for i in indices]
time_par_op3_1_1000 = [time_par_op3_1[i] for i in indices]
time_par_op3_2_1000 = [time_par_op3_2[i] for i in indices]
time_par_op3_4_1000 = [time_par_op3_4[i] for i in indices]
time_par_op3_8_1000 = [time_par_op3_8[i] for i in indices]
time_par_op3_20_1000 = [time_par_op3_20[i] for i in indices]
time_per_it_1_1000 = [time_seq_1[i]/it_seq_1[i] for i in indices]
time_per_it_2_1000 = [time_seq_2[i]/it_seq_2[i] for i in indices]
time_per_it_4_1000 = [time_seq_4[i]/it_seq_4[i] for i in indices]
time_per_it_8_1000 = [time_seq_8[i]/it_seq_8[i] for i in indices]
time_per_it_20_1000 = [time_seq_20[i]/it_seq_20[i] for i in indices]
time_per_it_op1_1_1000 = [time_par_op1_1[i]/it_par_op1_1[i] for i in indices]
time_per_it_op1_2_1000 = [time_par_op1_2[i]/it_par_op1_2[i] for i in indices]
time_per_it_op1_4_1000 = [time_par_op1_4[i]/it_par_op1_4[i] for i in indices]
time_per_it_op1_8_1000 = [time_par_op1_8[i]/it_par_op1_8[i] for i in indices]
time_per_it_op1_20_1000 = [time_par_op1_20[i]/it_par_op1_20[i] for i in indices]
time_per_it_op2_1_1000 = [time_par_op2_1[i]/it_par_op2_1[i] for i in indices]
time_per_it_op2_2_1000 = [time_par_op2_2[i]/it_par_op2_2[i] for i in indices]
time_per_it_op2_4_1000 = [time_par_op2_4[i]/it_par_op2_4[i] for i in indices]
time_per_it_op2_8_1000 = [time_par_op2_8[i]/it_par_op2_8[i] for i in indices]
time_per_it_op2_20_1000 = [time_par_op2_20[i]/it_par_op2_20[i] for i in indices]
time_per_it_op3_1_1000 = [time_par_op3_1[i]/it_par_op3_1[i] for i in indices]
time_per_it_op3_2_1000 = [time_par_op3_2[i]/it_par_op3_2[i] for i in indices]
time_per_it_op3_4_1000 = [time_par_op3_4[i]/it_par_op3_4[i] for i in indices]
time_per_it_op3_8_1000 = [time_par_op3_8[i]/it_par_op3_8[i] for i in indices]
time_per_it_op3_20_1000 = [time_par_op3_20[i]/it_par_op3_20[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (2, 4, 7)
it_seq_1_4000 = [it_seq_1[i] for i in indices]
it_seq_2_4000 = [it_seq_2[i] for i in indices]
it_seq_4_4000 = [it_seq_4[i] for i in indices]
it_seq_8_4000 = [it_seq_8[i] for i in indices]
it_seq_20_4000 = [it_seq_20[i] for i in indices]
it_par_op1_1_4000 = [it_par_op1_1[i] for i in indices]
it_par_op1_2_4000 = [it_par_op1_2[i] for i in indices]
it_par_op1_4_4000 = [it_par_op1_4[i] for i in indices]
it_par_op1_8_4000 = [it_par_op1_8[i] for i in indices]
it_par_op1_20_4000 = [it_par_op1_20[i] for i in indices]
it_par_op2_1_4000 = [it_par_op2_1[i] for i in indices]
it_par_op2_2_4000 = [it_par_op2_2[i] for i in indices]
it_par_op2_4_4000 = [it_par_op2_4[i] for i in indices]
it_par_op2_8_4000 = [it_par_op2_8[i] for i in indices]
it_par_op2_20_4000 = [it_par_op2_20[i] for i in indices]
it_par_op3_1_4000 = [it_par_op3_1[i] for i in indices]
it_par_op3_2_4000 = [it_par_op3_2[i] for i in indices]
it_par_op3_4_4000 = [it_par_op3_4[i] for i in indices]
it_par_op3_8_4000 = [it_par_op3_8[i] for i in indices]
it_par_op3_20_4000 = [it_par_op3_20[i] for i in indices]
time_seq_1_4000 = [time_seq_1[i] for i in indices]
time_seq_2_4000 = [time_seq_2[i] for i in indices]
time_seq_4_4000 = [time_seq_4[i] for i in indices]
time_seq_8_4000 = [time_seq_8[i] for i in indices]
time_seq_20_4000 = [time_seq_20[i] for i in indices]
time_par_op1_1_4000 = [time_par_op1_1[i] for i in indices]
time_par_op1_2_4000 = [time_par_op1_2[i] for i in indices]
time_par_op1_4_4000 = [time_par_op1_4[i] for i in indices]
time_par_op1_8_4000 = [time_par_op1_8[i] for i in indices]
time_par_op1_20_4000 = [time_par_op1_20[i] for i in indices]
time_par_op2_1_4000 = [time_par_op2_1[i] for i in indices]
time_par_op2_2_4000 = [time_par_op2_2[i] for i in indices]
time_par_op2_4_4000 = [time_par_op2_4[i] for i in indices]
time_par_op2_8_4000 = [time_par_op2_8[i] for i in indices]
time_par_op2_20_4000 = [time_par_op2_20[i] for i in indices]
time_par_op3_1_4000 = [time_par_op3_1[i] for i in indices]
time_par_op3_2_4000 = [time_par_op3_2[i] for i in indices]
time_par_op3_4_4000 = [time_par_op3_4[i] for i in indices]
time_par_op3_8_4000 = [time_par_op3_8[i] for i in indices]
time_par_op3_20_4000 = [time_par_op3_20[i] for i in indices]
time_per_it_1_4000 = [time_seq_1[i]/it_seq_1[i] for i in indices]
time_per_it_2_4000 = [time_seq_2[i]/it_seq_2[i] for i in indices]
time_per_it_4_4000 = [time_seq_4[i]/it_seq_4[i] for i in indices]
time_per_it_8_4000 = [time_seq_8[i]/it_seq_8[i] for i in indices]
time_per_it_20_4000 = [time_seq_20[i]/it_seq_20[i] for i in indices]
time_per_it_op1_1_4000 = [time_par_op1_1[i]/it_par_op1_1[i] for i in indices]
time_per_it_op1_2_4000 = [time_par_op1_2[i]/it_par_op1_2[i] for i in indices]
time_per_it_op1_4_4000 = [time_par_op1_4[i]/it_par_op1_4[i] for i in indices]
time_per_it_op1_8_4000 = [time_par_op1_8[i]/it_par_op1_8[i] for i in indices]
time_per_it_op1_20_4000 = [time_par_op1_20[i]/it_par_op1_20[i] for i in indices]
time_per_it_op2_1_4000 = [time_par_op2_1[i]/it_par_op2_1[i] for i in indices]
time_per_it_op2_2_4000 = [time_par_op2_2[i]/it_par_op2_2[i] for i in indices]
time_per_it_op2_4_4000 = [time_par_op2_4[i]/it_par_op2_4[i] for i in indices]
time_per_it_op2_8_4000 = [time_par_op2_8[i]/it_par_op2_8[i] for i in indices]
time_per_it_op2_20_4000 = [time_par_op2_20[i]/it_par_op2_20[i] for i in indices]
time_per_it_op3_1_4000 = [time_par_op3_1[i]/it_par_op3_1[i] for i in indices]
time_per_it_op3_2_4000 = [time_par_op3_2[i]/it_par_op3_2[i] for i in indices]
time_per_it_op3_4_4000 = [time_par_op3_4[i]/it_par_op3_4[i] for i in indices]
time_per_it_op3_8_4000 = [time_par_op3_8[i]/it_par_op3_8[i] for i in indices]
time_per_it_op3_20_4000 = [time_par_op3_20[i]/it_par_op3_20[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (5, 8)
it_seq_1_10000 = [it_seq_1[i] for i in indices]
it_seq_2_10000 = [it_seq_2[i] for i in indices]
it_seq_4_10000 = [it_seq_4[i] for i in indices]
it_seq_8_10000 = [it_seq_8[i] for i in indices]
it_seq_20_10000 = [it_seq_20[i] for i in indices]
it_par_op1_1_10000 = [it_par_op1_1[i] for i in indices]
it_par_op1_2_10000 = [it_par_op1_2[i] for i in indices]
it_par_op1_4_10000 = [it_par_op1_4[i] for i in indices]
it_par_op1_8_10000 = [it_par_op1_8[i] for i in indices]
it_par_op1_20_10000 = [it_par_op1_20[i] for i in indices]
it_par_op2_1_10000 = [it_par_op2_1[i] for i in indices]
it_par_op2_2_10000 = [it_par_op2_2[i] for i in indices]
it_par_op2_4_10000 = [it_par_op2_4[i] for i in indices]
it_par_op2_8_10000 = [it_par_op2_8[i] for i in indices]
it_par_op2_20_10000 = [it_par_op2_20[i] for i in indices]
it_par_op3_1_10000 = [it_par_op3_1[i] for i in indices]
it_par_op3_2_10000 = [it_par_op3_2[i] for i in indices]
it_par_op3_4_10000 = [it_par_op3_4[i] for i in indices]
it_par_op3_8_10000 = [it_par_op3_8[i] for i in indices]
it_par_op3_20_10000 = [it_par_op3_20[i] for i in indices]
time_seq_1_10000 = [time_seq_1[i] for i in indices]
time_seq_2_10000 = [time_seq_2[i] for i in indices]
time_seq_4_10000 = [time_seq_4[i] for i in indices]
time_seq_8_10000 = [time_seq_8[i] for i in indices]
time_seq_20_10000 = [time_seq_20[i] for i in indices]
time_par_op1_1_10000 = [time_par_op1_1[i] for i in indices]
time_par_op1_2_10000 = [time_par_op1_2[i] for i in indices]
time_par_op1_4_10000 = [time_par_op1_4[i] for i in indices]
time_par_op1_8_10000 = [time_par_op1_8[i] for i in indices]
time_par_op1_20_10000 = [time_par_op1_20[i] for i in indices]
time_par_op2_1_10000 = [time_par_op2_1[i] for i in indices]
time_par_op2_2_10000 = [time_par_op2_2[i] for i in indices]
time_par_op2_4_10000 = [time_par_op2_4[i] for i in indices]
time_par_op2_8_10000 = [time_par_op2_8[i] for i in indices]
time_par_op2_20_10000 = [time_par_op2_20[i] for i in indices]
time_par_op3_1_10000 = [time_par_op3_1[i] for i in indices]
time_par_op3_2_10000 = [time_par_op3_2[i] for i in indices]
time_par_op3_4_10000 = [time_par_op3_4[i] for i in indices]
time_par_op3_8_10000 = [time_par_op3_8[i] for i in indices]
time_par_op3_20_10000 = [time_par_op3_20[i] for i in indices]
time_per_it_1_10000 = [time_seq_1[i]/it_seq_1[i] for i in indices]
time_per_it_2_10000 = [time_seq_2[i]/it_seq_2[i] for i in indices]
time_per_it_4_10000 = [time_seq_4[i]/it_seq_4[i] for i in indices]
time_per_it_8_10000 = [time_seq_8[i]/it_seq_8[i] for i in indices]
time_per_it_20_10000 = [time_seq_20[i]/it_seq_20[i] for i in indices]
time_per_it_op1_1_10000 = [time_par_op1_1[i]/it_par_op1_1[i] for i in indices]
time_per_it_op1_2_10000 = [time_par_op1_2[i]/it_par_op1_2[i] for i in indices]
time_per_it_op1_4_10000 = [time_par_op1_4[i]/it_par_op1_4[i] for i in indices]
time_per_it_op1_8_10000 = [time_par_op1_8[i]/it_par_op1_8[i] for i in indices]
time_per_it_op1_20_10000 = [time_par_op1_20[i]/it_par_op1_20[i] for i in indices]
time_per_it_op2_1_10000 = [time_par_op2_1[i]/it_par_op2_1[i] for i in indices]
time_per_it_op2_2_10000 = [time_par_op2_2[i]/it_par_op2_2[i] for i in indices]
time_per_it_op2_4_10000 = [time_par_op2_4[i]/it_par_op2_4[i] for i in indices]
time_per_it_op2_8_10000 = [time_par_op2_8[i]/it_par_op2_8[i] for i in indices]
time_per_it_op2_20_10000 = [time_par_op2_20[i]/it_par_op2_20[i] for i in indices]
time_per_it_op3_1_10000 = [time_par_op3_1[i]/it_par_op3_1[i] for i in indices]
time_per_it_op3_2_10000 = [time_par_op3_2[i]/it_par_op3_2[i] for i in indices]
time_per_it_op3_4_10000 = [time_par_op3_4[i]/it_par_op3_4[i] for i in indices]
time_per_it_op3_8_10000 = [time_par_op3_8[i]/it_par_op3_8[i] for i in indices]
time_per_it_op3_20_10000 = [time_par_op3_20[i]/it_par_op3_20[i] for i in indices]
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

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_2_1000, color='orange')
plt.plot(x_1000, time_seq_2_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_2_4000, color='red')
plt.plot(x_4000, time_seq_2_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_2_10000, color='blue')
plt.plot(x_10000, time_seq_2_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_op1_2_1000, color='orange')
plt.plot(x_1000, time_par_op1_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'1 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op1_2_4000, color='red')
plt.plot(x_4000, time_par_op1_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'1 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op1_2_10000, color='blue')
plt.plot(x_10000, time_par_op1_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'1 Process per core - $n = 10000$')
plt.scatter(x_1000, time_par_op2_2_1000, color='orange')
plt.plot(x_1000, time_par_op2_2_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op2_2_4000, color='red')
plt.plot(x_4000, time_par_op2_2_4000, linestyle='-.', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op2_2_10000, color='blue')
plt.plot(x_10000, time_par_op2_2_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.scatter(x_1000, time_par_op3_2_1000, color='orange')
plt.plot(x_1000, time_par_op3_2_1000, linestyle=':', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op3_2_4000, color='red')
plt.plot(x_4000, time_par_op3_2_4000, linestyle=':', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op3_2_10000, color='blue')
plt.plot(x_10000, time_par_op3_2_10000, linestyle=':', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_2"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_2_1000, color='orange')
plt.plot(x_1000, it_seq_2_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_2_4000, color='red')
plt.plot(x_4000, it_seq_2_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_2_10000, color='blue')
plt.plot(x_10000, it_seq_2_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_op1_2_1000, color='orange')
plt.plot(x_1000, it_par_op1_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'1 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op1_2_4000, color='red')
plt.plot(x_4000, it_par_op1_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'1 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op1_2_10000, color='blue')
plt.plot(x_10000, it_par_op1_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'1 Process per core - $n = 10000$')
plt.scatter(x_1000, it_par_op2_2_1000, color='orange')
plt.plot(x_1000, it_par_op2_2_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op2_2_4000, color='red')
plt.plot(x_4000, it_par_op2_2_4000, linestyle='-.', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op2_2_10000, color='blue')
plt.plot(x_10000, it_par_op2_2_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.scatter(x_1000, it_par_op3_2_1000, color='orange')
plt.plot(x_1000, it_par_op3_2_1000, linestyle=':', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op3_2_4000, color='red')
plt.plot(x_4000, it_par_op3_2_4000, linestyle=':', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op3_2_10000, color='blue')
plt.plot(x_10000, it_par_op3_2_10000, linestyle=':', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_mpi_alpha_options_it_2"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_4_1000, color='orange')
plt.plot(x_1000, time_seq_4_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4_4000, color='red')
plt.plot(x_4000, time_seq_4_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_4_10000, color='blue')
plt.plot(x_10000, time_seq_4_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_op1_4_1000, color='orange')
plt.plot(x_1000, time_par_op1_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'1 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op1_4_4000, color='red')
plt.plot(x_4000, time_par_op1_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'1 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op1_4_10000, color='blue')
plt.plot(x_10000, time_par_op1_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'1 Process per core - $n = 10000$')
plt.scatter(x_1000, time_par_op2_4_1000, color='orange')
plt.plot(x_1000, time_par_op2_4_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op2_4_4000, color='red')
plt.plot(x_4000, time_par_op2_4_4000, linestyle='-.', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op2_4_10000, color='blue')
plt.plot(x_10000, time_par_op2_4_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.scatter(x_1000, time_par_op3_4_1000, color='orange')
plt.plot(x_1000, time_par_op3_4_1000, linestyle=':', linewidth=1.5, color='orange', label=r'4 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op3_4_4000, color='red')
plt.plot(x_4000, time_par_op3_4_4000, linestyle=':', linewidth=1.5, color='red', label=r'4 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op3_4_10000, color='blue')
plt.plot(x_10000, time_par_op3_4_10000, linestyle=':', linewidth=1.5, color='blue', label=r'4 Process per core - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_4"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_4_1000, color='orange')
plt.plot(x_1000, it_seq_4_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4_4000, color='red')
plt.plot(x_4000, it_seq_4_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_4_10000, color='blue')
plt.plot(x_10000, it_seq_4_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_op1_4_1000, color='orange')
plt.plot(x_1000, it_par_op1_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'1 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op1_4_4000, color='red')
plt.plot(x_4000, it_par_op1_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'1 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op1_4_10000, color='blue')
plt.plot(x_10000, it_par_op1_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'1 Process per core - $n = 10000$')
plt.scatter(x_1000, it_par_op2_4_1000, color='orange')
plt.plot(x_1000, it_par_op2_4_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op2_4_4000, color='red')
plt.plot(x_4000, it_par_op2_4_4000, linestyle='-.', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op2_4_10000, color='blue')
plt.plot(x_10000, it_par_op2_4_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.scatter(x_1000, it_par_op3_4_1000, color='orange')
plt.plot(x_1000, it_par_op3_4_1000, linestyle=':', linewidth=1.5, color='orange', label=r'4 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op3_4_4000, color='red')
plt.plot(x_4000, it_par_op3_4_4000, linestyle=':', linewidth=1.5, color='red', label=r'4 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op3_4_10000, color='blue')
plt.plot(x_10000, it_par_op3_4_10000, linestyle=':', linewidth=1.5, color='blue', label=r'4 Process per core - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_mpi_alpha_options_it_4"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_8_1000, color='orange')
plt.plot(x_1000, time_seq_8_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_8_4000, color='red')
plt.plot(x_4000, time_seq_8_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_8_10000, color='blue')
plt.plot(x_10000, time_seq_8_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_op1_8_1000, color='orange')
plt.plot(x_1000, time_par_op1_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'1 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op1_8_4000, color='red')
plt.plot(x_4000, time_par_op1_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'1 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op1_8_10000, color='blue')
plt.plot(x_10000, time_par_op1_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'1 Process per core - $n = 10000$')
plt.scatter(x_1000, time_par_op2_8_1000, color='orange')
plt.plot(x_1000, time_par_op2_8_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op2_8_4000, color='red')
plt.plot(x_4000, time_par_op2_8_4000, linestyle='-.', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op2_8_10000, color='blue')
plt.plot(x_10000, time_par_op2_8_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.scatter(x_1000, time_par_op3_8_1000, color='orange')
plt.plot(x_1000, time_par_op3_8_1000, linestyle=':', linewidth=1.5, color='orange', label=r'8 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op3_8_4000, color='red')
plt.plot(x_4000, time_par_op3_8_4000, linestyle=':', linewidth=1.5, color='red', label=r'8 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op3_8_10000, color='blue')
plt.plot(x_10000, time_par_op3_8_10000, linestyle=':', linewidth=1.5, color='blue', label=r'8 Process per core - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_8"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_8_1000, color='orange')
plt.plot(x_1000, it_seq_8_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_8_4000, color='red')
plt.plot(x_4000, it_seq_8_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_8_10000, color='blue')
plt.plot(x_10000, it_seq_8_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_op1_8_1000, color='orange')
plt.plot(x_1000, it_par_op1_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'1 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op1_8_4000, color='red')
plt.plot(x_4000, it_par_op1_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'1 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op1_8_10000, color='blue')
plt.plot(x_10000, it_par_op1_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'1 Process per core - $n = 10000$')
plt.scatter(x_1000, it_par_op2_8_1000, color='orange')
plt.plot(x_1000, it_par_op2_8_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op2_8_4000, color='red')
plt.plot(x_4000, it_par_op2_8_4000, linestyle='-.', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op2_8_10000, color='blue')
plt.plot(x_10000, it_par_op2_8_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.scatter(x_1000, it_par_op3_8_1000, color='orange')
plt.plot(x_1000, it_par_op3_8_1000, linestyle=':', linewidth=1.5, color='orange', label=r'8 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op3_8_4000, color='red')
plt.plot(x_4000, it_par_op3_8_4000, linestyle=':', linewidth=1.5, color='red', label=r'8 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op3_8_10000, color='blue')
plt.plot(x_10000, it_par_op3_8_10000, linestyle=':', linewidth=1.5, color='blue', label=r'8 Process per core - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_mpi_alpha_options_it_8"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_20_1000, color='orange')
plt.plot(x_1000, time_seq_20_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_20_4000, color='red')
plt.plot(x_4000, time_seq_20_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_20_10000, color='blue')
plt.plot(x_10000, time_seq_20_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_op1_20_1000, color='orange')
plt.plot(x_1000, time_par_op1_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'1 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op1_20_4000, color='red')
plt.plot(x_4000, time_par_op1_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'1 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op1_20_10000, color='blue')
plt.plot(x_10000, time_par_op1_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'1 Process per core - $n = 10000$')
plt.scatter(x_1000, time_par_op2_20_1000, color='orange')
plt.plot(x_1000, time_par_op2_20_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op2_20_4000, color='red')
plt.plot(x_4000, time_par_op2_20_4000, linestyle='-.', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op2_20_10000, color='blue')
plt.plot(x_10000, time_par_op2_20_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.scatter(x_1000, time_par_op3_20_1000, color='orange')
plt.plot(x_1000, time_par_op3_20_1000, linestyle=':', linewidth=1.5, color='orange', label=r'20 Process per core - $n = 1000$')
plt.scatter(x_4000, time_par_op3_20_4000, color='red')
plt.plot(x_4000, time_par_op3_20_4000, linestyle=':', linewidth=1.5, color='red', label=r'20 Process per core - $n = 4000$')
plt.scatter(x_10000, time_par_op3_20_10000, color='blue')
plt.plot(x_10000, time_par_op3_20_10000, linestyle=':', linewidth=1.5, color='blue', label=r'20 Process per core - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_20"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_20_1000, color='orange')
plt.plot(x_1000, it_seq_20_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_20_4000, color='red')
plt.plot(x_4000, it_seq_20_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_20_10000, color='blue')
plt.plot(x_10000, it_seq_20_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_op1_20_1000, color='orange')
plt.plot(x_1000, it_par_op1_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'1 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op1_20_4000, color='red')
plt.plot(x_4000, it_par_op1_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'1 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op1_20_10000, color='blue')
plt.plot(x_10000, it_par_op1_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'1 Process per core - $n = 10000$')
plt.scatter(x_1000, it_par_op2_20_1000, color='orange')
plt.plot(x_1000, it_par_op2_20_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'2 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op2_20_4000, color='red')
plt.plot(x_4000, it_par_op2_20_4000, linestyle='-.', linewidth=1.5, color='red', label=r'2 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op2_20_10000, color='blue')
plt.plot(x_10000, it_par_op2_20_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'2 Process per core - $n = 10000$')
plt.scatter(x_1000, it_par_op3_20_1000, color='orange')
plt.plot(x_1000, it_par_op3_20_1000, linestyle=':', linewidth=1.5, color='orange', label=r'20 Process per core - $n = 1000$')
plt.scatter(x_4000, it_par_op3_20_4000, color='red')
plt.plot(x_4000, it_par_op3_20_4000, linestyle=':', linewidth=1.5, color='red', label=r'20 Process per core - $n = 4000$')
plt.scatter(x_10000, it_par_op3_20_10000, color='blue')
plt.plot(x_10000, it_par_op3_20_10000, linestyle=':', linewidth=1.5, color='blue', label=r'20 Process per core - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_mpi_alpha_options_it_20"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_4_1000, color='gray')
plt.plot(x_1000, time_seq_4_1000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_1000, time_par_op1_4_1000, color='orange')
plt.plot(x_1000, time_par_op1_4_1000, linewidth=1.5, color='orange', label=r'1 Processs per node (4 nodes)')
plt.scatter(x_1000, time_par_op2_4_1000, color='red')
plt.plot(x_1000, time_par_op2_4_1000, linewidth=1.5, color='red', label=r'2 Processses per node (2 nodes)')
plt.scatter(x_1000, time_par_op3_4_1000, color='blue')
plt.plot(x_1000, time_par_op3_4_1000, linewidth=1.5, color='blue', label=r'4 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_4_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_8_1000, color='gray')
plt.plot(x_1000, time_seq_8_1000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_1000, time_par_op1_8_1000, color='orange')
plt.plot(x_1000, time_par_op1_8_1000, linewidth=1.5, color='orange', label=r'1 Processs per node (8 nodes)')
plt.scatter(x_1000, time_par_op2_8_1000, color='red')
plt.plot(x_1000, time_par_op2_8_1000, linewidth=1.5, color='red', label=r'2 Processses per node (4 nodes)')
plt.scatter(x_1000, time_par_op3_8_1000, color='blue')
plt.plot(x_1000, time_par_op3_8_1000, linewidth=1.5, color='blue', label=r'8 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_8_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_20_1000, color='gray')
plt.plot(x_1000, time_seq_20_1000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_1000, time_par_op1_20_1000, color='orange')
plt.plot(x_1000, time_par_op1_20_1000, linewidth=1.5, color='orange', label=r'1 Processs per node (20 nodes)')
plt.scatter(x_1000, time_par_op2_20_1000, color='red')
plt.plot(x_1000, time_par_op2_20_1000, linewidth=1.5, color='red', label=r'2 Processses per node (10 nodes)')
plt.scatter(x_1000, time_par_op3_20_1000, color='blue')
plt.plot(x_1000, time_par_op3_20_1000, linewidth=1.5, color='blue', label=r'20 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_20_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, time_seq_4_4000, color='gray')
plt.plot(x_4000, time_seq_4_4000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_4000, time_par_op1_4_4000, color='orange')
plt.plot(x_4000, time_par_op1_4_4000, linewidth=1.5, color='orange', label=r'1 Processs per node (4 nodes)')
plt.scatter(x_4000, time_par_op2_4_4000, color='red')
plt.plot(x_4000, time_par_op2_4_4000, linewidth=1.5, color='red', label=r'2 Processses per node (2 nodes)')
plt.scatter(x_4000, time_par_op3_4_4000, color='blue')
plt.plot(x_4000, time_par_op3_4_4000, linewidth=1.5, color='blue', label=r'4 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_4_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, time_seq_8_4000, color='gray')
plt.plot(x_4000, time_seq_8_4000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_4000, time_par_op1_8_4000, color='orange')
plt.plot(x_4000, time_par_op1_8_4000, linewidth=1.5, color='orange', label=r'1 Processs per node (8 nodes)')
plt.scatter(x_4000, time_par_op2_8_4000, color='red')
plt.plot(x_4000, time_par_op2_8_4000, linewidth=1.5, color='red', label=r'2 Processses per node (4 nodes)')
plt.scatter(x_4000, time_par_op3_8_4000, color='blue')
plt.plot(x_4000, time_par_op3_8_4000, linewidth=1.5, color='blue', label=r'8 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_8_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, time_seq_20_4000, color='gray')
plt.plot(x_4000, time_seq_20_4000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_4000, time_par_op1_20_4000, color='orange')
plt.plot(x_4000, time_par_op1_20_4000, linewidth=1.5, color='orange', label=r'1 Processs per node (20 nodes)')
plt.scatter(x_4000, time_par_op2_20_4000, color='red')
plt.plot(x_4000, time_par_op2_20_4000, linewidth=1.5, color='red', label=r'2 Processses per node (10 nodes)')
plt.scatter(x_4000, time_par_op3_20_4000, color='blue')
plt.plot(x_4000, time_par_op3_20_4000, linewidth=1.5, color='blue', label=r'20 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_20_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_seq_4_10000, color='gray')
plt.plot(x_10000, time_seq_4_10000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_10000, time_par_op1_4_10000, color='orange')
plt.plot(x_10000, time_par_op1_4_10000, linewidth=1.5, color='orange', label=r'1 Processs per node (4 nodes)')
plt.scatter(x_10000, time_par_op2_4_10000, color='red')
plt.plot(x_10000, time_par_op2_4_10000, linewidth=1.5, color='red', label=r'2 Processses per node (2 nodes)')
plt.scatter(x_10000, time_par_op3_4_10000, color='blue')
plt.plot(x_10000, time_par_op3_4_10000, linewidth=1.5, color='blue', label=r'4 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_4_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_seq_8_10000, color='gray')
plt.plot(x_10000, time_seq_8_10000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_10000, time_par_op1_8_10000, color='orange')
plt.plot(x_10000, time_par_op1_8_10000, linewidth=1.5, color='orange', label=r'1 Processs per node (8 nodes)')
plt.scatter(x_10000, time_par_op2_8_10000, color='red')
plt.plot(x_10000, time_par_op2_8_10000, linewidth=1.5, color='red', label=r'2 Processses per node (4 nodes)')
plt.scatter(x_10000, time_par_op3_8_10000, color='blue')
plt.plot(x_10000, time_par_op3_8_10000, linewidth=1.5, color='blue', label=r'8 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_8_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_seq_20_10000, color='gray')
plt.plot(x_10000, time_seq_20_10000, linewidth=1.5, color='gray', label=r'Sequential')
plt.scatter(x_10000, time_par_op1_20_10000, color='orange')
plt.plot(x_10000, time_par_op1_20_10000, linewidth=1.5, color='orange', label=r'1 Processs per node (20 nodes)')
plt.scatter(x_10000, time_par_op2_20_10000, color='red')
plt.plot(x_10000, time_par_op2_20_10000, linewidth=1.5, color='red', label=r'2 Processses per node (10 nodes)')
plt.scatter(x_10000, time_par_op3_20_10000, color='blue')
plt.plot(x_10000, time_par_op3_20_10000, linewidth=1.5, color='blue', label=r'20 Processses per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_mpi_alpha_options_time_20_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')