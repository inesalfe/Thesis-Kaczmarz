import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq_sparse/sparse_real_RK_rand.py

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

filename = "outputs/seq_sparse/sparse_real_RK_norep_rand.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(int(lines[i].split()[2]))
	time.append(float(lines[i].split()[3]))

x_RK_norep_rand = range(1,file_size+1)
RK_norep_rand_it = it
RK_norep_rand_time = time

filename = "outputs/seq_sparse/sparse_real_RK_norep_rand_noshuffle.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(file_size):
	it.append(int(lines[i].split()[2]))
	time.append(float(lines[i].split()[3]))

x_RK_norep_rand_noshuffle = range(1,file_size+1)
RK_norep_rand_noshuffle_it = it
RK_norep_rand_noshuffle_time = time

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

plot_title = r'Simple Randomized Kaczmarz for sparse real systems'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_RK_rand, RK_rand_time, color='yellow', label=r'With replacement')
plt.scatter(x_RK_norep_rand_noshuffle, RK_norep_rand_noshuffle_time, color='orange', label=r'Without replacement without shuffling')
plt.scatter(x_RK_norep_rand, RK_norep_rand_time, color='red', label=r'Without replacement')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xticks(x, labels)
plt.ylabel(r'Total Time (s)')

filename_fig = "sparse_real_RK_rand_time.pdf"

# plt.show()
fig.savefig("plots/seq_sparse/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_sparse/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r'Simple Randomized Kaczmarz for sparse real systems'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_RK_rand, RK_rand_it, color='yellow', label=r'With replacement')
plt.scatter(x_RK_norep_rand_noshuffle, RK_norep_rand_noshuffle_it, color='orange', label=r'Without replacement without shuffling')
plt.scatter(x_RK_norep_rand, RK_norep_rand_it, color='red', label=r'Without replacement')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xticks(x, labels)
plt.ylabel(r'Iterations')

filename_fig = "sparse_real_RK_rand_it.pdf"

# plt.show()
fig.savefig("plots/seq_sparse/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_sparse/png/"+filename_fig+".png", bbox_inches='tight')