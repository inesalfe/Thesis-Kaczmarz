import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RK_partial_block_size.py

filename = "outputs/omp/RK_partial_block_size.txt";

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

speedup_2 = [time_par_1[i]/time_par_2[i] for i in range(5)]
speedup_4 = [time_par_1[i]/time_par_4[i] for i in range(5)]
speedup_8 = [time_par_1[i]/time_par_8[i] for i in range(5)]
x=[5, 10, 50, 100, 500]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"Evolution of speedup with block size for a matrix $80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.scatter(x, speedup_2, color='orange')
plt.plot(x, speedup_2, linewidth=1.5, color='orange', label=r'2 Threads')
plt.scatter(x, speedup_4, color='red')
plt.plot(x, speedup_4, linewidth=1.5, color='red', label=r'4 Threads')
plt.scatter(x, speedup_8, color='blue')
plt.plot(x, speedup_8, linewidth=1.5, color='blue', label=r'8 Threads')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_partial_block_size"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()