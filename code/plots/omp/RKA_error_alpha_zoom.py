import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# python3 plots/omp/RKA_error_alpha_zoom.py 80000 1000 30000 30000 281.449 20000 25000 250 500

# ./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 1 500000 100
# ./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 2 500000 100
# ./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 4 500000 100
# ./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 8 500000 100
# ./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 20 500000 100
# ./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 50 500000 100
# ./bin/RKA_seq_error_alpha.exe ls_dense 80000 1000 100 500000 100

if (len(sys.argv) != 10):
	exit()

M = int(sys.argv[1])
N = int(sys.argv[2])
max_it_error = int(sys.argv[3])
max_it_res = int(sys.argv[4])
res_norm = float(sys.argv[5])
x_min_res = float(sys.argv[6])
x_max_res = float(sys.argv[7])
y_min_res = float(sys.argv[8])
y_max_res = float(sys.argv[9])

# filename_1 = "errors/omp/RKA_res_alpha_" + str(M) + "_" + str(N) + "_1.txt"
# filename_2 = "errors/omp/RKA_res_alpha_" + str(M) + "_" + str(N) + "_2.txt"
# filename_4 = "errors/omp/RKA_res_alpha_" + str(M) + "_" + str(N) + "_4.txt"
# filename_8 = "errors/omp/RKA_res_alpha_" + str(M) + "_" + str(N) + "_8.txt"
# filename_20 = "errors/omp/RKA_res_alpha_" + str(M) + "_" + str(N) + "_20.txt"
# filename_50 = "errors/omp/RKA_res_alpha_" + str(M) + "_" + str(N) + "_50.txt"

# filename_fig2 = "RKA_res_alpha_zoom_" + str(M) + "_" + str(N)

filename_1 = "errors/omp/best_alpha/RKA_res_alpha_" + str(M) + "_" + str(N) + "_1.txt"
filename_2 = "errors/omp/best_alpha/RKA_res_alpha_" + str(M) + "_" + str(N) + "_2.txt"
filename_4 = "errors/omp/best_alpha/RKA_res_alpha_" + str(M) + "_" + str(N) + "_4.txt"
filename_8 = "errors/omp/best_alpha/RKA_res_alpha_" + str(M) + "_" + str(N) + "_8.txt"
filename_20 = "errors/omp/best_alpha/RKA_res_alpha_" + str(M) + "_" + str(N) + "_20.txt"
filename_50 = "errors/omp/best_alpha/RKA_res_alpha_" + str(M) + "_" + str(N) + "_50.txt"

filename_fig2 = "RKA_res_best_alpha_zoom_" + str(M) + "_" + str(N)

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
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(it_res_1, res_1, color='yellow', label=r'$q = 1$')
ax.plot(it_res_2, res_2, color='orange', label=r'$q = 2$')
ax.plot(it_res_4, res_4, color='red', label=r'$q = 4$')
ax.plot(it_res_8, res_8, color='pink', label=r'$q = 8$')
ax.plot(it_res_20, res_20, color='magenta', label=r'$q = 20$')
ax.plot(it_res_50, res_50, color='purple', label=r'$q = 50$')
ax.axhline(y=res_norm, color='black', linestyle='--', label=r'$\|Ax_{LS}-b\|$')

ax.grid()
plt.xlim([1, max(it_res_1)])
ax.set_yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|Ax^{(k)}-b\|$')

axins = zoomed_inset_axes(ax, 3, loc=1)
axins.plot(it_res_1, res_1, color='yellow', label=r'$q = 1$')
axins.plot(it_res_2, res_2, color='orange', label=r'$q = 2$')
axins.plot(it_res_4, res_4, color='red', label=r'$q = 4$')
axins.plot(it_res_8, res_8, color='pink', label=r'$q = 8$')
axins.plot(it_res_20, res_20, color='magenta', label=r'$q = 20$')
axins.plot(it_res_50, res_50, color='purple', label=r'$q = 50$')
axins.axhline(y=res_norm, color='black', linestyle='--', label=r'$\|Ax_{LS}-b\|$')
axins.set_xlim(x_min_res, x_max_res)
axins.set_ylim(y_min_res, y_max_res)

plt.xticks(visible=False)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

ax.legend(loc=2)

plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig2+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig2+".png", bbox_inches='tight')
plt.close(fig)