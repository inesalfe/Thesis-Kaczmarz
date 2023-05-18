import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RK_parallel_N.py

filename = "outputs/omp/RK_seq.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
for i in range(37):
	time_seq.append(float(lines[i].split()[2]))

filename = "outputs/omp/RK_parallel.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_par = []
for i in range(148):
	time_par.append(float(lines[i].split()[2]))

time_par_1 = time_par[0::4]
time_par_2 = time_par[1::4]
time_par_4 = time_par[2::4]
time_par_8 = time_par[3::4]

indices = (0, 5, 11, 19, 28)
time_seq_50 = [time_seq[i] for i in indices]
time_par_1_50 = [time_par_1[i] for i in indices]
time_par_2_50 = [time_par_2[i] for i in indices]
time_par_4_50 = [time_par_4[i] for i in indices]
time_par_8_50 = [time_par_8[i] for i in indices]
speedup_2_50 = [time_par_1_50[i]/time_par_2_50[i] for i in range(len(indices))]
speedup_4_50 = [time_par_1_50[i]/time_par_4_50[i] for i in range(len(indices))]
speedup_8_50 = [time_par_1_50[i]/time_par_8_50[i] for i in range(len(indices))]
x_50 = [2000, 4000, 20000, 40000, 80000]

indices = (1, 6, 12, 20, 29)
time_seq_100 = [time_seq[i] for i in indices]
time_par_1_100 = [time_par_1[i] for i in indices]
time_par_2_100 = [time_par_2[i] for i in indices]
time_par_4_100 = [time_par_4[i] for i in indices]
time_par_8_100 = [time_par_8[i] for i in indices]
speedup_2_100 = [time_par_1_100[i]/time_par_2_100[i] for i in range(len(indices))]
speedup_4_100 = [time_par_1_100[i]/time_par_4_100[i] for i in range(len(indices))]
speedup_8_100 = [time_par_1_100[i]/time_par_8_100[i] for i in range(len(indices))]
x_100 = [2000, 4000, 20000, 40000, 80000]

indices = (2, 7, 13, 21, 30)
time_seq_200 = [time_seq[i] for i in indices]
time_par_1_200 = [time_par_1[i] for i in indices]
time_par_2_200 = [time_par_2[i] for i in indices]
time_par_4_200 = [time_par_4[i] for i in indices]
time_par_8_200 = [time_par_8[i] for i in indices]
speedup_2_200 = [time_par_1_200[i]/time_par_2_200[i] for i in range(len(indices))]
speedup_4_200 = [time_par_1_200[i]/time_par_4_200[i] for i in range(len(indices))]
speedup_8_200 = [time_par_1_200[i]/time_par_8_200[i] for i in range(len(indices))]
x_200 = [2000, 4000, 20000, 40000, 80000]

indices = (3, 8, 14, 22, 31)
time_seq_500 = [time_seq[i] for i in indices]
time_par_1_500 = [time_par_1[i] for i in indices]
time_par_2_500 = [time_par_2[i] for i in indices]
time_par_4_500 = [time_par_4[i] for i in indices]
time_par_8_500 = [time_par_8[i] for i in indices]
speedup_2_500 = [time_par_1_500[i]/time_par_2_500[i] for i in range(len(indices))]
speedup_4_500 = [time_par_1_500[i]/time_par_4_500[i] for i in range(len(indices))]
speedup_8_500 = [time_par_1_500[i]/time_par_8_500[i] for i in range(len(indices))]
x_500 = [2000, 4000, 20000, 40000, 80000]

indices = (4, 9, 15, 23, 32)
time_seq_750 = [time_seq[i] for i in indices]
time_par_1_750 = [time_par_1[i] for i in indices]
time_par_2_750 = [time_par_2[i] for i in indices]
time_par_4_750 = [time_par_4[i] for i in indices]
time_par_8_750 = [time_par_8[i] for i in indices]
speedup_2_750 = [time_par_1_750[i]/time_par_2_750[i] for i in range(len(indices))]
speedup_4_750 = [time_par_1_750[i]/time_par_4_750[i] for i in range(len(indices))]
speedup_8_750 = [time_par_1_750[i]/time_par_8_750[i] for i in range(len(indices))]
x_750 = [2000, 4000, 20000, 40000, 80000]

indices = (10, 16, 24, 33)
time_seq_1000 = [time_seq[i] for i in indices]
time_par_1_1000 = [time_par_1[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
speedup_2_1000 = [time_par_1_1000[i]/time_par_2_1000[i] for i in range(len(indices))]
speedup_4_1000 = [time_par_1_1000[i]/time_par_4_1000[i] for i in range(len(indices))]
speedup_8_1000 = [time_par_1_1000[i]/time_par_8_1000[i] for i in range(len(indices))]
x_1000 = [4000, 20000, 40000, 80000]

indices = (17, 28, 34)
time_seq_2000 = [time_seq[i] for i in indices]
time_par_1_2000 = [time_par_1[i] for i in indices]
time_par_2_2000 = [time_par_2[i] for i in indices]
time_par_4_2000 = [time_par_4[i] for i in indices]
time_par_8_2000 = [time_par_8[i] for i in indices]
speedup_2_2000 = [time_par_1_2000[i]/time_par_2_2000[i] for i in range(len(indices))]
speedup_4_2000 = [time_par_1_2000[i]/time_par_4_2000[i] for i in range(len(indices))]
speedup_8_2000 = [time_par_1_2000[i]/time_par_8_2000[i] for i in range(len(indices))]
x_2000 = [20000, 40000, 80000]

indices = (18, 26, 35)
time_seq_4000 = [time_seq[i] for i in indices]
time_par_1_4000 = [time_par_1[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
speedup_2_4000 = [time_par_1_4000[i]/time_par_2_4000[i] for i in range(len(indices))]
speedup_4_4000 = [time_par_1_4000[i]/time_par_4_4000[i] for i in range(len(indices))]
speedup_8_4000 = [time_par_1_4000[i]/time_par_8_4000[i] for i in range(len(indices))]
x_4000 = [20000, 40000, 80000]

indices = (27, 36)
time_seq_10000 = [time_seq[i] for i in indices]
time_par_1_10000 = [time_par_1[i] for i in indices]
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
speedup_2_10000 = [time_par_1_10000[i]/time_par_2_10000[i] for i in range(len(indices))]
speedup_4_10000 = [time_par_1_10000[i]/time_par_4_10000[i] for i in range(len(indices))]
speedup_8_10000 = [time_par_1_10000[i]/time_par_8_10000[i] for i in range(len(indices))]
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

plot_title = r"Speedup using 2 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_2_1000, linewidth=1.5, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_2_4000, linewidth=1.5, color='red')
plt.plot(x_4000, speedup_2_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_2_10000, linewidth=1.5, color='blue')
plt.plot(x_10000, speedup_2_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_N_speedup_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 4 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_4_1000, linewidth=1.5, color='orange')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_4_4000, linewidth=1.5, color='red')
plt.plot(x_4000, speedup_4_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_4_10000, linewidth=1.5, color='blue')
plt.plot(x_10000, speedup_4_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_N_speedup_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 8 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_8_1000, linewidth=1.5, color='orange')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_8_4000, linewidth=1.5, color='red')
plt.plot(x_4000, speedup_8_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_8_10000, linewidth=1.5, color='blue')
plt.plot(x_10000, speedup_8_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_N_speedup_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000, color='red')
plt.plot(x_1000, time_par_1_1000, linewidth=1.5, color='red', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000, color='orange')
plt.plot(x_4000, time_par_1_4000, linewidth=1.5, color='orange', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000, color='blue')
plt.plot(x_10000, time_par_1_10000, linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000, color='red')
plt.plot(x_1000, time_par_2_1000, linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000, color='orange')
plt.plot(x_4000, time_par_2_4000, linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000, color='blue')
plt.plot(x_10000, time_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_N_time_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000, color='red')
plt.plot(x_1000, time_par_1_1000, linewidth=1.5, color='red', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000, color='orange')
plt.plot(x_4000, time_par_1_4000, linewidth=1.5, color='orange', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000, color='blue')
plt.plot(x_10000, time_par_1_10000, linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000, color='red')
plt.plot(x_1000, time_par_4_1000, linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000, color='orange')
plt.plot(x_4000, time_par_4_4000, linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000, color='blue')
plt.plot(x_10000, time_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_N_time_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000, color='red')
plt.plot(x_1000, time_par_1_1000, linewidth=1.5, color='red', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000, color='orange')
plt.plot(x_4000, time_par_1_4000, linewidth=1.5, color='orange', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000, color='blue')
plt.plot(x_10000, time_par_1_10000, linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000, color='red')
plt.plot(x_1000, time_par_8_1000, linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000, color='orange')
plt.plot(x_4000, time_par_8_4000, linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000, color='blue')
plt.plot(x_10000, time_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_N_time_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_2_1000, linewidth=1.5, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_1000, speedup_4_1000, linewidth=1.5, color='red')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_1000, speedup_8_1000, linewidth=1.5, color='blue')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_N_speedup_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, speedup_2_4000, linewidth=1.5, color='orange')
plt.plot(x_4000, speedup_2_4000, linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_4000, speedup_4_4000, linewidth=1.5, color='red')
plt.plot(x_4000, speedup_4_4000, linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_4000, speedup_8_4000, linewidth=1.5, color='blue')
plt.plot(x_4000, speedup_8_4000, linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_N_speedup_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, speedup_2_10000, linewidth=1.5, color='orange')
plt.plot(x_10000, speedup_2_10000, linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_10000, speedup_4_10000, linewidth=1.5, color='red')
plt.plot(x_10000, speedup_4_10000, linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_10000, speedup_8_10000, linewidth=1.5, color='blue')
plt.plot(x_10000, speedup_8_10000, linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_N_speedup_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_2_1000, linewidth=1.5, color='orange')
plt.plot(x_1000, time_par_2_1000, linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_1000, time_par_4_1000, linewidth=1.5, color='red')
plt.plot(x_1000, time_par_4_1000, linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_1000, time_par_8_1000, linewidth=1.5, color='blue')
plt.plot(x_1000, time_par_8_1000, linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_N_time_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, time_par_2_4000, linewidth=1.5, color='orange')
plt.plot(x_4000, time_par_2_4000, linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_4000, time_par_4_4000, linewidth=1.5, color='red')
plt.plot(x_4000, time_par_4_4000, linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_4000, time_par_8_4000, linewidth=1.5, color='blue')
plt.plot(x_4000, time_par_8_4000, linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_N_time_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_par_2_10000, linewidth=1.5, color='orange')
plt.plot(x_10000, time_par_2_10000, linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_10000, time_par_4_10000, linewidth=1.5, color='red')
plt.plot(x_10000, time_par_4_10000, linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_10000, time_par_8_10000, linewidth=1.5, color='blue')
plt.plot(x_10000, time_par_8_10000, linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_N_time_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()