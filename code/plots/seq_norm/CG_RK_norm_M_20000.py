import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq_norm/CG_RK_norm_M_20000.py

x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000]

filename = "outputs/seq_norm/cg_norm_M_20000.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(8):
	time.append(float(lines[i].split()[3]))

cg_time_20000 = time

filename = "outputs/seq_norm/cgls_norm_M_20000.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(8):
	time.append(float(lines[i].split()[3]))

cgls_time_20000 = time

filename = "outputs/seq_norm/RK_norm_CG_M_20000.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(8):
	time.append(float(lines[i].split()[2]))

RK_time_20000 = time

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r'Overdetermined systems with $m=20000$ sampled from $N(0,1)$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_20000, cg_time_20000, color='green', linewidth=2, label=r'Conjugate Gradient')
plt.scatter(x_20000, cg_time_20000, color='green')
plt.plot(x_20000, cgls_time_20000, color='orange', linewidth=2, label=r'Conjugate Gradient for Least Squares')
plt.scatter(x_20000, cgls_time_20000, color='orange')
plt.plot(x_20000, RK_time_20000, color='red', linewidth=2, label=r'Randomized Kaczmarz')
plt.scatter(x_20000, RK_time_20000, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "CG_RK_norm_M_20000_time"

plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')