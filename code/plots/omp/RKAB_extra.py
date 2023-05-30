import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_extra.py

filename = "outputs/omp/RKAB_extra.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))

time_seq = time[0::6]
time_par_8 = time[1::6]
time_seq_uni1 = time[2::6]
time_par_8_uni1 = time[3::6]
time_seq_uni2 = time[4::6]
time_par_8_uni2 = time[5::6]

it_seq = it[0::6]
it_par_8 = it[1::6]
it_seq_uni1 = it[2::6]
it_par_8_uni1 = it[3::6]
it_seq_uni2 = it[4::6]
it_par_8_uni2 = it[5::6]

bsize = [500, 1000, 4000, 10000]
rep = [1, 2, 5, 10]

lines_seq = [it_seq[i]*8*bsize[int(i%4)]*rep[int(i/4)] for i in range(16)]
lines_seq_uni1 = [it_seq_uni1[i]*8*bsize[int(i%4)]*rep[int(i/4)] for i in range(16)]
lines_seq_uni2 = [it_seq_uni2[i]*8*bsize[int(i%4)]*rep[int(i/4)] for i in range(16)]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = [500, 1000, 4000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, it_seq[0:4], color='orange', label=r'Repetitions = 1')
plt.plot(x, it_seq[4:8], color='red', label=r'Repetitions = 2')
plt.plot(x, it_seq[8:12], color='blue', label=r'Repetitions = 5')
plt.plot(x, it_seq[12:16], color='purple', label=r'Repetitions = 10')
plt.scatter(x, it_seq[0:4], color='orange')
plt.scatter(x, it_seq[4:8], color='red')
plt.scatter(x, it_seq[8:12], color='blue')
plt.scatter(x, it_seq[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_extra_it_b_size"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, it_seq_uni1[0:4], color='orange', label=r'Option 1 - Repetitions = 1')
plt.plot(x, it_seq_uni1[4:8], color='red', label=r'Option 1 - Repetitions = 2')
plt.plot(x, it_seq_uni1[8:12], color='blue', label=r'Option 1 - Repetitions = 5')
plt.plot(x, it_seq_uni1[12:16], color='purple', label=r'Option 1 - Repetitions = 10')
plt.plot(x, it_seq_uni2[0:4], color='orange', linestyle='--', label=r'Option 2 - Repetitions = 1')
plt.plot(x, it_seq_uni2[4:8], color='red', linestyle='--', label=r'Option 2 - Repetitions = 2')
plt.plot(x, it_seq_uni2[8:12], color='blue', linestyle='--', label=r'Option 2 - Repetitions = 5')
plt.plot(x, it_seq_uni2[12:16], color='purple', linestyle='--', label=r'Option 2 - Repetitions = 10')
plt.scatter(x, it_seq_uni1[0:4], color='orange')
plt.scatter(x, it_seq_uni1[4:8], color='red')
plt.scatter(x, it_seq_uni1[8:12], color='blue')
plt.scatter(x, it_seq_uni1[12:16], color='purple')
plt.scatter(x, it_seq_uni2[0:4], color='orange')
plt.scatter(x, it_seq_uni2[4:8], color='red')
plt.scatter(x, it_seq_uni2[8:12], color='blue')
plt.scatter(x, it_seq_uni2[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_extra_it_b_size_uni"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [1, 2, 5, 10]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, it_seq[0::4], color='orange', label=r'Block Size = 500')
plt.plot(x, it_seq[1::4], color='red', label=r'Block Size = 1000')
plt.plot(x, it_seq[2::4], color='blue', label=r'Block Size = 4000')
plt.plot(x, it_seq[3::4], color='purple', label=r'Block Size = 10000')
plt.scatter(x, it_seq[0::4], color='orange')
plt.scatter(x, it_seq[1::4], color='red')
plt.scatter(x, it_seq[2::4], color='blue')
plt.scatter(x, it_seq[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_extra_it_rep"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, it_seq_uni1[0::4], color='orange', label=r'Option 1 - Block Size = 500')
plt.plot(x, it_seq_uni1[1::4], color='red', label=r'Option 1 - Block Size = 1000')
plt.plot(x, it_seq_uni1[2::4], color='blue', label=r'Option 1 - Block Size = 4000')
plt.plot(x, it_seq_uni1[3::4], color='purple', label=r'Option 1 - Block Size = 10000')
plt.plot(x, it_seq_uni2[0::4], color='orange', linestyle='--', label=r'Option 2 - Block Size = 500')
plt.plot(x, it_seq_uni2[1::4], color='red', linestyle='--', label=r'Option 2 - Block Size = 1000')
plt.plot(x, it_seq_uni2[2::4], color='blue', linestyle='--', label=r'Option 2 - Block Size = 4000')
plt.plot(x, it_seq_uni2[3::4], color='purple', linestyle='--', label=r'Option 2 - Block Size = 10000')
plt.scatter(x, it_seq_uni1[0::4], color='orange')
plt.scatter(x, it_seq_uni1[1::4], color='red')
plt.scatter(x, it_seq_uni1[2::4], color='blue')
plt.scatter(x, it_seq_uni1[3::4], color='purple')
plt.scatter(x, it_seq_uni2[0::4], color='orange')
plt.scatter(x, it_seq_uni2[1::4], color='red')
plt.scatter(x, it_seq_uni2[2::4], color='blue')
plt.scatter(x, it_seq_uni2[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_extra_it_rep_uni"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [500, 1000, 4000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, lines_seq[0:4], color='orange', label=r'Repetitions = 1')
plt.plot(x, lines_seq[4:8], color='red', label=r'Repetitions = 2')
plt.plot(x, lines_seq[8:12], color='blue', label=r'Repetitions = 5')
plt.plot(x, lines_seq[12:16], color='purple', label=r'Repetitions = 10')
plt.scatter(x, lines_seq[0:4], color='orange')
plt.scatter(x, lines_seq[4:8], color='red')
plt.scatter(x, lines_seq[8:12], color='blue')
plt.scatter(x, lines_seq[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_extra_lines_b_size"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, lines_seq_uni1[0:4], color='orange', label=r'Option 1 - Repetitions = 1')
plt.plot(x, lines_seq_uni1[4:8], color='red', label=r'Option 1 - Repetitions = 2')
plt.plot(x, lines_seq_uni1[8:12], color='blue', label=r'Option 1 - Repetitions = 5')
plt.plot(x, lines_seq_uni1[12:16], color='purple', label=r'Option 1 - Repetitions = 10')
plt.plot(x, lines_seq_uni2[0:4], color='orange', linestyle='--', label=r'Option 2 - Repetitions = 1')
plt.plot(x, lines_seq_uni2[4:8], color='red', linestyle='--', label=r'Option 2 - Repetitions = 2')
plt.plot(x, lines_seq_uni2[8:12], color='blue', linestyle='--', label=r'Option 2 - Repetitions = 5')
plt.plot(x, lines_seq_uni2[12:16], color='purple', linestyle='--', label=r'Option 2 - Repetitions = 10')
plt.scatter(x, lines_seq_uni1[0:4], color='orange')
plt.scatter(x, lines_seq_uni1[4:8], color='red')
plt.scatter(x, lines_seq_uni1[8:12], color='blue')
plt.scatter(x, lines_seq_uni1[12:16], color='purple')
plt.scatter(x, lines_seq_uni2[0:4], color='orange')
plt.scatter(x, lines_seq_uni2[4:8], color='red')
plt.scatter(x, lines_seq_uni2[8:12], color='blue')
plt.scatter(x, lines_seq_uni2[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_extra_lines_b_size_uni"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [1, 2, 5, 10]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, lines_seq[0::4], color='orange', label=r'Block Size = 500')
plt.plot(x, lines_seq[1::4], color='red', label=r'Block Size = 1000')
plt.plot(x, lines_seq[2::4], color='blue', label=r'Block Size = 4000')
plt.plot(x, lines_seq[3::4], color='purple', label=r'Block Size = 10000')
plt.scatter(x, lines_seq[0::4], color='orange')
plt.scatter(x, lines_seq[1::4], color='red')
plt.scatter(x, lines_seq[2::4], color='blue')
plt.scatter(x, lines_seq[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_extra_lines_rep"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, lines_seq_uni1[0::4], color='orange', label=r'Option 1 - Block Size = 500')
plt.plot(x, lines_seq_uni1[1::4], color='red', label=r'Option 1 - Block Size = 1000')
plt.plot(x, lines_seq_uni1[2::4], color='blue', label=r'Option 1 - Block Size = 4000')
plt.plot(x, lines_seq_uni1[3::4], color='purple', label=r'Option 1 - Block Size = 10000')
plt.plot(x, lines_seq_uni2[0::4], color='orange', linestyle='--', label=r'Option 2 - Block Size = 500')
plt.plot(x, lines_seq_uni2[1::4], color='red', linestyle='--', label=r'Option 2 - Block Size = 1000')
plt.plot(x, lines_seq_uni2[2::4], color='blue', linestyle='--', label=r'Option 2 - Block Size = 4000')
plt.plot(x, lines_seq_uni2[3::4], color='purple', linestyle='--', label=r'Option 2 - Block Size = 10000')
plt.scatter(x, lines_seq_uni1[0::4], color='orange')
plt.scatter(x, lines_seq_uni1[1::4], color='red')
plt.scatter(x, lines_seq_uni1[2::4], color='blue')
plt.scatter(x, lines_seq_uni1[3::4], color='purple')
plt.scatter(x, lines_seq_uni2[0::4], color='orange')
plt.scatter(x, lines_seq_uni2[1::4], color='red')
plt.scatter(x, lines_seq_uni2[2::4], color='blue')
plt.scatter(x, lines_seq_uni2[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_extra_lines_rep_uni"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [500, 1000, 4000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_par_8[0:4], color='orange', label=r'Repetitions = 1')
plt.plot(x, time_par_8[4:8], color='red', label=r'Repetitions = 2')
plt.plot(x, time_par_8[8:12], color='blue', label=r'Repetitions = 5')
plt.plot(x, time_par_8[12:16], color='purple', label=r'Repetitions = 10')
plt.scatter(x, time_par_8[0:4], color='orange')
plt.scatter(x, time_par_8[4:8], color='red')
plt.scatter(x, time_par_8[8:12], color='blue')
plt.scatter(x, time_par_8[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_extra_time_b_size"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_par_8_uni1[0:4], color='orange', label=r'Option 1 - Repetitions = 1')
plt.plot(x, time_par_8_uni1[4:8], color='red', label=r'Option 1 - Repetitions = 2')
plt.plot(x, time_par_8_uni1[8:12], color='blue', label=r'Option 1 - Repetitions = 5')
plt.plot(x, time_par_8_uni1[12:16], color='purple', label=r'Option 1 - Repetitions = 10')
plt.plot(x, time_par_8_uni2[0:4], color='orange', linestyle='--', label=r'Option 2 - Repetitions = 1')
plt.plot(x, time_par_8_uni2[4:8], color='red', linestyle='--', label=r'Option 2 - Repetitions = 2')
plt.plot(x, time_par_8_uni2[8:12], color='blue', linestyle='--', label=r'Option 2 - Repetitions = 5')
plt.plot(x, time_par_8_uni2[12:16], color='purple', linestyle='--', label=r'Option 2 - Repetitions = 10')
plt.scatter(x, time_par_8_uni1[0:4], color='orange')
plt.scatter(x, time_par_8_uni1[4:8], color='red')
plt.scatter(x, time_par_8_uni1[8:12], color='blue')
plt.scatter(x, time_par_8_uni1[12:16], color='purple')
plt.scatter(x, time_par_8_uni2[0:4], color='orange')
plt.scatter(x, time_par_8_uni2[4:8], color='red')
plt.scatter(x, time_par_8_uni2[8:12], color='blue')
plt.scatter(x, time_par_8_uni2[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_extra_time_b_size_uni"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [1, 2, 5, 10]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_par_8[0::4], color='orange', label=r'Block Size = 500')
plt.plot(x, time_par_8[1::4], color='red', label=r'Block Size = 1000')
plt.plot(x, time_par_8[2::4], color='blue', label=r'Block Size = 4000')
plt.plot(x, time_par_8[3::4], color='purple', label=r'Block Size = 10000')
plt.scatter(x, time_par_8[0::4], color='orange')
plt.scatter(x, time_par_8[1::4], color='red')
plt.scatter(x, time_par_8[2::4], color='blue')
plt.scatter(x, time_par_8[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_extra_time_rep"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_par_8_uni1[0::4], color='orange', label=r'Option 1 - Block Size = 500')
plt.plot(x, time_par_8_uni1[1::4], color='red', label=r'Option 1 - Block Size = 1000')
plt.plot(x, time_par_8_uni1[2::4], color='blue', label=r'Option 1 - Block Size = 4000')
plt.plot(x, time_par_8_uni1[3::4], color='purple', label=r'Option 1 - Block Size = 10000')
plt.plot(x, time_par_8_uni2[0::4], color='orange', linestyle='--', label=r'Option 2 - Block Size = 500')
plt.plot(x, time_par_8_uni2[1::4], color='red', linestyle='--', label=r'Option 2 - Block Size = 1000')
plt.plot(x, time_par_8_uni2[2::4], color='blue', linestyle='--', label=r'Option 2 - Block Size = 4000')
plt.plot(x, time_par_8_uni2[3::4], color='purple', linestyle='--', label=r'Option 2 - Block Size = 10000')
plt.scatter(x, time_par_8_uni1[0::4], color='orange')
plt.scatter(x, time_par_8_uni1[1::4], color='red')
plt.scatter(x, time_par_8_uni1[2::4], color='blue')
plt.scatter(x, time_par_8_uni1[3::4], color='purple')
plt.scatter(x, time_par_8_uni2[0::4], color='orange')
plt.scatter(x, time_par_8_uni2[1::4], color='red')
plt.scatter(x, time_par_8_uni2[2::4], color='blue')
plt.scatter(x, time_par_8_uni2[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_extra_time_rep_uni"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [500, 1000, 4000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_seq[i]/time_par_8[i] for i in range(0,4)], color='orange', label=r'Repetitions = 1')
plt.plot(x, [time_seq[i]/time_par_8[i] for i in range(4,8)], color='red', label=r'Repetitions = 2')
plt.plot(x, [time_seq[i]/time_par_8[i] for i in range(8,12)], color='blue', label=r'Repetitions = 5')
plt.plot(x, [time_seq[i]/time_par_8[i] for i in range(12,16)], color='purple', label=r'Repetitions = 10')
plt.scatter(x, [time_seq[i]/time_par_8[i] for i in range(0,4)], color='orange')
plt.scatter(x, [time_seq[i]/time_par_8[i] for i in range(4,8)], color='red')
plt.scatter(x, [time_seq[i]/time_par_8[i] for i in range(8,12)], color='blue')
plt.scatter(x, [time_seq[i]/time_par_8[i] for i in range(12,16)], color='purple')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_extra_speedup_b_size"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(0,4)], color='orange', label=r'Option 1 - Repetitions = 1')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(4,8)], color='red', label=r'Option 1 - Repetitions = 2')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(8,12)], color='blue', label=r'Option 1 - Repetitions = 5')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(12,16)], color='purple', label=r'Option 1 - Repetitions = 10')
plt.plot(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(0,4)], color='orange', linestyle='--', label=r'Option 2 - Repetitions = 1')
plt.plot(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(4,8)], color='red', linestyle='--', label=r'Option 2 - Repetitions = 2')
plt.plot(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(8,12)], color='blue', linestyle='--', label=r'Option 2 - Repetitions = 5')
plt.plot(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(12,16)], color='purple', linestyle='--', label=r'Option 2 - Repetitions = 10')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(0,4)], color='orange')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(4,8)], color='red')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(8,12)], color='blue')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(12,16)], color='purple')
plt.scatter(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(0,4)], color='orange')
plt.scatter(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(4,8)], color='red')
plt.scatter(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(8,12)], color='blue')
plt.scatter(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(12,16)], color='purple')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_extra_speedup_b_size_uni"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [1, 2, 5, 10]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_seq[i]/time_par_8[i] for i in range(0,16,4)], color='orange', label=r'Block Size = 500')
plt.plot(x, [time_seq[i]/time_par_8[i] for i in range(1,16,4)], color='red', label=r'Block Size = 1000')
plt.plot(x, [time_seq[i]/time_par_8[i] for i in range(2,16,4)], color='blue', label=r'Block Size = 4000')
plt.plot(x, [time_seq[i]/time_par_8[i] for i in range(3,16,4)], color='purple', label=r'Block Size = 10000')
plt.scatter(x, [time_seq[i]/time_par_8[i] for i in range(0,16,4)], color='orange')
plt.scatter(x, [time_seq[i]/time_par_8[i] for i in range(1,16,4)], color='red')
plt.scatter(x, [time_seq[i]/time_par_8[i] for i in range(2,16,4)], color='blue')
plt.scatter(x, [time_seq[i]/time_par_8[i] for i in range(3,16,4)], color='purple')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_extra_speedup_rep"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(0,16,4)], color='orange', label=r'Option 1 - Block Size = 500')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(1,16,4)], color='red', label=r'Option 1 - Block Size = 1000')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(2,16,4)], color='blue', label=r'Option 1 - Block Size = 4000')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(3,16,4)], color='purple', label=r'Option 1 - Block Size = 10000')
plt.plot(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(0,16,4)], color='orange', linestyle='--', label=r'Option 2 - Block Size = 500')
plt.plot(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(1,16,4)], color='red', linestyle='--', label=r'Option 2 - Block Size = 1000')
plt.plot(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(2,16,4)], color='blue', linestyle='--', label=r'Option 2 - Block Size = 4000')
plt.plot(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(3,16,4)], color='purple', linestyle='--', label=r'Option 2 - Block Size = 10000')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(0,16,4)], color='orange')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(1,16,4)], color='red')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(2,16,4)], color='blue')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(3,16,4)], color='purple')
plt.scatter(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(0,16,4)], color='orange')
plt.scatter(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(1,16,4)], color='red')
plt.scatter(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(2,16,4)], color='blue')
plt.scatter(x, [time_seq_uni2[i]/time_par_8_uni2[i] for i in range(3,16,4)], color='purple')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_extra_speedup_rep_uni"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [500, 1000, 4000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, it_seq_uni1[0:4], color='orange', label=r'Repetitions = 1')
plt.plot(x, it_seq_uni1[4:8], color='red', label=r'Repetitions = 2')
plt.plot(x, it_seq_uni1[8:12], color='blue', label=r'Repetitions = 5')
plt.plot(x, it_seq_uni1[12:16], color='purple', label=r'Repetitions = 10')
plt.scatter(x, it_seq_uni1[0:4], color='orange')
plt.scatter(x, it_seq_uni1[4:8], color='red')
plt.scatter(x, it_seq_uni1[8:12], color='blue')
plt.scatter(x, it_seq_uni1[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_extra_it_b_size_uni1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [1, 2, 5, 10]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, it_seq_uni1[0::4], color='orange', label=r'Block Size = 500')
plt.plot(x, it_seq_uni1[1::4], color='red', label=r'Block Size = 1000')
plt.plot(x, it_seq_uni1[2::4], color='blue', label=r'Block Size = 4000')
plt.plot(x, it_seq_uni1[3::4], color='purple', label=r'Block Size = 10000')
plt.scatter(x, it_seq_uni1[0::4], color='orange')
plt.scatter(x, it_seq_uni1[1::4], color='red')
plt.scatter(x, it_seq_uni1[2::4], color='blue')
plt.scatter(x, it_seq_uni1[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_extra_it_rep_uni1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [500, 1000, 4000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, lines_seq_uni1[0:4], color='orange', label=r'Repetitions = 1')
plt.plot(x, lines_seq_uni1[4:8], color='red', label=r'Repetitions = 2')
plt.plot(x, lines_seq_uni1[8:12], color='blue', label=r'Repetitions = 5')
plt.plot(x, lines_seq_uni1[12:16], color='purple', label=r'Repetitions = 10')
plt.scatter(x, lines_seq_uni1[0:4], color='orange')
plt.scatter(x, lines_seq_uni1[4:8], color='red')
plt.scatter(x, lines_seq_uni1[8:12], color='blue')
plt.scatter(x, lines_seq_uni1[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_extra_lines_b_size_uni1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [1, 2, 5, 10]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, lines_seq_uni1[0::4], color='orange', label=r'Block Size = 500')
plt.plot(x, lines_seq_uni1[1::4], color='red', label=r'Block Size = 1000')
plt.plot(x, lines_seq_uni1[2::4], color='blue', label=r'Block Size = 4000')
plt.plot(x, lines_seq_uni1[3::4], color='purple', label=r'Block Size = 10000')
plt.scatter(x, lines_seq_uni1[0::4], color='orange')
plt.scatter(x, lines_seq_uni1[1::4], color='red')
plt.scatter(x, lines_seq_uni1[2::4], color='blue')
plt.scatter(x, lines_seq_uni1[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_extra_lines_rep_uni1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [500, 1000, 4000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_par_8_uni1[0:4], color='orange', label=r'Repetitions = 1')
plt.plot(x, time_par_8_uni1[4:8], color='red', label=r'Repetitions = 2')
plt.plot(x, time_par_8_uni1[8:12], color='blue', label=r'Repetitions = 5')
plt.plot(x, time_par_8_uni1[12:16], color='purple', label=r'Repetitions = 10')
plt.scatter(x, time_par_8_uni1[0:4], color='orange')
plt.scatter(x, time_par_8_uni1[4:8], color='red')
plt.scatter(x, time_par_8_uni1[8:12], color='blue')
plt.scatter(x, time_par_8_uni1[12:16], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_extra_time_b_size_uni1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [1, 2, 5, 10]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, time_par_8_uni1[0::4], color='orange', label=r'Block Size = 500')
plt.plot(x, time_par_8_uni1[1::4], color='red', label=r'Block Size = 1000')
plt.plot(x, time_par_8_uni1[2::4], color='blue', label=r'Block Size = 4000')
plt.plot(x, time_par_8_uni1[3::4], color='purple', label=r'Block Size = 10000')
plt.scatter(x, time_par_8_uni1[0::4], color='orange')
plt.scatter(x, time_par_8_uni1[1::4], color='red')
plt.scatter(x, time_par_8_uni1[2::4], color='blue')
plt.scatter(x, time_par_8_uni1[3::4], color='purple')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_extra_time_rep_uni1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [500, 1000, 4000, 10000]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(0,4)], color='orange', label=r'Repetitions = 1')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(4,8)], color='red', label=r'Repetitions = 2')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(8,12)], color='blue', label=r'Repetitions = 5')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(12,16)], color='purple', label=r'Repetitions = 10')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(0,4)], color='orange')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(4,8)], color='red')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(8,12)], color='blue')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(12,16)], color='purple')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_extra_speedup_b_size_uni1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)

x = [1, 2, 5, 10]

fig = plt.figure(figsize=(10, 7))
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(0,16,4)], color='orange', label=r'Block Size = 500')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(1,16,4)], color='red', label=r'Block Size = 1000')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(2,16,4)], color='blue', label=r'Block Size = 4000')
plt.plot(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(3,16,4)], color='purple', label=r'Block Size = 10000')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(0,16,4)], color='orange')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(1,16,4)], color='red')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(2,16,4)], color='blue')
plt.scatter(x, [time_seq_uni1[i]/time_par_8_uni1[i] for i in range(3,16,4)], color='purple')
plt.grid()
plt.legend()
plt.xscale('log')
plt.xlabel(r'Repetitions')
plt.ylabel(r'Speedup')

filename_fig = "RKAB_extra_speedup_rep_uni1"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close(fig)