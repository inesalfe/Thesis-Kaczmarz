import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKA_N.py

filename = "outputs/omp/RKA.txt";

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

indices = (10, 16, 24, 33)
time_seq_1_1000 = [time_seq_1[i] for i in indices]
time_seq_2_1000 = [time_seq_2[i] for i in indices]
time_seq_4_1000 = [time_seq_4[i] for i in indices]
time_seq_8_1000 = [time_seq_8[i] for i in indices]
time_par_1_1000 = [time_par_1[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
speedup_2_1000 = [time_seq_2[i]/time_par_2[i] for i in indices]
speedup_4_1000 = [time_seq_4[i]/time_par_4[i] for i in indices]
speedup_8_1000 = [time_seq_8[i]/time_par_8[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (18, 26, 35)
time_seq_1_4000 = [time_seq_1[i] for i in indices]
time_seq_2_4000 = [time_seq_2[i] for i in indices]
time_seq_4_4000 = [time_seq_4[i] for i in indices]
time_seq_8_4000 = [time_seq_8[i] for i in indices]
time_par_1_4000 = [time_par_1[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
speedup_2_4000 = [time_seq_2[i]/time_par_2[i] for i in indices]
speedup_4_4000 = [time_seq_4[i]/time_par_4[i] for i in indices]
speedup_8_4000 = [time_seq_8[i]/time_par_8[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (27, 36)
time_seq_1_10000 = [time_seq_1[i] for i in indices]
time_seq_2_10000 = [time_seq_2[i] for i in indices]
time_seq_4_10000 = [time_seq_4[i] for i in indices]
time_seq_8_10000 = [time_seq_8[i] for i in indices]
time_par_1_10000 = [time_par_1[i] for i in indices]
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
speedup_2_10000 = [time_seq_2[i]/time_par_2[i] for i in indices]
speedup_4_10000 = [time_seq_4[i]/time_par_4[i] for i in indices]
speedup_8_10000 = [time_seq_8[i]/time_par_8[i] for i in indices]
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

plot_title = r"Average of 2 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_2_1000, color='orange')
plt.plot(x_1000, time_seq_2_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_2_4000, color='red')
plt.plot(x_4000, time_seq_2_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_2_10000, color='blue')
plt.plot(x_10000, time_seq_2_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000, color='red')
plt.plot(x_4000, time_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000, color='blue')
plt.plot(x_10000, time_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_N_time_2"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Average of 4 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_4_1000, color='orange')
plt.plot(x_1000, time_seq_4_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4_4000, color='red')
plt.plot(x_4000, time_seq_4_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_4_10000, color='blue')
plt.plot(x_10000, time_seq_4_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000, color='orange')
plt.plot(x_1000, time_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000, color='red')
plt.plot(x_4000, time_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000, color='blue')
plt.plot(x_10000, time_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_N_time_4"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Average of 8 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_8_1000, color='orange')
plt.plot(x_1000, time_seq_8_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_8_4000, color='red')
plt.plot(x_4000, time_seq_8_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_8_10000, color='blue')
plt.plot(x_10000, time_seq_8_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000, color='orange')
plt.plot(x_1000, time_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000, color='red')
plt.plot(x_4000, time_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000, color='blue')
plt.plot(x_10000, time_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_N_time_8"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Average of 2 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_2_1000, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_2_4000, color='red')
plt.plot(x_4000, speedup_2_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_2_10000, color='blue')
plt.plot(x_10000, speedup_2_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_N_speedup_2"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Average of 4 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_4_1000, color='orange')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_4_4000, color='red')
plt.plot(x_4000, speedup_4_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_4_10000, color='blue')
plt.plot(x_10000, speedup_4_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_N_speedup_4"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Average of 8 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_8_1000, color='orange')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_8_4000, color='red')
plt.plot(x_4000, speedup_8_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_8_10000, color='blue')
plt.plot(x_10000, speedup_8_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_N_speedup_8"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"$n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_2_1000, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x_1000, speedup_4_1000, color='red')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x_1000, speedup_8_1000, color='blue')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_N_speedup_1000"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"$n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, speedup_2_4000, color='orange')
plt.plot(x_4000, speedup_2_4000, linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x_4000, speedup_4_4000, color='red')
plt.plot(x_4000, speedup_4_4000, linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x_4000, speedup_8_4000, color='blue')
plt.plot(x_4000, speedup_8_4000, linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_N_speedup_4000"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"$n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, speedup_2_10000, color='orange')
plt.plot(x_10000, speedup_2_10000, linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x_10000, speedup_4_10000, color='red')
plt.plot(x_10000, speedup_4_10000, linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x_10000, speedup_8_10000, color='blue')
plt.plot(x_10000, speedup_8_10000, linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_N_speedup_10000"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"$n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linewidth=1.5, linestyle='--', color='orange', label=r'Parallel - Threads = 2')
plt.scatter(x_1000, time_par_4_1000, color='red')
plt.plot(x_1000, time_par_4_1000, linewidth=1.5, linestyle='--', color='red', label=r'Parallel - Threads = 4')
plt.scatter(x_1000, time_par_8_1000, color='blue')
plt.plot(x_1000, time_par_8_1000, linewidth=1.5, linestyle='--', color='blue', label=r'Parallel - Threads = 8')
plt.scatter(x_1000, time_seq_2_1000, color='orange')
plt.plot(x_1000, time_seq_2_1000, linewidth=1.5, color='orange', label=r'Sequential - Threads = 2')
plt.scatter(x_1000, time_seq_4_1000, color='red')
plt.plot(x_1000, time_seq_4_1000, linewidth=1.5, color='red', label=r'Sequential - Threads = 4')
plt.scatter(x_1000, time_seq_8_1000, color='blue')
plt.plot(x_1000, time_seq_8_1000, linewidth=1.5, color='blue', label=r'Sequential - Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_N_time_1000"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"$n = 4000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, time_par_2_4000, color='orange')
plt.plot(x_4000, time_par_2_4000, linewidth=1.5, linestyle='--', color='orange', label=r'Parallel - Threads = 2')
plt.scatter(x_4000, time_par_4_4000, color='red')
plt.plot(x_4000, time_par_4_4000, linewidth=1.5, linestyle='--', color='red', label=r'Parallel - Threads = 4')
plt.scatter(x_4000, time_par_8_4000, color='blue')
plt.plot(x_4000, time_par_8_4000, linewidth=1.5, linestyle='--', color='blue', label=r'Parallel - Threads = 8')
plt.scatter(x_4000, time_seq_2_4000, color='orange')
plt.plot(x_4000, time_seq_2_4000, linewidth=1.5, color='orange', label=r'Sequential - Threads = 2')
plt.scatter(x_4000, time_seq_4_4000, color='red')
plt.plot(x_4000, time_seq_4_4000, linewidth=1.5, color='red', label=r'Sequential - Threads = 4')
plt.scatter(x_4000, time_seq_8_4000, color='blue')
plt.plot(x_4000, time_seq_8_4000, linewidth=1.5, color='blue', label=r'Sequential - Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_N_time_4000"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"$n = 10000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_par_2_10000, color='orange')
plt.plot(x_10000, time_par_2_10000, linewidth=1.5, linestyle='--', color='orange', label=r'Parallel - Threads = 2')
plt.scatter(x_10000, time_par_4_10000, color='red')
plt.plot(x_10000, time_par_4_10000, linewidth=1.5, linestyle='--', color='red', label=r'Parallel - Threads = 4')
plt.scatter(x_10000, time_par_8_10000, color='blue')
plt.plot(x_10000, time_par_8_10000, linewidth=1.5, linestyle='--', color='blue', label=r'Parallel - Threads = 8')
plt.scatter(x_10000, time_seq_2_10000, color='orange')
plt.plot(x_10000, time_seq_2_10000, linewidth=1.5, color='orange', label=r'Sequential - Threads = 2')
plt.scatter(x_10000, time_seq_4_10000, color='red')
plt.plot(x_10000, time_seq_4_10000, linewidth=1.5, color='red', label=r'Sequential - Threads = 4')
plt.scatter(x_10000, time_seq_8_10000, color='blue')
plt.plot(x_10000, time_seq_8_10000, linewidth=1.5, color='blue', label=r'Sequential - Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_N_time_10000"

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')