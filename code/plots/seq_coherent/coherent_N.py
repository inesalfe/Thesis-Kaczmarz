import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq_coherent/coherent_N.py

x_1000 = [4000, 20000, 40000, 80000]

filename = "outputs/seq_coherent/RK_rand_coherent.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(1,5):
	it.append(int(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

RK_rand_it_1000 = it
RK_rand_time_1000 = time

filename = "outputs/seq_coherent/RK_coherent.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(1,5):
	it.append(int(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

RK_it_1000 = it
RK_time_1000 = time

filename = "outputs/seq_coherent/RK_cyclic_coherent.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(1,5):
	it.append(int(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

RK_cyclic_it_1000 = it
RK_cyclic_time_1000 = time

filename = "outputs/seq_coherent/RK_norep_rand_noshuffle_coherent.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(1,5):
	it.append(int(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

RK_norep_rand_noshuffle_it_1000 = it
RK_norep_rand_noshuffle_time_1000 = time

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r'Overdetermined systems with $n=1000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, RK_rand_time_1000, color='green', linewidth=2, label=r'SRK')
plt.scatter(x_1000, RK_rand_time_1000, color='green')
plt.plot(x_1000, RK_time_1000, color='orange', linewidth=2, label=r'RK')
plt.scatter(x_1000, RK_time_1000, color='orange')
plt.plot(x_1000, RK_cyclic_time_1000, color='red', linewidth=2, label=r'CK')
plt.scatter(x_1000, RK_cyclic_time_1000, color='red')
plt.plot(x_1000, RK_norep_rand_noshuffle_time_1000, color='blue', linewidth=2, label=r'SRKWOR')
plt.scatter(x_1000, RK_norep_rand_noshuffle_time_1000, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "coherent_N_time"

plt.show()
fig.savefig("plots/seq_coherent/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_coherent/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r'Overdetermined systems with $n=1000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_1000, RK_rand_it_1000, color='green', linewidth=2, label=r'SRK')
plt.scatter(x_1000, RK_rand_it_1000, color='green')
plt.plot(x_1000, RK_it_1000, color='orange', linewidth=2, label=r'RK')
plt.scatter(x_1000, RK_it_1000, color='orange')
plt.plot(x_1000, RK_cyclic_it_1000, color='red', linewidth=2, label=r'CK')
plt.scatter(x_1000, RK_cyclic_it_1000, color='red')
plt.plot(x_1000, RK_norep_rand_noshuffle_it_1000, color='blue', linewidth=2, label=r'SRKWOR')
plt.scatter(x_1000, RK_norep_rand_noshuffle_it_1000, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "coherent_N_it"

plt.show()
fig.savefig("plots/seq_coherent/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_coherent/png/"+filename_fig+".png", bbox_inches='tight')