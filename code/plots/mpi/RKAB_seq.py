import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi/RKAB_seq.py

filename = "outputs/omp/RK_seq.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
it_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))
	it_seq.append(float(lines[i].split()[3]))

filename = "outputs/mpi/RKAB_mpi.txt";

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

it_par_1 = it[1::20]
it_par_2 = it[5::20]
it_par_4 = it[9::20]
it_par_8 = it[13::20]
it_par_20 = it[17::20]

time_seq_1 = time[0::20]
time_seq_2 = time[4::20]
time_seq_4 = time[8::20]
time_seq_8 = time[12::20]
time_seq_20 = time[16::20]

time_par_1 = time[1::20]
time_par_2 = time[5::20]
time_par_4 = time[9::20]
time_par_8 = time[13::20]
time_par_20 = time[17::20]

indices = (0, 1, 3, 6)
indices2 = (10, 16, 24, 33)
it_seq_1000 = [it_seq[i] for i in indices2]
time_seq_1000 = [time_seq[i] for i in indices2]
it_seq_1_1000 = [it_seq_1[i] for i in indices]
it_seq_2_1000 = [it_seq_2[i] for i in indices]
it_seq_4_1000 = [it_seq_4[i] for i in indices]
it_seq_8_1000 = [it_seq_8[i] for i in indices]
it_seq_20_1000 = [it_seq_20[i] for i in indices]
it_par_1_1000 = [it_par_1[i] for i in indices]
it_par_2_1000 = [it_par_2[i] for i in indices]
it_par_4_1000 = [it_par_4[i] for i in indices]
it_par_8_1000 = [it_par_8[i] for i in indices]
it_par_20_1000 = [it_par_20[i] for i in indices]
time_seq_1_1000 = [time_seq_1[i] for i in indices]
time_seq_2_1000 = [time_seq_2[i] for i in indices]
time_seq_4_1000 = [time_seq_4[i] for i in indices]
time_seq_8_1000 = [time_seq_8[i] for i in indices]
time_seq_20_1000 = [time_seq_20[i] for i in indices]
time_par_1_1000 = [time_par_1[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
time_par_20_1000 = [time_par_20[i] for i in indices]
speedup_2_1000 = [time_seq[j]/time_par_2[i] for i,j in zip(indices,indices2)]
speedup_4_1000 = [time_seq[j]/time_par_4[i] for i,j in zip(indices,indices2)]
speedup_8_1000 = [time_seq[j]/time_par_8[i] for i,j in zip(indices,indices2)]
speedup_20_1000 = [time_seq[j]/time_par_20[i] for i,j in zip(indices,indices2)]
total_lines_par_1_1000 = [it_par_1[i]*1000 for i in indices]
total_lines_par_2_1000 = [2*it_par_2[i]*1000 for i in indices]
total_lines_par_4_1000 = [4*it_par_4[i]*1000 for i in indices]
total_lines_par_8_1000 = [8*it_par_8[i]*1000 for i in indices]
total_lines_par_20_1000 = [20*it_par_20[i]*1000 for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (2, 4, 7)
indices2 = (18, 26, 35)
it_seq_4000 = [it_seq[i] for i in indices2]
time_seq_4000 = [time_seq[i] for i in indices2]
it_seq_1_4000 = [it_seq_1[i] for i in indices]
it_seq_2_4000 = [it_seq_2[i] for i in indices]
it_seq_4_4000 = [it_seq_4[i] for i in indices]
it_seq_8_4000 = [it_seq_8[i] for i in indices]
it_seq_20_4000 = [it_seq_20[i] for i in indices]
it_par_1_4000 = [it_par_1[i] for i in indices]
it_par_2_4000 = [it_par_2[i] for i in indices]
it_par_4_4000 = [it_par_4[i] for i in indices]
it_par_8_4000 = [it_par_8[i] for i in indices]
it_par_20_4000 = [it_par_20[i] for i in indices]
time_seq_1_4000 = [time_seq_1[i] for i in indices]
time_seq_2_4000 = [time_seq_2[i] for i in indices]
time_seq_4_4000 = [time_seq_4[i] for i in indices]
time_seq_8_4000 = [time_seq_8[i] for i in indices]
time_seq_20_4000 = [time_seq_20[i] for i in indices]
time_par_1_4000 = [time_par_1[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
time_par_20_4000 = [time_par_20[i] for i in indices]
speedup_2_4000 = [time_seq[j]/time_par_2[i] for i,j in zip(indices,indices2)]
speedup_4_4000 = [time_seq[j]/time_par_4[i] for i,j in zip(indices,indices2)]
speedup_8_4000 = [time_seq[j]/time_par_8[i] for i,j in zip(indices,indices2)]
speedup_20_4000 = [time_seq[j]/time_par_20[i] for i,j in zip(indices,indices2)]
total_lines_par_1_4000 = [it_par_1[i]*4000 for i in indices]
total_lines_par_2_4000 = [2*it_par_2[i]*4000 for i in indices]
total_lines_par_4_4000 = [4*it_par_4[i]*4000 for i in indices]
total_lines_par_8_4000 = [8*it_par_8[i]*4000 for i in indices]
total_lines_par_20_4000 = [20*it_par_20[i]*4000 for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (5, 8)
indices2 = (27, 36)
it_seq_10000 = [it_seq[i] for i in indices2]
time_seq_10000 = [time_seq[i] for i in indices2]
it_seq_1_10000 = [it_seq_1[i] for i in indices]
it_seq_2_10000 = [it_seq_2[i] for i in indices]
it_seq_4_10000 = [it_seq_4[i] for i in indices]
it_seq_8_10000 = [it_seq_8[i] for i in indices]
it_seq_20_10000 = [it_seq_20[i] for i in indices]
it_par_1_10000 = [it_par_1[i] for i in indices]
it_par_2_10000 = [it_par_2[i] for i in indices]
it_par_4_10000 = [it_par_4[i] for i in indices]
it_par_8_10000 = [it_par_8[i] for i in indices]
it_par_20_10000 = [it_par_20[i] for i in indices]
time_seq_1_10000 = [time_seq_1[i] for i in indices]
time_seq_2_10000 = [time_seq_2[i] for i in indices]
time_seq_4_10000 = [time_seq_4[i] for i in indices]
time_seq_8_10000 = [time_seq_8[i] for i in indices]
time_seq_20_10000 = [time_seq_20[i] for i in indices]
time_par_1_10000 = [time_par_1[i] for i in indices]
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
time_par_20_10000 = [time_par_20[i] for i in indices]
speedup_2_10000 = [time_seq[j]/time_par_2[i] for i,j in zip(indices,indices2)]
speedup_4_10000 = [time_seq[j]/time_par_4[i] for i,j in zip(indices,indices2)]
speedup_8_10000 = [time_seq[j]/time_par_8[i] for i,j in zip(indices,indices2)]
speedup_20_10000 = [time_seq[j]/time_par_20[i] for i,j in zip(indices,indices2)]
total_lines_par_1_10000 = [it_par_1[i]*10000 for i in indices]
total_lines_par_2_10000 = [2*it_par_2[i]*10000 for i in indices]
total_lines_par_4_10000 = [4*it_par_4[i]*10000 for i in indices]
total_lines_par_8_10000 = [8*it_par_8[i]*10000 for i in indices]
total_lines_par_20_10000 = [20*it_par_20[i]*10000 for i in indices]
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

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, total_lines_par_2_1000, color='orange')
plt.plot(x_1000, total_lines_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 2 Tasks - $n = 1000$')
plt.scatter(x_4000, total_lines_par_2_4000, color='red')
plt.plot(x_4000, total_lines_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 2 Tasks - $n = 4000$')
plt.scatter(x_10000, total_lines_par_2_10000, color='blue')
plt.plot(x_10000, total_lines_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 2 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_seq_rows_2"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, total_lines_par_4_1000, color='orange')
plt.plot(x_1000, total_lines_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 4 Tasks - $n = 1000$')
plt.scatter(x_4000, total_lines_par_4_4000, color='red')
plt.plot(x_4000, total_lines_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 4 Tasks - $n = 4000$')
plt.scatter(x_10000, total_lines_par_4_10000, color='blue')
plt.plot(x_10000, total_lines_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 4 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_seq_rows_4"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, total_lines_par_8_1000, color='orange')
plt.plot(x_1000, total_lines_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 8 Tasks - $n = 1000$')
plt.scatter(x_4000, total_lines_par_8_4000, color='red')
plt.plot(x_4000, total_lines_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 8 Tasks - $n = 4000$')
plt.scatter(x_10000, total_lines_par_8_10000, color='blue')
plt.plot(x_10000, total_lines_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 8 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_seq_rows_8"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, total_lines_par_20_1000, color='orange')
plt.plot(x_1000, total_lines_par_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 20 Tasks - $n = 1000$')
plt.scatter(x_4000, total_lines_par_20_4000, color='red')
plt.plot(x_4000, total_lines_par_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 20 Tasks - $n = 4000$')
plt.scatter(x_10000, total_lines_par_20_10000, color='blue')
plt.plot(x_10000, total_lines_par_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 20 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_seq_rows_20"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_2_1000, color='orange')
plt.plot(x_1000, it_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 2 Tasks - $n = 1000$')
plt.scatter(x_4000, it_par_2_4000, color='red')
plt.plot(x_4000, it_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 2 Tasks - $n = 4000$')
plt.scatter(x_10000, it_par_2_10000, color='blue')
plt.plot(x_10000, it_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 2 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_seq_it_2"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_4_1000, color='orange')
plt.plot(x_1000, it_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 4 Tasks - $n = 1000$')
plt.scatter(x_4000, it_par_4_4000, color='red')
plt.plot(x_4000, it_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 4 Tasks - $n = 4000$')
plt.scatter(x_10000, it_par_4_10000, color='blue')
plt.plot(x_10000, it_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 4 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_seq_it_4"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_8_1000, color='orange')
plt.plot(x_1000, it_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 8 Tasks - $n = 1000$')
plt.scatter(x_4000, it_par_8_4000, color='red')
plt.plot(x_4000, it_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 8 Tasks - $n = 4000$')
plt.scatter(x_10000, it_par_8_10000, color='blue')
plt.plot(x_10000, it_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 8 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_seq_it_8"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_20_1000, color='orange')
plt.plot(x_1000, it_par_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 20 Tasks - $n = 1000$')
plt.scatter(x_4000, it_par_20_4000, color='red')
plt.plot(x_4000, it_par_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 20 Tasks - $n = 4000$')
plt.scatter(x_10000, it_par_20_10000, color='blue')
plt.plot(x_10000, it_par_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 20 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_seq_it_20"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 2 Tasks - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000, color='red')
plt.plot(x_4000, time_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 2 Tasks - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000, color='blue')
plt.plot(x_10000, time_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 2 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_seq_time_2"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000, color='orange')
plt.plot(x_1000, time_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 4 Tasks - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000, color='red')
plt.plot(x_4000, time_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 4 Tasks - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000, color='blue')
plt.plot(x_10000, time_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 4 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_seq_time_4"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000, color='orange')
plt.plot(x_1000, time_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 8 Tasks - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000, color='red')
plt.plot(x_4000, time_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 8 Tasks - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000, color='blue')
plt.plot(x_10000, time_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 8 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_seq_time_8"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_20_1000, color='orange')
plt.plot(x_1000, time_par_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKAB with 20 Tasks - $n = 1000$')
plt.scatter(x_4000, time_par_20_4000, color='red')
plt.plot(x_4000, time_par_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKAB with 20 Tasks - $n = 4000$')
plt.scatter(x_10000, time_par_20_10000, color='blue')
plt.plot(x_10000, time_par_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKAB with 20 Tasks - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_seq_time_20"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Total Number of Used Rows using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='gray')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='gray', label=r'RK')
plt.scatter(x_1000, total_lines_par_2_1000, color='orange')
plt.plot(x_1000, total_lines_par_2_1000, linewidth=1.5, color='orange', label=r'RKAB with 2 Tasks')
plt.scatter(x_1000, total_lines_par_4_1000, color='red')
plt.plot(x_1000, total_lines_par_4_1000, linewidth=1.5, color='red', label=r'RKAB with 4 Tasks')
plt.scatter(x_1000, total_lines_par_8_1000, color='blue')
plt.plot(x_1000, total_lines_par_8_1000, linewidth=1.5, color='blue', label=r'RKAB with 8 Tasks')
plt.scatter(x_1000, total_lines_par_20_1000, color='purple')
plt.plot(x_1000, total_lines_par_20_1000, linewidth=1.5, color='purple', label=r'RKAB with 20 Tasks')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_seq_rows_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='gray')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='gray', label=r'RK')
plt.scatter(x_1000, it_par_2_1000, color='orange')
plt.plot(x_1000, it_par_2_1000, linewidth=1.5, color='orange', label=r'RKAB with 2 Tasks')
plt.scatter(x_1000, it_par_4_1000, color='red')
plt.plot(x_1000, it_par_4_1000, linewidth=1.5, color='red', label=r'RKAB with 4 Tasks')
plt.scatter(x_1000, it_par_8_1000, color='blue')
plt.plot(x_1000, it_par_8_1000, linewidth=1.5, color='blue', label=r'RKAB with 8 Tasks')
plt.scatter(x_1000, it_par_20_1000, color='purple')
plt.plot(x_1000, it_par_20_1000, linewidth=1.5, color='purple', label=r'RKAB with 20 Tasks')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_seq_it_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='gray')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='gray', label=r'RK')
plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linewidth=1.5, color='orange', label=r'RKAB with 2 Tasks')
plt.scatter(x_1000, time_par_4_1000, color='red')
plt.plot(x_1000, time_par_4_1000, linewidth=1.5, color='red', label=r'RKAB with 4 Tasks')
plt.scatter(x_1000, time_par_8_1000, color='blue')
plt.plot(x_1000, time_par_8_1000, linewidth=1.5, color='blue', label=r'RKAB with 8 Tasks')
plt.scatter(x_1000, time_par_20_1000, color='purple')
plt.plot(x_1000, time_par_20_1000, linewidth=1.5, color='purple', label=r'RKAB with 20 Tasks')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_seq_time_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_2_1000, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'2 Tasks')
plt.scatter(x_1000, speedup_4_1000, color='red')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='red', label=r'4 Tasks')
plt.scatter(x_1000, speedup_8_1000, color='blue')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='blue', label=r'8 Tasks')
plt.scatter(x_1000, speedup_20_1000, color='purple')
plt.plot(x_1000, speedup_20_1000, linewidth=1.5, color='purple', label=r'20 Tasks')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_seq_speedup_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')