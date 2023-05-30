import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/mpi/RKAB_block_size.py

filename = "outputs/mpi/RKAB_mpi_8.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
    time.append(float(lines[i].split()[2]))
    it.append(float(lines[i].split()[3]))

x1 = [1, 5, 10, 100, 500, 1000]
x2 = [1, 5, 10, 100, 1000, 10000]
x3 = [1, 5, 10, 100, 1000, 4000]
x4 = [1, 5, 10, 100, 1000, 10000]
x5 = [1, 5, 10, 100, 500, 1000]

time_dim1_seq = time[0:24:4]
time_dim1_par1 = time[1:24:4]
time_dim1_par2 = time[2:24:4]
time_dim1_par3 = time[3:24:4]

it_dim1_seq = it[0:24:4]
it_dim1_par1 = it[1:24:4]
it_dim1_par2 = it[2:24:4]
it_dim1_par3 = it[3:24:4]

lines_dim1_seq = [it_dim1_seq[i]*8*x1[i] for i in range(len(x1))]
lines_dim1_par1 = [it_dim1_par1[i]*8*x1[i] for i in range(len(x1))]
lines_dim1_par2 = [it_dim1_par2[i]*8*x1[i] for i in range(len(x1))]
lines_dim1_par3 = [it_dim1_par3[i]*8*x1[i] for i in range(len(x1))]

time_dim2_seq = time[24:48:4]
time_dim2_par1 = time[25:48:4]
time_dim2_par2 = time[26:48:4]
time_dim2_par3 = time[27:48:4]

it_dim2_seq = it[24:48:4]
it_dim2_par1 = it[25:48:4]
it_dim2_par2 = it[26:48:4]
it_dim2_par3 = it[27:48:4]

lines_dim2_seq = [it_dim2_seq[i]*8*x2[i] for i in range(len(x2))]
lines_dim2_par1 = [it_dim2_par1[i]*8*x2[i] for i in range(len(x2))]
lines_dim2_par2 = [it_dim2_par2[i]*8*x2[i] for i in range(len(x2))]
lines_dim2_par3 = [it_dim2_par3[i]*8*x2[i] for i in range(len(x2))]

time_dim3_seq = time[48:72:4]
time_dim3_par1 = time[49:72:4]
time_dim3_par2 = time[50:72:4]
time_dim3_par3 = time[51:72:4]

it_dim3_seq = it[48:72:4]
it_dim3_par1 = it[49:72:4]
it_dim3_par2 = it[50:72:4]
it_dim3_par3 = it[51:72:4]

lines_dim3_seq = [it_dim3_seq[i]*8*x3[i] for i in range(len(x3))]
lines_dim3_par1 = [it_dim3_par1[i]*8*x3[i] for i in range(len(x3))]
lines_dim3_par2 = [it_dim3_par2[i]*8*x3[i] for i in range(len(x3))]
lines_dim3_par3 = [it_dim3_par3[i]*8*x3[i] for i in range(len(x3))]

time_dim4_seq = time[72:96:4]
time_dim4_par1 = time[73:96:4]
time_dim4_par2 = time[74:96:4]
time_dim4_par3 = time[75:96:4]

it_dim4_seq = it[72:96:4]
it_dim4_par1 = it[73:96:4]
it_dim4_par2 = it[74:96:4]
it_dim4_par3 = it[75:96:4]

lines_dim4_seq = [it_dim4_seq[i]*8*x4[i] for i in range(len(x4))]
lines_dim4_par1 = [it_dim4_par1[i]*8*x4[i] for i in range(len(x4))]
lines_dim4_par2 = [it_dim4_par2[i]*8*x4[i] for i in range(len(x4))]
lines_dim4_par3 = [it_dim4_par3[i]*8*x4[i] for i in range(len(x4))]

time_dim5_seq = time[96:120:4]
time_dim5_par1 = time[97:120:4]
time_dim5_par2 = time[98:120:4]
time_dim5_par3 = time[99:120:4]

it_dim5_seq = it[96:120:4]
it_dim5_par1 = it[97:120:4]
it_dim5_par2 = it[98:120:4]
it_dim5_par3 = it[99:120:4]

lines_dim5_seq = [it_dim5_seq[i]*8*x5[i] for i in range(len(x5))]
lines_dim5_par1 = [it_dim5_par1[i]*8*x5[i] for i in range(len(x5))]
lines_dim5_par2 = [it_dim5_par2[i]*8*x5[i] for i in range(len(x5))]
lines_dim5_par3 = [it_dim5_par3[i]*8*x5[i] for i in range(len(x5))]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x1, time_dim1_seq, color='black')
plt.plot(x1, time_dim1_seq, linewidth=1.5, color='black', label=r'Sequential')
plt.scatter(x1, time_dim1_par1, color='orange')
plt.plot(x1, time_dim1_par1, linewidth=1.5, color='orange', label=r'1 Process per node (8 nodes)')
plt.scatter(x1, time_dim1_par2, color='red')
plt.plot(x1, time_dim1_par2, linewidth=1.5, color='red', label=r'2 Processes per node (4 nodes)')
plt.scatter(x1, time_dim1_par3, color='blue')
plt.plot(x1, time_dim1_par3, linewidth=1.5, color='blue', label=r'8 Processes per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_block_size_time_8_4000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x1, lines_dim1_seq, color='black')
plt.plot(x1, lines_dim1_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_lines_8_4000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x1, it_dim1_seq, color='black')
plt.plot(x1, it_dim1_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_it_8_4000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x2, time_dim2_seq, color='black')
plt.plot(x2, time_dim2_seq, linewidth=1.5, color='black', label=r'Sequential')
plt.scatter(x2, time_dim2_par1, color='orange')
plt.plot(x2, time_dim2_par1, linewidth=1.5, color='orange', label=r'1 Process per node (8 nodes)')
plt.scatter(x2, time_dim2_par2, color='red')
plt.plot(x2, time_dim2_par2, linewidth=1.5, color='red', label=r'2 Processes per node (4 nodes)')
plt.scatter(x2, time_dim2_par3, color='blue')
plt.plot(x2, time_dim2_par3, linewidth=1.5, color='blue', label=r'8 Processes per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_block_size_time_8_40000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x2, lines_dim2_seq, color='black')
plt.plot(x2, lines_dim2_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_lines_8_40000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x2, it_dim2_seq, color='black')
plt.plot(x2, it_dim2_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_it_8_40000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x3, time_dim3_seq, color='black')
plt.plot(x3, time_dim3_seq, linewidth=1.5, color='black', label=r'Sequential')
plt.scatter(x3, time_dim3_par1, color='orange')
plt.plot(x3, time_dim3_par1, linewidth=1.5, color='orange', label=r'1 Process per node (8 nodes)')
plt.scatter(x3, time_dim3_par2, color='red')
plt.plot(x3, time_dim3_par2, linewidth=1.5, color='red', label=r'2 Processes per node (4 nodes)')
plt.scatter(x3, time_dim3_par3, color='blue')
plt.plot(x3, time_dim3_par3, linewidth=1.5, color='blue', label=r'8 Processes per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_block_size_time_8_20000_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x3, lines_dim3_seq, color='black')
plt.plot(x3, lines_dim3_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_lines_8_20000_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x3, it_dim3_seq, color='black')
plt.plot(x3, it_dim3_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_it_8_20000_4000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x4, time_dim4_seq, color='black')
plt.plot(x4, time_dim4_seq, linewidth=1.5, color='black', label=r'Sequential')
plt.scatter(x4, time_dim4_par1, color='orange')
plt.plot(x4, time_dim4_par1, linewidth=1.5, color='orange', label=r'1 Process per node (8 nodes)')
plt.scatter(x4, time_dim4_par2, color='red')
plt.plot(x4, time_dim4_par2, linewidth=1.5, color='red', label=r'2 Processes per node (4 nodes)')
plt.scatter(x4, time_dim4_par3, color='blue')
plt.plot(x4, time_dim4_par3, linewidth=1.5, color='blue', label=r'8 Processes per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_block_size_time_8_80000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x4, lines_dim4_seq, color='black')
plt.plot(x4, lines_dim4_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_lines_8_80000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x4, it_dim4_seq, color='black')
plt.plot(x4, it_dim4_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_it_8_80000_10000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x5, time_dim5_seq, color='black')
plt.plot(x5, time_dim5_seq, linewidth=1.5, color='black', label=r'Sequential')
plt.scatter(x5, time_dim5_par1, color='orange')
plt.plot(x5, time_dim5_par1, linewidth=1.5, color='orange', label=r'1 Process per node (8 nodes)')
plt.scatter(x5, time_dim5_par2, color='red')
plt.plot(x5, time_dim5_par2, linewidth=1.5, color='red', label=r'2 Processes per node (4 nodes)')
plt.scatter(x5, time_dim5_par3, color='blue')
plt.plot(x5, time_dim5_par3, linewidth=1.5, color='blue', label=r'8 Processes per node (1 node)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_block_size_time_8_80000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x5, lines_dim5_seq, color='black')
plt.plot(x5, lines_dim5_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
# plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_lines_8_80000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x5, it_dim5_seq, color='black')
plt.plot(x5, it_dim5_seq, linewidth=1.5, color='black')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total numbers of used rows')

filename_fig = "RKAB_block_size_it_8_80000_1000"

# plt.show()
fig.savefig("plots/mpi/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/mpi/png/"+filename_fig+".png", bbox_inches='tight')