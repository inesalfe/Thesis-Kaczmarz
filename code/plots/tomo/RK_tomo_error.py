import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/tomo/RK_tomo_error.py ct_gaussian 19558 16384 50000000

# python3 plots/tomo/RK_tomo_error.py ct_poisson 19558 16384 30000000

if (len(sys.argv) != 5):
	exit()

data_set = sys.argv[1]
M = int(sys.argv[2])
N = int(sys.argv[3])
max_it = int(sys.argv[4])

if (data_set == "ct_gaussian"):
	error_folder = "errors/tomo_gauss/"
	output_foler = "_gauss/"
elif (data_set == "ct_poisson"):
	error_folder = "errors/tomo_poisson/"
	output_foler = "_poisson/"
else:
	exit()

filename = error_folder + "RK_error_" + str(M) + "_" + str(N) + "_1_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_1 = []
error_1 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_1.append(int(lines[i].split()[0]))
		error_1.append(float(lines[i].split()[1]))

filename = error_folder + "RK_error_" + str(M) + "_" + str(N) + "_2_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_2 = []
error_2 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_2.append(int(lines[i].split()[0]))
		error_2.append(float(lines[i].split()[1]))

filename = error_folder + "RK_error_" + str(M) + "_" + str(N) + "_3_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_3 = []
error_3 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_3.append(int(lines[i].split()[0]))
		error_3.append(float(lines[i].split()[1]))

filename = error_folder + "RK_error_" + str(M) + "_" + str(N) + "_4_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_4 = []
error_4 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error_4.append(int(lines[i].split()[0]))
		error_4.append(float(lines[i].split()[1]))

filename = error_folder + "RK_res_" + str(M) + "_" + str(N) + "_1_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_1 = []
res_1 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res_1.append(int(lines[i].split()[0]))
		res_1.append(float(lines[i].split()[1]))

filename = error_folder + "RK_res_" + str(M) + "_" + str(N) + "_2_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_2 = []
res_2 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res_2.append(int(lines[i].split()[0]))
		res_2.append(float(lines[i].split()[1]))

filename = error_folder + "RK_res_" + str(M) + "_" + str(N) + "_3_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_3 = []
res_3 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res_3.append(int(lines[i].split()[0]))
		res_3.append(float(lines[i].split()[1]))

filename = error_folder + "RK_res_" + str(M) + "_" + str(N) + "_4_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_4 = []
res_4 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res_4.append(int(lines[i].split()[0]))
		res_4.append(float(lines[i].split()[1]))

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'larger',
         'ytick.labelsize':'larger'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure(figsize=(10,7))

if (data_set == "ct_gaussian"):
	plt.plot(it_res_1, res_1, color='magenta', label=r'$\eta = 0.001$')
	plt.plot(it_res_2, res_2, color='orange', label=r'$\eta = 0.002$')
	plt.plot(it_res_3, res_3, color='red', label=r'$\eta = 0.004$')
	plt.plot(it_res_4, res_4, color='pink', label=r'$\eta = 0.008$')
elif (data_set == "ct_poisson"):
	plt.plot(it_res_1, res_1, color='magenta', label=r'$I_0 = 10^{13}$')
	plt.plot(it_res_2, res_2, color='orange', label=r'$I_0 = 4 \times 10^{13}$')
	plt.plot(it_res_3, res_3, color='red', label=r'$I_0 = 8 \times 10^{13}$')
	plt.plot(it_res_4, res_4, color='pink', label=r'$I_0 = 10^{14}$')

plt.grid()
plt.yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|A x^{(k)}-b\|$')

plt.legend(loc='best')

filename_fig = "RK_tomo_error_res_" + str(M) + "_" + str(N) + "_" + str(max_it)

# plt.show()
fig.savefig("plots/tomo/pdf"+output_foler+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/tomo/png"+output_foler+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10,7))

if (data_set == "ct_gaussian"):
	plt.plot(it_error_1, error_1, color='magenta', label=r'$\eta = 0.001$')
	plt.plot(it_error_2, error_2, color='orange', label=r'$\eta = 0.002$')
	plt.plot(it_error_3, error_3, color='red', label=r'$\eta = 0.004$')
	plt.plot(it_error_4, error_4, color='pink', label=r'$\eta = 0.008$')
	plt.scatter(it_error_1[error_1.index(min(error_1))], min(error_1), color='magenta', label=r'Minimum - $\eta = 0.001$')
	print(it_error_1[error_1.index(min(error_1))], end=' ')
	print(min(error_1))
	plt.scatter(it_error_2[error_2.index(min(error_2))], min(error_2), color='orange', label=r'Minimum - $\eta = 0.002$')
	print(it_error_2[error_2.index(min(error_2))], end=' ')
	print(min(error_2))
	plt.scatter(it_error_3[error_3.index(min(error_3))], min(error_3), color='red', label=r'Minimum - $\eta = 0.004$')
	print(it_error_3[error_3.index(min(error_3))], end=' ')
	print(min(error_3))
	plt.scatter(it_error_4[error_4.index(min(error_4))], min(error_4), color='pink', label=r'Minimum - $\eta = 0.008$')
	print(it_error_4[error_4.index(min(error_4))], end=' ')
	print(min(error_4))
elif (data_set == "ct_poisson"):
	plt.plot(it_error_1, error_1, color='magenta', label=r'$I_0 = 10^{13}$')
	plt.plot(it_error_2, error_2, color='orange', label=r'$I_0 = 4 \times 10^{13}$')
	plt.plot(it_error_3, error_3, color='red', label=r'$I_0 = 8 \times 10^{13}$')
	plt.plot(it_error_4, error_4, color='pink', label=r'$I_0 = 10^{14}$')
	plt.scatter(it_error_1[error_1.index(min(error_1))], min(error_1), color='magenta', label=r'Minimum - $I_0 = 10^{13}$')
	print(it_error_1[error_1.index(min(error_1))], end=' ')
	print(min(error_1))
	plt.scatter(it_error_2[error_2.index(min(error_2))], min(error_2), color='orange', label=r'Minimum - $I_0 = 4 \times 10^{13}$')
	print(it_error_2[error_2.index(min(error_2))], end=' ')
	print(min(error_2))
	plt.scatter(it_error_3[error_3.index(min(error_3))], min(error_3), color='red', label=r'Minimum - $I_0 = 8 \times 10^{13}$')
	print(it_error_3[error_3.index(min(error_3))], end=' ')
	print(min(error_3))
	plt.scatter(it_error_4[error_4.index(min(error_4))], min(error_4), color='pink', label=r'Minimum - $I_0 = 10^{14}$')
	print(it_error_4[error_4.index(min(error_4))], end=' ')
	print(min(error_4))

plt.grid()
plt.yscale('log')

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|x^{(k)}-\overline{x}\|$')

plt.legend(loc='best')

filename_fig = "RK_tomo_error_error_" + str(M) + "_" + str(N) + "_" + str(max_it)

# plt.show()
fig.savefig("plots/tomo/pdf"+output_foler+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/tomo/png"+output_foler+filename_fig+".png", bbox_inches='tight')
plt.close()