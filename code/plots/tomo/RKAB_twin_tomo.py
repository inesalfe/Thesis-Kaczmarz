import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/tomo/RKAB_twin_tomo.py ct_gaussian 19558 16384 3 1000 13 10 56 1


# python3 plots/tomo/RKAB_twin_tomo.py ct_poisson 19558 16384 3 1000 26 14 114 1


if (len(sys.argv) != 10):
	exit()

data_set = sys.argv[1]
M = int(sys.argv[2])
N = int(sys.argv[3])
seed = int(sys.argv[4])
max_it = int(sys.argv[5])
it_stop_1 = int(sys.argv[6])
it_stop_2 = int(sys.argv[7])
it_stop_4 = int(sys.argv[8])
it_stop_8 = int(sys.argv[9])

if (data_set == "ct_gaussian"):
	error_folder = "errors/tomo_gauss/"
	output_foler = "_gauss/"
elif (data_set == "ct_poisson"):
	error_folder = "errors/tomo_poisson/"
	output_foler = "_poisson/"
else:
	exit()

filename_1 = error_folder + "RKAB_twin_error_" + str(M) + "_" + str(N) + "_" + str(seed) + "_1_" + str(max_it) + ".txt"
with open(filename_1) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_1 = []
error_1 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_1.append(int(lines[i].split()[0]))
		error_1.append(float(lines[i].split()[1]))
filename_2 = error_folder + "RKAB_twin_error_" + str(M) + "_" + str(N) + "_" + str(seed) + "_2_" + str(max_it) + ".txt"
with open(filename_2) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_2 = []
error_2 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_2.append(int(lines[i].split()[0]))
		error_2.append(float(lines[i].split()[1]))
filename_4 = error_folder + "RKAB_twin_error_" + str(M) + "_" + str(N) + "_" + str(seed) + "_4_" + str(max_it) + ".txt"
with open(filename_4) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_4 = []
error_4 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_4.append(int(lines[i].split()[0]))
		error_4.append(float(lines[i].split()[1]))
filename_8 = error_folder + "RKAB_twin_error_" + str(M) + "_" + str(N) + "_" + str(seed) + "_8_" + str(max_it) + ".txt"
with open(filename_8) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_8 = []
error_8 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_8.append(int(lines[i].split()[0]))
		error_8.append(float(lines[i].split()[1]))

filename_1 = error_folder + "RKAB_twin_error_diff_" + str(M) + "_" + str(N) + "_" + str(seed) + "_1_" + str(max_it) + ".txt"
with open(filename_1) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_diff_1 = []
error_diff_1 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_diff_1.append(int(lines[i].split()[0]))
		error_diff_1.append(float(lines[i].split()[1]))
filename_2 = error_folder + "RKAB_twin_error_diff_" + str(M) + "_" + str(N) + "_" + str(seed) + "_2_" + str(max_it) + ".txt"
with open(filename_2) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_diff_2 = []
error_diff_2 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_diff_2.append(int(lines[i].split()[0]))
		error_diff_2.append(float(lines[i].split()[1]))
filename_4 = error_folder + "RKAB_twin_error_diff_" + str(M) + "_" + str(N) + "_" + str(seed) + "_4_" + str(max_it) + ".txt"
with open(filename_4) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_diff_4 = []
error_diff_4 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_diff_4.append(int(lines[i].split()[0]))
		error_diff_4.append(float(lines[i].split()[1]))
filename_8 = error_folder + "RKAB_twin_error_diff_" + str(M) + "_" + str(N) + "_" + str(seed) + "_8_" + str(max_it) + ".txt"
with open(filename_8) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_diff_8 = []
error_diff_8 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_diff_8.append(int(lines[i].split()[0]))
		error_diff_8.append(float(lines[i].split()[1]))

filename_1 = error_folder + "RKAB_twin_res_" + str(M) + "_" + str(N) + "_" + str(seed) + "_1_" + str(max_it) + ".txt"
with open(filename_1) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_1 = []
res_1 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res_1.append(int(lines[i].split()[0]))
		res_1.append(float(lines[i].split()[1]))
filename_2 = error_folder + "RKAB_twin_res_" + str(M) + "_" + str(N) + "_" + str(seed) + "_2_" + str(max_it) + ".txt"
with open(filename_2) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_2 = []
res_2 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res_2.append(int(lines[i].split()[0]))
		res_2.append(float(lines[i].split()[1]))
filename_4 = error_folder + "RKAB_twin_res_" + str(M) + "_" + str(N) + "_" + str(seed) + "_4_" + str(max_it) + ".txt"
with open(filename_4) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_4 = []
res_4 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res_4.append(int(lines[i].split()[0]))
		res_4.append(float(lines[i].split()[1]))
filename_8 = error_folder + "RKAB_twin_res_" + str(M) + "_" + str(N) + "_" + str(seed) + "_8_" + str(max_it) + ".txt"
with open(filename_8) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_8 = []
res_8 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res_8.append(int(lines[i].split()[0]))
		res_8.append(float(lines[i].split()[1]))

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure(figsize=(10,7))

plt.plot(it_error_diff_1, error_diff_1, color='magenta', label=r'$q = 1$')
plt.plot(it_error_diff_2, error_diff_2, color='orange', label=r'$q = 2$')
plt.plot(it_error_diff_4, error_diff_4, color='red', label=r'$q = 4$')
plt.plot(it_error_diff_8, error_diff_8, color='pink', label=r'$q = 8$')

plt.scatter(it_stop_1, error_diff_1[it_stop_1-1], color='magenta')
plt.scatter(it_stop_2, error_diff_2[it_stop_2-1], color='orange')
plt.scatter(it_stop_4, error_diff_4[it_stop_4-1], color='red')
plt.scatter(it_stop_8, error_diff_8[it_stop_8-1], color='pink')

# print(it_stop_1, end=' ')
# print(error_1[it_stop_1-1])
# print(it_stop_2, end=' ')
# print(error_2[it_stop_2-1])
# print(it_stop_4, end=' ')
# print(error_4[it_stop_4-1])
# print(it_stop_8, end=' ')
# print(error_8[it_stop_8-1])

plt.grid()
plt.yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|x_{up}-x_{down}\|$')

plt.legend(loc='best')

filename_fig = "RKAB_twin_tomo_error_diff_" + str(M) + "_" + str(N) + "_" + str(seed) + "_" + str(max_it)

plt.show()
fig.savefig("plots/tomo/pdf"+output_foler+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/tomo/png"+output_foler+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10,7))

plt.plot(it_error_1, error_1, color='magenta', label=r'$q = 1$')
plt.plot(it_error_2, error_2, color='orange', label=r'$q = 2$')
plt.plot(it_error_4, error_4, color='red', label=r'$q = 4$')
plt.plot(it_error_8, error_8, color='pink', label=r'$q = 8$')

plt.scatter(it_error_1[error_1.index(min(error_1))], min(error_1), color='magenta')
plt.scatter(it_error_2[error_2.index(min(error_2))], min(error_2), color='orange')
plt.scatter(it_error_4[error_4.index(min(error_4))], min(error_4), color='red')
plt.scatter(it_error_8[error_8.index(min(error_8))], min(error_8), color='pink')

print(it_error_1[error_1.index(min(error_1))], end=' ')
print(min(error_1))
print(it_error_2[error_2.index(min(error_2))], end=' ')
print(min(error_2))
print(it_error_4[error_4.index(min(error_4))], end=' ')
print(min(error_4))
print(it_error_8[error_8.index(min(error_8))], end=' ')
print(min(error_8))

plt.grid()
plt.yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|x^{(k)}-\overline{x}\|$')

plt.legend(loc='best')

filename_fig = "RKAB_twin_tomo_error_" + str(M) + "_" + str(N) + "_" + str(seed) + "_" + str(max_it)

plt.show()
fig.savefig("plots/tomo/pdf"+output_foler+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/tomo/png"+output_foler+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10,7))

plt.plot(it_res_1, res_1, color='magenta', label=r'$q = 1$')
plt.plot(it_res_2, res_2, color='orange', label=r'$q = 2$')
plt.plot(it_res_4, res_4, color='red', label=r'$q = 4$')
plt.plot(it_res_8, res_8, color='pink', label=r'$q = 8$')

plt.grid()
plt.yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|A x^{(k)}-b\|$')

plt.legend(loc='best')

filename_fig = "RKAB_twin_tomo_res_" + str(M) + "_" + str(N) + "_" + str(seed) + "_" + str(max_it)

plt.show()
fig.savefig("plots/tomo/pdf"+output_foler+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/tomo/png"+output_foler+filename_fig+".png", bbox_inches='tight')
plt.close()