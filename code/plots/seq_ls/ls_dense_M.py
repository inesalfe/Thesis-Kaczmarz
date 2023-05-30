import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq_ls/ls_dense_M.py

filename = "outputs/seq_ls/REK_ls_dense_max_it.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_REK = []
it_REK = []
for i in range(file_size):
	time_REK.append(float(lines[i].split()[2]))
	it_REK.append(int(lines[i].split()[3]))

filename = "outputs/seq_ls/RGS_ls_dense_max_it.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_RGS = []
it_RGS = []
for i in range(file_size):
	time_RGS.append(float(lines[i].split()[2]))
	it_RGS.append(int(lines[i].split()[3]))

filename = "outputs/seq_ls/cgls_ls_dense.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_CGLS = []
it_CGLS = []
for i in range(file_size):
	time_CGLS.append(float(lines[i].split()[3]))
	it_CGLS.append(int(lines[i].split()[2]))

x_2000 = [50, 100, 200, 500, 750]
x_4000 = [50, 100, 200, 500, 750, 1000]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000]
x_40000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]
x_80000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

it_REK_2000 = it_REK[0:5]
time_REK_2000 = time_REK[0:5]
it_RGS_2000 = it_RGS[0:5]
time_RGS_2000 = time_RGS[0:5]

it_REK_4000 = it_REK[5:11]
time_REK_4000 = time_REK[5:11]
it_RGS_4000 = it_RGS[5:11]
time_RGS_4000 = time_RGS[5:11]

it_REK_20000 = it_REK[11:19]
time_REK_20000 = time_REK[11:19]
it_RGS_20000 = it_RGS[11:19]
time_RGS_20000 = time_RGS[11:19]

it_REK_40000 = it_REK[19:28]
time_REK_40000 = time_REK[19:28]
it_RGS_40000 = it_RGS[19:28]
time_RGS_40000 = time_RGS[19:28]

it_REK_80000 = it_REK[28:37]
time_REK_80000 = time_REK[28:37]
it_RGS_80000 = it_RGS[28:37]
time_RGS_80000 = time_RGS[28:37]

it_CGLS_2000 = it_CGLS[0:5]
time_CGLS_2000 = time_CGLS[0:5]

it_CGLS_4000 = it_CGLS[5:11]
time_CGLS_4000 = time_CGLS[5:11]

it_CGLS_20000 = it_CGLS[11:19]
time_CGLS_20000 = time_CGLS[11:19]

it_CGLS_40000 = it_CGLS[19:28]
time_CGLS_40000 = time_CGLS[19:28]

it_CGLS_80000 = it_CGLS[28:37]
time_CGLS_80000 = time_CGLS[28:37]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# fig = plt.figure(figsize=(10, 7))
# plt.plot(x_2000, time_RGS_2000, color='red', linewidth=2, label=r'RGS')
# plt.scatter(x_2000, time_RGS_2000, color='red')
# plt.plot(x_2000, time_REK_2000, color='blue', linewidth=2, label=r'REK')
# plt.scatter(x_2000, time_REK_2000, color='blue')
# plt.grid()
# plt.legend()
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$n$')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "plots/seq_ls/ls_dense_M_time_2000"

# plt.show()
# fig.savefig(filename_fig+".pdf", bbox_inches='tight')
# fig.savefig(filename_fig+".png", bbox_inches='tight')

# fig = plt.figure(figsize=(10, 7))
# plt.plot(x_4000, time_RGS_4000, color='red', linewidth=2, label=r'RGS')
# plt.scatter(x_4000, time_RGS_4000, color='red')
# plt.plot(x_4000, time_REK_4000, color='blue', linewidth=2, label=r'REK')
# plt.scatter(x_4000, time_REK_4000, color='blue')
# plt.grid()
# plt.legend()
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$n$')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "plots/seq_ls/ls_dense_M_time_4000"

# plt.show()
# fig.savefig(filename_fig+".pdf", bbox_inches='tight')
# fig.savefig(filename_fig+".png", bbox_inches='tight')

# fig = plt.figure(figsize=(10, 7))
# plt.plot(x_20000, time_RGS_20000, color='red', linewidth=2, label=r'RGS')
# plt.scatter(x_20000, time_RGS_20000, color='red')
# plt.plot(x_20000, time_REK_20000, color='blue', linewidth=2, label=r'REK')
# plt.scatter(x_20000, time_REK_20000, color='blue')
# plt.grid()
# plt.legend()
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$n$')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "plots/seq_ls/ls_dense_M_time_20000"

# plt.show()
# fig.savefig(filename_fig+".pdf", bbox_inches='tight')
# fig.savefig(filename_fig+".png", bbox_inches='tight')

# fig = plt.figure(figsize=(10, 7))
# plt.plot(x_2000, it_RGS_2000, color='red', linewidth=2, label=r'RGS')
# plt.scatter(x_2000, it_RGS_2000, color='red')
# plt.plot(x_2000, it_REK_2000, color='blue', linewidth=2, label=r'REK')
# plt.scatter(x_2000, it_REK_2000, color='blue')
# plt.grid()
# plt.legend()
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$n$')
# plt.ylabel(r'Iterations')

# filename_fig = "plots/seq_ls/ls_dense_M_it_2000"

# plt.show()
# fig.savefig(filename_fig+".pdf", bbox_inches='tight')
# fig.savefig(filename_fig+".png", bbox_inches='tight')

# fig = plt.figure(figsize=(10, 7))
# plt.plot(x_4000, it_RGS_4000, color='red', linewidth=2, label=r'RGS')
# plt.scatter(x_4000, it_RGS_4000, color='red')
# plt.plot(x_4000, it_REK_4000, color='blue', linewidth=2, label=r'REK')
# plt.scatter(x_4000, it_REK_4000, color='blue')
# plt.grid()
# plt.legend()
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$n$')
# plt.ylabel(r'Iterations')

# filename_fig = "plots/seq_ls/ls_dense_M_it_4000"

# plt.show()
# fig.savefig(filename_fig+".pdf", bbox_inches='tight')
# fig.savefig(filename_fig+".png", bbox_inches='tight')

# fig = plt.figure(figsize=(10, 7))
# plt.plot(x_20000, it_RGS_20000, color='red', linewidth=2, label=r'RGS')
# plt.scatter(x_20000, it_RGS_20000, color='red')
# plt.plot(x_20000, it_REK_20000, color='blue', linewidth=2, label=r'REK')
# plt.scatter(x_20000, it_REK_20000, color='blue')
# plt.grid()
# plt.legend()
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$n$')
# plt.ylabel(r'Iterations')

# filename_fig = "plots/seq_ls/ls_dense_M_it_20000"

# plt.show()
# fig.savefig(filename_fig+".pdf", bbox_inches='tight')
# fig.savefig(filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.plot(x_20000, time_RGS_20000, color='orange', linewidth=2, label=r'RGS - $m=20000$')
plt.scatter(x_20000, time_RGS_20000, color='orange')
plt.plot(x_20000, time_REK_20000, color='orange', linestyle='--', linewidth=2, label=r'REK - $m=20000$')
plt.scatter(x_20000, time_REK_20000, color='orange')
plt.plot(x_40000, time_RGS_40000, color='red', linewidth=2, label=r'RGS - $m=40000$')
plt.scatter(x_40000, time_RGS_40000, color='red')
plt.plot(x_40000, time_REK_40000, color='red', linestyle='--', linewidth=2, label=r'REK - $m=40000$')
plt.scatter(x_40000, time_REK_40000, color='red')
plt.plot(x_80000, time_RGS_80000, color='blue', linewidth=2, label=r'RGS - $m=80000$')
plt.scatter(x_80000, time_RGS_80000, color='blue')
plt.plot(x_80000, time_REK_80000, color='blue', linestyle='--', linewidth=2, label=r'REK - $m=80000$')
plt.scatter(x_80000, time_REK_80000, color='blue')
plt.plot(x_20000, time_CGLS_20000, color='orange', linestyle='dashdot', linewidth=2, label=r'CGLS - $m=20000$')
plt.scatter(x_20000, time_CGLS_20000, color='orange')
plt.plot(x_40000, time_CGLS_40000, color='red', linestyle='dashdot', linewidth=2, label=r'CGLS - $m=40000$')
plt.scatter(x_40000, time_CGLS_40000, color='red')
plt.plot(x_80000, time_CGLS_80000, color='blue', linestyle='dashdot', linewidth=2, label=r'CGLS - $m=80000$')
plt.scatter(x_80000, time_CGLS_80000, color='blue')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "plots/seq_ls/ls_dense_M_time_all"

plt.show()
fig.savefig(filename_fig+".pdf", bbox_inches='tight')
fig.savefig(filename_fig+".png", bbox_inches='tight')

# fig = plt.figure(figsize=(10, 7))
# plt.plot(x_20000, it_RGS_20000, color='blue', linewidth=2, label=r'RGS - $m=20000$')
# plt.scatter(x_20000, it_RGS_20000, color='blue')
# plt.plot(x_20000, it_REK_20000, color='blue', linestyle='--', linewidth=2, label=r'REK - $m=20000$')
# plt.scatter(x_20000, it_REK_20000, color='blue')
# plt.plot(x_40000, it_RGS_40000, color='purple', linewidth=2, label=r'RGS - $m=40000$')
# plt.scatter(x_40000, it_RGS_40000, color='purple')
# plt.plot(x_40000, it_REK_40000, color='purple', linestyle='--', linewidth=2, label=r'REK - $m=40000$')
# plt.scatter(x_40000, it_REK_40000, color='purple')
# plt.plot(x_80000, it_RGS_80000, color='black', linewidth=2, label=r'RGS - $m=80000$')
# plt.scatter(x_80000, it_RGS_80000, color='black')
# plt.plot(x_80000, it_REK_80000, color='black', linestyle='--', linewidth=2, label=r'REK - $m=80000$')
# plt.scatter(x_80000, it_REK_80000, color='black')
# plt.plot(x_20000, it_CGLS_20000, color='blue', linestyle='dashdot', linewidth=2, label=r'CGLS - $m=20000$')
# plt.scatter(x_20000, it_CGLS_20000, color='blue')
# plt.plot(x_40000, it_CGLS_40000, color='purple', linestyle='dashdot', linewidth=2, label=r'CGLS - $m=40000$')
# plt.scatter(x_40000, it_CGLS_40000, color='purple')
# plt.plot(x_80000, it_CGLS_80000, color='black', linestyle='dashdot', linewidth=2, label=r'CGLS - $m=80000$')
# plt.scatter(x_80000, it_CGLS_80000, color='black')
# plt.grid()
# plt.legend()
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$n$')
# plt.ylabel(r'Iterations')

# filename_fig = "plots/seq_ls/ls_dense_M_it_all"

# plt.show()
# fig.savefig(filename_fig+".pdf", bbox_inches='tight')
# fig.savefig(filename_fig+".png", bbox_inches='tight')