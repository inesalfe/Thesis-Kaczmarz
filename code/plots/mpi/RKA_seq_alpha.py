import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi/RKA_seq_alpha.py

filename = "outputs/omp/RK_seq.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
it_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))
	it_seq.append(float(lines[i].split()[3]))

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

# it_par_1 = it[3::20]
# it_par_2 = it[7::20]
# it_par_4 = it[11::20]
# it_par_8 = it[15::20]
# it_par_20 = it[19::20]

it_par_1 = it[2::20]
it_par_2 = it[6::20]
it_par_4 = it[10::20]
it_par_8 = it[14::20]
it_par_20 = it[18::20]

time_seq_1 = time[0::20]
time_seq_2 = time[4::20]
time_seq_4 = time[8::20]
time_seq_8 = time[12::20]
time_seq_20 = time[16::20]

# time_par_1 = time[3::20]
# time_par_2 = time[7::20]
# time_par_4 = time[11::20]
# time_par_8 = time[15::20]
# time_par_20 = time[19::20]

time_par_1 = time[2::20]
time_par_2 = time[6::20]
time_par_4 = time[10::20]
time_par_8 = time[14::20]
time_par_20 = time[18::20]

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
total_lines_par_1_1000 = [it_par_1[i] for i in indices]
total_lines_par_2_1000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_1000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_1000 = [8*it_par_8[i] for i in indices]
total_lines_par_20_1000 = [20*it_par_20[i] for i in indices]
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
total_lines_par_1_4000 = [it_par_1[i] for i in indices]
total_lines_par_2_4000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_4000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_4000 = [8*it_par_8[i] for i in indices]
total_lines_par_20_4000 = [20*it_par_20[i] for i in indices]
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
total_lines_par_1_10000 = [it_par_1[i] for i in indices]
total_lines_par_2_10000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_10000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_10000 = [8*it_par_8[i] for i in indices]
total_lines_par_20_10000 = [20*it_par_20[i] for i in indices]
x_10000 = [40000, 80000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
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
plt.plot(x_1000, total_lines_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 2 Processes - $n = 1000$')
plt.scatter(x_4000, total_lines_par_2_4000, color='red')
plt.plot(x_4000, total_lines_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 2 Processes - $n = 4000$')
plt.scatter(x_10000, total_lines_par_2_10000, color='blue')
plt.plot(x_10000, total_lines_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 2 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_alpha_rows_2"

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
plt.plot(x_1000, total_lines_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 4 Processes - $n = 1000$')
plt.scatter(x_4000, total_lines_par_4_4000, color='red')
plt.plot(x_4000, total_lines_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 4 Processes - $n = 4000$')
plt.scatter(x_10000, total_lines_par_4_10000, color='blue')
plt.plot(x_10000, total_lines_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 4 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_alpha_rows_4"

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
plt.plot(x_1000, total_lines_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 8 Processes - $n = 1000$')
plt.scatter(x_4000, total_lines_par_8_4000, color='red')
plt.plot(x_4000, total_lines_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 8 Processes - $n = 4000$')
plt.scatter(x_10000, total_lines_par_8_10000, color='blue')
plt.plot(x_10000, total_lines_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 8 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_alpha_rows_8"

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
plt.plot(x_1000, total_lines_par_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 20 Processes - $n = 1000$')
plt.scatter(x_4000, total_lines_par_20_4000, color='red')
plt.plot(x_4000, total_lines_par_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 20 Processes - $n = 4000$')
plt.scatter(x_10000, total_lines_par_20_10000, color='blue')
plt.plot(x_10000, total_lines_par_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 20 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_alpha_rows_20"

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
plt.plot(x_1000, it_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 2 Processes - $n = 1000$')
plt.scatter(x_4000, it_par_2_4000, color='red')
plt.plot(x_4000, it_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 2 Processes - $n = 4000$')
plt.scatter(x_10000, it_par_2_10000, color='blue')
plt.plot(x_10000, it_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 2 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_alpha_it_2"

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
plt.plot(x_1000, it_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 4 Processes - $n = 1000$')
plt.scatter(x_4000, it_par_4_4000, color='red')
plt.plot(x_4000, it_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 4 Processes - $n = 4000$')
plt.scatter(x_10000, it_par_4_10000, color='blue')
plt.plot(x_10000, it_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 4 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_alpha_it_4"

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
plt.plot(x_1000, it_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 8 Processes - $n = 1000$')
plt.scatter(x_4000, it_par_8_4000, color='red')
plt.plot(x_4000, it_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 8 Processes - $n = 4000$')
plt.scatter(x_10000, it_par_8_10000, color='blue')
plt.plot(x_10000, it_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 8 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_alpha_it_8"

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
plt.plot(x_1000, it_par_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 20 Processes - $n = 1000$')
plt.scatter(x_4000, it_par_20_4000, color='red')
plt.plot(x_4000, it_par_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 20 Processes - $n = 4000$')
plt.scatter(x_10000, it_par_20_10000, color='blue')
plt.plot(x_10000, it_par_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 20 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_alpha_it_20"

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
plt.plot(x_1000, time_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 2 Processes - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000, color='red')
plt.plot(x_4000, time_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 2 Processes - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000, color='blue')
plt.plot(x_10000, time_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 2 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_alpha_time_2"

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
plt.plot(x_1000, time_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 4 Processes - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000, color='red')
plt.plot(x_4000, time_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 4 Processes - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000, color='blue')
plt.plot(x_10000, time_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 4 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_alpha_time_4"

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
plt.plot(x_1000, time_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 8 Processes - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000, color='red')
plt.plot(x_4000, time_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 8 Processes - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000, color='blue')
plt.plot(x_10000, time_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 8 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_alpha_time_8"

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
plt.plot(x_1000, time_par_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'RKA with 20 Processes - $n = 1000$')
plt.scatter(x_4000, time_par_20_4000, color='red')
plt.plot(x_4000, time_par_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'RKA with 20 Processes - $n = 4000$')
plt.scatter(x_10000, time_par_20_10000, color='blue')
plt.plot(x_10000, time_par_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'RKA with 20 Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_alpha_time_20"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Total Number of Used Rows using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='black')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='black', label=r'RK')
plt.scatter(x_1000, total_lines_par_2_1000, color='orange')
plt.plot(x_1000, total_lines_par_2_1000, linewidth=1.5, color='orange', label=r'RKA with 2 Processes')
plt.scatter(x_1000, total_lines_par_4_1000, color='red')
plt.plot(x_1000, total_lines_par_4_1000, linewidth=1.5, color='red', label=r'RKA with 4 Processes')
plt.scatter(x_1000, total_lines_par_8_1000, color='blue')
plt.plot(x_1000, total_lines_par_8_1000, linewidth=1.5, color='blue', label=r'RKA with 8 Processes')
plt.scatter(x_1000, total_lines_par_20_1000, color='purple')
plt.plot(x_1000, total_lines_par_20_1000, linewidth=1.5, color='purple', label=r'RKA with 20 Processes')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_alpha_rows_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='black')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='black', label=r'RK')
plt.scatter(x_1000, it_par_2_1000, color='orange')
plt.plot(x_1000, it_par_2_1000, linewidth=1.5, color='orange', label=r'RKA with 2 Processes')
plt.scatter(x_1000, it_par_4_1000, color='red')
plt.plot(x_1000, it_par_4_1000, linewidth=1.5, color='red', label=r'RKA with 4 Processes')
plt.scatter(x_1000, it_par_8_1000, color='blue')
plt.plot(x_1000, it_par_8_1000, linewidth=1.5, color='blue', label=r'RKA with 8 Processes')
plt.scatter(x_1000, it_par_20_1000, color='purple')
plt.plot(x_1000, it_par_20_1000, linewidth=1.5, color='purple', label=r'RKA with 20 Processes')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_alpha_it_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='black')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='black', label=r'RK')
plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linewidth=1.5, color='orange', label=r'RKA with 2 Processes')
plt.scatter(x_1000, time_par_4_1000, color='red')
plt.plot(x_1000, time_par_4_1000, linewidth=1.5, color='red', label=r'RKA with 4 Processes')
plt.scatter(x_1000, time_par_8_1000, color='blue')
plt.plot(x_1000, time_par_8_1000, linewidth=1.5, color='blue', label=r'RKA with 8 Processes')
plt.scatter(x_1000, time_par_20_1000, color='purple')
plt.plot(x_1000, time_par_20_1000, linewidth=1.5, color='purple', label=r'RKA with 20 Processes')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_alpha_time_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_2_1000, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'2 Processes')
plt.scatter(x_1000, speedup_4_1000, color='red')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='red', label=r'4 Processes')
plt.scatter(x_1000, speedup_8_1000, color='blue')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='blue', label=r'8 Processes')
plt.scatter(x_1000, speedup_20_1000, color='purple')
plt.plot(x_1000, speedup_20_1000, linewidth=1.5, color='purple', label=r'20 Processes')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_seq_alpha_speedup_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')