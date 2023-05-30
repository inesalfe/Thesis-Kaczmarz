import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RK_partial_block_N.py

filename = "outputs/omp/RK_partial_block.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(float(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

it_par_1 = it[0::4]
it_par_2 = it[1::4]
it_par_4 = it[2::4]
it_par_8 = it[3::4]

time_par_1 = time[0::4]
time_par_2 = time[1::4]
time_par_4 = time[2::4]
time_par_8 = time[3::4]

indices = (5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 35, 36, 37, 38, 39, 60, 61, 62, 63, 64)
it_par_1_1000 = [it_par_1[i] for i in indices]
it_par_2_1000 = [it_par_2[i] for i in indices]
it_par_4_1000 = [it_par_4[i] for i in indices]
it_par_8_1000 = [it_par_8[i] for i in indices]
time_par_1_1000 = [time_par_1[i] for i in indices]
time_par_2_1000 = [time_par_2[i] for i in indices]
time_par_4_1000 = [time_par_4[i] for i in indices]
time_par_8_1000 = [time_par_8[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (25, 26, 27, 28, 29, 45, 46, 47, 48, 49, 70, 71, 72, 73, 74)
it_par_1_4000 = [it_par_1[i] for i in indices]
it_par_2_4000 = [it_par_2[i] for i in indices]
it_par_4_4000 = [it_par_4[i] for i in indices]
it_par_8_4000 = [it_par_8[i] for i in indices]
time_par_1_4000 = [time_par_1[i] for i in indices]
time_par_2_4000 = [time_par_2[i] for i in indices]
time_par_4_4000 = [time_par_4[i] for i in indices]
time_par_8_4000 = [time_par_8[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (50, 51, 52, 53, 54, 75, 76, 77, 78, 79)
it_par_1_10000 = [it_par_1[i] for i in indices]
it_par_2_10000 = [it_par_2[i] for i in indices]
it_par_4_10000 = [it_par_4[i] for i in indices]
it_par_8_10000 = [it_par_8[i] for i in indices]
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

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[0::5], color='orange')
plt.plot(x_1000, it_par_1_1000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[0::5], color='red')
plt.plot(x_4000, it_par_1_4000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[0::5], color='blue')
plt.plot(x_10000, it_par_1_10000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_2_1000[0::5], color='orange')
plt.plot(x_1000, it_par_2_1000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_2_4000[0::5], color='red')
plt.plot(x_4000, it_par_2_4000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_2_10000[0::5], color='blue')
plt.plot(x_10000, it_par_2_10000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_2_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[0::5], color='orange')
plt.plot(x_1000, it_par_1_1000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[0::5], color='red')
plt.plot(x_4000, it_par_1_4000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[0::5], color='blue')
plt.plot(x_10000, it_par_1_10000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_4_1000[0::5], color='orange')
plt.plot(x_1000, it_par_4_1000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_4_4000[0::5], color='red')
plt.plot(x_4000, it_par_4_4000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_4_10000[0::5], color='blue')
plt.plot(x_10000, it_par_4_10000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_4_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[0::5], color='orange')
plt.plot(x_1000, it_par_1_1000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[0::5], color='red')
plt.plot(x_4000, it_par_1_4000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[0::5], color='blue')
plt.plot(x_10000, it_par_1_10000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_8_1000[0::5], color='orange')
plt.plot(x_1000, it_par_8_1000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_8_4000[0::5], color='red')
plt.plot(x_4000, it_par_8_4000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_8_10000[0::5], color='blue')
plt.plot(x_10000, it_par_8_10000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_8_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[0::5], color='orange')
plt.plot(x_1000, time_par_1_1000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[0::5], color='red')
plt.plot(x_4000, time_par_1_4000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[0::5], color='blue')
plt.plot(x_10000, time_par_1_10000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000[0::5], color='orange')
plt.plot(x_1000, time_par_2_1000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000[0::5], color='red')
plt.plot(x_4000, time_par_2_4000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000[0::5], color='blue')
plt.plot(x_10000, time_par_2_10000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_2_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[0::5], color='orange')
plt.plot(x_1000, time_par_1_1000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[0::5], color='red')
plt.plot(x_4000, time_par_1_4000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[0::5], color='blue')
plt.plot(x_10000, time_par_1_10000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000[0::5], color='orange')
plt.plot(x_1000, time_par_4_1000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000[0::5], color='red')
plt.plot(x_4000, time_par_4_4000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000[0::5], color='blue')
plt.plot(x_10000, time_par_4_10000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_4_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[0::5], color='orange')
plt.plot(x_1000, time_par_1_1000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[0::5], color='red')
plt.plot(x_4000, time_par_1_4000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[0::5], color='blue')
plt.plot(x_10000, time_par_1_10000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000[0::5], color='orange')
plt.plot(x_1000, time_par_8_1000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000[0::5], color='red')
plt.plot(x_4000, time_par_8_4000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000[0::5], color='blue')
plt.plot(x_10000, time_par_8_10000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_8_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[1::5], color='orange')
plt.plot(x_1000, it_par_1_1000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[1::5], color='red')
plt.plot(x_4000, it_par_1_4000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[1::5], color='blue')
plt.plot(x_10000, it_par_1_10000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_2_1000[1::5], color='orange')
plt.plot(x_1000, it_par_2_1000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_2_4000[1::5], color='red')
plt.plot(x_4000, it_par_2_4000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_2_10000[1::5], color='blue')
plt.plot(x_10000, it_par_2_10000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_2_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[1::5], color='orange')
plt.plot(x_1000, it_par_1_1000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[1::5], color='red')
plt.plot(x_4000, it_par_1_4000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[1::5], color='blue')
plt.plot(x_10000, it_par_1_10000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_4_1000[1::5], color='orange')
plt.plot(x_1000, it_par_4_1000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_4_4000[1::5], color='red')
plt.plot(x_4000, it_par_4_4000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_4_10000[1::5], color='blue')
plt.plot(x_10000, it_par_4_10000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_4_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[1::5], color='orange')
plt.plot(x_1000, it_par_1_1000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[1::5], color='red')
plt.plot(x_4000, it_par_1_4000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[1::5], color='blue')
plt.plot(x_10000, it_par_1_10000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_8_1000[1::5], color='orange')
plt.plot(x_1000, it_par_8_1000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_8_4000[1::5], color='red')
plt.plot(x_4000, it_par_8_4000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_8_10000[1::5], color='blue')
plt.plot(x_10000, it_par_8_10000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_8_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[1::5], color='orange')
plt.plot(x_1000, time_par_1_1000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[1::5], color='red')
plt.plot(x_4000, time_par_1_4000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[1::5], color='blue')
plt.plot(x_10000, time_par_1_10000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000[1::5], color='orange')
plt.plot(x_1000, time_par_2_1000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000[1::5], color='red')
plt.plot(x_4000, time_par_2_4000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000[1::5], color='blue')
plt.plot(x_10000, time_par_2_10000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_2_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[1::5], color='orange')
plt.plot(x_1000, time_par_1_1000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[1::5], color='red')
plt.plot(x_4000, time_par_1_4000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[1::5], color='blue')
plt.plot(x_10000, time_par_1_10000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000[1::5], color='orange')
plt.plot(x_1000, time_par_4_1000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000[1::5], color='red')
plt.plot(x_4000, time_par_4_4000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000[1::5], color='blue')
plt.plot(x_10000, time_par_4_10000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_4_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[1::5], color='orange')
plt.plot(x_1000, time_par_1_1000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[1::5], color='red')
plt.plot(x_4000, time_par_1_4000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[1::5], color='blue')
plt.plot(x_10000, time_par_1_10000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000[1::5], color='orange')
plt.plot(x_1000, time_par_8_1000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000[1::5], color='red')
plt.plot(x_4000, time_par_8_4000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000[1::5], color='blue')
plt.plot(x_10000, time_par_8_10000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_8_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[2::5], color='orange')
plt.plot(x_1000, it_par_1_1000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[2::5], color='red')
plt.plot(x_4000, it_par_1_4000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[2::5], color='blue')
plt.plot(x_10000, it_par_1_10000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_2_1000[2::5], color='orange')
plt.plot(x_1000, it_par_2_1000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_2_4000[2::5], color='red')
plt.plot(x_4000, it_par_2_4000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_2_10000[2::5], color='blue')
plt.plot(x_10000, it_par_2_10000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_2_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[2::5], color='orange')
plt.plot(x_1000, it_par_1_1000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[2::5], color='red')
plt.plot(x_4000, it_par_1_4000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[2::5], color='blue')
plt.plot(x_10000, it_par_1_10000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_4_1000[2::5], color='orange')
plt.plot(x_1000, it_par_4_1000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_4_4000[2::5], color='red')
plt.plot(x_4000, it_par_4_4000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_4_10000[2::5], color='blue')
plt.plot(x_10000, it_par_4_10000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_4_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[2::5], color='orange')
plt.plot(x_1000, it_par_1_1000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[2::5], color='red')
plt.plot(x_4000, it_par_1_4000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[2::5], color='blue')
plt.plot(x_10000, it_par_1_10000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_8_1000[2::5], color='orange')
plt.plot(x_1000, it_par_8_1000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_8_4000[2::5], color='red')
plt.plot(x_4000, it_par_8_4000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_8_10000[2::5], color='blue')
plt.plot(x_10000, it_par_8_10000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_8_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[2::5], color='orange')
plt.plot(x_1000, time_par_1_1000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[2::5], color='red')
plt.plot(x_4000, time_par_1_4000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[2::5], color='blue')
plt.plot(x_10000, time_par_1_10000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000[2::5], color='orange')
plt.plot(x_1000, time_par_2_1000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000[2::5], color='red')
plt.plot(x_4000, time_par_2_4000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000[2::5], color='blue')
plt.plot(x_10000, time_par_2_10000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_2_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[2::5], color='orange')
plt.plot(x_1000, time_par_1_1000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[2::5], color='red')
plt.plot(x_4000, time_par_1_4000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[2::5], color='blue')
plt.plot(x_10000, time_par_1_10000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000[2::5], color='orange')
plt.plot(x_1000, time_par_4_1000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000[2::5], color='red')
plt.plot(x_4000, time_par_4_4000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000[2::5], color='blue')
plt.plot(x_10000, time_par_4_10000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_4_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[2::5], color='orange')
plt.plot(x_1000, time_par_1_1000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[2::5], color='red')
plt.plot(x_4000, time_par_1_4000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[2::5], color='blue')
plt.plot(x_10000, time_par_1_10000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000[2::5], color='orange')
plt.plot(x_1000, time_par_8_1000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000[2::5], color='red')
plt.plot(x_4000, time_par_8_4000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000[2::5], color='blue')
plt.plot(x_10000, time_par_8_10000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_8_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[3::5], color='orange')
plt.plot(x_1000, it_par_1_1000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[3::5], color='red')
plt.plot(x_4000, it_par_1_4000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[3::5], color='blue')
plt.plot(x_10000, it_par_1_10000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_2_1000[3::5], color='orange')
plt.plot(x_1000, it_par_2_1000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_2_4000[3::5], color='red')
plt.plot(x_4000, it_par_2_4000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_2_10000[3::5], color='blue')
plt.plot(x_10000, it_par_2_10000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_2_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[3::5], color='orange')
plt.plot(x_1000, it_par_1_1000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[3::5], color='red')
plt.plot(x_4000, it_par_1_4000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[3::5], color='blue')
plt.plot(x_10000, it_par_1_10000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_4_1000[3::5], color='orange')
plt.plot(x_1000, it_par_4_1000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_4_4000[3::5], color='red')
plt.plot(x_4000, it_par_4_4000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_4_10000[3::5], color='blue')
plt.plot(x_10000, it_par_4_10000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_4_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[3::5], color='orange')
plt.plot(x_1000, it_par_1_1000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[3::5], color='red')
plt.plot(x_4000, it_par_1_4000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[3::5], color='blue')
plt.plot(x_10000, it_par_1_10000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_8_1000[3::5], color='orange')
plt.plot(x_1000, it_par_8_1000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_8_4000[3::5], color='red')
plt.plot(x_4000, it_par_8_4000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_8_10000[3::5], color='blue')
plt.plot(x_10000, it_par_8_10000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_8_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[3::5], color='orange')
plt.plot(x_1000, time_par_1_1000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[3::5], color='red')
plt.plot(x_4000, time_par_1_4000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[3::5], color='blue')
plt.plot(x_10000, time_par_1_10000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000[3::5], color='orange')
plt.plot(x_1000, time_par_2_1000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000[3::5], color='red')
plt.plot(x_4000, time_par_2_4000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000[3::5], color='blue')
plt.plot(x_10000, time_par_2_10000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_2_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[3::5], color='orange')
plt.plot(x_1000, time_par_1_1000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[3::5], color='red')
plt.plot(x_4000, time_par_1_4000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[3::5], color='blue')
plt.plot(x_10000, time_par_1_10000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000[3::5], color='orange')
plt.plot(x_1000, time_par_4_1000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000[3::5], color='red')
plt.plot(x_4000, time_par_4_4000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000[3::5], color='blue')
plt.plot(x_10000, time_par_4_10000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_4_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[3::5], color='orange')
plt.plot(x_1000, time_par_1_1000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[3::5], color='red')
plt.plot(x_4000, time_par_1_4000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[3::5], color='blue')
plt.plot(x_10000, time_par_1_10000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000[3::5], color='orange')
plt.plot(x_1000, time_par_8_1000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000[3::5], color='red')
plt.plot(x_4000, time_par_8_4000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000[3::5], color='blue')
plt.plot(x_10000, time_par_8_10000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_8_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[4::5], color='orange')
plt.plot(x_1000, it_par_1_1000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[4::5], color='red')
plt.plot(x_4000, it_par_1_4000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[4::5], color='blue')
plt.plot(x_10000, it_par_1_10000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_2_1000[4::5], color='orange')
plt.plot(x_1000, it_par_2_1000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_2_4000[4::5], color='red')
plt.plot(x_4000, it_par_2_4000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_2_10000[4::5], color='blue')
plt.plot(x_10000, it_par_2_10000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_2_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[4::5], color='orange')
plt.plot(x_1000, it_par_1_1000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[4::5], color='red')
plt.plot(x_4000, it_par_1_4000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[4::5], color='blue')
plt.plot(x_10000, it_par_1_10000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_4_1000[4::5], color='orange')
plt.plot(x_1000, it_par_4_1000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_4_4000[4::5], color='red')
plt.plot(x_4000, it_par_4_4000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_4_10000[4::5], color='blue')
plt.plot(x_10000, it_par_4_10000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_4_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_par_1_1000[4::5], color='orange')
plt.plot(x_1000, it_par_1_1000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, it_par_1_4000[4::5], color='red')
plt.plot(x_4000, it_par_1_4000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, it_par_1_10000[4::5], color='blue')
plt.plot(x_10000, it_par_1_10000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, it_par_8_1000[4::5], color='orange')
plt.plot(x_1000, it_par_8_1000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, it_par_8_4000[4::5], color='red')
plt.plot(x_4000, it_par_8_4000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, it_par_8_10000[4::5], color='blue')
plt.plot(x_10000, it_par_8_10000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_N_it_8_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[4::5], color='orange')
plt.plot(x_1000, time_par_1_1000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[4::5], color='red')
plt.plot(x_4000, time_par_1_4000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[4::5], color='blue')
plt.plot(x_10000, time_par_1_10000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_2_1000[4::5], color='orange')
plt.plot(x_1000, time_par_2_1000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_2_4000[4::5], color='red')
plt.plot(x_4000, time_par_2_4000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_2_10000[4::5], color='blue')
plt.plot(x_10000, time_par_2_10000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_2_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[4::5], color='orange')
plt.plot(x_1000, time_par_1_1000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[4::5], color='red')
plt.plot(x_4000, time_par_1_4000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[4::5], color='blue')
plt.plot(x_10000, time_par_1_10000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_4_1000[4::5], color='orange')
plt.plot(x_1000, time_par_4_1000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_4_4000[4::5], color='red')
plt.plot(x_4000, time_par_4_4000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_4_10000[4::5], color='blue')
plt.plot(x_10000, time_par_4_10000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_4_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_par_1_1000[4::5], color='orange')
plt.plot(x_1000, time_par_1_1000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $n = 1000$')
plt.scatter(x_4000, time_par_1_4000[4::5], color='red')
plt.plot(x_4000, time_par_1_4000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $n = 4000$')
plt.scatter(x_10000, time_par_1_10000[4::5], color='blue')
plt.plot(x_10000, time_par_1_10000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $n = 10000$')
plt.scatter(x_1000, time_par_8_1000[4::5], color='orange')
plt.plot(x_1000, time_par_8_1000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $n = 1000$')
plt.scatter(x_4000, time_par_8_4000[4::5], color='red')
plt.plot(x_4000, time_par_8_4000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $n = 4000$')
plt.scatter(x_10000, time_par_8_10000[4::5], color='blue')
plt.plot(x_10000, time_par_8_10000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_N_time_8_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()