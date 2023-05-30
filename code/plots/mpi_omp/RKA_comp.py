import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi_omp/RKA_comp.py

filename = "outputs/mpi_omp/RKA_mpi_omp_alpha.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))

time_par_2 = time[1::24]
time_par_10 = time[4::24]
time_par_4 = time[7::24]
time_par_20 = time[10::24]
time_par_8 = time[13::24]
time_par_40 = time[16::24]
time_par_16 = time[19::24]
time_par_80 = time[22::24]

# time_par_2 = time[2::24]
# time_par_10 = time[5::24]
# time_par_4 = time[8::24]
# time_par_20 = time[11::24]
# time_par_8 = time[14::24]
# time_par_40 = time[17::24]
# time_par_16 = time[20::24]
# time_par_80 = time[23::24]

indices = (0, 1, 3, 6)
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
time_par_16_1000 = [time_par_16[i] for i in indices]
time_par_10_1000 = [time_par_10[i] for i in indices]
time_par_20_1000 = [time_par_20[i] for i in indices]
time_par_40_1000 = [time_par_40[i] for i in indices]
time_par_80_1000 = [time_par_80[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (2, 4, 7)
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
time_par_16_4000 = [time_par_16[i] for i in indices]
time_par_10_4000 = [time_par_10[i] for i in indices]
time_par_20_4000 = [time_par_20[i] for i in indices]
time_par_40_4000 = [time_par_40[i] for i in indices]
time_par_80_4000 = [time_par_80[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (5, 8)
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
time_par_16_10000 = [time_par_16[i] for i in indices]
time_par_10_10000 = [time_par_10[i] for i in indices]
time_par_20_10000 = [time_par_20[i] for i in indices]
time_par_40_10000 = [time_par_40[i] for i in indices]
time_par_80_10000 = [time_par_80[i] for i in indices]
x_10000 = [40000, 80000]

filename = "outputs/mpi/RKA_mpi_alpha.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))

time_par_mpi_1 = time[1::20]
time_par_mpi_2 = time[5::20]
time_par_mpi_4 = time[9::20]
time_par_mpi_8 = time[13::20]
time_par_mpi_20 = time[17::20]

indices = (0, 1, 3, 6)
time_par_mpi_1_1000 = [time_par_mpi_1[i] for i in indices]
time_par_mpi_2_1000 = [time_par_mpi_2[i] for i in indices]
time_par_mpi_4_1000 = [time_par_mpi_4[i] for i in indices]
time_par_mpi_8_1000 = [time_par_mpi_8[i] for i in indices]
time_par_mpi_20_1000 = [time_par_mpi_20[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (2, 4, 7)
time_par_mpi_1_4000 = [time_par_mpi_1[i] for i in indices]
time_par_mpi_2_4000 = [time_par_mpi_2[i] for i in indices]
time_par_mpi_4_4000 = [time_par_mpi_4[i] for i in indices]
time_par_mpi_8_4000 = [time_par_mpi_8[i] for i in indices]
time_par_mpi_20_4000 = [time_par_mpi_20[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (5, 8)
time_par_mpi_1_10000 = [time_par_mpi_1[i] for i in indices]
time_par_mpi_2_10000 = [time_par_mpi_2[i] for i in indices]
time_par_mpi_4_10000 = [time_par_mpi_4[i] for i in indices]
time_par_mpi_8_10000 = [time_par_mpi_8[i] for i in indices]
time_par_mpi_20_10000 = [time_par_mpi_20[i] for i in indices]
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

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linewidth=1.5, color='orange', label=r'2 MPI + OpenMP Processes - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000, color='red')
plt.plot(x_4000, time_par_2_4000, linewidth=1.5, color='red', label=r'2 MPI + OpenMP Processes - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000, color='blue')
plt.plot(x_10000, time_par_2_10000, linewidth=1.5, color='blue', label=r'2 MPI + OpenMP Processes - $n = 10000$')
plt.scatter(x_1000, time_par_mpi_2_1000, color='orange')
plt.plot(x_1000, time_par_mpi_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'2 MPI Processes - $n = 1000$')
plt.scatter(x_4000, time_par_mpi_2_4000, color='red')
plt.plot(x_4000, time_par_mpi_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'2 MPI Processes - $n = 4000$')
plt.scatter(x_10000, time_par_mpi_2_10000, color='blue')
plt.plot(x_10000, time_par_mpi_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'2 MPI Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_comp_time_2"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_4_1000, color='orange')
plt.plot(x_1000, time_par_4_1000, linewidth=1.5, color='orange', label=r'4 MPI + OpenMP Processes - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000, color='red')
plt.plot(x_4000, time_par_4_4000, linewidth=1.5, color='red', label=r'4 MPI + OpenMP Processes - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000, color='blue')
plt.plot(x_10000, time_par_4_10000, linewidth=1.5, color='blue', label=r'4 MPI + OpenMP Processes - $n = 10000$')
plt.scatter(x_1000, time_par_mpi_4_1000, color='orange')
plt.plot(x_1000, time_par_mpi_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'4 MPI Processes - $n = 1000$')
plt.scatter(x_4000, time_par_mpi_4_4000, color='red')
plt.plot(x_4000, time_par_mpi_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'4 MPI Processes - $n = 4000$')
plt.scatter(x_10000, time_par_mpi_4_10000, color='blue')
plt.plot(x_10000, time_par_mpi_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'4 MPI Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_comp_time_4"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_8_1000, color='orange')
plt.plot(x_1000, time_par_8_1000, linewidth=1.5, color='orange', label=r'4 MPI + OpenMP Processes - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000, color='red')
plt.plot(x_4000, time_par_8_4000, linewidth=1.5, color='red', label=r'4 MPI + OpenMP Processes - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000, color='blue')
plt.plot(x_10000, time_par_8_10000, linewidth=1.5, color='blue', label=r'4 MPI + OpenMP Processes - $n = 10000$')
plt.scatter(x_1000, time_par_mpi_8_1000, color='orange')
plt.plot(x_1000, time_par_mpi_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'4 MPI Processes - $n = 1000$')
plt.scatter(x_4000, time_par_mpi_8_4000, color='red')
plt.plot(x_4000, time_par_mpi_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'4 MPI Processes - $n = 4000$')
plt.scatter(x_10000, time_par_mpi_8_10000, color='blue')
plt.plot(x_10000, time_par_mpi_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'4 MPI Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_comp_time_8"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_20_1000, color='orange')
plt.plot(x_1000, time_par_20_1000, linewidth=1.5, color='orange', label=r'4 MPI + OpenMP Processes - $n = 1000$')
plt.scatter(x_4000, time_par_20_4000, color='red')
plt.plot(x_4000, time_par_20_4000, linewidth=1.5, color='red', label=r'4 MPI + OpenMP Processes - $n = 4000$')
plt.scatter(x_10000, time_par_20_10000, color='blue')
plt.plot(x_10000, time_par_20_10000, linewidth=1.5, color='blue', label=r'4 MPI + OpenMP Processes - $n = 10000$')
plt.scatter(x_1000, time_par_mpi_20_1000, color='orange')
plt.plot(x_1000, time_par_mpi_20_1000, linestyle='--', linewidth=1.5, color='orange', label=r'4 MPI Processes - $n = 1000$')
plt.scatter(x_4000, time_par_mpi_20_4000, color='red')
plt.plot(x_4000, time_par_mpi_20_4000, linestyle='--', linewidth=1.5, color='red', label=r'4 MPI Processes - $n = 4000$')
plt.scatter(x_10000, time_par_mpi_20_10000, color='blue')
plt.plot(x_10000, time_par_mpi_20_10000, linestyle='--', linewidth=1.5, color='blue', label=r'4 MPI Processes - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_comp_time_20"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')