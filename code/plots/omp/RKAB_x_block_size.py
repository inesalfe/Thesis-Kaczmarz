import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_x_block_size.py 80000 4000

if (len(sys.argv) != 3):
	exit()

M = int(sys.argv[1])
N = int(sys.argv[2])

filename = "outputs/omp/RKAB_400.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_1_1_400 = []
time_1_2_400 = []
time_1_5_400 = []
time_1_10_400 = []
time_2_1_400 = []
time_2_2_400 = []
time_2_5_400 = []
time_2_10_400 = []
time_4_1_400 = []
time_4_2_400 = []
time_4_5_400 = []
time_4_10_400 = []
time_8_1_400 = []
time_8_2_400 = []
time_8_5_400 = []
time_8_10_400 = []
for i in range(7):
	time_1_1_400.append(float(lines[1+5*i].split()[2]))
	time_1_2_400.append(float(lines[36+5*i].split()[2]))
	time_1_5_400.append(float(lines[71+5*i].split()[2]))
	time_1_10_400.append(float(lines[106+5*i].split()[2]))
	time_2_1_400.append(float(lines[2+5*i].split()[2]))
	time_2_2_400.append(float(lines[37+5*i].split()[2]))
	time_2_5_400.append(float(lines[72+5*i].split()[2]))
	time_2_10_400.append(float(lines[107+5*i].split()[2]))
	time_4_1_400.append(float(lines[3+5*i].split()[2]))
	time_4_2_400.append(float(lines[38+5*i].split()[2]))
	time_4_5_400.append(float(lines[73+5*i].split()[2]))
	time_4_10_400.append(float(lines[108+5*i].split()[2]))
	time_8_1_400.append(float(lines[4+5*i].split()[2]))
	time_8_2_400.append(float(lines[39+5*i].split()[2]))
	time_8_5_400.append(float(lines[74+5*i].split()[2]))
	time_8_10_400.append(float(lines[109+5*i].split()[2]))

speedup_1_1_400 = np.zeros(7)
speedup_1_2_400 = np.zeros(7)
speedup_1_5_400 = np.zeros(7)
speedup_1_10_400 = np.zeros(7)
speedup_2_1_400 = np.zeros(7)
speedup_2_2_400 = np.zeros(7)
speedup_2_5_400 = np.zeros(7)
speedup_2_10_400 = np.zeros(7)
speedup_4_1_400 = np.zeros(7)
speedup_4_2_400 = np.zeros(7)
speedup_4_5_400 = np.zeros(7)
speedup_4_10_400 = np.zeros(7)
speedup_8_1_400 = np.zeros(7)
speedup_8_2_400 = np.zeros(7)
speedup_8_5_400 = np.zeros(7)
speedup_8_10_400 = np.zeros(7)
for i in range(7):
	speedup_1_1_400[i] = time_1_1_400[i]/time_1_1_400[i];
	speedup_1_2_400[i] = time_1_2_400[i]/time_1_2_400[i];
	speedup_1_5_400[i] = time_1_5_400[i]/time_1_5_400[i];
	speedup_1_10_400[i] = time_1_10_400[i]/time_1_10_400[i];
	speedup_2_1_400[i] = time_1_1_400[i]/time_2_1_400[i];
	speedup_2_2_400[i] = time_1_2_400[i]/time_2_2_400[i];
	speedup_2_5_400[i] = time_1_5_400[i]/time_2_5_400[i];
	speedup_2_10_400[i] = time_1_10_400[i]/time_2_10_400[i];
	speedup_4_1_400[i] = time_1_1_400[i]/time_4_1_400[i];
	speedup_4_2_400[i] = time_1_2_400[i]/time_4_2_400[i];
	speedup_4_5_400[i] = time_1_5_400[i]/time_4_5_400[i];
	speedup_4_10_400[i] = time_1_10_400[i]/time_4_10_400[i];
	speedup_8_1_400[i] = time_1_1_400[i]/time_8_1_400[i];
	speedup_8_2_400[i] = time_1_2_400[i]/time_8_2_400[i];
	speedup_8_5_400[i] = time_1_5_400[i]/time_8_5_400[i];
	speedup_8_10_400[i] = time_1_10_400[i]/time_8_10_400[i];

filename = "outputs/omp/RKAB_200.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_1_1_200 = []
time_1_2_200 = []
time_1_5_200 = []
time_1_10_200 = []
time_2_1_200 = []
time_2_2_200 = []
time_2_5_200 = []
time_2_10_200 = []
time_4_1_200 = []
time_4_2_200 = []
time_4_5_200 = []
time_4_10_200 = []
time_8_1_200 = []
time_8_2_200 = []
time_8_5_200 = []
time_8_10_200 = []
for i in range(7):
	time_1_1_200.append(float(lines[1+5*i].split()[2]))
	time_1_2_200.append(float(lines[36+5*i].split()[2]))
	time_1_5_200.append(float(lines[71+5*i].split()[2]))
	time_1_10_200.append(float(lines[106+5*i].split()[2]))
	time_2_1_200.append(float(lines[2+5*i].split()[2]))
	time_2_2_200.append(float(lines[37+5*i].split()[2]))
	time_2_5_200.append(float(lines[72+5*i].split()[2]))
	time_2_10_200.append(float(lines[107+5*i].split()[2]))
	time_4_1_200.append(float(lines[3+5*i].split()[2]))
	time_4_2_200.append(float(lines[38+5*i].split()[2]))
	time_4_5_200.append(float(lines[73+5*i].split()[2]))
	time_4_10_200.append(float(lines[108+5*i].split()[2]))
	time_8_1_200.append(float(lines[4+5*i].split()[2]))
	time_8_2_200.append(float(lines[39+5*i].split()[2]))
	time_8_5_200.append(float(lines[74+5*i].split()[2]))
	time_8_10_200.append(float(lines[109+5*i].split()[2]))

speedup_1_1_200 = np.zeros(7)
speedup_1_2_200 = np.zeros(7)
speedup_1_5_200 = np.zeros(7)
speedup_1_10_200 = np.zeros(7)
speedup_2_1_200 = np.zeros(7)
speedup_2_2_200 = np.zeros(7)
speedup_2_5_200 = np.zeros(7)
speedup_2_10_200 = np.zeros(7)
speedup_4_1_200 = np.zeros(7)
speedup_4_2_200 = np.zeros(7)
speedup_4_5_200 = np.zeros(7)
speedup_4_10_200 = np.zeros(7)
speedup_8_1_200 = np.zeros(7)
speedup_8_2_200 = np.zeros(7)
speedup_8_5_200 = np.zeros(7)
speedup_8_10_200 = np.zeros(7)
for i in range(7):
	speedup_1_1_200[i] = time_1_1_200[i]/time_1_1_200[i];
	speedup_1_2_200[i] = time_1_2_200[i]/time_1_2_200[i];
	speedup_1_5_200[i] = time_1_5_200[i]/time_1_5_200[i];
	speedup_1_10_200[i] = time_1_10_200[i]/time_1_10_200[i];
	speedup_2_1_200[i] = time_1_1_200[i]/time_2_1_200[i];
	speedup_2_2_200[i] = time_1_2_200[i]/time_2_2_200[i];
	speedup_2_5_200[i] = time_1_5_200[i]/time_2_5_200[i];
	speedup_2_10_200[i] = time_1_10_200[i]/time_2_10_200[i];
	speedup_4_1_200[i] = time_1_1_200[i]/time_4_1_200[i];
	speedup_4_2_200[i] = time_1_2_200[i]/time_4_2_200[i];
	speedup_4_5_200[i] = time_1_5_200[i]/time_4_5_200[i];
	speedup_4_10_200[i] = time_1_10_200[i]/time_4_10_200[i];
	speedup_8_1_200[i] = time_1_1_200[i]/time_8_1_200[i];
	speedup_8_2_200[i] = time_1_2_200[i]/time_8_2_200[i];
	speedup_8_5_200[i] = time_1_5_200[i]/time_8_5_200[i];
	speedup_8_10_200[i] = time_1_10_200[i]/time_8_10_200[i];

filename = "outputs/omp/RKAB_50.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_1_1_50 = []
time_1_2_50 = []
time_1_5_50 = []
time_1_10_50 = []
time_2_1_50 = []
time_2_2_50 = []
time_2_5_50 = []
time_2_10_50 = []
time_4_1_50 = []
time_4_2_50 = []
time_4_5_50 = []
time_4_10_50 = []
time_8_1_50 = []
time_8_2_50 = []
time_8_5_50 = []
time_8_10_50 = []
for i in range(7):
	time_1_1_50.append(float(lines[1+5*i].split()[2]))
	time_1_2_50.append(float(lines[36+5*i].split()[2]))
	time_1_5_50.append(float(lines[71+5*i].split()[2]))
	time_1_10_50.append(float(lines[106+5*i].split()[2]))
	time_2_1_50.append(float(lines[2+5*i].split()[2]))
	time_2_2_50.append(float(lines[37+5*i].split()[2]))
	time_2_5_50.append(float(lines[72+5*i].split()[2]))
	time_2_10_50.append(float(lines[107+5*i].split()[2]))
	time_4_1_50.append(float(lines[3+5*i].split()[2]))
	time_4_2_50.append(float(lines[38+5*i].split()[2]))
	time_4_5_50.append(float(lines[73+5*i].split()[2]))
	time_4_10_50.append(float(lines[108+5*i].split()[2]))
	time_8_1_50.append(float(lines[4+5*i].split()[2]))
	time_8_2_50.append(float(lines[39+5*i].split()[2]))
	time_8_5_50.append(float(lines[74+5*i].split()[2]))
	time_8_10_50.append(float(lines[109+5*i].split()[2]))

speedup_1_1_50 = np.zeros(7)
speedup_1_2_50 = np.zeros(7)
speedup_1_5_50 = np.zeros(7)
speedup_1_10_50 = np.zeros(7)
speedup_2_1_50 = np.zeros(7)
speedup_2_2_50 = np.zeros(7)
speedup_2_5_50 = np.zeros(7)
speedup_2_10_50 = np.zeros(7)
speedup_4_1_50 = np.zeros(7)
speedup_4_2_50 = np.zeros(7)
speedup_4_5_50 = np.zeros(7)
speedup_4_10_50 = np.zeros(7)
speedup_8_1_50 = np.zeros(7)
speedup_8_2_50 = np.zeros(7)
speedup_8_5_50 = np.zeros(7)
speedup_8_10_50 = np.zeros(7)
for i in range(7):
	speedup_1_1_50[i] = time_1_1_50[i]/time_1_1_50[i];
	speedup_1_2_50[i] = time_1_2_50[i]/time_1_2_50[i];
	speedup_1_5_50[i] = time_1_5_50[i]/time_1_5_50[i];
	speedup_1_10_50[i] = time_1_10_50[i]/time_1_10_50[i];
	speedup_2_1_50[i] = time_1_1_50[i]/time_2_1_50[i];
	speedup_2_2_50[i] = time_1_2_50[i]/time_2_2_50[i];
	speedup_2_5_50[i] = time_1_5_50[i]/time_2_5_50[i];
	speedup_2_10_50[i] = time_1_10_50[i]/time_2_10_50[i];
	speedup_4_1_50[i] = time_1_1_50[i]/time_4_1_50[i];
	speedup_4_2_50[i] = time_1_2_50[i]/time_4_2_50[i];
	speedup_4_5_50[i] = time_1_5_50[i]/time_4_5_50[i];
	speedup_4_10_50[i] = time_1_10_50[i]/time_4_10_50[i];
	speedup_8_1_50[i] = time_1_1_50[i]/time_8_1_50[i];
	speedup_8_2_50[i] = time_1_2_50[i]/time_8_2_50[i];
	speedup_8_5_50[i] = time_1_5_50[i]/time_8_5_50[i];
	speedup_8_10_50[i] = time_1_10_50[i]/time_8_10_50[i];

x = [50, 200, 400]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r"8 blocks with no repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_1_50[3], time_1_1_200[3], time_1_1_400[3]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_1_50[3], time_2_1_200[3], time_2_1_400[3]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_1_50[3], time_4_1_200[3], time_4_1_400[3]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_1_50[3], time_8_1_200[3], time_8_1_400[3]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_1_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with no repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_1_50[3], speedup_1_1_200[3], speedup_1_1_400[3]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_1_50[3], speedup_2_1_200[3], speedup_2_1_400[3]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_1_50[3], speedup_4_1_200[3], speedup_4_1_400[3]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_1_50[3], speedup_8_1_200[3], speedup_8_1_400[3]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_1_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with no repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_1_50[4], time_1_1_200[4], time_1_1_400[4]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_1_50[4], time_2_1_200[4], time_2_1_400[4]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_1_50[4], time_4_1_200[4], time_4_1_400[4]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_1_50[4], time_8_1_200[4], time_8_1_400[4]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_1_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with no repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_1_50[4], speedup_1_1_200[4], speedup_1_1_400[4]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_1_50[4], speedup_2_1_200[4], speedup_2_1_400[4]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_1_50[4], speedup_4_1_200[4], speedup_4_1_400[4]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_1_50[4], speedup_8_1_200[4], speedup_8_1_400[4]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_1_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with no repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_1_50[5], time_1_1_200[5], time_1_1_400[5]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_1_50[5], time_2_1_200[5], time_2_1_400[5]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_1_50[5], time_4_1_200[5], time_4_1_400[5]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_1_50[5], time_8_1_200[5], time_8_1_400[5]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_1_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with no repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_1_50[5], speedup_1_1_200[5], speedup_1_1_400[5]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_1_50[5], speedup_2_1_200[5], speedup_2_1_400[5]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_1_50[5], speedup_4_1_200[5], speedup_4_1_400[5]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_1_50[5], speedup_8_1_200[5], speedup_8_1_400[5]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_1_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with no repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_1_50[6], time_1_1_200[6], time_1_1_400[6]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_1_50[6], time_2_1_200[6], time_2_1_400[6]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_1_50[6], time_4_1_200[6], time_4_1_400[6]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_1_50[6], time_8_1_200[6], time_8_1_400[6]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_1_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with no repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_1_50[6], speedup_1_1_200[6], speedup_1_1_400[6]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_1_50[6], speedup_2_1_200[6], speedup_2_1_400[6]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_1_50[6], speedup_4_1_200[6], speedup_4_1_400[6]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_1_50[6], speedup_8_1_200[6], speedup_8_1_400[6]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_1_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_2_50[3], time_1_2_200[3], time_1_2_400[3]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_2_50[3], time_2_2_200[3], time_2_2_400[3]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_2_50[3], time_4_2_200[3], time_4_2_400[3]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_2_50[3], time_8_2_200[3], time_8_2_400[3]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_2_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_2_50[3], speedup_1_2_200[3], speedup_1_2_400[3]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_2_50[3], speedup_2_2_200[3], speedup_2_2_400[3]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_2_50[3], speedup_4_2_200[3], speedup_4_2_400[3]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_2_50[3], speedup_8_2_200[3], speedup_8_2_400[3]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_2_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_2_50[4], time_1_2_200[4], time_1_2_400[4]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_2_50[4], time_2_2_200[4], time_2_2_400[4]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_2_50[4], time_4_2_200[4], time_4_2_400[4]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_2_50[4], time_8_2_200[4], time_8_2_400[4]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_2_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_2_50[4], speedup_1_2_200[4], speedup_1_2_400[4]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_2_50[4], speedup_2_2_200[4], speedup_2_2_400[4]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_2_50[4], speedup_4_2_200[4], speedup_4_2_400[4]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_2_50[4], speedup_8_2_200[4], speedup_8_2_400[4]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_2_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_2_50[5], time_1_2_200[5], time_1_2_400[5]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_2_50[5], time_2_2_200[5], time_2_2_400[5]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_2_50[5], time_4_2_200[5], time_4_2_400[5]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_2_50[5], time_8_2_200[5], time_8_2_400[5]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_2_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_2_50[5], speedup_1_2_200[5], speedup_1_2_400[5]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_2_50[5], speedup_2_2_200[5], speedup_2_2_400[5]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_2_50[5], speedup_4_2_200[5], speedup_4_2_400[5]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_2_50[5], speedup_8_2_200[5], speedup_8_2_400[5]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_2_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_2_50[6], time_1_2_200[6], time_1_2_400[6]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_2_50[6], time_2_2_200[6], time_2_2_400[6]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_2_50[6], time_4_2_200[6], time_4_2_400[6]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_2_50[6], time_8_2_200[6], time_8_2_400[6]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_2_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_2_50[6], speedup_1_2_200[6], speedup_1_2_400[6]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_2_50[6], speedup_2_2_200[6], speedup_2_2_400[6]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_2_50[6], speedup_4_2_200[6], speedup_4_2_400[6]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_2_50[6], speedup_8_2_200[6], speedup_8_2_400[6]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_2_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_5_50[3], time_1_5_200[3], time_1_5_400[3]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_5_50[3], time_2_5_200[3], time_2_5_400[3]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_5_50[3], time_4_5_200[3], time_4_5_400[3]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_5_50[3], time_8_5_200[3], time_8_5_400[3]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_5_50[3], speedup_1_5_200[3], speedup_1_5_400[3]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_5_50[3], speedup_2_5_200[3], speedup_2_5_400[3]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_5_50[3], speedup_4_5_200[3], speedup_4_5_400[3]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_5_50[3], speedup_8_5_200[3], speedup_8_5_400[3]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_5_50[4], time_1_5_200[4], time_1_5_400[4]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_5_50[4], time_2_5_200[4], time_2_5_400[4]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_5_50[4], time_4_5_200[4], time_4_5_400[4]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_5_50[4], time_8_5_200[4], time_8_5_400[4]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_5_50[4], speedup_1_5_200[4], speedup_1_5_400[4]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_5_50[4], speedup_2_5_200[4], speedup_2_5_400[4]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_5_50[4], speedup_4_5_200[4], speedup_4_5_400[4]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_5_50[4], speedup_8_5_200[4], speedup_8_5_400[4]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_5_50[5], time_1_5_200[5], time_1_5_400[5]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_5_50[5], time_2_5_200[5], time_2_5_400[5]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_5_50[5], time_4_5_200[5], time_4_5_400[5]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_5_50[5], time_8_5_200[5], time_8_5_400[5]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_5_50[5], speedup_1_5_200[5], speedup_1_5_400[5]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_5_50[5], speedup_2_5_200[5], speedup_2_5_400[5]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_5_50[5], speedup_4_5_200[5], speedup_4_5_400[5]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_5_50[5], speedup_8_5_200[5], speedup_8_5_400[5]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_5_50[6], time_1_5_200[6], time_1_5_400[6]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_5_50[6], time_2_5_200[6], time_2_5_400[6]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_5_50[6], time_4_5_200[6], time_4_5_400[6]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_5_50[6], time_8_5_200[6], time_8_5_400[6]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_5_50[6], speedup_1_5_200[6], speedup_1_5_400[6]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_5_50[6], speedup_2_5_200[6], speedup_2_5_400[6]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_5_50[6], speedup_4_5_200[6], speedup_4_5_400[6]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_5_50[6], speedup_8_5_200[6], speedup_8_5_400[6]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_10_50[3], time_1_10_200[3], time_1_10_400[3]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_10_50[3], time_2_10_200[3], time_2_10_400[3]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_10_50[3], time_4_10_200[3], time_4_10_400[3]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_10_50[3], time_8_10_200[3], time_8_10_400[3]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_10_50[3], speedup_1_10_200[3], speedup_1_10_400[3]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_10_50[3], speedup_2_10_200[3], speedup_2_10_400[3]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_10_50[3], speedup_4_10_200[3], speedup_4_10_400[3]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_10_50[3], speedup_8_10_200[3], speedup_8_10_400[3]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_10_50[4], time_1_10_200[4], time_1_10_400[4]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_10_50[4], time_2_10_200[4], time_2_10_400[4]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_10_50[4], time_4_10_200[4], time_4_10_400[4]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_10_50[4], time_8_10_200[4], time_8_10_400[4]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_10_50[4], speedup_1_10_200[4], speedup_1_10_400[4]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_10_50[4], speedup_2_10_200[4], speedup_2_10_400[4]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_10_50[4], speedup_4_10_200[4], speedup_4_10_400[4]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_10_50[4], speedup_8_10_200[4], speedup_8_10_400[4]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_10_50[5], time_1_10_200[5], time_1_10_400[5]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_10_50[5], time_2_10_200[5], time_2_10_400[5]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_10_50[5], time_4_10_200[5], time_4_10_400[5]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_10_50[5], time_8_10_200[5], time_8_10_400[5]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_10_50[5], speedup_1_10_200[5], speedup_1_10_400[5]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_10_50[5], speedup_2_10_200[5], speedup_2_10_400[5]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_10_50[5], speedup_4_10_200[5], speedup_4_10_400[5]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_10_50[5], speedup_8_10_200[5], speedup_8_10_400[5]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_10_50[6], time_1_10_200[6], time_1_10_400[6]], color='orange', label=r'Threads = 1')
plt.plot(x, [time_2_10_50[6], time_2_10_200[6], time_2_10_400[6]], color='red', label=r'Threads = 2')
plt.plot(x, [time_4_10_50[6], time_4_10_200[6], time_4_10_400[6]], color='blue', label=r'Threads = 4')
plt.plot(x, [time_8_10_50[6], time_8_10_200[6], time_8_10_400[6]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_10_50[6], speedup_1_10_200[6], speedup_1_10_400[6]], color='orange', label=r'Threads = 1')
plt.plot(x, [speedup_2_10_50[6], speedup_2_10_200[6], speedup_2_10_400[6]], color='red', label=r'Threads = 2')
plt.plot(x, [speedup_4_10_50[6], speedup_4_10_200[6], speedup_4_10_400[6]], color='blue', label=r'Threads = 4')
plt.plot(x, [speedup_8_10_50[6], speedup_8_10_200[6], speedup_8_10_400[6]], color='purple', label=r'Threads = 8')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 1 thread - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_1_50[3], time_1_1_200[3], time_1_1_400[3]], color='orange', label=r'No repetitions')
plt.plot(x, [time_1_2_50[3], time_1_2_200[3], time_1_2_400[3]], color='red', label=r'2 repetitions')
plt.plot(x, [time_1_5_50[3], time_1_5_200[3], time_1_5_400[3]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_1_10_50[3], time_1_10_200[3], time_1_10_400[3]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_1_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 1 thread - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_1_50[3], speedup_1_1_200[3], speedup_1_1_400[3]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_1_2_50[3], speedup_1_2_200[3], speedup_1_2_400[3]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_1_5_50[3], speedup_1_5_200[3], speedup_1_5_400[3]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_1_10_50[3], speedup_1_10_200[3], speedup_1_10_400[3]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_1_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 1 thread - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_1_50[4], time_1_1_200[4], time_1_1_400[4]], color='orange', label=r'No repetitions')
plt.plot(x, [time_1_2_50[4], time_1_2_200[4], time_1_2_400[4]], color='red', label=r'2 repetitions')
plt.plot(x, [time_1_5_50[4], time_1_5_200[4], time_1_5_400[4]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_1_10_50[4], time_1_10_200[4], time_1_10_400[4]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_1_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 1 thread - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_1_50[4], speedup_1_1_200[4], speedup_1_1_400[4]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_1_2_50[4], speedup_1_2_200[4], speedup_1_2_400[4]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_1_5_50[4], speedup_1_5_200[4], speedup_1_5_400[4]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_1_10_50[4], speedup_1_10_200[4], speedup_1_10_400[4]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_1_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 1 thread - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_1_50[5], time_1_1_200[5], time_1_1_400[5]], color='orange', label=r'No repetitions')
plt.plot(x, [time_1_2_50[5], time_1_2_200[5], time_1_2_400[5]], color='red', label=r'2 repetitions')
plt.plot(x, [time_1_5_50[5], time_1_5_200[5], time_1_5_400[5]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_1_10_50[5], time_1_10_200[5], time_1_10_400[5]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_1_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 1 thread - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_1_50[5], speedup_1_1_200[5], speedup_1_1_400[5]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_1_2_50[5], speedup_1_2_200[5], speedup_1_2_400[5]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_1_5_50[5], speedup_1_5_200[5], speedup_1_5_400[5]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_1_10_50[5], speedup_1_10_200[5], speedup_1_10_400[5]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_1_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 1 thread - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_1_1_50[6], time_1_1_200[6], time_1_1_400[6]], color='orange', label=r'No repetitions')
plt.plot(x, [time_1_2_50[6], time_1_2_200[6], time_1_2_400[6]], color='red', label=r'2 repetitions')
plt.plot(x, [time_1_5_50[6], time_1_5_200[6], time_1_5_400[6]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_1_10_50[6], time_1_10_200[6], time_1_10_400[6]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_1_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 1 thread - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_1_1_50[6], speedup_1_1_200[6], speedup_1_1_400[6]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_1_2_50[6], speedup_1_2_200[6], speedup_1_2_400[6]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_1_5_50[6], speedup_1_5_200[6], speedup_1_5_400[6]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_1_10_50[6], speedup_1_10_200[6], speedup_1_10_400[6]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_1_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_2_1_50[3], time_2_1_200[3], time_2_1_400[3]], color='orange', label=r'No repetitions')
plt.plot(x, [time_2_2_50[3], time_2_2_200[3], time_2_2_400[3]], color='red', label=r'2 repetitions')
plt.plot(x, [time_2_5_50[3], time_2_5_200[3], time_2_5_400[3]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_2_10_50[3], time_2_10_200[3], time_2_10_400[3]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_2_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_2_1_50[3], speedup_2_1_200[3], speedup_2_1_400[3]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_2_2_50[3], speedup_2_2_200[3], speedup_2_2_400[3]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_2_5_50[3], speedup_2_5_200[3], speedup_2_5_400[3]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_2_10_50[3], speedup_2_10_200[3], speedup_2_10_400[3]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_2_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_2_1_50[4], time_2_1_200[4], time_2_1_400[4]], color='orange', label=r'No repetitions')
plt.plot(x, [time_2_2_50[4], time_2_2_200[4], time_2_2_400[4]], color='red', label=r'2 repetitions')
plt.plot(x, [time_2_5_50[4], time_2_5_200[4], time_2_5_400[4]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_2_10_50[4], time_2_10_200[4], time_2_10_400[4]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_2_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_2_1_50[4], speedup_2_1_200[4], speedup_2_1_400[4]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_2_2_50[4], speedup_2_2_200[4], speedup_2_2_400[4]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_2_5_50[4], speedup_2_5_200[4], speedup_2_5_400[4]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_2_10_50[4], speedup_2_10_200[4], speedup_2_10_400[4]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_2_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_2_1_50[5], time_2_1_200[5], time_2_1_400[5]], color='orange', label=r'No repetitions')
plt.plot(x, [time_2_2_50[5], time_2_2_200[5], time_2_2_400[5]], color='red', label=r'2 repetitions')
plt.plot(x, [time_2_5_50[5], time_2_5_200[5], time_2_5_400[5]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_2_10_50[5], time_2_10_200[5], time_2_10_400[5]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_2_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_2_1_50[5], speedup_2_1_200[5], speedup_2_1_400[5]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_2_2_50[5], speedup_2_2_200[5], speedup_2_2_400[5]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_2_5_50[5], speedup_2_5_200[5], speedup_2_5_400[5]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_2_10_50[5], speedup_2_10_200[5], speedup_2_10_400[5]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_2_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_2_1_50[6], time_2_1_200[6], time_2_1_400[6]], color='orange', label=r'No repetitions')
plt.plot(x, [time_2_2_50[6], time_2_2_200[6], time_2_2_400[6]], color='red', label=r'2 repetitions')
plt.plot(x, [time_2_5_50[6], time_2_5_200[6], time_2_5_400[6]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_2_10_50[6], time_2_10_200[6], time_2_10_400[6]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_2_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 2 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_2_1_50[6], speedup_2_1_200[6], speedup_2_1_400[6]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_2_2_50[6], speedup_2_2_200[6], speedup_2_2_400[6]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_2_5_50[6], speedup_2_5_200[6], speedup_2_5_400[6]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_2_10_50[6], speedup_2_10_200[6], speedup_2_10_400[6]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_2_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_4_1_50[3], time_4_1_200[3], time_4_1_400[3]], color='orange', label=r'No repetitions')
plt.plot(x, [time_4_2_50[3], time_4_2_200[3], time_4_2_400[3]], color='red', label=r'2 repetitions')
plt.plot(x, [time_4_5_50[3], time_4_5_200[3], time_4_5_400[3]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_4_10_50[3], time_4_10_200[3], time_4_10_400[3]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_4_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_4_1_50[3], speedup_4_1_200[3], speedup_4_1_400[3]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_4_2_50[3], speedup_4_2_200[3], speedup_4_2_400[3]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_4_5_50[3], speedup_4_5_200[3], speedup_4_5_400[3]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_4_10_50[3], speedup_4_10_200[3], speedup_4_10_400[3]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_4_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_4_1_50[4], time_4_1_200[4], time_4_1_400[4]], color='orange', label=r'No repetitions')
plt.plot(x, [time_4_2_50[4], time_4_2_200[4], time_4_2_400[4]], color='red', label=r'2 repetitions')
plt.plot(x, [time_4_5_50[4], time_4_5_200[4], time_4_5_400[4]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_4_10_50[4], time_4_10_200[4], time_4_10_400[4]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_4_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_4_1_50[4], speedup_4_1_200[4], speedup_4_1_400[4]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_4_2_50[4], speedup_4_2_200[4], speedup_4_2_400[4]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_4_5_50[4], speedup_4_5_200[4], speedup_4_5_400[4]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_4_10_50[4], speedup_4_10_200[4], speedup_4_10_400[4]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_4_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_4_1_50[5], time_4_1_200[5], time_4_1_400[5]], color='orange', label=r'No repetitions')
plt.plot(x, [time_4_2_50[5], time_4_2_200[5], time_4_2_400[5]], color='red', label=r'2 repetitions')
plt.plot(x, [time_4_5_50[5], time_4_5_200[5], time_4_5_400[5]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_4_10_50[5], time_4_10_200[5], time_4_10_400[5]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_4_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_4_1_50[5], speedup_4_1_200[5], speedup_4_1_400[5]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_4_2_50[5], speedup_4_2_200[5], speedup_4_2_400[5]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_4_5_50[5], speedup_4_5_200[5], speedup_4_5_400[5]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_4_10_50[5], speedup_4_10_200[5], speedup_4_10_400[5]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_4_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_4_1_50[6], time_4_1_200[6], time_4_1_400[6]], color='orange', label=r'No repetitions')
plt.plot(x, [time_4_2_50[6], time_4_2_200[6], time_4_2_400[6]], color='red', label=r'2 repetitions')
plt.plot(x, [time_4_5_50[6], time_4_5_200[6], time_4_5_400[6]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_4_10_50[6], time_4_10_200[6], time_4_10_400[6]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_4_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 4 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_4_1_50[6], speedup_4_1_200[6], speedup_4_1_400[6]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_4_2_50[6], speedup_4_2_200[6], speedup_4_2_400[6]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_4_5_50[6], speedup_4_5_200[6], speedup_4_5_400[6]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_4_10_50[6], speedup_4_10_200[6], speedup_4_10_400[6]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_4_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_8_1_50[3], time_8_1_200[3], time_8_1_400[3]], color='orange', label=r'No repetitions')
plt.plot(x, [time_8_2_50[3], time_8_2_200[3], time_8_2_400[3]], color='red', label=r'2 repetitions')
plt.plot(x, [time_8_5_50[3], time_8_5_200[3], time_8_5_400[3]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_8_10_50[3], time_8_10_200[3], time_8_10_400[3]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_8_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 blocks with 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_8_1_50[3], speedup_8_1_200[3], speedup_8_1_400[3]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_8_2_50[3], speedup_8_2_200[3], speedup_8_2_400[3]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_8_5_50[3], speedup_8_5_200[3], speedup_8_5_400[3]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_8_10_50[3], speedup_8_10_200[3], speedup_8_10_400[3]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_8_blocks_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_8_1_50[4], time_8_1_200[4], time_8_1_400[4]], color='orange', label=r'No repetitions')
plt.plot(x, [time_8_2_50[4], time_8_2_200[4], time_8_2_400[4]], color='red', label=r'2 repetitions')
plt.plot(x, [time_8_5_50[4], time_8_5_200[4], time_8_5_400[4]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_8_10_50[4], time_8_10_200[4], time_8_10_400[4]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_8_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"16 blocks with 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_8_1_50[4], speedup_8_1_200[4], speedup_8_1_400[4]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_8_2_50[4], speedup_8_2_200[4], speedup_8_2_400[4]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_8_5_50[4], speedup_8_5_200[4], speedup_8_5_400[4]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_8_10_50[4], speedup_8_10_200[4], speedup_8_10_400[4]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_8_blocks_16"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_8_1_50[5], time_8_1_200[5], time_8_1_400[5]], color='orange', label=r'No repetitions')
plt.plot(x, [time_8_2_50[5], time_8_2_200[5], time_8_2_400[5]], color='red', label=r'2 repetitions')
plt.plot(x, [time_8_5_50[5], time_8_5_200[5], time_8_5_400[5]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_8_10_50[5], time_8_10_200[5], time_8_10_400[5]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_8_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"32 blocks with 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_8_1_50[5], speedup_8_1_200[5], speedup_8_1_400[5]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_8_2_50[5], speedup_8_2_200[5], speedup_8_2_400[5]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_8_5_50[5], speedup_8_5_200[5], speedup_8_5_400[5]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_8_10_50[5], speedup_8_10_200[5], speedup_8_10_400[5]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_8_blocks_32"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_8_1_50[6], time_8_1_200[6], time_8_1_400[6]], color='orange', label=r'No repetitions')
plt.plot(x, [time_8_2_50[6], time_8_2_200[6], time_8_2_400[6]], color='red', label=r'2 repetitions')
plt.plot(x, [time_8_5_50[6], time_8_5_200[6], time_8_5_400[6]], color='blue', label=r'5 repetitions')
plt.plot(x, [time_8_10_50[6], time_8_10_200[6], time_8_10_400[6]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_thread_8_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"64 blocks with 8 threads - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_8_1_50[6], speedup_8_1_200[6], speedup_8_1_400[6]], color='orange', label=r'No repetitions')
plt.plot(x, [speedup_8_2_50[6], speedup_8_2_200[6], speedup_8_2_400[6]], color='red', label=r'2 repetitions')
plt.plot(x, [speedup_8_5_50[6], speedup_8_5_200[6], speedup_8_5_400[6]], color='blue', label=r'5 repetitions')
plt.plot(x, [speedup_8_10_50[6], speedup_8_10_200[6], speedup_8_10_400[6]], color='purple', label=r'10 repetitions')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_thread_8_blocks_64"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"2 threads with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_2_2_50[3], time_2_2_200[3], time_2_2_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_2_2_50[4], time_2_2_200[4], time_2_2_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_2_2_50[5], time_2_2_200[5], time_2_2_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_2_2_50[6], time_2_2_200[6], time_2_2_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_2_thread_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"2 threads with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_2_2_50[3], speedup_2_2_200[3], speedup_2_2_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_2_2_50[4], speedup_2_2_200[4], speedup_2_2_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_2_2_50[5], speedup_2_2_200[5], speedup_2_2_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_2_2_50[6], speedup_2_2_200[6], speedup_2_2_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_2_thread_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"4 threads with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_4_2_50[3], time_4_2_200[3], time_4_2_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_4_2_50[4], time_4_2_200[4], time_4_2_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_4_2_50[5], time_4_2_200[5], time_4_2_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_4_2_50[6], time_4_2_200[6], time_4_2_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_2_thread_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"4 threads with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_4_2_50[3], speedup_4_2_200[3], speedup_4_2_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_4_2_50[4], speedup_4_2_200[4], speedup_4_2_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_4_2_50[5], speedup_4_2_200[5], speedup_4_2_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_4_2_50[6], speedup_4_2_200[6], speedup_4_2_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_2_thread_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 threads with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_8_2_50[3], time_8_2_200[3], time_8_2_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_8_2_50[4], time_8_2_200[4], time_8_2_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_8_2_50[5], time_8_2_200[5], time_8_2_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_8_2_50[6], time_8_2_200[6], time_8_2_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_2_thread_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 threads with 2 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_8_2_50[3], speedup_8_2_200[3], speedup_8_2_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_8_2_50[4], speedup_8_2_200[4], speedup_8_2_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_8_2_50[5], speedup_8_2_200[5], speedup_8_2_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_8_2_50[6], speedup_8_2_200[6], speedup_8_2_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_2_thread_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"2 threads with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_2_5_50[3], time_2_5_200[3], time_2_5_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_2_5_50[4], time_2_5_200[4], time_2_5_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_2_5_50[5], time_2_5_200[5], time_2_5_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_2_5_50[6], time_2_5_200[6], time_2_5_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_thread_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"2 threads with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_2_5_50[3], speedup_2_5_200[3], speedup_2_5_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_2_5_50[4], speedup_2_5_200[4], speedup_2_5_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_2_5_50[5], speedup_2_5_200[5], speedup_2_5_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_2_5_50[6], speedup_2_5_200[6], speedup_2_5_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_thread_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"4 threads with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_4_5_50[3], time_4_5_200[3], time_4_5_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_4_5_50[4], time_4_5_200[4], time_4_5_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_4_5_50[5], time_4_5_200[5], time_4_5_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_4_5_50[6], time_4_5_200[6], time_4_5_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_thread_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"4 threads with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_4_5_50[3], speedup_4_5_200[3], speedup_4_5_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_4_5_50[4], speedup_4_5_200[4], speedup_4_5_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_4_5_50[5], speedup_4_5_200[5], speedup_4_5_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_4_5_50[6], speedup_4_5_200[6], speedup_4_5_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_thread_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 threads with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_8_5_50[3], time_8_5_200[3], time_8_5_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_8_5_50[4], time_8_5_200[4], time_8_5_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_8_5_50[5], time_8_5_200[5], time_8_5_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_8_5_50[6], time_8_5_200[6], time_8_5_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_5_thread_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 threads with 5 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_8_5_50[3], speedup_8_5_200[3], speedup_8_5_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_8_5_50[4], speedup_8_5_200[4], speedup_8_5_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_8_5_50[5], speedup_8_5_200[5], speedup_8_5_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_8_5_50[6], speedup_8_5_200[6], speedup_8_5_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_5_thread_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"2 threads with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_2_10_50[3], time_2_10_200[3], time_2_10_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_2_10_50[4], time_2_10_200[4], time_2_10_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_2_10_50[5], time_2_10_200[5], time_2_10_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_2_10_50[6], time_2_10_200[6], time_2_10_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_10_thread_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"2 threads with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_2_10_50[3], speedup_2_10_200[3], speedup_2_10_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_2_10_50[4], speedup_2_10_200[4], speedup_2_10_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_2_10_50[5], speedup_2_10_200[5], speedup_2_10_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_2_10_50[6], speedup_2_10_200[6], speedup_2_10_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_10_thread_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"4 threads with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_4_10_50[3], time_4_10_200[3], time_4_10_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_4_10_50[4], time_4_10_200[4], time_4_10_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_4_10_50[5], time_4_10_200[5], time_4_10_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_4_10_50[6], time_4_10_200[6], time_4_10_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_10_thread_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"4 threads with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_4_10_50[3], speedup_4_10_200[3], speedup_4_10_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_4_10_50[4], speedup_4_10_200[4], speedup_4_10_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_4_10_50[5], speedup_4_10_200[5], speedup_4_10_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_4_10_50[6], speedup_4_10_200[6], speedup_4_10_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_10_thread_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 threads with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_8_10_50[3], time_8_10_200[3], time_8_10_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [time_8_10_50[4], time_8_10_200[4], time_8_10_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [time_8_10_50[5], time_8_10_200[5], time_8_10_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [time_8_10_50[6], time_8_10_200[6], time_8_10_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Time')

filename_fig = "RKAB_x_block_size_time_rep_10_thread_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

plot_title = r"8 threads with 10 repetitions - " + str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [speedup_8_10_50[3], speedup_8_10_200[3], speedup_8_10_400[3]], color='orange', label=r'Blocks = 8')
plt.plot(x, [speedup_8_10_50[4], speedup_8_10_200[4], speedup_8_10_400[4]], color='red', label=r'Blocks = 16')
plt.plot(x, [speedup_8_10_50[5], speedup_8_10_200[5], speedup_8_10_400[5]], color='blue', label=r'Blocks = 32')
plt.plot(x, [speedup_8_10_50[6], speedup_8_10_200[6], speedup_8_10_400[6]], color='purple', label=r'Blocks = 64')
plt.grid()
plt.legend()
plt.title(plot_title)
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_x_block_size_speedup_rep_10_thread_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)