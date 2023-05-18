import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_error_extra.py 80000 1000 1000 31 31 281.449

if (len(sys.argv) != 7):
	exit()

M = int(sys.argv[1])
N = int(sys.argv[2])
block = int(sys.argv[3])
max_it_error = int(sys.argv[4])
max_it_res = int(sys.argv[5])
res_norm = float(sys.argv[6])

filename_1 = "errors/omp/RKAB_single_error_" + str(M) + "_" + str(N) + "_" + str(block) + "_1.txt"
filename_2 = "errors/omp/RKAB_single_error_" + str(M) + "_" + str(N) + "_" + str(block) + "_2.txt"
filename_4 = "errors/omp/RKAB_single_error_" + str(M) + "_" + str(N) + "_" + str(block) + "_4.txt"
filename_8 = "errors/omp/RKAB_single_error_" + str(M) + "_" + str(N) + "_" + str(block) + "_8.txt"
filename_20 = "errors/omp/RKAB_single_error_" + str(M) + "_" + str(N) + "_" + str(block) + "_20.txt"
filename_50 = "errors/omp/RKAB_single_error_" + str(M) + "_" + str(N) + "_" + str(block) + "_50.txt"

with open(filename_1) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_1 = []
error_1 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_error):
		it_error_1.append(int(lines[i].split()[0]))
		error_1.append(float(lines[i].split()[1]))
with open(filename_2) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_2 = []
error_2 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_error):
		it_error_2.append(int(lines[i].split()[0]))
		error_2.append(float(lines[i].split()[1]))
with open(filename_4) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_4 = []
error_4 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_error):
		it_error_4.append(int(lines[i].split()[0]))
		error_4.append(float(lines[i].split()[1]))
with open(filename_8) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_8 = []
error_8 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_error):
		it_error_8.append(int(lines[i].split()[0]))
		error_8.append(float(lines[i].split()[1]))
with open(filename_20) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_20 = []
error_20 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_error):
		it_error_20.append(int(lines[i].split()[0]))
		error_20.append(float(lines[i].split()[1]))
with open(filename_50) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_50 = []
error_50 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_error):
		it_error_50.append(int(lines[i].split()[0]))
		error_50.append(float(lines[i].split()[1]))

filename_1 = "errors/omp/RKAB_single_res_" + str(M) + "_" + str(N) + "_" + str(block) + "_1.txt"
filename_2 = "errors/omp/RKAB_single_res_" + str(M) + "_" + str(N) + "_" + str(block) + "_2.txt"
filename_4 = "errors/omp/RKAB_single_res_" + str(M) + "_" + str(N) + "_" + str(block) + "_4.txt"
filename_8 = "errors/omp/RKAB_single_res_" + str(M) + "_" + str(N) + "_" + str(block) + "_8.txt"
filename_20 = "errors/omp/RKAB_single_res_" + str(M) + "_" + str(N) + "_" + str(block) + "_20.txt"
filename_50 = "errors/omp/RKAB_single_res_" + str(M) + "_" + str(N) + "_" + str(block) + "_50.txt"

with open(filename_1) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_1 = []
res_1 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_res):
		it_res_1.append(int(lines[i].split()[0]))
		res_1.append(float(lines[i].split()[1]))
with open(filename_2) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_2 = []
res_2 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_res):
		it_res_2.append(int(lines[i].split()[0]))
		res_2.append(float(lines[i].split()[1]))
with open(filename_4) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_4 = []
res_4 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_res):
		it_res_4.append(int(lines[i].split()[0]))
		res_4.append(float(lines[i].split()[1]))
with open(filename_8) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_8 = []
res_8 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_res):
		it_res_8.append(int(lines[i].split()[0]))
		res_8.append(float(lines[i].split()[1]))
with open(filename_20) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_20 = []
res_20 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_res):
		it_res_20.append(int(lines[i].split()[0]))
		res_20.append(float(lines[i].split()[1]))
with open(filename_50) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_50 = []
res_50 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_res):
		it_res_50.append(int(lines[i].split()[0]))
		res_50.append(float(lines[i].split()[1]))

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig1 = plt.figure(figsize=(10, 7))

plt.plot(it_error_1, error_1, color='yellow', label=r'$q = 1$')
plt.plot(it_error_2, error_2, color='orange', label=r'$q = 2$')
plt.plot(it_error_4, error_4, color='red', label=r'$q = 4$')
plt.plot(it_error_8, error_8, color='pink', label=r'$q = 8$')
plt.plot(it_error_20, error_20, color='magenta', label=r'$q = 20$')
plt.plot(it_error_50, error_50, color='purple', label=r'$q = 50$')

filename_fig1 = "RKAB_single_error_" + str(M) + "_" + str(N) + "_" + str(block)

plt.grid()
plt.xlim([1, max(it_res_1)])
plt.yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|x^{(k)}-x_{LS}\|$')

plt.legend(loc='best')
plt.show()
fig1.savefig("plots/omp/pdf/"+filename_fig1+".pdf", bbox_inches='tight')
fig1.savefig("plots/omp/png/"+filename_fig1+".png", bbox_inches='tight')
plt.close(fig1)

fig2 = plt.figure(figsize=(10, 7))

plt.plot(it_res_1, res_1, color='yellow', label=r'$q = 1$')
plt.plot(it_res_2, res_2, color='orange', label=r'$q = 2$')
plt.plot(it_res_4, res_4, color='red', label=r'$q = 4$')
plt.plot(it_res_8, res_8, color='pink', label=r'$q = 8$')
plt.plot(it_res_20, res_20, color='magenta', label=r'$q = 20$')
plt.plot(it_res_50, res_50, color='purple', label=r'$q = 50$')
plt.axhline(y=res_norm, color='grey', linestyle='--', label=r'$\|Ax_{LS}-b\|$')

filename_fig2 = "RKAB_single_res_" + str(M) + "_" + str(N) + "_" + str(block)

plt.grid()
plt.xlim([1, max(it_res_1)])
plt.yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|Ax^{(k)}-b\|$')

plt.legend(loc='best')
plt.show()
fig2.savefig("plots/omp/pdf/"+filename_fig2+".pdf", bbox_inches='tight')
fig2.savefig("plots/omp/png/"+filename_fig2+".png", bbox_inches='tight')
plt.close(fig2)