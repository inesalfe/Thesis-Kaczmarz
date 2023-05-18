import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RK_partial_block_M.py

filename = "outputs/omp/RK_partial_block.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(float(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

time_par_1_4000 = time[0:40:4]
time_par_2_4000 = time[1:40:4]
time_par_4_4000 = time[2:40:4]
time_par_8_4000 = time[3:40:4]
it_par_1_4000 = it[0:40:4]
it_par_2_4000 = it[1:40:4]
it_par_4_4000 = it[2:40:4]
it_par_8_4000 = it[3:40:4]
x_4000 = [750, 1000]

time_par_1_20000 = time[40:120:4]
time_par_2_20000 = time[41:120:4]
time_par_4_20000 = time[42:120:4]
time_par_8_20000 = time[43:120:4]
it_par_1_20000 = it[40:120:4]
it_par_2_20000 = it[41:120:4]
it_par_4_20000 = it[42:120:4]
it_par_8_20000 = it[43:120:4]
x_20000 = [750, 1000, 2000, 4000]

time_par_1_40000 = time[120:220:4]
time_par_2_40000 = time[121:220:4]
time_par_4_40000 = time[122:220:4]
time_par_8_40000 = time[123:220:4]
it_par_1_40000 = it[120:220:4]
it_par_2_40000 = it[121:220:4]
it_par_4_40000 = it[122:220:4]
it_par_8_40000 = it[123:220:4]
x_40000 = [750, 1000, 2000, 4000, 10000]

time_par_1_80000 = time[220:320:4]
time_par_2_80000 = time[221:320:4]
time_par_4_80000 = time[222:320:4]
time_par_8_80000 = time[223:320:4]
it_par_1_80000 = it[220:320:4]
it_par_2_80000 = it[221:320:4]
it_par_4_80000 = it[222:320:4]
it_par_8_80000 = it[223:320:4]
x_80000 = [750, 1000, 2000, 4000, 10000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[0::5], color='orange')
plt.plot(x_20000, it_par_1_20000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[0::5], color='red')
plt.plot(x_40000, it_par_1_40000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[0::5], color='blue')
plt.plot(x_80000, it_par_1_80000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_2_20000[0::5], color='orange')
plt.plot(x_20000, it_par_2_20000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_2_40000[0::5], color='red')
plt.plot(x_40000, it_par_2_40000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_2_80000[0::5], color='blue')
plt.plot(x_80000, it_par_2_80000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_2_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[0::5], color='orange')
plt.plot(x_20000, it_par_1_20000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[0::5], color='red')
plt.plot(x_40000, it_par_1_40000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[0::5], color='blue')
plt.plot(x_80000, it_par_1_80000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_4_20000[0::5], color='orange')
plt.plot(x_20000, it_par_4_20000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_4_40000[0::5], color='red')
plt.plot(x_40000, it_par_4_40000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_4_80000[0::5], color='blue')
plt.plot(x_80000, it_par_4_80000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_4_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[0::5], color='orange')
plt.plot(x_20000, it_par_1_20000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[0::5], color='red')
plt.plot(x_40000, it_par_1_40000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[0::5], color='blue')
plt.plot(x_80000, it_par_1_80000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_8_20000[0::5], color='orange')
plt.plot(x_20000, it_par_8_20000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_8_40000[0::5], color='red')
plt.plot(x_40000, it_par_8_40000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_8_80000[0::5], color='blue')
plt.plot(x_80000, it_par_8_80000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_8_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[0::5], color='orange')
plt.plot(x_20000, time_par_1_20000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[0::5], color='red')
plt.plot(x_40000, time_par_1_40000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[0::5], color='blue')
plt.plot(x_80000, time_par_1_80000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_2_20000[0::5], color='orange')
plt.plot(x_20000, time_par_2_20000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_2_40000[0::5], color='red')
plt.plot(x_40000, time_par_2_40000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_2_80000[0::5], color='blue')
plt.plot(x_80000, time_par_2_80000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_2_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[0::5], color='orange')
plt.plot(x_20000, time_par_1_20000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[0::5], color='red')
plt.plot(x_40000, time_par_1_40000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[0::5], color='blue')
plt.plot(x_80000, time_par_1_80000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_4_20000[0::5], color='orange')
plt.plot(x_20000, time_par_4_20000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_4_40000[0::5], color='red')
plt.plot(x_40000, time_par_4_40000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_4_80000[0::5], color='blue')
plt.plot(x_80000, time_par_4_80000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_4_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 5 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[0::5], color='orange')
plt.plot(x_20000, time_par_1_20000[0::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[0::5], color='red')
plt.plot(x_40000, time_par_1_40000[0::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[0::5], color='blue')
plt.plot(x_80000, time_par_1_80000[0::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_8_20000[0::5], color='orange')
plt.plot(x_20000, time_par_8_20000[0::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_8_40000[0::5], color='red')
plt.plot(x_40000, time_par_8_40000[0::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_8_80000[0::5], color='blue')
plt.plot(x_80000, time_par_8_80000[0::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_8_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[1::5], color='orange')
plt.plot(x_20000, it_par_1_20000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[1::5], color='red')
plt.plot(x_40000, it_par_1_40000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[1::5], color='blue')
plt.plot(x_80000, it_par_1_80000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_2_20000[1::5], color='orange')
plt.plot(x_20000, it_par_2_20000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_2_40000[1::5], color='red')
plt.plot(x_40000, it_par_2_40000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_2_80000[1::5], color='blue')
plt.plot(x_80000, it_par_2_80000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_2_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[1::5], color='orange')
plt.plot(x_20000, it_par_1_20000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[1::5], color='red')
plt.plot(x_40000, it_par_1_40000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[1::5], color='blue')
plt.plot(x_80000, it_par_1_80000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_4_20000[1::5], color='orange')
plt.plot(x_20000, it_par_4_20000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_4_40000[1::5], color='red')
plt.plot(x_40000, it_par_4_40000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_4_80000[1::5], color='blue')
plt.plot(x_80000, it_par_4_80000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_4_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[1::5], color='orange')
plt.plot(x_20000, it_par_1_20000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[1::5], color='red')
plt.plot(x_40000, it_par_1_40000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[1::5], color='blue')
plt.plot(x_80000, it_par_1_80000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_8_20000[1::5], color='orange')
plt.plot(x_20000, it_par_8_20000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_8_40000[1::5], color='red')
plt.plot(x_40000, it_par_8_40000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_8_80000[1::5], color='blue')
plt.plot(x_80000, it_par_8_80000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_8_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[1::5], color='orange')
plt.plot(x_20000, time_par_1_20000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[1::5], color='red')
plt.plot(x_40000, time_par_1_40000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[1::5], color='blue')
plt.plot(x_80000, time_par_1_80000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_2_20000[1::5], color='orange')
plt.plot(x_20000, time_par_2_20000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_2_40000[1::5], color='red')
plt.plot(x_40000, time_par_2_40000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_2_80000[1::5], color='blue')
plt.plot(x_80000, time_par_2_80000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_2_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[1::5], color='orange')
plt.plot(x_20000, time_par_1_20000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[1::5], color='red')
plt.plot(x_40000, time_par_1_40000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[1::5], color='blue')
plt.plot(x_80000, time_par_1_80000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_4_20000[1::5], color='orange')
plt.plot(x_20000, time_par_4_20000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_4_40000[1::5], color='red')
plt.plot(x_40000, time_par_4_40000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_4_80000[1::5], color='blue')
plt.plot(x_80000, time_par_4_80000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_4_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 10 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[1::5], color='orange')
plt.plot(x_20000, time_par_1_20000[1::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[1::5], color='red')
plt.plot(x_40000, time_par_1_40000[1::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[1::5], color='blue')
plt.plot(x_80000, time_par_1_80000[1::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_8_20000[1::5], color='orange')
plt.plot(x_20000, time_par_8_20000[1::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_8_40000[1::5], color='red')
plt.plot(x_40000, time_par_8_40000[1::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_8_80000[1::5], color='blue')
plt.plot(x_80000, time_par_8_80000[1::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_8_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[2::5], color='orange')
plt.plot(x_20000, it_par_1_20000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[2::5], color='red')
plt.plot(x_40000, it_par_1_40000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[2::5], color='blue')
plt.plot(x_80000, it_par_1_80000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_2_20000[2::5], color='orange')
plt.plot(x_20000, it_par_2_20000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_2_40000[2::5], color='red')
plt.plot(x_40000, it_par_2_40000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_2_80000[2::5], color='blue')
plt.plot(x_80000, it_par_2_80000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_2_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[2::5], color='orange')
plt.plot(x_20000, it_par_1_20000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[2::5], color='red')
plt.plot(x_40000, it_par_1_40000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[2::5], color='blue')
plt.plot(x_80000, it_par_1_80000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_4_20000[2::5], color='orange')
plt.plot(x_20000, it_par_4_20000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_4_40000[2::5], color='red')
plt.plot(x_40000, it_par_4_40000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_4_80000[2::5], color='blue')
plt.plot(x_80000, it_par_4_80000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_4_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[2::5], color='orange')
plt.plot(x_20000, it_par_1_20000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[2::5], color='red')
plt.plot(x_40000, it_par_1_40000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[2::5], color='blue')
plt.plot(x_80000, it_par_1_80000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_8_20000[2::5], color='orange')
plt.plot(x_20000, it_par_8_20000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_8_40000[2::5], color='red')
plt.plot(x_40000, it_par_8_40000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_8_80000[2::5], color='blue')
plt.plot(x_80000, it_par_8_80000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_8_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[2::5], color='orange')
plt.plot(x_20000, time_par_1_20000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[2::5], color='red')
plt.plot(x_40000, time_par_1_40000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[2::5], color='blue')
plt.plot(x_80000, time_par_1_80000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_2_20000[2::5], color='orange')
plt.plot(x_20000, time_par_2_20000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_2_40000[2::5], color='red')
plt.plot(x_40000, time_par_2_40000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_2_80000[2::5], color='blue')
plt.plot(x_80000, time_par_2_80000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_2_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[2::5], color='orange')
plt.plot(x_20000, time_par_1_20000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[2::5], color='red')
plt.plot(x_40000, time_par_1_40000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[2::5], color='blue')
plt.plot(x_80000, time_par_1_80000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_4_20000[2::5], color='orange')
plt.plot(x_20000, time_par_4_20000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_4_40000[2::5], color='red')
plt.plot(x_40000, time_par_4_40000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_4_80000[2::5], color='blue')
plt.plot(x_80000, time_par_4_80000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_4_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 50 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[2::5], color='orange')
plt.plot(x_20000, time_par_1_20000[2::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[2::5], color='red')
plt.plot(x_40000, time_par_1_40000[2::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[2::5], color='blue')
plt.plot(x_80000, time_par_1_80000[2::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_8_20000[2::5], color='orange')
plt.plot(x_20000, time_par_8_20000[2::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_8_40000[2::5], color='red')
plt.plot(x_40000, time_par_8_40000[2::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_8_80000[2::5], color='blue')
plt.plot(x_80000, time_par_8_80000[2::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_8_50"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[3::5], color='orange')
plt.plot(x_20000, it_par_1_20000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[3::5], color='red')
plt.plot(x_40000, it_par_1_40000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[3::5], color='blue')
plt.plot(x_80000, it_par_1_80000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_2_20000[3::5], color='orange')
plt.plot(x_20000, it_par_2_20000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_2_40000[3::5], color='red')
plt.plot(x_40000, it_par_2_40000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_2_80000[3::5], color='blue')
plt.plot(x_80000, it_par_2_80000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_2_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[3::5], color='orange')
plt.plot(x_20000, it_par_1_20000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[3::5], color='red')
plt.plot(x_40000, it_par_1_40000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[3::5], color='blue')
plt.plot(x_80000, it_par_1_80000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_4_20000[3::5], color='orange')
plt.plot(x_20000, it_par_4_20000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_4_40000[3::5], color='red')
plt.plot(x_40000, it_par_4_40000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_4_80000[3::5], color='blue')
plt.plot(x_80000, it_par_4_80000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_4_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[3::5], color='orange')
plt.plot(x_20000, it_par_1_20000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[3::5], color='red')
plt.plot(x_40000, it_par_1_40000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[3::5], color='blue')
plt.plot(x_80000, it_par_1_80000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_8_20000[3::5], color='orange')
plt.plot(x_20000, it_par_8_20000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_8_40000[3::5], color='red')
plt.plot(x_40000, it_par_8_40000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_8_80000[3::5], color='blue')
plt.plot(x_80000, it_par_8_80000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_8_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[3::5], color='orange')
plt.plot(x_20000, time_par_1_20000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[3::5], color='red')
plt.plot(x_40000, time_par_1_40000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[3::5], color='blue')
plt.plot(x_80000, time_par_1_80000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_2_20000[3::5], color='orange')
plt.plot(x_20000, time_par_2_20000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_2_40000[3::5], color='red')
plt.plot(x_40000, time_par_2_40000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_2_80000[3::5], color='blue')
plt.plot(x_80000, time_par_2_80000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_2_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[3::5], color='orange')
plt.plot(x_20000, time_par_1_20000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[3::5], color='red')
plt.plot(x_40000, time_par_1_40000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[3::5], color='blue')
plt.plot(x_80000, time_par_1_80000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_4_20000[3::5], color='orange')
plt.plot(x_20000, time_par_4_20000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_4_40000[3::5], color='red')
plt.plot(x_40000, time_par_4_40000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_4_80000[3::5], color='blue')
plt.plot(x_80000, time_par_4_80000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_4_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 100 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[3::5], color='orange')
plt.plot(x_20000, time_par_1_20000[3::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[3::5], color='red')
plt.plot(x_40000, time_par_1_40000[3::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[3::5], color='blue')
plt.plot(x_80000, time_par_1_80000[3::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_8_20000[3::5], color='orange')
plt.plot(x_20000, time_par_8_20000[3::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_8_40000[3::5], color='red')
plt.plot(x_40000, time_par_8_40000[3::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_8_80000[3::5], color='blue')
plt.plot(x_80000, time_par_8_80000[3::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_8_100"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[4::5], color='orange')
plt.plot(x_20000, it_par_1_20000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[4::5], color='red')
plt.plot(x_40000, it_par_1_40000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[4::5], color='blue')
plt.plot(x_80000, it_par_1_80000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_2_20000[4::5], color='orange')
plt.plot(x_20000, it_par_2_20000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_2_40000[4::5], color='red')
plt.plot(x_40000, it_par_2_40000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_2_80000[4::5], color='blue')
plt.plot(x_80000, it_par_2_80000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_2_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[4::5], color='orange')
plt.plot(x_20000, it_par_1_20000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[4::5], color='red')
plt.plot(x_40000, it_par_1_40000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[4::5], color='blue')
plt.plot(x_80000, it_par_1_80000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_4_20000[4::5], color='orange')
plt.plot(x_20000, it_par_4_20000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_4_40000[4::5], color='red')
plt.plot(x_40000, it_par_4_40000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_4_80000[4::5], color='blue')
plt.plot(x_80000, it_par_4_80000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_4_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, it_par_1_20000[4::5], color='orange')
plt.plot(x_20000, it_par_1_20000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, it_par_1_40000[4::5], color='red')
plt.plot(x_40000, it_par_1_40000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, it_par_1_80000[4::5], color='blue')
plt.plot(x_80000, it_par_1_80000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, it_par_8_20000[4::5], color='orange')
plt.plot(x_20000, it_par_8_20000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, it_par_8_40000[4::5], color='red')
plt.plot(x_40000, it_par_8_40000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, it_par_8_80000[4::5], color='blue')
plt.plot(x_80000, it_par_8_80000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "RK_partial_block_M_it_8_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[4::5], color='orange')
plt.plot(x_20000, time_par_1_20000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[4::5], color='red')
plt.plot(x_40000, time_par_1_40000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[4::5], color='blue')
plt.plot(x_80000, time_par_1_80000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_2_20000[4::5], color='orange')
plt.plot(x_20000, time_par_2_20000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'2 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_2_40000[4::5], color='red')
plt.plot(x_40000, time_par_2_40000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'2 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_2_80000[4::5], color='blue')
plt.plot(x_80000, time_par_2_80000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'2 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_2_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[4::5], color='orange')
plt.plot(x_20000, time_par_1_20000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[4::5], color='red')
plt.plot(x_40000, time_par_1_40000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[4::5], color='blue')
plt.plot(x_80000, time_par_1_80000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_4_20000[4::5], color='orange')
plt.plot(x_20000, time_par_4_20000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'4 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_4_40000[4::5], color='red')
plt.plot(x_40000, time_par_4_40000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'4 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_4_80000[4::5], color='blue')
plt.plot(x_80000, time_par_4_80000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'4 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_4_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"Update of the solution vector every 500 iterations"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, time_par_1_20000[4::5], color='orange')
plt.plot(x_20000, time_par_1_20000[4::5], linewidth=1.5, color='orange', label=r'1 Thread - $m = 20000$')
plt.scatter(x_40000, time_par_1_40000[4::5], color='red')
plt.plot(x_40000, time_par_1_40000[4::5], linewidth=1.5, color='red', label=r'1 Thread - $m = 40000$')
plt.scatter(x_80000, time_par_1_80000[4::5], color='blue')
plt.plot(x_80000, time_par_1_80000[4::5], linewidth=1.5, color='blue', label=r'1 Thread - $m = 80000$')
plt.scatter(x_20000, time_par_8_20000[4::5], color='orange')
plt.plot(x_20000, time_par_8_20000[4::5], linestyle='--', linewidth=1.5, color='orange', label=r'8 Threads - $m = 20000$')
plt.scatter(x_40000, time_par_8_40000[4::5], color='red')
plt.plot(x_40000, time_par_8_40000[4::5], linestyle='--', linewidth=1.5, color='red', label=r'8 Threads - $m = 40000$')
plt.scatter(x_80000, time_par_8_80000[4::5], color='blue')
plt.plot(x_80000, time_par_8_80000[4::5], linestyle='--', linewidth=1.5, color='blue', label=r'8 Threads - $m = 80000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_M_time_8_500"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()