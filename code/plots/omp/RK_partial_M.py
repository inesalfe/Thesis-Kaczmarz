import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RK_partial_M.py

filename = "outputs/omp/RK_partial.txt";

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

time_par_1_20000 = time_par_1[15:19]
time_par_2_20000 = time_par_2[15:19]
time_par_4_20000 = time_par_4[15:19]
time_par_8_20000 = time_par_8[15:19]
it_par_1_20000 = it_par_1[15:19]
it_par_2_20000 = it_par_2[15:19]
it_par_4_20000 = it_par_4[15:19]
it_par_8_20000 = it_par_8[15:19]
x_20000 = [750, 1000, 2000, 4000]

time_par_1_40000 = time_par_1[23:28]
time_par_2_40000 = time_par_2[23:28]
time_par_4_40000 = time_par_4[23:28]
time_par_8_40000 = time_par_8[23:28]
it_par_1_40000 = it_par_1[23:28]
it_par_2_40000 = it_par_2[23:28]
it_par_4_40000 = it_par_4[23:28]
it_par_8_40000 = it_par_8[23:28]
x_40000 = [750, 1000, 2000, 4000, 10000]

time_par_1_80000 = time_par_1[32:37]
time_par_2_80000 = time_par_2[32:37]
time_par_4_80000 = time_par_4[32:37]
time_par_8_80000 = time_par_8[32:37]
it_par_1_80000 = it_par_1[32:37]
it_par_2_80000 = it_par_2[32:37]
it_par_4_80000 = it_par_4[32:37]
it_par_8_80000 = it_par_8[32:37]
x_80000 = [750, 1000, 2000, 4000, 10000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000, color='orange')
plt.plot(x_20000, it_par_1_20000, linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000, color='red')
plt.plot(x_40000, it_par_1_40000, linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000, color='blue')
plt.plot(x_80000, it_par_1_80000, linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_2_20000, color='orange')
plt.plot(x_20000, it_par_2_20000, linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_2_40000, color='red')
plt.plot(x_40000, it_par_2_40000, linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_2_80000, color='blue')
plt.plot(x_80000, it_par_2_80000, linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_M_it_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000, color='orange')
plt.plot(x_20000, it_par_1_20000, linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000, color='red')
plt.plot(x_40000, it_par_1_40000, linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000, color='blue')
plt.plot(x_80000, it_par_1_80000, linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_4_20000, color='orange')
plt.plot(x_20000, it_par_4_20000, linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_4_40000, color='red')
plt.plot(x_40000, it_par_4_40000, linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_4_80000, color='blue')
plt.plot(x_80000, it_par_4_80000, linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_M_it_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000, color='orange')
plt.plot(x_20000, it_par_1_20000, linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000, color='red')
plt.plot(x_40000, it_par_1_40000, linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000, color='blue')
plt.plot(x_80000, it_par_1_80000, linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_8_20000, color='orange')
plt.plot(x_20000, it_par_8_20000, linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_8_40000, color='red')
plt.plot(x_40000, it_par_8_40000, linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_8_80000, color='blue')
plt.plot(x_80000, it_par_8_80000, linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_M_it_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000, color='orange')
plt.plot(x_20000, time_par_1_20000, linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000, color='red')
plt.plot(x_40000, time_par_1_40000, linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000, color='blue')
plt.plot(x_80000, time_par_1_80000, linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_2_20000, color='orange')
plt.plot(x_20000, time_par_2_20000, linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_2_40000, color='red')
plt.plot(x_40000, time_par_2_40000, linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_2_80000, color='blue')
plt.plot(x_80000, time_par_2_80000, linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_M_time_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000, color='orange')
plt.plot(x_20000, time_par_1_20000, linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000, color='red')
plt.plot(x_40000, time_par_1_40000, linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000, color='blue')
plt.plot(x_80000, time_par_1_80000, linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_4_20000, color='orange')
plt.plot(x_20000, time_par_4_20000, linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_4_40000, color='red')
plt.plot(x_40000, time_par_4_40000, linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_4_80000, color='blue')
plt.plot(x_80000, time_par_4_80000, linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_M_time_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Time"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000, color='orange')
plt.plot(x_20000, time_par_1_20000, linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000, color='red')
plt.plot(x_40000, time_par_1_40000, linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000, color='blue')
plt.plot(x_80000, time_par_1_80000, linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_8_20000, color='orange')
plt.plot(x_20000, time_par_8_20000, linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_8_40000, color='red')
plt.plot(x_40000, time_par_8_40000, linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_8_80000, color='blue')
plt.plot(x_80000, time_par_8_80000, linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_M_time_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()