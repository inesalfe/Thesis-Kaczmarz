import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKA_seq_uni_N_alpha.py

filename = "outputs/omp/RK_seq_uni.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
it_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))
	it_seq.append(float(lines[i].split()[3]))

filename = "outputs/omp/RKA_uni_alpha.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(float(lines[i].split()[3]))

it_seq_RKA = it[0::8]
it_par_RKA = it[1::8]
time_seq_RKA = time[0::8]
time_par_RKA = time[1::8]

it_seq_1 = it_seq_RKA[0::4]
it_seq_2 = it_seq_RKA[1::4]
it_seq_4 = it_seq_RKA[2::4]
it_seq_8 = it_seq_RKA[3::4]

it_par_1 = it_par_RKA[0::4]
it_par_2 = it_par_RKA[1::4]
it_par_4 = it_par_RKA[2::4]
it_par_8 = it_par_RKA[3::4]

time_seq_1 = time_seq_RKA[0::4]
time_seq_2 = time_seq_RKA[1::4]
time_seq_4 = time_seq_RKA[2::4]
time_seq_8 = time_seq_RKA[3::4]

time_par_1 = time_par_RKA[0::4]
time_par_2 = time_par_RKA[1::4]
time_par_4 = time_par_RKA[2::4]
time_par_8 = time_par_RKA[3::4]

indices = (10, 16, 24, 33)
it_seq_1_1000 = [it_seq_1[i] for i in indices]
it_seq_2_1000 = [it_seq_2[i] for i in indices]
it_seq_4_1000 = [it_seq_4[i] for i in indices]
it_seq_8_1000 = [it_seq_8[i] for i in indices]
time_seq_1_1000 = [time_seq_1[i] for i in indices]
time_seq_2_1000 = [time_seq_2[i] for i in indices]
time_seq_4_1000 = [time_seq_4[i] for i in indices]
time_seq_8_1000 = [time_seq_8[i] for i in indices]
it_seq_1000 = [it_seq[i] for i in indices]
time_seq_1000 = [time_seq[i] for i in indices]
it_par_1_1000 = [it_par_1[i] for i in indices]
it_par_2_1000 = [it_par_2[i] for i in indices]
it_par_4_1000 = [it_par_4[i] for i in indices]
it_par_8_1000 = [it_par_8[i] for i in indices]
total_lines_par_1_1000 = [it_par_1[i] for i in indices]
total_lines_par_2_1000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_1000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_1000 = [8*it_par_8[i] for i in indices]
time_par_1_1000 = [time_par_1[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
speedup_2_1000 = [time_seq[i]/time_par_2[i] for i in indices]
speedup_4_1000 = [time_seq[i]/time_par_4[i] for i in indices]
speedup_8_1000 = [time_seq[i]/time_par_8[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (18, 26, 35)
it_seq_1_4000 = [it_seq_1[i] for i in indices]
it_seq_2_4000 = [it_seq_2[i] for i in indices]
it_seq_4_4000 = [it_seq_4[i] for i in indices]
it_seq_8_4000 = [it_seq_8[i] for i in indices]
time_seq_1_4000 = [time_seq_1[i] for i in indices]
time_seq_2_4000 = [time_seq_2[i] for i in indices]
time_seq_4_4000 = [time_seq_4[i] for i in indices]
time_seq_8_4000 = [time_seq_8[i] for i in indices]
it_seq_4000 = [it_seq[i] for i in indices]
time_seq_4000 = [time_seq[i] for i in indices]
it_par_1_4000 = [it_par_1[i] for i in indices]
it_par_2_4000 = [it_par_2[i] for i in indices]
it_par_4_4000 = [it_par_4[i] for i in indices]
it_par_8_4000 = [it_par_8[i] for i in indices]
total_lines_par_1_4000 = [it_par_1[i] for i in indices]
total_lines_par_2_4000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_4000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_4000 = [8*it_par_8[i] for i in indices]
time_par_1_4000 = [time_par_1[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (27, 36)
it_seq_1_10000 = [it_seq_1[i] for i in indices]
it_seq_2_10000 = [it_seq_2[i] for i in indices]
it_seq_4_10000 = [it_seq_4[i] for i in indices]
it_seq_8_10000 = [it_seq_8[i] for i in indices]
time_seq_1_10000 = [time_seq_1[i] for i in indices]
time_seq_2_10000 = [time_seq_2[i] for i in indices]
time_seq_4_10000 = [time_seq_4[i] for i in indices]
time_seq_8_10000 = [time_seq_8[i] for i in indices]
it_seq_10000 = [it_seq[i] for i in indices]
time_seq_10000 = [time_seq[i] for i in indices]
it_par_1_10000 = [it_par_1[i] for i in indices]
it_par_2_10000 = [it_par_2[i] for i in indices]
it_par_4_10000 = [it_par_4[i] for i in indices]
it_par_8_10000 = [it_par_8[i] for i in indices]
total_lines_par_1_10000 = [it_par_1[i] for i in indices]
total_lines_par_2_10000 = [2*it_par_2[i] for i in indices]
total_lines_par_4_10000 = [4*it_par_4[i] for i in indices]
total_lines_par_8_10000 = [8*it_par_8[i] for i in indices]
time_par_1_10000 = [time_par_1[i] for i in indices]
time_par_2_10000 = [time_par_2[i] for i in indices]
time_par_4_10000 = [time_par_4[i] for i in indices]
time_par_8_10000 = [time_par_8[i] for i in indices]
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
plt.plot(x_1000, total_lines_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 2 Threads - $n = 1000$')
plt.scatter(x_4000, total_lines_par_2_4000, color='red')
plt.plot(x_4000, total_lines_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 2 Threads - $n = 4000$')
plt.scatter(x_10000, total_lines_par_2_10000, color='blue')
plt.plot(x_10000, total_lines_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_uni_N_alpha_rows_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, total_lines_par_4_1000, color='orange')
plt.plot(x_1000, total_lines_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 4 Threads - $n = 1000$')
plt.scatter(x_4000, total_lines_par_4_4000, color='red')
plt.plot(x_4000, total_lines_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 4 Threads - $n = 4000$')
plt.scatter(x_10000, total_lines_par_4_10000, color='blue')
plt.plot(x_10000, total_lines_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_uni_N_alpha_rows_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Total Number of Used Rows"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, total_lines_par_8_1000, color='orange')
plt.plot(x_1000, total_lines_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 8 Threads - $n = 1000$')
plt.scatter(x_4000, total_lines_par_8_4000, color='red')
plt.plot(x_4000, total_lines_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 8 Threads - $n = 4000$')
plt.scatter(x_10000, total_lines_par_8_10000, color='blue')
plt.plot(x_10000, total_lines_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_uni_N_alpha_rows_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_2_1000, color='orange')
plt.plot(x_1000, it_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 2 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_2_4000, color='red')
plt.plot(x_4000, it_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 2 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_2_10000, color='blue')
plt.plot(x_10000, it_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_uni_N_alpha_it_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_4_1000, color='orange')
plt.plot(x_1000, it_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 4 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_4_4000, color='red')
plt.plot(x_4000, it_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 4 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_4_10000, color='blue')
plt.plot(x_10000, it_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_uni_N_alpha_it_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='orange')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, it_seq_4000, color='red')
plt.plot(x_4000, it_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, it_seq_10000, color='blue')
plt.plot(x_10000, it_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, it_par_8_1000, color='orange')
plt.plot(x_1000, it_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 8 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_8_4000, color='red')
plt.plot(x_4000, it_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 8 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_8_10000, color='blue')
plt.plot(x_10000, it_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_uni_N_alpha_it_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 2 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000, color='red')
plt.plot(x_4000, time_par_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 2 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000, color='blue')
plt.plot(x_10000, time_par_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_uni_N_alpha_time_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000, color='orange')
plt.plot(x_1000, time_par_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 4 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000, color='red')
plt.plot(x_4000, time_par_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 4 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000, color='blue')
plt.plot(x_10000, time_par_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_uni_N_alpha_time_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='orange')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='orange', label=r'Sequential - $n = 1000$')
plt.scatter(x_4000, time_seq_4000, color='red')
plt.plot(x_4000, time_seq_4000, linewidth=1.5, color='red', label=r'Sequential - $n = 4000$')
plt.scatter(x_10000, time_seq_10000, color='blue')
plt.plot(x_10000, time_seq_10000, linewidth=1.5, color='blue', label=r'Sequential - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000, color='orange')
plt.plot(x_1000, time_par_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'SRKAWOR with 8 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000, color='red')
plt.plot(x_4000, time_par_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'SRKAWOR with 8 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000, color='blue')
plt.plot(x_10000, time_par_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'SRKAWOR with 8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_uni_N_alpha_time_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Total Number of Used Rows using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='black')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='black', label=r'SRKWOR')
plt.scatter(x_1000, total_lines_par_2_1000, color='orange')
plt.plot(x_1000, total_lines_par_2_1000, linewidth=1.5, color='orange', label=r'SRKAWOR with 2 Threads')
plt.scatter(x_1000, total_lines_par_4_1000, color='red')
plt.plot(x_1000, total_lines_par_4_1000, linewidth=1.5, color='red', label=r'SRKAWOR with 4 Threads')
plt.scatter(x_1000, total_lines_par_8_1000, color='blue')
plt.plot(x_1000, total_lines_par_8_1000, linewidth=1.5, color='blue', label=r'SRKAWOR with 8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKA_seq_uni_N_alpha_rows_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Iterations using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_seq_1000, color='black')
plt.plot(x_1000, it_seq_1000, linewidth=1.5, color='black', label=r'SRKWOR')
plt.scatter(x_1000, it_par_2_1000, color='orange')
plt.plot(x_1000, it_par_2_1000, linewidth=1.5, color='orange', label=r'SRKAWOR with 2 Threads')
plt.scatter(x_1000, it_par_4_1000, color='red')
plt.plot(x_1000, it_par_4_1000, linewidth=1.5, color='red', label=r'SRKAWOR with 4 Threads')
plt.scatter(x_1000, it_par_8_1000, color='blue')
plt.plot(x_1000, it_par_8_1000, linewidth=1.5, color='blue', label=r'SRKAWOR with 8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_seq_uni_N_alpha_it_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"Time using $n = 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_seq_1000, color='black')
plt.plot(x_1000, time_seq_1000, linewidth=1.5, color='black', label=r'SRKWOR')
plt.scatter(x_1000, time_par_2_1000, color='orange')
plt.plot(x_1000, time_par_2_1000, linewidth=1.5, color='orange', label=r'SRKAWOR with 2 Threads')
plt.scatter(x_1000, time_par_4_1000, color='red')
plt.plot(x_1000, time_par_4_1000, linewidth=1.5, color='red', label=r'SRKAWOR with 4 Threads')
plt.scatter(x_1000, time_par_8_1000, color='blue')
plt.plot(x_1000, time_par_8_1000, linewidth=1.5, color='blue', label=r'SRKAWOR with 8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_seq_uni_N_alpha_time_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, speedup_2_1000, color='orange')
plt.plot(x_1000, speedup_2_1000, linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x_1000, speedup_4_1000, color='red')
plt.plot(x_1000, speedup_4_1000, linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x_1000, speedup_8_1000, color='blue')
plt.plot(x_1000, speedup_8_1000, linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Speedup')

filename_fig = "RKA_seq_uni_N_alpha_speedup_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')