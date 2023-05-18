import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RK_partial_error.py

filename = "errors/omp/RK_partial_op1.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

error_opt1 = []
it_opt1 = []
for i in range(file_size):
	error_opt1.append(float(lines[i].split()[0]))
	it_opt1.append((i+1)*10)

filename = "errors/omp/RK_partial_op2.txt"

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

error_opt2 = []
it_opt2 = []
for i in range(file_size):
	error_opt2.append(float(lines[i].split()[0]))
	it_opt2.append((i+1)*10)

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure(figsize=(10, 7))

plt.plot(it_opt1, error_opt1, linewidth=1.5, color='blue')

filename_fig = "plots/omp/RK_partial_opt1"

plt.grid()
plt.yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')
plt.xlim([min(it_opt1), max(it_opt1)])
plt.show()
fig.savefig("plots/omp/pdf/RK_partial_opt1.pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/RK_partial_opt1.png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))

plt.plot(it_opt2, error_opt2, linewidth=1.5, color='blue')

plt.grid()
plt.yscale('log')
plt.xlim([min(it_opt2), max(it_opt2)])
plt.xlabel(r'Iteration')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

plt.show()
fig.savefig("plots/omp/pdf/RK_partial_opt2.pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/RK_partial_opt2.png", bbox_inches='tight')