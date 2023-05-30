import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_x_number_of_blocks_block_size_400_seq.py 80000 4000

if (len(sys.argv) != 3):
	exit()

M = int(sys.argv[1])
N = int(sys.argv[2])

filename = "outputs/omp/RK_seq.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))

filename = "outputs/omp/RKAB_400.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

# threads / n_repeat
# x -> Number of blocks

time_1_1 = []
time_1_2 = []
time_1_5 = []
time_1_10 = []
time_2_1 = []
time_2_2 = []
time_2_5 = []
time_2_10 = []
time_4_1 = []
time_4_2 = []
time_4_5 = []
time_4_10 = []
time_8_1 = []
time_8_2 = []
time_8_5 = []
time_8_10 = []
for i in range(7):
	time_1_1.append(float(lines[1+5*i].split()[2]))
	time_1_2.append(float(lines[36+5*i].split()[2]))
	time_1_5.append(float(lines[71+5*i].split()[2]))
	time_1_10.append(float(lines[106+5*i].split()[2]))
	time_2_1.append(float(lines[2+5*i].split()[2]))
	time_2_2.append(float(lines[37+5*i].split()[2]))
	time_2_5.append(float(lines[72+5*i].split()[2]))
	time_2_10.append(float(lines[107+5*i].split()[2]))
	time_4_1.append(float(lines[3+5*i].split()[2]))
	time_4_2.append(float(lines[38+5*i].split()[2]))
	time_4_5.append(float(lines[73+5*i].split()[2]))
	time_4_10.append(float(lines[108+5*i].split()[2]))
	time_8_1.append(float(lines[4+5*i].split()[2]))
	time_8_2.append(float(lines[39+5*i].split()[2]))
	time_8_5.append(float(lines[74+5*i].split()[2]))
	time_8_10.append(float(lines[109+5*i].split()[2]))

x = [1, 2, 4, 8, 16, 32, 64]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"No repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq[35], linestyle='--', color='black', label=r'Sequential')
plt.plot(x, time_2_1, color='red', label=r'Threads = 2')
plt.plot(x, time_4_1, color='blue', label=r'Threads = 4')
plt.plot(x, time_8_1, color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_number_of_blocks_block_size_400_seq_time_rep_1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq[35], linestyle='--', color='black', label=r'Sequential')
plt.plot(x, time_2_2, color='red', label=r'Threads = 2')
plt.plot(x, time_4_2, color='blue', label=r'Threads = 4')
plt.plot(x, time_8_2, color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_number_of_blocks_block_size_400_seq_time_rep_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq[35], linestyle='--', color='black', label=r'Sequential')
plt.plot(x, time_2_5, color='red', label=r'Threads = 2')
plt.plot(x, time_4_5, color='blue', label=r'Threads = 4')
plt.plot(x, time_8_5, color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_number_of_blocks_block_size_400_seq_time_rep_5"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq[35], linestyle='--', color='black', label=r'Sequential')
plt.plot(x, time_2_10, color='red', label=r'Threads = 2')
plt.plot(x, time_4_10, color='blue', label=r'Threads = 4')
plt.plot(x, time_8_10, color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of Blocks')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_number_of_blocks_block_size_400_seq_time_rep_10"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)