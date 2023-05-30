import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RK_parallel_uni_copy_M.py

filename = "outputs/omp/RK_seq_uni_copy.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
for i in range(37):
	time_seq.append(float(lines[i].split()[2]))

filename = "outputs/omp/RK_parallel_uni_copy.txt";

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

time_seq_2000 = time_seq[0:5]
time_par_1_2000 = time_par_1[0:5]
time_par_2_2000 = time_par_2[0:5]
time_par_4_2000 = time_par_4[0:5]
time_par_8_2000 = time_par_8[0:5]
speedup_2_2000 = [time_par_1_2000[i]/time_par_2_2000[i] for i in range(5)]
speedup_4_2000 = [time_par_1_2000[i]/time_par_4_2000[i] for i in range(5)]
speedup_8_2000 = [time_par_1_2000[i]/time_par_8_2000[i] for i in range(5)]
x_2000 = [50, 100, 200, 500, 750]

time_seq_4000 = time_seq[5:11]
time_par_1_4000 = time_par_1[5:11]
time_par_2_4000 = time_par_2[5:11]
time_par_4_4000 = time_par_4[5:11]
time_par_8_4000 = time_par_8[5:11]
speedup_2_4000 = [time_par_1_4000[i]/time_par_2_4000[i] for i in range(6)]
speedup_4_4000 = [time_par_1_4000[i]/time_par_4_4000[i] for i in range(6)]
speedup_8_4000 = [time_par_1_4000[i]/time_par_8_4000[i] for i in range(6)]
x_4000 = [50, 100, 200, 500, 750, 1000]

time_seq_20000 = time_seq[11:19]
time_par_1_20000 = time_par_1[11:19]
time_par_2_20000 = time_par_2[11:19]
time_par_4_20000 = time_par_4[11:19]
time_par_8_20000 = time_par_8[11:19]
speedup_2_20000 = [time_par_1_20000[i]/time_par_2_20000[i] for i in range(8)]
speedup_4_20000 = [time_par_1_20000[i]/time_par_4_20000[i] for i in range(8)]
speedup_8_20000 = [time_par_1_20000[i]/time_par_8_20000[i] for i in range(8)]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000]

time_seq_40000 = time_seq[19:28]
time_par_1_40000 = time_par_1[19:28]
time_par_2_40000 = time_par_2[19:28]
time_par_4_40000 = time_par_4[19:28]
time_par_8_40000 = time_par_8[19:28]
speedup_2_40000 = [time_par_1_40000[i]/time_par_2_40000[i] for i in range(9)]
speedup_4_40000 = [time_par_1_40000[i]/time_par_4_40000[i] for i in range(9)]
speedup_8_40000 = [time_par_1_40000[i]/time_par_8_40000[i] for i in range(9)]
x_40000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

time_seq_80000 = time_seq[28:37]
time_par_1_80000 = time_par_1[28:37]
time_par_2_80000 = time_par_2[28:37]
time_par_4_80000 = time_par_4[28:37]
time_par_8_80000 = time_par_8[28:37]
speedup_2_80000 = [time_par_1_80000[i]/time_par_2_80000[i] for i in range(9)]
speedup_4_80000 = [time_par_1_80000[i]/time_par_4_80000[i] for i in range(9)]
speedup_8_80000 = [time_par_1_80000[i]/time_par_8_80000[i] for i in range(9)]
x_80000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000[2::], time_par_1_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_1_20000[2::], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000[2::], time_par_1_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_1_40000[2::], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000[2::], time_par_1_80000[2::], color='blue')
plt.plot(x_80000[2::], time_par_1_80000[2::], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000[2::], time_par_2_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_2_20000[2::], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000[2::], time_par_2_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_2_40000[2::], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000[2::], time_par_2_80000[2::], color='blue')
plt.plot(x_80000[2::], time_par_2_80000[2::], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_uni_copy_M_time_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000[2::], time_par_1_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_1_20000[2::], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000[2::], time_par_1_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_1_40000[2::], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000[2::], time_par_1_80000[2::], color='blue')
plt.plot(x_80000[2::], time_par_1_80000[2::], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000[2::], time_par_4_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_4_20000[2::], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000[2::], time_par_4_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_4_40000[2::], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000[2::], time_par_4_80000[2::], color='blue')
plt.plot(x_80000[2::], time_par_4_80000[2::], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_uni_copy_M_time_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000[2::], time_par_1_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_1_20000[2::], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000[2::], time_par_1_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_1_40000[2::], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000[2::], time_par_1_80000[2::], color='blue')
plt.plot(x_80000[2::], time_par_1_80000[2::], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000[2::], time_par_8_20000[2::], color='orange')
plt.plot(x_20000[2::], time_par_8_20000[2::], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000[2::], time_par_8_40000[2::], color='red')
plt.plot(x_40000[2::], time_par_8_40000[2::], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000[2::], time_par_8_80000[2::], color='blue')
plt.plot(x_80000[2::], time_par_8_80000[2::], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_uni_copy_M_time_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 2 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000[2::], speedup_2_20000[2::], color='orange')
plt.plot(x_20000[2::], speedup_2_20000[2::], linewidth=1.5, color='orange', label=r'$m = 20000$')
plt.scatter(x_40000[2::], speedup_2_40000[2::], color='red')
plt.plot(x_40000[2::], speedup_2_40000[2::], linewidth=1.5, color='red', label=r'$m = 40000$')
plt.scatter(x_80000[2::], speedup_2_80000[2::], color='blue')
plt.plot(x_80000[2::], speedup_2_80000[2::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_uni_copy_M_speedup_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 4 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000[2::], speedup_4_20000[2::], color='orange')
plt.plot(x_20000[2::], speedup_4_20000[2::], linewidth=1.5, color='orange', label=r'$m = 20000$')
plt.scatter(x_40000[2::], speedup_4_40000[2::], color='red')
plt.plot(x_40000[2::], speedup_4_40000[2::], linewidth=1.5, color='red', label=r'$m = 40000$')
plt.scatter(x_80000[2::], speedup_4_80000[2::], color='blue')
plt.plot(x_80000[2::], speedup_4_80000[2::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_uni_copy_M_speedup_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Speedup using 8 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000[2::], speedup_8_20000[2::], color='orange')
plt.plot(x_20000[2::], speedup_8_20000[2::], linewidth=1.5, color='orange', label=r'$m = 20000$')
plt.scatter(x_40000[2::], speedup_8_40000[2::], color='red')
plt.plot(x_40000[2::], speedup_8_40000[2::], linewidth=1.5, color='red', label=r'$m = 40000$')
plt.scatter(x_80000[2::], speedup_8_80000[2::], color='blue')
plt.plot(x_80000[2::], speedup_8_80000[2::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_uni_copy_M_speedup_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 20000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000[2::], speedup_2_20000[2::], linewidth=1.5, color='orange')
plt.plot(x_20000[2::], speedup_2_20000[2::], linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_20000[2::], speedup_4_20000[2::], linewidth=1.5, color='red')
plt.plot(x_20000[2::], speedup_4_20000[2::], linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_20000[2::], speedup_8_20000[2::], linewidth=1.5, color='blue')
plt.plot(x_20000[2::], speedup_8_20000[2::], linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_uni_copy_M_speedup_20000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 40000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_40000[2::], speedup_2_40000[2::], linewidth=1.5, color='orange')
plt.plot(x_40000[2::], speedup_2_40000[2::], linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_40000[2::], speedup_4_40000[2::], linewidth=1.5, color='red')
plt.plot(x_40000[2::], speedup_4_40000[2::], linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_40000[2::], speedup_8_40000[2::], linewidth=1.5, color='blue')
plt.plot(x_40000[2::], speedup_8_40000[2::], linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_uni_copy_M_speedup_40000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 80000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000[2::], speedup_2_80000[2::], linewidth=1.5, color='orange')
plt.plot(x_80000[2::], speedup_2_80000[2::], linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_80000[2::], speedup_4_80000[2::], linewidth=1.5, color='red')
plt.plot(x_80000[2::], speedup_4_80000[2::], linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_80000[2::], speedup_8_80000[2::], linewidth=1.5, color='blue')
plt.plot(x_80000[2::], speedup_8_80000[2::], linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RK_parallel_uni_copy_M_speedup_80000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 20000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000[2::], time_par_2_20000[2::], linewidth=1.5, color='orange')
plt.plot(x_20000[2::], time_par_2_20000[2::], linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_20000[2::], time_par_4_20000[2::], linewidth=1.5, color='red')
plt.plot(x_20000[2::], time_par_4_20000[2::], linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_20000[2::], time_par_8_20000[2::], linewidth=1.5, color='blue')
plt.plot(x_20000[2::], time_par_8_20000[2::], linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_uni_copy_M_time_20000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 40000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_40000[2::], time_par_2_40000[2::], linewidth=1.5, color='orange')
plt.plot(x_40000[2::], time_par_2_40000[2::], linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_40000[2::], time_par_4_40000[2::], linewidth=1.5, color='red')
plt.plot(x_40000[2::], time_par_4_40000[2::], linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_40000[2::], time_par_8_40000[2::], linewidth=1.5, color='blue')
plt.plot(x_40000[2::], time_par_8_40000[2::], linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_uni_copy_M_time_40000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$n = 80000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000[2::], time_par_2_80000[2::], linewidth=1.5, color='orange')
plt.plot(x_80000[2::], time_par_2_80000[2::], linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_80000[2::], time_par_4_80000[2::], linewidth=1.5, color='red')
plt.plot(x_80000[2::], time_par_4_80000[2::], linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_80000[2::], time_par_8_80000[2::], linewidth=1.5, color='blue')
plt.plot(x_80000[2::], time_par_8_80000[2::], linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_parallel_uni_copy_M_time_80000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()