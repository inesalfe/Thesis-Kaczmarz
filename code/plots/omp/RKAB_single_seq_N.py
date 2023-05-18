import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_single_seq_N.py

filename = "outputs/omp/RK_seq.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
it_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))
	it_seq.append(int(lines[i].split()[3]))

indices = (10, 16, 18, 24, 26, 27, 33, 35, 36)
time_seq_dim = [time_seq[i] for i in indices]
it_seq_dim = [it_seq[i] for i in indices]
indices = (10, 16, 24, 33, 18, 26, 35, 27, 36)
time_seq = [time_seq[i] for i in indices]
it_seq = [it_seq[i] for i in indices]

indices = (0, 1, 3, 6)
time_seq_1000 = [time_seq_dim[i] for i in indices]
it_seq_1000 = [it_seq_dim[i] for i in indices]
indices = (2, 4, 7)
time_seq_4000 = [time_seq_dim[i] for i in indices]
it_seq_4000 = [it_seq_dim[i] for i in indices]
indices = (5, 8)
time_seq_10000 = [time_seq_dim[i] for i in indices]
it_seq_10000 = [it_seq_dim[i] for i in indices]

filename = "outputs/omp/RKAB_single.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))

time_par_1 = time[1::8]
time_par_2 = time[3::8]
time_par_4 = time[5::8]
time_par_8 = time[7::8]

time_par_1_5 = time_par_1[0::7]
time_par_2_5 = time_par_2[0::7]
time_par_4_5 = time_par_4[0::7]
time_par_8_5 = time_par_8[0::7]
speedup_2_5 = [time_seq_dim[i]/time_par_2_5[i] for i in range(9)]
speedup_4_5 = [time_seq_dim[i]/time_par_4_5[i] for i in range(9)]
speedup_8_5 = [time_seq_dim[i]/time_par_8_5[i] for i in range(9)]

time_par_1_10 = time_par_1[1::7]
time_par_2_10 = time_par_2[1::7]
time_par_4_10 = time_par_4[1::7]
time_par_8_10 = time_par_8[1::7]
speedup_2_10 = [time_seq_dim[i]/time_par_2_10[i] for i in range(9)]
speedup_4_10 = [time_seq_dim[i]/time_par_4_10[i] for i in range(9)]
speedup_8_10 = [time_seq_dim[i]/time_par_8_10[i] for i in range(9)]

time_par_1_50 = time_par_1[2::7]
time_par_2_50 = time_par_2[2::7]
time_par_4_50 = time_par_4[2::7]
time_par_8_50 = time_par_8[2::7]
speedup_2_50 = [time_seq_dim[i]/time_par_2_50[i] for i in range(9)]
speedup_4_50 = [time_seq_dim[i]/time_par_4_50[i] for i in range(9)]
speedup_8_50 = [time_seq_dim[i]/time_par_8_50[i] for i in range(9)]

time_par_1_100 = time_par_1[3::7]
time_par_2_100 = time_par_2[3::7]
time_par_4_100 = time_par_4[3::7]
time_par_8_100 = time_par_8[3::7]
speedup_2_100 = [time_seq_dim[i]/time_par_2_100[i] for i in range(9)]
speedup_4_100 = [time_seq_dim[i]/time_par_4_100[i] for i in range(9)]
speedup_8_100 = [time_seq_dim[i]/time_par_8_100[i] for i in range(9)]

time_par_1_500 = time_par_1[4::7]
time_par_2_500 = time_par_2[4::7]
time_par_4_500 = time_par_4[4::7]
time_par_8_500 = time_par_8[4::7]
speedup_2_500 = [time_seq_dim[i]/time_par_2_500[i] for i in range(9)]
speedup_4_500 = [time_seq_dim[i]/time_par_4_500[i] for i in range(9)]
speedup_8_500 = [time_seq_dim[i]/time_par_8_500[i] for i in range(9)]

time_par_1_1000 = time_par_1[5::7]
time_par_2_1000 = time_par_2[5::7]
time_par_4_1000 = time_par_4[5::7]
time_par_8_1000 = time_par_8[5::7]
speedup_2_1000 = [time_seq_dim[i]/time_par_2_1000[i] for i in range(9)]
speedup_4_1000 = [time_seq_dim[i]/time_par_4_1000[i] for i in range(9)]
speedup_8_1000 = [time_seq_dim[i]/time_par_8_1000[i] for i in range(9)]

time_par_1_10000 = time_par_1[6::7]
time_par_2_10000 = time_par_2[6::7]
time_par_4_10000 = time_par_4[6::7]
time_par_8_10000 = time_par_8[6::7]
speedup_2_10000 = [time_seq_dim[i]/time_par_2_10000[i] for i in range(9)]
speedup_4_10000 = [time_seq_dim[i]/time_par_4_10000[i] for i in range(9)]
speedup_8_10000 = [time_seq_dim[i]/time_par_8_10000[i] for i in range(9)]

it_par_1 = it[1::8]
it_par_2 = it[3::8]
it_par_4 = it[5::8]
it_par_8 = it[7::8]

blocks = [5, 10, 50, 100, 500, 1000, 10000]

lines_par_2 = [it_par_2[i]*2*blocks[i%7] for i in range(len(it_par_2))]
lines_par_4 = [it_par_4[i]*4*blocks[i%7] for i in range(len(it_par_4))]
lines_par_8 = [it_par_8[i]*8*blocks[i%7] for i in range(len(it_par_8))]

it_par_1_5 = it_par_1[0::7]
it_par_2_5 = it_par_2[0::7]
it_par_4_5 = it_par_4[0::7]
it_par_8_5 = it_par_8[0::7]

lines_par_1_5 = [it_par_1_5[i]*1*5 for i in range(9)]
lines_par_2_5 = [it_par_2_5[i]*2*5 for i in range(9)]
lines_par_4_5 = [it_par_4_5[i]*4*5 for i in range(9)]
lines_par_8_5 = [it_par_8_5[i]*8*5 for i in range(9)]

it_par_1_10 = it_par_1[1::7]
it_par_2_10 = it_par_2[1::7]
it_par_4_10 = it_par_4[1::7]
it_par_8_10 = it_par_8[1::7]

lines_par_1_10 = [it_par_1_10[i]*1*10 for i in range(9)]
lines_par_2_10 = [it_par_2_10[i]*2*10 for i in range(9)]
lines_par_4_10 = [it_par_4_10[i]*4*10 for i in range(9)]
lines_par_8_10 = [it_par_8_10[i]*8*10 for i in range(9)]

it_par_1_50 = it_par_1[2::7]
it_par_2_50 = it_par_2[2::7]
it_par_4_50 = it_par_4[2::7]
it_par_8_50 = it_par_8[2::7]

lines_par_1_50 = [it_par_1_50[i]*1*50 for i in range(9)]
lines_par_2_50 = [it_par_2_50[i]*2*50 for i in range(9)]
lines_par_4_50 = [it_par_4_50[i]*4*50 for i in range(9)]
lines_par_8_50 = [it_par_8_50[i]*8*50 for i in range(9)]

it_par_1_100 = it_par_1[3::7]
it_par_2_100 = it_par_2[3::7]
it_par_4_100 = it_par_4[3::7]
it_par_8_100 = it_par_8[3::7]

lines_par_1_100 = [it_par_1_100[i]*1*100 for i in range(9)]
lines_par_2_100 = [it_par_2_100[i]*2*100 for i in range(9)]
lines_par_4_100 = [it_par_4_100[i]*4*100 for i in range(9)]
lines_par_8_100 = [it_par_8_100[i]*8*100 for i in range(9)]

it_par_1_500 = it_par_1[4::7]
it_par_2_500 = it_par_2[4::7]
it_par_4_500 = it_par_4[4::7]
it_par_8_500 = it_par_8[4::7]

lines_par_1_500 = [it_par_1_500[i]*1*500 for i in range(9)]
lines_par_2_500 = [it_par_2_500[i]*2*500 for i in range(9)]
lines_par_4_500 = [it_par_4_500[i]*4*500 for i in range(9)]
lines_par_8_500 = [it_par_8_500[i]*8*500 for i in range(9)]

it_par_1_1000 = it_par_1[5::7]
it_par_2_1000 = it_par_2[5::7]
it_par_4_1000 = it_par_4[5::7]
it_par_8_1000 = it_par_8[5::7]

lines_par_1_1000 = [it_par_1_1000[i]*1*1000 for i in range(9)]
lines_par_2_1000 = [it_par_2_1000[i]*2*1000 for i in range(9)]
lines_par_4_1000 = [it_par_4_1000[i]*4*1000 for i in range(9)]
lines_par_8_1000 = [it_par_8_1000[i]*8*1000 for i in range(9)]

it_par_1_10000 = it_par_1[6::7]
it_par_2_10000 = it_par_2[6::7]
it_par_4_10000 = it_par_4[6::7]
it_par_8_10000 = it_par_8[6::7]

lines_par_1_10000 = [it_par_1_10000[i]*1*10000 for i in range(9)]
lines_par_2_10000 = [it_par_2_10000[i]*2*10000 for i in range(9)]
lines_par_4_10000 = [it_par_4_10000[i]*4*10000 for i in range(9)]
lines_par_8_10000 = [it_par_8_10000[i]*8*10000 for i in range(9)]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x_1000 = [4000, 20000, 40000, 80000]
x_4000 = [20000, 40000, 80000]
x_10000 = [40000, 80000]

plot_title = r"Average of Threads = 2 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_2_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_2_5[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_2_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_2_5[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_2_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_2_5[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_2_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_4_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_4_5[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_4_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_4_5[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_4_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_4_5[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_4_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_8_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_8_5[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_8_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_8_5[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_8_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_8_5[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_8_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_2_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_2_5[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_2_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_2_5[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_2_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_2_5[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_2_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_4_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_4_5[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_4_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_4_5[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_4_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_4_5[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_4_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_8_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_8_5[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_8_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_8_5[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_8_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_8_5[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_8_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_2_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_2_10[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_2_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_2_10[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_2_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_2_10[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_2_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_4_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_4_10[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_4_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_4_10[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_4_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_4_10[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_4_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_8_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_8_10[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_8_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_8_10[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_8_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_8_10[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_8_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_2_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_2_10[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_2_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_2_10[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_2_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_2_10[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_2_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_4_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_4_10[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_4_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_4_10[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_4_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_4_10[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_4_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_8_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_8_10[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_8_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_8_10[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_8_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_8_10[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_8_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_2_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_2_50[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_2_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_2_50[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_2_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_2_50[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_2_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_4_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_4_50[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_4_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_4_50[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_4_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_4_50[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_4_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_8_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_8_50[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_8_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_8_50[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_8_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_8_50[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_8_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_2_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_2_50[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_2_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_2_50[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_2_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_2_50[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_2_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_4_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_4_50[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_4_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_4_50[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_4_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_4_50[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_4_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_8_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_8_50[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_8_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_8_50[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_8_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_8_50[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_8_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_2_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_2_100[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_2_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_2_100[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_2_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_2_100[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_2_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_4_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_4_100[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_4_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_4_100[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_4_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_4_100[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_4_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_8_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_8_100[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_8_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_8_100[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_8_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_8_100[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_8_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_2_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_2_100[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_2_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_2_100[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_2_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_2_100[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_2_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_4_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_4_100[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_4_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_4_100[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_4_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_4_100[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_4_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_8_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_8_100[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_8_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_8_100[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_8_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_8_100[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_8_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_2_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_2_500[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_2_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_2_500[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_2_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_2_500[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_2_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_4_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_4_500[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_4_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_4_500[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_4_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_4_500[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_4_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_8_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_8_500[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_8_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_8_500[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_8_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_8_500[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_8_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_2_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_2_500[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_2_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_2_500[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_2_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_2_500[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_2_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_4_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_4_500[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_4_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_4_500[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_4_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_4_500[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_4_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_8_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_8_500[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_8_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_8_500[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_8_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_8_500[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_8_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_2_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_2_1000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_2_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_2_1000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_2_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_2_1000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_2_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_4_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_4_1000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_4_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_4_1000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_4_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_4_1000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_4_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_8_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_8_1000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_8_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_8_1000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_8_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_8_1000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_8_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_2_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_2_1000[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_2_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_2_1000[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_2_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_2_1000[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_2_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_4_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_4_1000[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_4_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_4_1000[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_4_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_4_1000[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_4_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_8_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_8_1000[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_8_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_8_1000[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_8_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_8_1000[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_8_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_2_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_2_10000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_2_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_2_10000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_2_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_2_10000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_2_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_4_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_4_10000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_4_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_4_10000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_4_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_4_10000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_4_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [time_par_8_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [time_par_8_10000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [time_par_8_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [time_par_8_10000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [time_par_8_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [time_par_8_10000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_8_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_2_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_2_10000[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_2_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_2_10000[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_2_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_2_10000[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_2_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_4_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_4_10000[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_4_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_4_10000[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_4_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_4_10000[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_4_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, [speedup_8_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [speedup_8_10000[x] for x in [0,1,3,6]], linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, [speedup_8_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [speedup_8_10000[x] for x in [2,4,7]], linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, [speedup_8_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [speedup_8_10000[x] for x in [5,8]], linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_single_seq_N_speedup_8_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

x = [5, 10, 50, 100, 500, 1000, 10000]

plot_title = r"$4000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[0], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[0:7], color='orange')
plt.plot(x, time_par_2[0:7], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[0:7], color='red')
plt.plot(x, time_par_4[0:7], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[0:7], color='blue')
plt.plot(x, time_par_8[0:7], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_4000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$20000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[1], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[7:14], color='orange')
plt.plot(x, time_par_2[7:14], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[7:14], color='red')
plt.plot(x, time_par_4[7:14], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[7:14], color='blue')
plt.plot(x, time_par_8[7:14], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_20000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$20000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[2], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[14:21], color='orange')
plt.plot(x, time_par_2[14:21], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[14:21], color='red')
plt.plot(x, time_par_4[14:21], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[14:21], color='blue')
plt.plot(x, time_par_8[14:21], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_20000_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[3], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[21:28], color='orange')
plt.plot(x, time_par_2[21:28], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[21:28], color='red')
plt.plot(x, time_par_4[21:28], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[21:28], color='blue')
plt.plot(x, time_par_8[21:28], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_40000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[4], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[28:35], color='orange')
plt.plot(x, time_par_2[28:35], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[28:35], color='red')
plt.plot(x, time_par_4[28:35], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[28:35], color='blue')
plt.plot(x, time_par_8[28:35], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_40000_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[5], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[35:42], color='orange')
plt.plot(x, time_par_2[35:42], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[35:42], color='red')
plt.plot(x, time_par_4[35:42], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[35:42], color='blue')
plt.plot(x, time_par_8[35:42], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_40000_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x, time_par_8[35:42], color='blue')
plt.plot(x, time_par_8[35:42], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_40000_10000_extra"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[6], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[42:49], color='orange')
plt.plot(x, time_par_2[42:49], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[42:49], color='red')
plt.plot(x, time_par_4[42:49], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[42:49], color='blue')
plt.plot(x, time_par_8[42:49], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_80000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[7], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[49:56], color='orange')
plt.plot(x, time_par_2[49:56], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[49:56], color='red')
plt.plot(x, time_par_4[49:56], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[49:56], color='blue')
plt.plot(x, time_par_8[49:56], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_80000_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[8], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, time_par_2[56:63], color='orange')
plt.plot(x, time_par_2[56:63], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[56:63], color='red')
plt.plot(x, time_par_4[56:63], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[56:63], color='blue')
plt.plot(x, time_par_8[56:63], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_N_time_80000_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

x_1000 = [4000, 20000, 40000, 80000]
x_4000 = [20000, 40000, 80000]
x_10000 = [40000, 80000]

plot_title = r"Average of Threads = 2 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_2_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_2_5[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_2_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_2_5[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_2_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_2_5[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_2_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_4_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_4_5[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_4_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_4_5[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_4_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_4_5[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_4_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 5 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_8_5[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_8_5[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_8_5[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_8_5[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_8_5[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_8_5[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_8_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_2_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_2_10[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_2_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_2_10[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_2_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_2_10[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_2_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_4_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_4_10[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_4_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_4_10[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_4_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_4_10[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_4_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 10 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_8_10[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_8_10[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_8_10[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_8_10[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_8_10[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_8_10[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_8_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_2_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_2_50[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_2_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_2_50[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_2_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_2_50[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_2_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_4_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_4_50[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_4_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_4_50[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_4_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_4_50[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_4_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 50 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_8_50[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_8_50[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_8_50[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_8_50[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_8_50[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_8_50[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_8_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_2_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_2_100[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_2_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_2_100[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_2_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_2_100[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_2_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_4_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_4_100[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_4_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_4_100[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_4_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_4_100[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_4_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 100 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_8_100[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_8_100[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_8_100[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_8_100[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_8_100[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_8_100[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_8_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_2_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_2_500[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_2_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_2_500[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_2_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_2_500[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_2_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_4_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_4_500[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_4_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_4_500[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_4_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_4_500[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_4_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 500 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_8_500[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_8_500[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_8_500[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_8_500[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_8_500[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_8_500[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_8_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_2_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_2_1000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_2_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_2_1000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_2_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_2_1000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_2_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_4_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_4_1000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_4_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_4_1000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_4_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_4_1000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_4_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 1000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_8_1000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_8_1000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_8_1000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_8_1000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_8_1000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_8_1000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_8_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 2 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_2_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_2_10000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_2_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_2_10000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_2_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_2_10000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_2_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 4 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_4_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_4_10000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_4_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_4_10000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_4_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_4_10000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_4_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Average of Threads = 8 of 10000 projections"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, [lines_par_8_10000[x] for x in [0,1,3,6]], color='orange')
plt.plot(x_1000, [lines_par_8_10000[x] for x in [0,1,3,6]], linestyle='--', linewidth=1.5, color='orange', label=r'Parallel - $n = 1000$')
plt.scatter(x_4000, [lines_par_8_10000[x] for x in [2,4,7]], color='red')
plt.plot(x_4000, [lines_par_8_10000[x] for x in [2,4,7]], linestyle='--', linewidth=1.5, color='red', label=r'Parallel - $n = 4000$')
plt.scatter(x_10000, [lines_par_8_10000[x] for x in [5,8]], color='blue')
plt.plot(x_10000, [lines_par_8_10000[x] for x in [5,8]], linestyle='--', linewidth=1.5, color='blue', label=r'Parallel - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_8_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

x = [5, 10, 50, 100, 500, 1000, 10000]

plot_title = r"$4000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[0], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[0:7], color='orange')
plt.plot(x, lines_par_2[0:7], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[0:7], color='red')
plt.plot(x, lines_par_4[0:7], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[0:7], color='blue')
plt.plot(x, lines_par_8[0:7], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_4000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$20000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[1], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[7:14], color='orange')
plt.plot(x, lines_par_2[7:14], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[7:14], color='red')
plt.plot(x, lines_par_4[7:14], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[7:14], color='blue')
plt.plot(x, lines_par_8[7:14], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_20000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$20000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[2], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[14:21], color='orange')
plt.plot(x, lines_par_2[14:21], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[14:21], color='red')
plt.plot(x, lines_par_4[14:21], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[14:21], color='blue')
plt.plot(x, lines_par_8[14:21], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_20000_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[3], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[21:28], color='orange')
plt.plot(x, lines_par_2[21:28], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[21:28], color='red')
plt.plot(x, lines_par_4[21:28], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[21:28], color='blue')
plt.plot(x, lines_par_8[21:28], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_40000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[4], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[28:35], color='orange')
plt.plot(x, lines_par_2[28:35], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[28:35], color='red')
plt.plot(x, lines_par_4[28:35], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[28:35], color='blue')
plt.plot(x, lines_par_8[28:35], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_40000_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[5], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[35:42], color='orange')
plt.plot(x, lines_par_2[35:42], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[35:42], color='red')
plt.plot(x, lines_par_4[35:42], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[35:42], color='blue')
plt.plot(x, lines_par_8[35:42], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_40000_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$40000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x, lines_par_8[35:42], color='blue')
plt.plot(x, lines_par_8[35:42], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_40000_10000_extra"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[6], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[42:49], color='orange')
plt.plot(x, lines_par_2[42:49], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[42:49], color='red')
plt.plot(x, lines_par_4[42:49], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[42:49], color='blue')
plt.plot(x, lines_par_8[42:49], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_80000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 4000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[7], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[49:56], color='orange')
plt.plot(x, lines_par_2[49:56], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[49:56], color='red')
plt.plot(x, lines_par_4[49:56], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[49:56], color='blue')
plt.plot(x, lines_par_8[49:56], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_80000_4000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 10000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=it_seq_dim[8], linestyle='--', linewidth=1.5, color='grey', label=r'Sequential')
plt.scatter(x, lines_par_2[56:63], color='orange')
plt.plot(x, lines_par_2[56:63], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[56:63], color='red')
plt.plot(x, lines_par_4[56:63], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[56:63], color='blue')
plt.plot(x, lines_par_8[56:63], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_N_lines_80000_10000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()