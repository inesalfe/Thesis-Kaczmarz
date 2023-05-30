import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi_omp/RKA_speedup_seq.py

filename = "outputs/mpi_omp/RKA_mpi_omp_alpha.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))

time_seq_2 = time[0::24]
time_seq_10 = time[3::24]
time_seq_4 = time[6::24]
time_seq_20 = time[9::24]
time_seq_8 = time[12::24]
time_seq_40 = time[15::24]
time_seq_16 = time[18::24]
time_seq_80 = time[21::24]

time_par_op1_2 = time[1::24]
time_par_op1_10 = time[4::24]
time_par_op1_4 = time[7::24]
time_par_op1_20 = time[10::24]
time_par_op1_8 = time[13::24]
time_par_op1_40 = time[16::24]
time_par_op1_16 = time[19::24]
time_par_op1_80 = time[22::24]

time_par_op2_2 = time[2::24]
time_par_op2_10 = time[5::24]
time_par_op2_4 = time[8::24]
time_par_op2_20 = time[11::24]
time_par_op2_8 = time[14::24]
time_par_op2_40 = time[17::24]
time_par_op2_16 = time[20::24]
time_par_op2_80 = time[23::24]

indices = (0, 1, 3, 6)
time_seq_2_1000 = [time_seq_2[i] for i in indices]
time_seq_4_1000 = [time_seq_4[i] for i in indices]
time_seq_8_1000 = [time_seq_8[i] for i in indices]
time_seq_16_1000 = [time_seq_16[i] for i in indices]
time_seq_10_1000 = [time_seq_10[i] for i in indices]
time_seq_20_1000 = [time_seq_20[i] for i in indices]
time_seq_40_1000 = [time_seq_40[i] for i in indices]
time_seq_80_1000 = [time_seq_80[i] for i in indices]
time_par_op1_2_1000 = [time_par_op1_2[i] for i in indices]
time_par_op1_4_1000 = [time_par_op1_4[i] for i in indices]
time_par_op1_8_1000 = [time_par_op1_8[i] for i in indices]
time_par_op1_16_1000 = [time_par_op1_16[i] for i in indices]
time_par_op1_10_1000 = [time_par_op1_10[i] for i in indices]
time_par_op1_20_1000 = [time_par_op1_20[i] for i in indices]
time_par_op1_40_1000 = [time_par_op1_40[i] for i in indices]
time_par_op1_80_1000 = [time_par_op1_80[i] for i in indices]
time_par_op2_2_1000 = [time_par_op2_2[i] for i in indices]
time_par_op2_4_1000 = [time_par_op2_4[i] for i in indices]
time_par_op2_8_1000 = [time_par_op2_8[i] for i in indices]
time_par_op2_16_1000 = [time_par_op2_16[i] for i in indices]
time_par_op2_10_1000 = [time_par_op2_10[i] for i in indices]
time_par_op2_20_1000 = [time_par_op2_20[i] for i in indices]
time_par_op2_40_1000 = [time_par_op2_40[i] for i in indices]
time_par_op2_80_1000 = [time_par_op2_80[i] for i in indices]
speedup_2_1000 = [time_seq_2[i]/time_par_op1_2[i] for i in indices]
speedup_4_1000 = [time_seq_4[i]/time_par_op1_4[i] for i in indices]
speedup_8_1000 = [time_seq_8[i]/time_par_op1_8[i] for i in indices]
speedup_16_1000 = [time_seq_16[i]/time_par_op1_16[i] for i in indices]
speedup_10_1000 = [time_seq_10[i]/time_par_op1_10[i] for i in indices]
speedup_20_1000 = [time_seq_20[i]/time_par_op1_20[i] for i in indices]
speedup_40_1000 = [time_seq_40[i]/time_par_op1_40[i] for i in indices]
speedup_80_1000 = [time_seq_80[i]/time_par_op1_80[i] for i in indices]
# speedup_2_1000 = [time_seq_2[i]/time_par_op2_2[i] for i in indices]
# speedup_4_1000 = [time_seq_4[i]/time_par_op2_4[i] for i in indices]
# speedup_8_1000 = [time_seq_8[i]/time_par_op2_8[i] for i in indices]
# speedup_16_1000 = [time_seq_16[i]/time_par_op2_16[i] for i in indices]
# speedup_10_1000 = [time_seq_10[i]/time_par_op2_10[i] for i in indices]
# speedup_20_1000 = [time_seq_20[i]/time_par_op2_20[i] for i in indices]
# speedup_40_1000 = [time_seq_40[i]/time_par_op2_40[i] for i in indices]
# speedup_80_1000 = [time_seq_80[i]/time_par_op2_80[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (2, 4, 7)
time_seq_2_4000 = [time_seq_2[i] for i in indices]
time_seq_4_4000 = [time_seq_4[i] for i in indices]
time_seq_8_4000 = [time_seq_8[i] for i in indices]
time_seq_16_4000 = [time_seq_16[i] for i in indices]
time_seq_10_4000 = [time_seq_10[i] for i in indices]
time_seq_20_4000 = [time_seq_20[i] for i in indices]
time_seq_40_4000 = [time_seq_40[i] for i in indices]
time_seq_80_4000 = [time_seq_80[i] for i in indices]
time_par_op1_2_4000 = [time_par_op1_2[i] for i in indices]
time_par_op1_4_4000 = [time_par_op1_4[i] for i in indices]
time_par_op1_8_4000 = [time_par_op1_8[i] for i in indices]
time_par_op1_16_4000 = [time_par_op1_16[i] for i in indices]
time_par_op1_10_4000 = [time_par_op1_10[i] for i in indices]
time_par_op1_20_4000 = [time_par_op1_20[i] for i in indices]
time_par_op1_40_4000 = [time_par_op1_40[i] for i in indices]
time_par_op1_80_4000 = [time_par_op1_80[i] for i in indices]
time_par_op2_2_4000 = [time_par_op2_2[i] for i in indices]
time_par_op2_4_4000 = [time_par_op2_4[i] for i in indices]
time_par_op2_8_4000 = [time_par_op2_8[i] for i in indices]
time_par_op2_16_4000 = [time_par_op2_16[i] for i in indices]
time_par_op2_10_4000 = [time_par_op2_10[i] for i in indices]
time_par_op2_20_4000 = [time_par_op2_20[i] for i in indices]
time_par_op2_40_4000 = [time_par_op2_40[i] for i in indices]
time_par_op2_80_4000 = [time_par_op2_80[i] for i in indices]
speedup_2_4000 = [time_seq_2[i]/time_par_op1_2[i] for i in indices]
speedup_4_4000 = [time_seq_4[i]/time_par_op1_4[i] for i in indices]
speedup_8_4000 = [time_seq_8[i]/time_par_op1_8[i] for i in indices]
speedup_16_4000 = [time_seq_16[i]/time_par_op1_16[i] for i in indices]
speedup_10_4000 = [time_seq_10[i]/time_par_op1_10[i] for i in indices]
speedup_20_4000 = [time_seq_20[i]/time_par_op1_20[i] for i in indices]
speedup_40_4000 = [time_seq_40[i]/time_par_op1_40[i] for i in indices]
speedup_80_4000 = [time_seq_80[i]/time_par_op1_80[i] for i in indices]
# speedup_2_4000 = [time_seq_2[i]/time_par_op2_2[i] for i in indices]
# speedup_4_4000 = [time_seq_4[i]/time_par_op2_4[i] for i in indices]
# speedup_8_4000 = [time_seq_8[i]/time_par_op2_8[i] for i in indices]
# speedup_16_4000 = [time_seq_16[i]/time_par_op2_16[i] for i in indices]
# speedup_10_4000 = [time_seq_10[i]/time_par_op2_10[i] for i in indices]
# speedup_20_4000 = [time_seq_20[i]/time_par_op2_20[i] for i in indices]
# speedup_40_4000 = [time_seq_40[i]/time_par_op2_40[i] for i in indices]
# speedup_80_4000 = [time_seq_80[i]/time_par_op2_80[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (5, 8)
time_seq_2_10000 = [time_seq_2[i] for i in indices]
time_seq_4_10000 = [time_seq_4[i] for i in indices]
time_seq_8_10000 = [time_seq_8[i] for i in indices]
time_seq_16_10000 = [time_seq_16[i] for i in indices]
time_seq_10_10000 = [time_seq_10[i] for i in indices]
time_seq_20_10000 = [time_seq_20[i] for i in indices]
time_seq_40_10000 = [time_seq_40[i] for i in indices]
time_seq_80_10000 = [time_seq_80[i] for i in indices]
time_par_op1_2_10000 = [time_par_op1_2[i] for i in indices]
time_par_op1_4_10000 = [time_par_op1_4[i] for i in indices]
time_par_op1_8_10000 = [time_par_op1_8[i] for i in indices]
time_par_op1_16_10000 = [time_par_op1_16[i] for i in indices]
time_par_op1_10_10000 = [time_par_op1_10[i] for i in indices]
time_par_op1_20_10000 = [time_par_op1_20[i] for i in indices]
time_par_op1_40_10000 = [time_par_op1_40[i] for i in indices]
time_par_op1_80_10000 = [time_par_op1_80[i] for i in indices]
time_par_op2_2_10000 = [time_par_op2_2[i] for i in indices]
time_par_op2_4_10000 = [time_par_op2_4[i] for i in indices]
time_par_op2_8_10000 = [time_par_op2_8[i] for i in indices]
time_par_op2_16_10000 = [time_par_op2_16[i] for i in indices]
time_par_op2_10_10000 = [time_par_op2_10[i] for i in indices]
time_par_op2_20_10000 = [time_par_op2_20[i] for i in indices]
time_par_op2_40_10000 = [time_par_op2_40[i] for i in indices]
time_par_op2_80_10000 = [time_par_op2_80[i] for i in indices]
speedup_2_10000 = [time_seq_2[i]/time_par_op1_2[i] for i in indices]
speedup_4_10000 = [time_seq_4[i]/time_par_op1_4[i] for i in indices]
speedup_8_10000 = [time_seq_8[i]/time_par_op1_8[i] for i in indices]
speedup_16_10000 = [time_seq_16[i]/time_par_op1_16[i] for i in indices]
speedup_10_10000 = [time_seq_10[i]/time_par_op1_10[i] for i in indices]
speedup_20_10000 = [time_seq_20[i]/time_par_op1_20[i] for i in indices]
speedup_40_10000 = [time_seq_40[i]/time_par_op1_40[i] for i in indices]
speedup_80_10000 = [time_seq_80[i]/time_par_op1_80[i] for i in indices]
# speedup_2_10000 = [time_seq_2[i]/time_par_op2_2[i] for i in indices]
# speedup_4_10000 = [time_seq_4[i]/time_par_op2_4[i] for i in indices]
# speedup_8_10000 = [time_seq_8[i]/time_par_op2_8[i] for i in indices]
# speedup_16_10000 = [time_seq_16[i]/time_par_op2_16[i] for i in indices]
# speedup_10_10000 = [time_seq_10[i]/time_par_op2_10[i] for i in indices]
# speedup_20_10000 = [time_seq_20[i]/time_par_op2_20[i] for i in indices]
# speedup_40_10000 = [time_seq_40[i]/time_par_op2_40[i] for i in indices]
# speedup_80_10000 = [time_seq_80[i]/time_par_op2_80[i] for i in indices]
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

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_2_1000, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_2_4000, color='red')
plt.plot(x_4000, speedup_2_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_2_10000, color='blue')
plt.plot(x_10000, speedup_2_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_speedup_seq_mpi_speedup_2"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_4_1000, color='orange')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_4_4000, color='red')
plt.plot(x_4000, speedup_4_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_4_10000, color='blue')
plt.plot(x_10000, speedup_4_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_speedup_seq_mpi_speedup_4"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_8_1000, color='orange')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_8_4000, color='red')
plt.plot(x_4000, speedup_8_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_8_10000, color='blue')
plt.plot(x_10000, speedup_8_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_speedup_seq_mpi_speedup_8"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_16_1000, color='orange')
plt.plot(x_1000, speedup_16_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_16_4000, color='red')
plt.plot(x_4000, speedup_16_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_16_10000, color='blue')
plt.plot(x_10000, speedup_16_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_speedup_seq_mpi_speedup_16"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_10_1000, color='orange')
plt.plot(x_1000, speedup_10_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_10_4000, color='red')
plt.plot(x_4000, speedup_10_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_10_10000, color='blue')
plt.plot(x_10000, speedup_10_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_speedup_seq_mpi_speedup_10"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_20_1000, color='orange')
plt.plot(x_1000, speedup_20_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_20_4000, color='red')
plt.plot(x_4000, speedup_20_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_20_10000, color='blue')
plt.plot(x_10000, speedup_20_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_speedup_seq_mpi_speedup_20"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_40_1000, color='orange')
plt.plot(x_1000, speedup_40_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_40_4000, color='red')
plt.plot(x_4000, speedup_40_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_40_10000, color='blue')
plt.plot(x_10000, speedup_40_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_speedup_seq_mpi_speedup_40"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_80_1000, color='orange')
plt.plot(x_1000, speedup_80_1000, linewidth=1.5, color='orange', label=r'$n = 1000$')
plt.scatter(x_4000, speedup_80_4000, color='red')
plt.plot(x_4000, speedup_80_4000, linewidth=1.5, color='red', label=r'$n = 4000$')
plt.scatter(x_10000, speedup_80_10000, color='blue')
plt.plot(x_10000, speedup_80_10000, linewidth=1.5, color='blue', label=r'$n = 10000$')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_speedup_seq_mpi_speedup_80"

# plt.show()
fig.savefig("plots/mpi_omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi_omp/png/"+filename_fig+".png", bbox_inches='tight')