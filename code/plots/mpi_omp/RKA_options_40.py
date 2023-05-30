import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi_omp/RKA_options_40.py

filename = "outputs/mpi_omp/RKA_mpi_omp_alpha_80000_1000.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))
    it.append(float(lines[i].split()[3]))

it_seq_80000_10000 = it[0:4]
it_par_op1_80000_10000 = it[4:8]
it_par_op2_80000_10000 = it[8:12]
time_seq_80000_10000 = time[0:4]
time_par_op1_80000_10000 = time[4:8]
time_par_op2_80000_10000 = time[8:12]
x_80000_10000 = [4, 8, 20, 40]

filename = "outputs/mpi_omp/RKA_mpi_omp_alpha_40.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))
    it.append(float(lines[i].split()[3]))

it_seq_4_10 = it[0::9]
it_seq_8_5 = it[3::9]
it_seq_20_2 = it[6::9]

it_par_op1_4_10 = it[1::9]
it_par_op1_8_5 = it[4::9]
it_par_op1_20_2 = it[7::9]

it_par_op2_4_10 = it[2::9]
it_par_op2_8_5 = it[5::9]
it_par_op2_20_2 = it[8::9]

time_seq_4_10 = time[0::9]
time_seq_8_5 = time[3::9]
time_seq_20_2 = time[6::9]

time_par_op1_4_10 = time[1::9]
time_par_op1_8_5 = time[4::9]
time_par_op1_20_2 = time[7::9]

time_par_op2_4_10 = time[2::9]
time_par_op2_8_5 = time[5::9]
time_par_op2_20_2 = time[8::9]

indices = (0, 1, 3, 6)
it_seq_4_10_1000 = [it_seq_4_10[i] for i in indices]
it_seq_8_5_1000 = [it_seq_8_5[i] for i in indices]
it_seq_20_2_1000 = [it_seq_20_2[i] for i in indices]
it_par_op1_4_10_1000 = [it_par_op1_4_10[i] for i in indices]
it_par_op1_8_5_1000 = [it_par_op1_8_5[i] for i in indices]
it_par_op1_20_2_1000 = [it_par_op1_20_2[i] for i in indices]
it_par_op2_4_10_1000 = [it_par_op2_4_10[i] for i in indices]
it_par_op2_8_5_1000 = [it_par_op2_8_5[i] for i in indices]
it_par_op2_20_2_1000 = [it_par_op2_20_2[i] for i in indices]
time_seq_4_10_1000 = [time_seq_4_10[i] for i in indices]
time_seq_8_5_1000 = [time_seq_8_5[i] for i in indices]
time_seq_20_2_1000 = [time_seq_20_2[i] for i in indices]
time_par_op1_4_10_1000 = [time_par_op1_4_10[i] for i in indices]
time_par_op1_8_5_1000 = [time_par_op1_8_5[i] for i in indices]
time_par_op1_20_2_1000 = [time_par_op1_20_2[i] for i in indices]
time_par_op2_4_10_1000 = [time_par_op2_4_10[i] for i in indices]
time_par_op2_8_5_1000 = [time_par_op2_8_5[i] for i in indices]
time_par_op2_20_2_1000 = [time_par_op2_20_2[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (2, 4, 7)
it_seq_4_10_4000 = [it_seq_4_10[i] for i in indices]
it_seq_8_5_4000 = [it_seq_8_5[i] for i in indices]
it_seq_20_2_4000 = [it_seq_20_2[i] for i in indices]
it_par_op1_4_10_4000 = [it_par_op1_4_10[i] for i in indices]
it_par_op1_8_5_4000 = [it_par_op1_8_5[i] for i in indices]
it_par_op1_20_2_4000 = [it_par_op1_20_2[i] for i in indices]
it_par_op2_4_10_4000 = [it_par_op2_4_10[i] for i in indices]
it_par_op2_8_5_4000 = [it_par_op2_8_5[i] for i in indices]
it_par_op2_20_2_4000 = [it_par_op2_20_2[i] for i in indices]
time_seq_4_10_4000 = [time_seq_4_10[i] for i in indices]
time_seq_8_5_4000 = [time_seq_8_5[i] for i in indices]
time_seq_20_2_4000 = [time_seq_20_2[i] for i in indices]
time_par_op1_4_10_4000 = [time_par_op1_4_10[i] for i in indices]
time_par_op1_8_5_4000 = [time_par_op1_8_5[i] for i in indices]
time_par_op1_20_2_4000 = [time_par_op1_20_2[i] for i in indices]
time_par_op2_4_10_4000 = [time_par_op2_4_10[i] for i in indices]
time_par_op2_8_5_4000 = [time_par_op2_8_5[i] for i in indices]
time_par_op2_20_2_4000 = [time_par_op2_20_2[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (5, 8)
it_seq_4_10_10000 = [it_seq_4_10[i] for i in indices]
it_seq_8_5_10000 = [it_seq_8_5[i] for i in indices]
it_seq_20_2_10000 = [it_seq_20_2[i] for i in indices]
it_par_op1_4_10_10000 = [it_par_op1_4_10[i] for i in indices]
it_par_op1_8_5_10000 = [it_par_op1_8_5[i] for i in indices]
it_par_op1_20_2_10000 = [it_par_op1_20_2[i] for i in indices]
it_par_op2_4_10_10000 = [it_par_op2_4_10[i] for i in indices]
it_par_op2_8_5_10000 = [it_par_op2_8_5[i] for i in indices]
it_par_op2_20_2_10000 = [it_par_op2_20_2[i] for i in indices]
time_seq_4_10_10000 = [time_seq_4_10[i] for i in indices]
time_seq_8_5_10000 = [time_seq_8_5[i] for i in indices]
time_seq_20_2_10000 = [time_seq_20_2[i] for i in indices]
time_par_op1_4_10_10000 = [time_par_op1_4_10[i] for i in indices]
time_par_op1_8_5_10000 = [time_par_op1_8_5[i] for i in indices]
time_par_op1_20_2_10000 = [time_par_op1_20_2[i] for i in indices]
time_par_op2_4_10_10000 = [time_par_op2_4_10[i] for i in indices]
time_par_op2_8_5_10000 = [time_par_op2_8_5[i] for i in indices]
time_par_op2_20_2_10000 = [time_par_op2_20_2[i] for i in indices]
x_10000 = [40000, 80000]

filename = "outputs/mpi_omp/RKA_mpi_omp_alpha_10000.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))
    it.append(float(lines[i].split()[3]))

it_seq_40_1_10000 = it[0::3]
it_par_op1_40_1_10000 = it[1::3]
it_par_op2_40_1_10000 = it[2::3]

time_seq_40_1_10000 = time[0::3]
time_par_op1_40_1_10000 = time[1::3]
time_par_op2_40_1_10000 = time[2::3]

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
plt.scatter(x_1000, time_seq_4_10_1000, color='orange')
plt.plot(x_1000, time_seq_4_10_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, time_seq_4_10_4000, color='red')
plt.plot(x_4000, time_seq_4_10_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, time_seq_4_10_10000, color='blue')
plt.plot(x_10000, time_seq_4_10_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.scatter(x_1000, time_par_op1_4_10_1000, color='orange')
plt.plot(x_1000, time_par_op1_4_10_1000, linestyle='--', linewidth=1.5, color='orange', label=r'Option 1 - $n = 1000$')
plt.scatter(x_4000, time_par_op1_4_10_4000, color='red')
plt.plot(x_4000, time_par_op1_4_10_4000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 4000$')
plt.scatter(x_10000, time_par_op1_4_10_10000, color='blue')
plt.plot(x_10000, time_par_op1_4_10_10000, linestyle='--', linewidth=1.5, color='blue', label=r'Option 1 - $n = 10000$')
plt.scatter(x_1000, time_par_op2_4_10_1000, color='orange')
plt.plot(x_1000, time_par_op2_4_10_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'Option 2 - $n = 1000$')
plt.scatter(x_4000, time_par_op2_4_10_4000, color='red')
plt.plot(x_4000, time_par_op2_4_10_4000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 4000$')
plt.scatter(x_10000, time_par_op2_4_10_10000, color='blue')
plt.plot(x_10000, time_par_op2_4_10_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'Option 2 - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_4_10"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_8_5_1000, color='orange')
plt.plot(x_1000, time_seq_8_5_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, time_seq_8_5_4000, color='red')
plt.plot(x_4000, time_seq_8_5_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, time_seq_8_5_10000, color='blue')
plt.plot(x_10000, time_seq_8_5_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.scatter(x_1000, time_par_op1_8_5_1000, color='orange')
plt.plot(x_1000, time_par_op1_8_5_1000, linestyle='--', linewidth=1.5, color='orange', label=r'Option 1 - $n = 1000$')
plt.scatter(x_4000, time_par_op1_8_5_4000, color='red')
plt.plot(x_4000, time_par_op1_8_5_4000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 4000$')
plt.scatter(x_10000, time_par_op1_8_5_10000, color='blue')
plt.plot(x_10000, time_par_op1_8_5_10000, linestyle='--', linewidth=1.5, color='blue', label=r'Option 1 - $n = 10000$')
plt.scatter(x_1000, time_par_op2_8_5_1000, color='orange')
plt.plot(x_1000, time_par_op2_8_5_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'Option 2 - $n = 1000$')
plt.scatter(x_4000, time_par_op2_8_5_4000, color='red')
plt.plot(x_4000, time_par_op2_8_5_4000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 4000$')
plt.scatter(x_10000, time_par_op2_8_5_10000, color='blue')
plt.plot(x_10000, time_par_op2_8_5_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'Option 2 - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_8_5"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_20_2_1000, color='orange')
plt.plot(x_1000, time_seq_20_2_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, time_seq_20_2_4000, color='red')
plt.plot(x_4000, time_seq_20_2_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, time_seq_20_2_10000, color='blue')
plt.plot(x_10000, time_seq_20_2_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.scatter(x_1000, time_par_op1_20_2_1000, color='orange')
plt.plot(x_1000, time_par_op1_20_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'Option 1 - $n = 1000$')
plt.scatter(x_4000, time_par_op1_20_2_4000, color='red')
plt.plot(x_4000, time_par_op1_20_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 4000$')
plt.scatter(x_10000, time_par_op1_20_2_10000, color='blue')
plt.plot(x_10000, time_par_op1_20_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'Option 1 - $n = 10000$')
plt.scatter(x_1000, time_par_op2_20_2_1000, color='orange')
plt.plot(x_1000, time_par_op2_20_2_1000, linestyle='-.', linewidth=1.5, color='orange', label=r'Option 2 - $n = 1000$')
plt.scatter(x_4000, time_par_op2_20_2_4000, color='red')
plt.plot(x_4000, time_par_op2_20_2_4000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 4000$')
plt.scatter(x_10000, time_par_op2_20_2_10000, color='blue')
plt.plot(x_10000, time_par_op2_20_2_10000, linestyle='-.', linewidth=1.5, color='blue', label=r'Option 2 - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_20_2"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_4_10_1000, color='red')
plt.plot(x_1000, time_seq_4_10_1000, linewidth=1.5, color='red', label=r'$n = 1000$')
plt.scatter(x_1000, time_par_op1_4_10_1000, color='red')
plt.plot(x_1000, time_par_op1_4_10_1000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 1000$')
plt.scatter(x_1000, time_par_op2_4_10_1000, color='red')
plt.plot(x_1000, time_par_op2_4_10_1000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_4_10_1000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_8_5_1000, color='red')
plt.plot(x_1000, time_seq_8_5_1000, linewidth=1.5, color='red', label=r'$n = 1000$')
plt.scatter(x_1000, time_par_op1_8_5_1000, color='red')
plt.plot(x_1000, time_par_op1_8_5_1000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 1000$')
plt.scatter(x_1000, time_par_op2_8_5_1000, color='red')
plt.plot(x_1000, time_par_op2_8_5_1000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_8_5_1000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_20_2_1000, color='red')
plt.plot(x_1000, time_seq_20_2_1000, linewidth=1.5, color='red', label=r'$n = 1000$')
plt.scatter(x_1000, time_par_op1_20_2_1000, color='red')
plt.plot(x_1000, time_par_op1_20_2_1000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 1000$')
plt.scatter(x_1000, time_par_op2_20_2_1000, color='red')
plt.plot(x_1000, time_par_op2_20_2_1000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_20_2_1000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, time_seq_4_10_4000, color='red')
plt.plot(x_4000, time_seq_4_10_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_4000, time_par_op1_4_10_4000, color='red')
plt.plot(x_4000, time_par_op1_4_10_4000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 4000$')
plt.scatter(x_4000, time_par_op2_4_10_4000, color='red')
plt.plot(x_4000, time_par_op2_4_10_4000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 4000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_4_10_4000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, time_seq_8_5_4000, color='red')
plt.plot(x_4000, time_seq_8_5_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_4000, time_par_op1_8_5_4000, color='red')
plt.plot(x_4000, time_par_op1_8_5_4000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 4000$')
plt.scatter(x_4000, time_par_op2_8_5_4000, color='red')
plt.plot(x_4000, time_par_op2_8_5_4000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 4000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_8_5_4000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, time_seq_20_2_4000, color='red')
plt.plot(x_4000, time_seq_20_2_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_4000, time_par_op1_20_2_4000, color='red')
plt.plot(x_4000, time_par_op1_20_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 4000$')
plt.scatter(x_4000, time_par_op2_20_2_4000, color='red')
plt.plot(x_4000, time_par_op2_20_2_4000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 4000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_20_2_4000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_seq_4_10_10000, color='red')
plt.plot(x_10000, time_seq_4_10_10000, linewidth=1.5, color='red', label=r'$n = 10000$')
plt.scatter(x_10000, time_par_op1_4_10_10000, color='red')
plt.plot(x_10000, time_par_op1_4_10_10000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 10000$')
plt.scatter(x_10000, time_par_op2_4_10_10000, color='red')
plt.plot(x_10000, time_par_op2_4_10_10000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_4_10_10000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_seq_8_5_10000, color='red')
plt.plot(x_10000, time_seq_8_5_10000, linewidth=1.5, color='red', label=r'$n = 10000$')
plt.scatter(x_10000, time_par_op1_8_5_10000, color='red')
plt.plot(x_10000, time_par_op1_8_5_10000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 10000$')
plt.scatter(x_10000, time_par_op2_8_5_10000, color='red')
plt.plot(x_10000, time_par_op2_8_5_10000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_8_5_10000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_seq_20_2_10000, color='red')
plt.plot(x_10000, time_seq_20_2_10000, linewidth=1.5, color='red', label=r'$n = 10000$')
plt.scatter(x_10000, time_par_op1_20_2_10000, color='red')
plt.plot(x_10000, time_par_op1_20_2_10000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 10000$')
plt.scatter(x_10000, time_par_op2_20_2_10000, color='red')
plt.plot(x_10000, time_par_op2_20_2_10000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_20_2_10000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, time_seq_40_1_10000, color='red')
plt.plot(x_10000, time_seq_40_1_10000, linewidth=1.5, color='red', label=r'$n = 10000$')
plt.scatter(x_10000, time_par_op1_40_1_10000, color='red')
plt.plot(x_10000, time_par_op1_40_1_10000, linestyle='--', linewidth=1.5, color='red', label=r'Option 1 - $n = 10000$')
plt.scatter(x_10000, time_par_op2_40_1_10000, color='red')
plt.plot(x_10000, time_par_op2_40_1_10000, linestyle='-.', linewidth=1.5, color='red', label=r'Option 2 - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_40_1_10000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000_10000, time_seq_80000_10000, color='orange')
plt.plot(x_80000_10000, time_seq_80000_10000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_10000, time_par_op1_80000_10000, color='red')
plt.plot(x_80000_10000, time_par_op1_80000_10000, linewidth=1.5, color='red', label=r'1 Task per node')
plt.scatter(x_80000_10000, time_par_op2_80000_10000, color='blue')
plt.plot(x_80000_10000, time_par_op2_80000_10000, linewidth=1.5, color='blue', label=r'2 Tasks per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Tasks')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_options_40_mpi_time_80000_10000"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')