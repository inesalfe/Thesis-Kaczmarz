import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# ./bin/RKAB_seq_error.exe ls_dense 2000 100 1 50 25 5 1
# ./bin/RKAB_seq_error.exe ls_dense 2000 100 2 50 25 5 1
# ./bin/RKAB_seq_error.exe ls_dense 2000 100 4 50 25 5 1
# ./bin/RKAB_seq_error.exe ls_dense 2000 100 8 50 25 5 1
# ./bin/RKAB_seq_error.exe ls_dense 2000 100 20 50 25 5 1
# ./bin/RKAB_seq_error.exe ls_dense 2000 100 50 50 25 5 1
# ./bin/RKAB_seq_error.exe ls_dense 2000 100 100 50 25 5 1
# ./bin/RKAB_seq_error.exe ls_dense 2000 100 1000 50 25 5 1

# python3 plots/omp/RKAB_error.py 2000 100 50 5 25 25 42.9463

# ./bin/RKAB_seq_error.exe ls_dense 20000 1000 1 50 250 5 1
# ./bin/RKAB_seq_error.exe ls_dense 20000 1000 2 50 250 5 1
# ./bin/RKAB_seq_error.exe ls_dense 20000 1000 4 50 250 5 1
# ./bin/RKAB_seq_error.exe ls_dense 20000 1000 8 50 250 5 1
# ./bin/RKAB_seq_error.exe ls_dense 20000 1000 20 50 250 5 1
# ./bin/RKAB_seq_error.exe ls_dense 20000 1000 50 50 250 5 1
# ./bin/RKAB_seq_error.exe ls_dense 20000 1000 100 50 250 5 1
# ./bin/RKAB_seq_error.exe ls_dense 20000 1000 1000 50 250 5 1

# python3 plots/omp/RKAB_error.py 20000 1000 50 5 250 250 137.332

if (len(sys.argv) != 8):
	exit()

M = int(sys.argv[1])
N = int(sys.argv[2])
it_per_thread = int(sys.argv[3])
block_repeat = int(sys.argv[4])
max_it_error = int(sys.argv[5])
max_it_res = int(sys.argv[6])
res_norm = float(sys.argv[7])

filename_1 = "errors/omp/RKAB_error_" + str(M) + "_" + str(N) + "_1_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_2 = "errors/omp/RKAB_error_" + str(M) + "_" + str(N) + "_2_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_4 = "errors/omp/RKAB_error_" + str(M) + "_" + str(N) + "_4_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_8 = "errors/omp/RKAB_error_" + str(M) + "_" + str(N) + "_8_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_20 = "errors/omp/RKAB_error_" + str(M) + "_" + str(N) + "_20_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_50 = "errors/omp/RKAB_error_" + str(M) + "_" + str(N) + "_50_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_100 = "errors/omp/RKAB_error_" + str(M) + "_" + str(N) + "_100_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_1000 = "errors/omp/RKAB_error_" + str(M) + "_" + str(N) + "_1000_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"

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
with open(filename_100) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_100 = []
error_100 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_error):
		it_error_100.append(int(lines[i].split()[0]))
		error_100.append(float(lines[i].split()[1]))
with open(filename_1000) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error_1000 = []
error_1000 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_error):
		it_error_1000.append(int(lines[i].split()[0]))
		error_1000.append(float(lines[i].split()[1]))

filename_1 = "errors/omp/RKAB_res_" + str(M) + "_" + str(N) + "_1_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_2 = "errors/omp/RKAB_res_" + str(M) + "_" + str(N) + "_2_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_4 = "errors/omp/RKAB_res_" + str(M) + "_" + str(N) + "_4_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_8 = "errors/omp/RKAB_res_" + str(M) + "_" + str(N) + "_8_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_20 = "errors/omp/RKAB_res_" + str(M) + "_" + str(N) + "_20_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_50 = "errors/omp/RKAB_res_" + str(M) + "_" + str(N) + "_50_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_100 = "errors/omp/RKAB_res_" + str(M) + "_" + str(N) + "_100_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"
filename_1000 = "errors/omp/RKAB_res_" + str(M) + "_" + str(N) + "_1000_" + str(it_per_thread) + "_" + str(block_repeat) + ".txt"

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
with open(filename_100) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_100 = []
res_100 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_res):
		it_res_100.append(int(lines[i].split()[0]))
		res_100.append(float(lines[i].split()[1]))
with open(filename_1000) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res_1000 = []
res_1000 = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it_res):
		it_res_1000.append(int(lines[i].split()[0]))
		res_1000.append(float(lines[i].split()[1]))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig1 = plt.figure()

plot_title = r"Error evolution for a " + str(M) + " by " + str(N) + " matrix using the RKAB method w repetition"

plt.plot(it_error_1, error_1, color='yellow', label=r'$q = 1$')
plt.plot(it_error_2, error_2, color='orange', label=r'$q = 2$')
plt.plot(it_error_4, error_4, color='red', label=r'$q = 4$')
plt.plot(it_error_8, error_8, color='pink', label=r'$q = 8$')
plt.plot(it_error_20, error_20, color='magenta', label=r'$q = 20$')
plt.plot(it_error_50, error_50, color='purple', label=r'$q = 50$')
plt.plot(it_error_100, error_100, color='blue', label=r'$q = 100$')
plt.plot(it_error_1000, error_1000, color='black', label=r'$q = 1000$')

filename_fig1 = "RKAB_error_" + str(M) + "_" + str(N) + "_" + str(it_per_thread) + "_" + str(block_repeat)

plt.grid()
plt.yscale('log')
plt.title(plot_title)

plt.xlabel(r'Iteration')
plt.ylabel(r'$\|x_k-x^*\|$')

plt.legend(loc='best')
plt.show()
fig1.savefig("plots/omp/pdf/"+filename_fig1+".pdf", bbox_inches='tight')
fig1.savefig("plots/omp/png/"+filename_fig1+".png", bbox_inches='tight')
plt.close(fig1)

fig2 = plt.figure()

plot_title = r"Residual evolution for a " + str(M) + " by " + str(N) + " matrix using the RKAB method w repetition"

plt.plot(it_res_1, res_1, color='yellow', label=r'$q = 1$')
plt.plot(it_res_2, res_2, color='orange', label=r'$q = 2$')
plt.plot(it_res_4, res_4, color='red', label=r'$q = 4$')
plt.plot(it_res_8, res_8, color='pink', label=r'$q = 8$')
plt.plot(it_res_20, res_20, color='magenta', label=r'$q = 20$')
plt.plot(it_res_50, res_50, color='purple', label=r'$q = 50$')
plt.plot(it_res_100, res_100, color='blue', label=r'$q = 100$')
plt.plot(it_res_1000, res_1000, color='black', label=r'$q = 1000$')
plt.axhline(y=res_norm, color='grey', linestyle='--', label=r'$\|Ax_{LS}-b\|$')

filename_fig2 = "RKAB_res_" + str(M) + "_" + str(N) + "_" + str(it_per_thread) + "_" + str(block_repeat)

plt.grid()
plt.yscale('log')
plt.title(plot_title)

plt.xlabel(r'Iteration')
plt.ylabel(r'Residual')

plt.legend(loc='best')
plt.show()
fig2.savefig("plots/omp/pdf/"+filename_fig2+".pdf", bbox_inches='tight')
fig2.savefig("plots/omp/png/"+filename_fig2+".png", bbox_inches='tight')
plt.close(fig2)