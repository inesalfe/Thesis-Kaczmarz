import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi_omp/RKAB_options_40_extra.py

filename = "outputs/mpi_omp/RKAB_40_tasks.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))
    it.append(float(lines[i].split()[3]))

indices = (0, 3, 6, 9)
time_seq_80000_1000 = [time[i] for i in indices]
time_par_op1_80000_1000 = [time[i+1] for i in indices]
time_par_op2_80000_1000 = [time[i+2] for i in indices]
it_seq_80000_1000 = [it[i] for i in indices]
it_par_op1_80000_1000 = [it[i+1] for i in indices]
it_par_op2_80000_1000 = [it[i+2] for i in indices]
x_80000_1000 = [4, 8, 20, 40]

indices = (15, 18, 21, 24)
time_seq_80000_10000 = [time[i] for i in indices]
time_par_op1_80000_10000 = [time[i+1] for i in indices]
time_par_op2_80000_10000 = [time[i+2] for i in indices]
it_seq_80000_10000 = [it[i] for i in indices]
it_par_op1_80000_10000 = [it[i+1] for i in indices]
it_par_op2_80000_10000 = [it[i+2] for i in indices]
x_80000_10000 = [4, 8, 20, 40]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000_1000, time_seq_80000_1000, color='orange')
plt.plot(x_80000_1000, time_seq_80000_1000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_1000, time_par_op1_80000_1000, color='red')
plt.plot(x_80000_1000, time_par_op1_80000_1000, linewidth=1.5, color='red', label=r'1 Process per node')
plt.scatter(x_80000_1000, time_par_op2_80000_1000, color='blue')
plt.plot(x_80000_1000, time_par_op2_80000_1000, linewidth=1.5, color='blue', label=r'2 Processes per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# plt.xlabel(r'Processes')
plt.ylabel(r'Total Time (s)')
labels = [r'\hspace{-0.45cm}4 Processses\\(10 Threads)', r'\hspace{-0.45cm}8 Processses\\(5 Threads)', r'\hspace{-0.55cm}20 Processses\\(2 Threads)', r'\hspace{-0.6cm}40 Processses\\(1 Thread)']
plt.xticks(x_80000_1000, labels)

filename_fig = "RKAB_options_40_extra_mpi_time_80000_1000_1"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000_1000, it_seq_80000_1000, color='orange')
plt.plot(x_80000_1000, it_seq_80000_1000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_1000, it_par_op1_80000_1000, color='red')
plt.plot(x_80000_1000, it_par_op1_80000_1000, linewidth=1.5, color='red', label=r'1 Process per node')
plt.scatter(x_80000_1000, it_par_op2_80000_1000, color='blue')
plt.plot(x_80000_1000, it_par_op2_80000_1000, linewidth=1.5, color='blue', label=r'2 Processes per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# plt.xlabel(r'Processes')
plt.ylabel(r'Iterations')
labels = [r'\hspace{-0.45cm}4 Processses\\(10 Threads)', r'\hspace{-0.45cm}8 Processses\\(5 Threads)', r'\hspace{-0.55cm}20 Processses\\(2 Threads)', r'\hspace{-0.6cm}40 Processses\\(1 Thread)']
plt.xticks(x_80000_1000, labels)

filename_fig = "RKAB_options_40_extra_mpi_it_80000_1000_1"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000_10000, time_seq_80000_10000, color='orange')
plt.plot(x_80000_10000, time_seq_80000_10000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_10000, time_par_op1_80000_10000, color='red')
plt.plot(x_80000_10000, time_par_op1_80000_10000, linewidth=1.5, color='red', label=r'1 Process per node')
plt.scatter(x_80000_10000, time_par_op2_80000_10000, color='blue')
plt.plot(x_80000_10000, time_par_op2_80000_10000, linewidth=1.5, color='blue', label=r'2 Processes per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# plt.xlabel(r'Processes')
plt.ylabel(r'Total Time (s)')
labels = [r'\hspace{-0.45cm}4 Processses\\(10 Threads)', r'\hspace{-0.45cm}8 Processses\\(5 Threads)', r'\hspace{-0.55cm}20 Processses\\(2 Threads)', r'\hspace{-0.6cm}40 Processses\\(1 Thread)']
plt.xticks(x_80000_10000, labels)

filename_fig = "RKAB_options_40_extra_mpi_time_80000_10000_1"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000_10000, it_seq_80000_10000, color='orange')
plt.plot(x_80000_10000, it_seq_80000_10000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_10000, it_par_op1_80000_10000, color='red')
plt.plot(x_80000_10000, it_par_op1_80000_10000, linewidth=1.5, color='red', label=r'1 Process per node')
plt.scatter(x_80000_10000, it_par_op2_80000_10000, color='blue')
plt.plot(x_80000_10000, it_par_op2_80000_10000, linewidth=1.5, color='blue', label=r'2 Processes per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# plt.xlabel(r'Processes')
plt.ylabel(r'Iterations')
labels = [r'\hspace{-0.45cm}4 Processses\\(10 Threads)', r'\hspace{-0.45cm}8 Processses\\(5 Threads)', r'\hspace{-0.55cm}20 Processses\\(2 Threads)', r'\hspace{-0.6cm}40 Processses\\(1 Thread)']
plt.xticks(x_80000_10000, labels)

filename_fig = "RKAB_options_40_extra_mpi_it_80000_10000_1"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

filename = "outputs/mpi_omp/RKAB_40_tasks.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))
    it.append(float(lines[i].split()[3]))

indices = (0, 3, 6, 12)
time_seq_80000_1000 = [time[i] for i in indices]
time_par_op1_80000_1000 = [time[i+1] for i in indices]
time_par_op2_80000_1000 = [time[i+2] for i in indices]
it_seq_80000_1000 = [it[i] for i in indices]
it_par_op1_80000_1000 = [it[i+1] for i in indices]
it_par_op2_80000_1000 = [it[i+2] for i in indices]
x_80000_1000 = [4, 8, 20, 40]

indices = (15, 18, 21, 27)
time_seq_80000_10000 = [time[i] for i in indices]
time_par_op1_80000_10000 = [time[i+1] for i in indices]
time_par_op2_80000_10000 = [time[i+2] for i in indices]
it_seq_80000_10000 = [it[i] for i in indices]
it_par_op1_80000_10000 = [it[i+1] for i in indices]
it_par_op2_80000_10000 = [it[i+2] for i in indices]
x_80000_10000 = [4, 8, 20, 40]

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
plt.scatter(x_80000_1000, time_seq_80000_1000, color='orange')
plt.plot(x_80000_1000, time_seq_80000_1000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_1000, time_par_op1_80000_1000, color='red')
plt.plot(x_80000_1000, time_par_op1_80000_1000, linewidth=1.5, color='red', label=r'1 Process per node')
plt.scatter(x_80000_1000, time_par_op2_80000_1000, color='blue')
plt.plot(x_80000_1000, time_par_op2_80000_1000, linewidth=1.5, color='blue', label=r'2 Processes per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# plt.xlabel(r'Processes')
plt.ylabel(r'Total Time (s)')
labels = [r'\hspace{-0.45cm}4 Processses\\(10 Threads)', r'\hspace{-0.45cm}8 Processses\\(5 Threads)', r'\hspace{-0.55cm}20 Processses\\(2 Threads)', r'\hspace{-0.6cm}40 Processses\\(1 Thread)']
plt.xticks(x_80000_1000, labels)

filename_fig = "RKAB_options_40_extra_mpi_time_80000_1000_2"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000_1000, it_seq_80000_1000, color='orange')
plt.plot(x_80000_1000, it_seq_80000_1000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_1000, it_par_op1_80000_1000, color='red')
plt.plot(x_80000_1000, it_par_op1_80000_1000, linewidth=1.5, color='red', label=r'1 Process per node')
plt.scatter(x_80000_1000, it_par_op2_80000_1000, color='blue')
plt.plot(x_80000_1000, it_par_op2_80000_1000, linewidth=1.5, color='blue', label=r'2 Processes per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# plt.xlabel(r'Processes')
plt.ylabel(r'Iterations')
labels = [r'\hspace{-0.45cm}4 Processses\\(10 Threads)', r'\hspace{-0.45cm}8 Processses\\(5 Threads)', r'\hspace{-0.55cm}20 Processses\\(2 Threads)', r'\hspace{-0.6cm}40 Processses\\(1 Thread)']
plt.xticks(x_80000_1000, labels)

filename_fig = "RKAB_options_40_extra_mpi_it_80000_1000_2"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000_10000, time_seq_80000_10000, color='orange')
plt.plot(x_80000_10000, time_seq_80000_10000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_10000, time_par_op1_80000_10000, color='red')
plt.plot(x_80000_10000, time_par_op1_80000_10000, linewidth=1.5, color='red', label=r'1 Process per node')
plt.scatter(x_80000_10000, time_par_op2_80000_10000, color='blue')
plt.plot(x_80000_10000, time_par_op2_80000_10000, linewidth=1.5, color='blue', label=r'2 Processes per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# plt.xlabel(r'Processes')
plt.ylabel(r'Total Time (s)')
labels = [r'\hspace{-0.45cm}4 Processses\\(10 Threads)', r'\hspace{-0.45cm}8 Processses\\(5 Threads)', r'\hspace{-0.55cm}20 Processses\\(2 Threads)', r'\hspace{-0.6cm}40 Processses\\(1 Thread)']
plt.xticks(x_80000_10000, labels)

filename_fig = "RKAB_options_40_extra_mpi_time_80000_10000_2"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000_10000, it_seq_80000_10000, color='orange')
plt.plot(x_80000_10000, it_seq_80000_10000, linewidth=1.5, color='orange', label=r'Sequential')
plt.scatter(x_80000_10000, it_par_op1_80000_10000, color='red')
plt.plot(x_80000_10000, it_par_op1_80000_10000, linewidth=1.5, color='red', label=r'1 Process per node')
plt.scatter(x_80000_10000, it_par_op2_80000_10000, color='blue')
plt.plot(x_80000_10000, it_par_op2_80000_10000, linewidth=1.5, color='blue', label=r'2 Processes per node')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# plt.xlabel(r'Processes')
plt.ylabel(r'Iterations')
labels = [r'\hspace{-0.45cm}4 Processses\\(10 Threads)', r'\hspace{-0.45cm}8 Processses\\(5 Threads)', r'\hspace{-0.55cm}20 Processses\\(2 Threads)', r'\hspace{-0.6cm}40 Processses\\(1 Thread)']
plt.xticks(x_80000_10000, labels)

filename_fig = "RKAB_options_40_extra_mpi_it_80000_10000_2"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')