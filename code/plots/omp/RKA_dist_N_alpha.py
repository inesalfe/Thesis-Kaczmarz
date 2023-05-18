import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKA_dist_N_alpha.py

filename = "outputs/omp/RKA_dist_alpha.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))

it_1000 = it[200:232]
it_4000 = it[256:280]
it_10000 = it[280::]

it_1000_dist = it_1000[1::2]
it_4000_dist = it_4000[1::2]
it_10000_dist = it_10000[1::2]

it_1000 = it_1000[0::2]
it_4000 = it_4000[0::2]
it_10000 = it_10000[0::2]

it_1_1000 = it_1000[0::4]
it_2_1000 = it_1000[1::4]
it_4_1000 = it_1000[2::4]
it_8_1000 = it_1000[3::4]
it_dist_1_1000 = it_1000_dist[0::4]
it_dist_2_1000 = it_1000_dist[1::4]
it_dist_4_1000 = it_1000_dist[2::4]
it_dist_8_1000 = it_1000_dist[3::4]
x_1000 = [4000, 20000, 40000, 80000]

it_1_4000 = it_4000[0::4]
it_2_4000 = it_4000[1::4]
it_4_4000 = it_4000[2::4]
it_8_4000 = it_4000[3::4]
it_dist_1_4000 = it_4000_dist[0::4]
it_dist_2_4000 = it_4000_dist[1::4]
it_dist_4_4000 = it_4000_dist[2::4]
it_dist_8_4000 = it_4000_dist[3::4]
x_4000 = [20000, 40000, 80000]

it_1_10000 = it_10000[0::4]
it_2_10000 = it_10000[1::4]
it_4_10000 = it_10000[2::4]
it_8_10000 = it_10000[3::4]
it_dist_1_10000 = it_10000_dist[0::4]
it_dist_2_10000 = it_10000_dist[1::4]
it_dist_4_10000 = it_10000_dist[2::4]
it_dist_8_10000 = it_10000_dist[3::4]
x_10000 = [40000, 80000]

time_1000 = time[200:232]
time_4000 = time[256:280]
time_10000 = time[280::]

time_1000_dist = time_1000[1::2]
time_4000_dist = time_4000[1::2]
time_10000_dist = time_10000[1::2]

time_1000 = time_1000[0::2]
time_4000 = time_4000[0::2]
time_10000 = time_10000[0::2]

time_1_1000 = time_1000[0::4]
time_2_1000 = time_1000[1::4]
time_4_1000 = time_1000[2::4]
time_8_1000 = time_1000[3::4]
time_dist_1_1000 = time_1000_dist[0::4]
time_dist_2_1000 = time_1000_dist[1::4]
time_dist_4_1000 = time_1000_dist[2::4]
time_dist_8_1000 = time_1000_dist[3::4]
x_1000 = [4000, 20000, 40000, 80000]

time_1_4000 = time_4000[0::4]
time_2_4000 = time_4000[1::4]
time_4_4000 = time_4000[2::4]
time_8_4000 = time_4000[3::4]
time_dist_1_4000 = time_4000_dist[0::4]
time_dist_2_4000 = time_4000_dist[1::4]
time_dist_4_4000 = time_4000_dist[2::4]
time_dist_8_4000 = time_4000_dist[3::4]
x_4000 = [20000, 40000, 80000]

time_1_10000 = time_10000[0::4]
time_2_10000 = time_10000[1::4]
time_4_10000 = time_10000[2::4]
time_8_10000 = time_10000[3::4]
time_dist_1_10000 = time_10000_dist[0::4]
time_dist_2_10000 = time_10000_dist[1::4]
time_dist_4_10000 = time_10000_dist[2::4]
time_dist_8_10000 = time_10000_dist[3::4]
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

plot_title = r"RKA using 2 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_2_1000, color='orange')
plt.plot(x_1000, it_2_1000, linewidth=1.5, color='orange', label=r'W/o partition - $n = 1000$')
plt.scatter(x_4000, it_2_4000, color='red')
plt.plot(x_4000, it_2_4000, linewidth=1.5, color='red', label=r'W/o partition - $n = 4000$')
plt.scatter(x_10000, it_2_10000, color='blue')
plt.plot(x_10000, it_2_10000, linewidth=1.5, color='blue', label=r'W/o partition - $n = 10000$')
plt.scatter(x_1000, it_dist_2_1000, color='orange')
plt.plot(x_1000, it_dist_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'W/ partition - $n = 1000$')
plt.scatter(x_4000, it_dist_2_4000, color='red')
plt.plot(x_4000, it_dist_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'W/ partition - $n = 4000$')
plt.scatter(x_10000, it_dist_2_10000, color='blue')
plt.plot(x_10000, it_dist_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'W/ partition - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_dist_N_alpha_it_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"RKA using 4 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_4_1000, color='orange')
plt.plot(x_1000, it_4_1000, linewidth=1.5, color='orange', label=r'W/o partition - $n = 1000$')
plt.scatter(x_4000, it_4_4000, color='red')
plt.plot(x_4000, it_4_4000, linewidth=1.5, color='red', label=r'W/o partition - $n = 4000$')
plt.scatter(x_10000, it_4_10000, color='blue')
plt.plot(x_10000, it_4_10000, linewidth=1.5, color='blue', label=r'W/o partition - $n = 10000$')
plt.scatter(x_1000, it_dist_4_1000, color='orange')
plt.plot(x_1000, it_dist_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'W/ partition - $n = 1000$')
plt.scatter(x_4000, it_dist_4_4000, color='red')
plt.plot(x_4000, it_dist_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'W/ partition - $n = 4000$')
plt.scatter(x_10000, it_dist_4_10000, color='blue')
plt.plot(x_10000, it_dist_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'W/ partition - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_dist_N_alpha_it_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"RKA using 8 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, it_8_1000, color='orange')
plt.plot(x_1000, it_8_1000, linewidth=1.5, color='orange', label=r'W/o partition - $n = 1000$')
plt.scatter(x_4000, it_8_4000, color='red')
plt.plot(x_4000, it_8_4000, linewidth=1.5, color='red', label=r'W/o partition - $n = 4000$')
plt.scatter(x_10000, it_8_10000, color='blue')
plt.plot(x_10000, it_8_10000, linewidth=1.5, color='blue', label=r'W/o partition - $n = 10000$')
plt.scatter(x_1000, it_dist_8_1000, color='orange')
plt.plot(x_1000, it_dist_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'W/ partition - $n = 1000$')
plt.scatter(x_4000, it_dist_8_4000, color='red')
plt.plot(x_4000, it_dist_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'W/ partition - $n = 4000$')
plt.scatter(x_10000, it_dist_8_10000, color='blue')
plt.plot(x_10000, it_dist_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'W/ partition - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "RKA_dist_N_alpha_it_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"RKA using 2 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_2_1000, color='orange')
plt.plot(x_1000, time_2_1000, linewidth=1.5, color='orange', label=r'W/o partition - $n = 1000$')
plt.scatter(x_4000, time_2_4000, color='red')
plt.plot(x_4000, time_2_4000, linewidth=1.5, color='red', label=r'W/o partition - $n = 4000$')
plt.scatter(x_10000, time_2_10000, color='blue')
plt.plot(x_10000, time_2_10000, linewidth=1.5, color='blue', label=r'W/o partition - $n = 10000$')
plt.scatter(x_1000, time_dist_2_1000, color='orange')
plt.plot(x_1000, time_dist_2_1000, linestyle='--', linewidth=1.5, color='orange', label=r'W/ partition - $n = 1000$')
plt.scatter(x_4000, time_dist_2_4000, color='red')
plt.plot(x_4000, time_dist_2_4000, linestyle='--', linewidth=1.5, color='red', label=r'W/ partition - $n = 4000$')
plt.scatter(x_10000, time_dist_2_10000, color='blue')
plt.plot(x_10000, time_dist_2_10000, linestyle='--', linewidth=1.5, color='blue', label=r'W/ partition - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_dist_N_alpha_time_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"RKA using 4 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_4_1000, color='orange')
plt.plot(x_1000, time_4_1000, linewidth=1.5, color='orange', label=r'W/o partition - $n = 1000$')
plt.scatter(x_4000, time_4_4000, color='red')
plt.plot(x_4000, time_4_4000, linewidth=1.5, color='red', label=r'W/o partition - $n = 4000$')
plt.scatter(x_10000, time_4_10000, color='blue')
plt.plot(x_10000, time_4_10000, linewidth=1.5, color='blue', label=r'W/o partition - $n = 10000$')
plt.scatter(x_1000, time_dist_4_1000, color='orange')
plt.plot(x_1000, time_dist_4_1000, linestyle='--', linewidth=1.5, color='orange', label=r'W/ partition - $n = 1000$')
plt.scatter(x_4000, time_dist_4_4000, color='red')
plt.plot(x_4000, time_dist_4_4000, linestyle='--', linewidth=1.5, color='red', label=r'W/ partition - $n = 4000$')
plt.scatter(x_10000, time_dist_4_10000, color='blue')
plt.plot(x_10000, time_dist_4_10000, linestyle='--', linewidth=1.5, color='blue', label=r'W/ partition - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_dist_N_alpha_time_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r"RKA using 8 threads"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, time_8_1000, color='orange')
plt.plot(x_1000, time_8_1000, linewidth=1.5, color='orange', label=r'W/o partition - $n = 1000$')
plt.scatter(x_4000, time_8_4000, color='red')
plt.plot(x_4000, time_8_4000, linewidth=1.5, color='red', label=r'W/o partition - $n = 4000$')
plt.scatter(x_10000, time_8_10000, color='blue')
plt.plot(x_10000, time_8_10000, linewidth=1.5, color='blue', label=r'W/o partition - $n = 10000$')
plt.scatter(x_1000, time_dist_8_1000, color='orange')
plt.plot(x_1000, time_dist_8_1000, linestyle='--', linewidth=1.5, color='orange', label=r'W/ partition - $n = 1000$')
plt.scatter(x_4000, time_dist_8_4000, color='red')
plt.plot(x_4000, time_dist_8_4000, linestyle='--', linewidth=1.5, color='red', label=r'W/ partition - $n = 4000$')
plt.scatter(x_10000, time_dist_8_10000, color='blue')
plt.plot(x_10000, time_dist_8_10000, linestyle='--', linewidth=1.5, color='blue', label=r'W/ partition - $n = 10000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKA_dist_N_alpha_time_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')