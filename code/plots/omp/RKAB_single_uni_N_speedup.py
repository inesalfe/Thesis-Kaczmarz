import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_single_uni_N_speedup.py

filename = "outputs/omp/RKAB_single_uni_speedup.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))

time_seq_1 = time[0::8]
time_seq_2 = time[2::8]
time_seq_4 = time[4::8]
time_seq_8 = time[6::8]

time_par_1 = time[1::8]
time_par_2 = time[3::8]
time_par_4 = time[5::8]
time_par_8 = time[7::8]

speedup_2 = [time_seq_2[i]/time_par_2[i] for i in range(len(time_seq_2))]
speedup_4 = [time_seq_4[i]/time_par_4[i] for i in range(len(time_seq_4))]
speedup_8 = [time_seq_8[i]/time_par_8[i] for i in range(len(time_seq_8))]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x_1000 = [4000, 20000, 40000, 80000]
x_4000 = [20000, 40000, 80000]
x_10000 = [40000, 80000]

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_2[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_2[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x_1000, [speedup_4[x] for x in [0,1,3,6]], color='red')
plt.plot(x_1000, [speedup_4[x] for x in [0,1,3,6]], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x_1000, [speedup_8[x] for x in [0,1,3,6]], color='blue')
plt.plot(x_1000, [speedup_8[x] for x in [0,1,3,6]], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend(loc = 'upper right')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_uni_N_speedup_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, [speedup_2[x] for x in [2,4,7]], color='orange')
plt.plot(x_4000, [speedup_2[x] for x in [2,4,7]], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x_4000, [speedup_4[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_4[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x_4000, [speedup_8[x] for x in [2,4,7]], color='blue')
plt.plot(x_4000, [speedup_8[x] for x in [2,4,7]], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend(loc = 'lower right')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_uni_N_speedup_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, [speedup_2[x] for x in [5,8]], color='orange')
plt.plot(x_10000, [speedup_2[x] for x in [5,8]], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x_10000, [speedup_4[x] for x in [5,8]], color='red')
plt.plot(x_10000, [speedup_4[x] for x in [5,8]], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x_10000, [speedup_8[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_8[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend(loc = 'lower right')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_uni_N_speedup_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()