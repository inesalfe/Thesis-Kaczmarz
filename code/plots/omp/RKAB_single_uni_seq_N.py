import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_single_uni_seq_N.py

filename = "outputs/omp/RK_seq.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time_seq = []
for i in range(file_size):
	time_seq.append(float(lines[i].split()[2]))

indices = (10, 16, 18, 24, 26, 27, 33, 35, 36)
time_seq_dim = [time_seq[i] for i in indices]

filename = "outputs/omp/RKAB_single.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))

time_par_1 = time[1::8]
time_par_2 = time[3::8]
time_par_4 = time[5::8]
time_par_8 = time[7::8]

filename = "outputs/omp/RKAB_single_uni.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))

time_par_2_uni_1 = time[9::32]
time_par_2_uni_2 = time[11::32]
time_par_2_uni_3 = time[13::32]
time_par_2_uni_4 = time[15::32]

time_par_4_uni_1 = time[17::32]
time_par_4_uni_2 = time[19::32]
time_par_4_uni_3 = time[21::32]
time_par_4_uni_4 = time[23::32]

time_par_8_uni_1 = time[25::32]
time_par_8_uni_2 = time[27::32]
time_par_8_uni_3 = time[29::32]
time_par_8_uni_4 = time[31::32]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# x = [5, 10, 50, 100, 500]

# plot_title = r"2 Threads - $4000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[0], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_2[0:5], color='orange')
# plt.plot(x, time_par_2[0:5], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_2_uni_1[0:5], color='red')
# plt.plot(x, time_par_2_uni_1[0:5], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_2_uni_2[0:5], color='blue')
# plt.plot(x, time_par_2_uni_2[0:5], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3[0:5], color='purple')
# plt.plot(x, time_par_2_uni_3[0:5], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4[0:5], color='black')
# plt.plot(x, time_par_2_uni_4[0:5], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_4000_1000_2"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# x = [5, 10, 50, 100, 500, 1000]

# plot_title = r"2 Threads - $20000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[1], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_2[5:11], color='orange')
# plt.plot(x, time_par_2[5:11], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_2_uni_1[5:11], color='red')
# plt.plot(x, time_par_2_uni_1[5:11], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_2_uni_2[5:11], color='blue')
# plt.plot(x, time_par_2_uni_2[5:11], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3[5:11], color='purple')
# plt.plot(x, time_par_2_uni_3[5:11], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4[5:11], color='black')
# plt.plot(x, time_par_2_uni_4[5:11], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_20000_1000_2"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"2 Threads - $20000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[2], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_2[11:17], color='orange')
# plt.plot(x, time_par_2[11:17], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_2_uni_1[11:17], color='red')
# plt.plot(x, time_par_2_uni_1[11:17], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_2_uni_2[11:17], color='blue')
# plt.plot(x, time_par_2_uni_2[11:17], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3[11:17], color='purple')
# plt.plot(x, time_par_2_uni_3[11:17], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4[11:17], color='black')
# plt.plot(x, time_par_2_uni_4[11:17], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_20000_4000_2"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# x = [5, 10, 50, 100, 500, 1000]

# plot_title = r"2 Threads - $40000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[3], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_2[17:23], color='orange')
# plt.plot(x, time_par_2[17:23], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_2_uni_1[17:23], color='red')
# plt.plot(x, time_par_2_uni_1[17:23], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_2_uni_2[17:23], color='blue')
# plt.plot(x, time_par_2_uni_2[17:23], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3[17:23], color='purple')
# plt.plot(x, time_par_2_uni_3[17:23], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4[17:23], color='black')
# plt.plot(x, time_par_2_uni_4[17:23], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_1000_2"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"2 Threads - $40000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[4], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_2[23:29], color='orange')
# plt.plot(x, time_par_2[23:29], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_2_uni_1[23:29], color='red')
# plt.plot(x, time_par_2_uni_1[23:29], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_2_uni_2[23:29], color='blue')
# plt.plot(x, time_par_2_uni_2[23:29], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3[23:29], color='purple')
# plt.plot(x, time_par_2_uni_3[23:29], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4[23:29], color='black')
# plt.plot(x, time_par_2_uni_4[23:29], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_4000_2"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"2 Threads - $40000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[5], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_2[29:35], color='orange')
# plt.plot(x, time_par_2[29:35], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_2_uni_1[29:35], color='red')
# plt.plot(x, time_par_2_uni_1[29:35], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_2_uni_2[29:35], color='blue')
# plt.plot(x, time_par_2_uni_2[29:35], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3[29:35], color='purple')
# plt.plot(x, time_par_2_uni_3[29:35], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4[29:35], color='black')
# plt.plot(x, time_par_2_uni_4[29:35], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_10000_2"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

x = [5, 10, 50, 100, 500, 1000, 10000]

plot_title = r"2 Threads - $80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[6], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
plt.scatter(x, time_par_2[42:49], color='orange')
plt.plot(x, time_par_2[42:49], linewidth=1.5, color='orange', label=r'RKAB')
plt.scatter(x, time_par_2_uni_1, color='red')
plt.plot(x, time_par_2_uni_1, linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
plt.scatter(x, time_par_2_uni_2, color='blue')
plt.plot(x, time_par_2_uni_2, linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3, color='purple')
# plt.plot(x, time_par_2_uni_3, linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4, color='black')
# plt.plot(x, time_par_2_uni_4, linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_uni_seq_N_time_80000_1000_2"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"2 Threads - $80000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[7], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_2[42:49], color='orange')
# plt.plot(x, time_par_2[42:49], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_2_uni_1[42:49], color='red')
# plt.plot(x, time_par_2_uni_1[42:49], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_2_uni_2[42:49], color='blue')
# plt.plot(x, time_par_2_uni_2[42:49], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3[42:49], color='purple')
# plt.plot(x, time_par_2_uni_3[42:49], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4[42:49], color='black')
# plt.plot(x, time_par_2_uni_4[42:49], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_80000_4000_2"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"2 Threads - $80000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[8], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_2[49:56], color='orange')
# plt.plot(x, time_par_2[49:56], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_2_uni_1[49:56], color='red')
# plt.plot(x, time_par_2_uni_1[49:56], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_2_uni_2[49:56], color='blue')
# plt.plot(x, time_par_2_uni_2[49:56], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_2_uni_3[49:56], color='purple')
# plt.plot(x, time_par_2_uni_3[49:56], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_2_uni_4[49:56], color='black')
# plt.plot(x, time_par_2_uni_4[49:56], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_80000_10000_2"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"4 Threads - $4000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[0], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_4[0:5], color='orange')
# plt.plot(x, time_par_4[0:5], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_4_uni_1[0:5], color='red')
# plt.plot(x, time_par_4_uni_1[0:5], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_4_uni_2[0:5], color='blue')
# plt.plot(x, time_par_4_uni_2[0:5], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3[0:5], color='purple')
# plt.plot(x, time_par_4_uni_3[0:5], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4[0:5], color='black')
# plt.plot(x, time_par_4_uni_4[0:5], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_4000_1000_4"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# x = [5, 10, 50, 100, 500, 1000]

# plot_title = r"4 Threads - $20000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[1], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_4[5:11], color='orange')
# plt.plot(x, time_par_4[5:11], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_4_uni_1[5:11], color='red')
# plt.plot(x, time_par_4_uni_1[5:11], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_4_uni_2[5:11], color='blue')
# plt.plot(x, time_par_4_uni_2[5:11], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3[5:11], color='purple')
# plt.plot(x, time_par_4_uni_3[5:11], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4[5:11], color='black')
# plt.plot(x, time_par_4_uni_4[5:11], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_20000_1000_4"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"4 Threads - $20000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[2], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_4[11:17], color='orange')
# plt.plot(x, time_par_4[11:17], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_4_uni_1[11:17], color='red')
# plt.plot(x, time_par_4_uni_1[11:17], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_4_uni_2[11:17], color='blue')
# plt.plot(x, time_par_4_uni_2[11:17], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3[11:17], color='purple')
# plt.plot(x, time_par_4_uni_3[11:17], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4[11:17], color='black')
# plt.plot(x, time_par_4_uni_4[11:17], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_20000_4000_4"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# x = [5, 10, 50, 100, 500, 1000]

# plot_title = r"4 Threads - $40000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[3], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_4[17:23], color='orange')
# plt.plot(x, time_par_4[17:23], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_4_uni_1[17:23], color='red')
# plt.plot(x, time_par_4_uni_1[17:23], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_4_uni_2[17:23], color='blue')
# plt.plot(x, time_par_4_uni_2[17:23], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3[17:23], color='purple')
# plt.plot(x, time_par_4_uni_3[17:23], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4[17:23], color='black')
# plt.plot(x, time_par_4_uni_4[17:23], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_1000_4"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"4 Threads - $40000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[4], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_4[23:29], color='orange')
# plt.plot(x, time_par_4[23:29], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_4_uni_1[23:29], color='red')
# plt.plot(x, time_par_4_uni_1[23:29], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_4_uni_2[23:29], color='blue')
# plt.plot(x, time_par_4_uni_2[23:29], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3[23:29], color='purple')
# plt.plot(x, time_par_4_uni_3[23:29], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4[23:29], color='black')
# plt.plot(x, time_par_4_uni_4[23:29], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_4000_4"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"4 Threads - $40000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[5], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_4[29:35], color='orange')
# plt.plot(x, time_par_4[29:35], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_4_uni_1[29:35], color='red')
# plt.plot(x, time_par_4_uni_1[29:35], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_4_uni_2[29:35], color='blue')
# plt.plot(x, time_par_4_uni_2[29:35], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3[29:35], color='purple')
# plt.plot(x, time_par_4_uni_3[29:35], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4[29:35], color='black')
# plt.plot(x, time_par_4_uni_4[29:35], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_10000_4"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

x = [5, 10, 50, 100, 500, 1000, 10000]

plot_title = r"4 Threads - $80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[6], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
plt.scatter(x, time_par_4[42:49], color='orange')
plt.plot(x, time_par_4[42:49], linewidth=1.5, color='orange', label=r'RKAB')
plt.scatter(x, time_par_4_uni_1, color='red')
plt.plot(x, time_par_4_uni_1, linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
plt.scatter(x, time_par_4_uni_2, color='blue')
plt.plot(x, time_par_4_uni_2, linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3, color='purple')
# plt.plot(x, time_par_4_uni_3, linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4, color='black')
# plt.plot(x, time_par_4_uni_4, linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_uni_seq_N_time_80000_1000_4"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"4 Threads - $80000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[7], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_4[42:49], color='orange')
# plt.plot(x, time_par_4[42:49], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_4_uni_1[42:49], color='red')
# plt.plot(x, time_par_4_uni_1[42:49], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_4_uni_2[42:49], color='blue')
# plt.plot(x, time_par_4_uni_2[42:49], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3[42:49], color='purple')
# plt.plot(x, time_par_4_uni_3[42:49], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4[42:49], color='black')
# plt.plot(x, time_par_4_uni_4[42:49], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_80000_4000_4"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"4 Threads - $80000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[8], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_4[49:56], color='orange')
# plt.plot(x, time_par_4[49:56], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_4_uni_1[49:56], color='red')
# plt.plot(x, time_par_4_uni_1[49:56], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_4_uni_2[49:56], color='blue')
# plt.plot(x, time_par_4_uni_2[49:56], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_4_uni_3[49:56], color='purple')
# plt.plot(x, time_par_4_uni_3[49:56], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_4_uni_4[49:56], color='black')
# plt.plot(x, time_par_4_uni_4[49:56], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_80000_10000_4"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"8 Threads - $4000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[0], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_8[0:5], color='orange')
# plt.plot(x, time_par_8[0:5], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_8_uni_1[0:5], color='red')
# plt.plot(x, time_par_8_uni_1[0:5], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_8_uni_2[0:5], color='blue')
# plt.plot(x, time_par_8_uni_2[0:5], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3[0:5], color='purple')
# plt.plot(x, time_par_8_uni_3[0:5], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4[0:5], color='black')
# plt.plot(x, time_par_8_uni_4[0:5], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_4000_1000_8"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# x = [5, 10, 50, 100, 500, 1000]

# plot_title = r"8 Threads - $20000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[1], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_8[5:11], color='orange')
# plt.plot(x, time_par_8[5:11], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_8_uni_1[5:11], color='red')
# plt.plot(x, time_par_8_uni_1[5:11], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_8_uni_2[5:11], color='blue')
# plt.plot(x, time_par_8_uni_2[5:11], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3[5:11], color='purple')
# plt.plot(x, time_par_8_uni_3[5:11], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4[5:11], color='black')
# plt.plot(x, time_par_8_uni_4[5:11], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_20000_1000_8"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"8 Threads - $20000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[2], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_8[11:17], color='orange')
# plt.plot(x, time_par_8[11:17], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_8_uni_1[11:17], color='red')
# plt.plot(x, time_par_8_uni_1[11:17], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_8_uni_2[11:17], color='blue')
# plt.plot(x, time_par_8_uni_2[11:17], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3[11:17], color='purple')
# plt.plot(x, time_par_8_uni_3[11:17], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4[11:17], color='black')
# plt.plot(x, time_par_8_uni_4[11:17], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_20000_4000_8"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# x = [5, 10, 50, 100, 500, 1000]

# plot_title = r"8 Threads - $40000 \times 1000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[3], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_8[17:23], color='orange')
# plt.plot(x, time_par_8[17:23], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_8_uni_1[17:23], color='red')
# plt.plot(x, time_par_8_uni_1[17:23], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_8_uni_2[17:23], color='blue')
# plt.plot(x, time_par_8_uni_2[17:23], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3[17:23], color='purple')
# plt.plot(x, time_par_8_uni_3[17:23], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4[17:23], color='black')
# plt.plot(x, time_par_8_uni_4[17:23], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_1000_8"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"8 Threads - $40000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[4], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_8[23:29], color='orange')
# plt.plot(x, time_par_8[23:29], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_8_uni_1[23:29], color='red')
# plt.plot(x, time_par_8_uni_1[23:29], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_8_uni_2[23:29], color='blue')
# plt.plot(x, time_par_8_uni_2[23:29], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3[23:29], color='purple')
# plt.plot(x, time_par_8_uni_3[23:29], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4[23:29], color='black')
# plt.plot(x, time_par_8_uni_4[23:29], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_4000_8"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"8 Threads - $40000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[5], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_8[29:35], color='orange')
# plt.plot(x, time_par_8[29:35], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_8_uni_1[29:35], color='red')
# plt.plot(x, time_par_8_uni_1[29:35], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_8_uni_2[29:35], color='blue')
# plt.plot(x, time_par_8_uni_2[29:35], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3[29:35], color='purple')
# plt.plot(x, time_par_8_uni_3[29:35], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4[29:35], color='black')
# plt.plot(x, time_par_8_uni_4[29:35], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_40000_10000_8"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

x = [5, 10, 50, 100, 500, 1000, 10000]

plot_title = r"8 Threads - $80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
plt.axhline(y=time_seq_dim[6], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
plt.scatter(x, time_par_8[42:49], color='orange')
plt.plot(x, time_par_8[42:49], linewidth=1.5, color='orange', label=r'RKAB')
plt.scatter(x, time_par_8_uni_1, color='red')
plt.plot(x, time_par_8_uni_1, linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
plt.scatter(x, time_par_8_uni_2, color='blue')
plt.plot(x, time_par_8_uni_2, linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3, color='purple')
# plt.plot(x, time_par_8_uni_3, linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4, color='black')
# plt.plot(x, time_par_8_uni_4, linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_uni_seq_N_time_80000_1000_8"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"8 Threads - $80000 \times 4000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[7], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_8[42:49], color='orange')
# plt.plot(x, time_par_8[42:49], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_8_uni_1[42:49], color='red')
# plt.plot(x, time_par_8_uni_1[42:49], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_8_uni_2[42:49], color='blue')
# plt.plot(x, time_par_8_uni_2[42:49], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3[42:49], color='purple')
# plt.plot(x, time_par_8_uni_3[42:49], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4[42:49], color='black')
# plt.plot(x, time_par_8_uni_4[42:49], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_80000_4000_8"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r"8 Threads - $80000 \times 10000$"

# fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[8], linestyle='--', linewidth=1.5, color='grey', label=r'RK (Sequential)')
# plt.scatter(x, time_par_8[49:56], color='orange')
# plt.plot(x, time_par_8[49:56], linewidth=1.5, color='orange', label=r'RKAB')
# plt.scatter(x, time_par_8_uni_1[49:56], color='red')
# plt.plot(x, time_par_8_uni_1[49:56], linewidth=1.5, color='red', label=r'SRKABWOR (Option 1)')
# plt.scatter(x, time_par_8_uni_2[49:56], color='blue')
# plt.plot(x, time_par_8_uni_2[49:56], linewidth=1.5, color='blue', label=r'SRKABWOR (Option 2)')
# plt.scatter(x, time_par_8_uni_3[49:56], color='purple')
# plt.plot(x, time_par_8_uni_3[49:56], linewidth=1.5, color='purple', label=r'SRKAB w/o replacement \\ (option 1 w/ copy)')
# plt.scatter(x, time_par_8_uni_4[49:56], color='black')
# plt.plot(x, time_par_8_uni_4[49:56], linewidth=1.5, color='black', label=r'SRKAB w/o replacement \\ (option 2 w/ copy)')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'Block Size')
# plt.ylabel(r'Total Time (s)')

# filename_fig = "RKAB_single_uni_seq_N_time_80000_10000_8"

# # plt.show()
# fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')