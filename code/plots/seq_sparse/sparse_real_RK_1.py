import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq_sparse/sparse_real_RK_1.py

filename = "outputs/seq_sparse/sparse_real_RK_rand.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(int(lines[i].split()[2]))
	time.append(float(lines[i].split()[3]))

x_RK_rand = range(1,file_size+1)
RK_rand_it = it
RK_rand_time = time

filename = "outputs/seq_sparse/sparse_real_RK_quasirand.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(int(lines[i].split()[2]))
	time.append(float(lines[i].split()[3]))

x_RK_quasirand = range(1,file_size+1)
RK_quasirand_it = it
RK_quasirand_time = time

filename = "outputs/seq_sparse/sparse_real_RK.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(int(lines[i].split()[2]))
	time.append(float(lines[i].split()[3]))

x_RK = range(1,file_size+1)
RK_it = it
RK_time = time

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = range(1,7)
labels = [r'$71952 \times 2704$', r'$171369\times 47271$', r'$477976 \times 1600$', r'$1748122 \times 62729$', r'$5921786 \times 274669$', r'$1548649 \times 955128$']

plot_title = r'Sparse real systems'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_RK_rand, RK_rand_time, color='yellow', label=r'Simple Randomized Kaczmarz (uniform distribution)')
plt.scatter(x_RK, RK_time, color='orange', label=r'Randomized Kaczmarz')
plt.scatter(x_RK_quasirand, RK_quasirand_time, color='red', label=r'Simple Randomized Kaczmarz (quasirandom numbers)')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xticks(x, labels)
plt.ylabel(r'Total Time (s)')

filename_fig = "sparse_real_RK_1_time.pdf"

# plt.show()
fig.savefig("plots/seq_sparse/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_sparse/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r'Sparse real systems'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_RK_rand, RK_rand_it, color='yellow', label=r'Simple Randomized Kaczmarz (uniform distribution)')
plt.scatter(x_RK, RK_it, color='orange', label=r'Randomized Kaczmarz')
plt.scatter(x_RK_quasirand, RK_quasirand_it, color='red', label=r'Simple Randomized Kaczmarz (quasirandom numbers)')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xticks(x, labels)
plt.ylabel(r'Iterations')

filename_fig = "sparse_real_RK_1_it.pdf"

# plt.show()
fig.savefig("plots/seq_sparse/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_sparse/png/"+filename_fig+".png", bbox_inches='tight')