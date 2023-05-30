import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/omp/RKAB_single_seq_extra.py

filename = "outputs/omp/RKAB_single.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
it = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))

time_par_1 = time[1::8]
time_par_2 = time[3::8]
time_par_4 = time[5::8]
time_par_8 = time[7::8]

time_par_1_5 = time_par_1[0::7]
time_par_2_5 = time_par_2[0::7]
time_par_4_5 = time_par_4[0::7]
time_par_8_5 = time_par_8[0::7]

time_par_1_10 = time_par_1[1::7]
time_par_2_10 = time_par_2[1::7]
time_par_4_10 = time_par_4[1::7]
time_par_8_10 = time_par_8[1::7]

time_par_1_50 = time_par_1[2::7]
time_par_2_50 = time_par_2[2::7]
time_par_4_50 = time_par_4[2::7]
time_par_8_50 = time_par_8[2::7]

time_par_1_100 = time_par_1[3::7]
time_par_2_100 = time_par_2[3::7]
time_par_4_100 = time_par_4[3::7]
time_par_8_100 = time_par_8[3::7]

time_par_1_500 = time_par_1[4::7]
time_par_2_500 = time_par_2[4::7]
time_par_4_500 = time_par_4[4::7]
time_par_8_500 = time_par_8[4::7]

time_par_1_1000 = time_par_1[5::7]
time_par_2_1000 = time_par_2[5::7]
time_par_4_1000 = time_par_4[5::7]
time_par_8_1000 = time_par_8[5::7]

time_par_1_10000 = time_par_1[6::7]
time_par_2_10000 = time_par_2[6::7]
time_par_4_10000 = time_par_4[6::7]
time_par_8_10000 = time_par_8[6::7]

it_par_1 = it[1::8]
it_par_2 = it[3::8]
it_par_4 = it[5::8]
it_par_8 = it[7::8]

blocks = [5, 10, 50, 100, 500, 1000, 10000]

lines_par_2 = [it_par_2[i]*2*blocks[i%7] for i in range(len(it_par_2))]
lines_par_4 = [it_par_4[i]*4*blocks[i%7] for i in range(len(it_par_4))]
lines_par_8 = [it_par_8[i]*8*blocks[i%7] for i in range(len(it_par_8))]

it_par_1_5 = it_par_1[0::7]
it_par_2_5 = it_par_2[0::7]
it_par_4_5 = it_par_4[0::7]
it_par_8_5 = it_par_8[0::7]

lines_par_1_5 = [it_par_1_5[i]*1*5 for i in range(9)]
lines_par_2_5 = [it_par_2_5[i]*2*5 for i in range(9)]
lines_par_4_5 = [it_par_4_5[i]*4*5 for i in range(9)]
lines_par_8_5 = [it_par_8_5[i]*8*5 for i in range(9)]

it_par_1_10 = it_par_1[1::7]
it_par_2_10 = it_par_2[1::7]
it_par_4_10 = it_par_4[1::7]
it_par_8_10 = it_par_8[1::7]

lines_par_1_10 = [it_par_1_10[i]*1*10 for i in range(9)]
lines_par_2_10 = [it_par_2_10[i]*2*10 for i in range(9)]
lines_par_4_10 = [it_par_4_10[i]*4*10 for i in range(9)]
lines_par_8_10 = [it_par_8_10[i]*8*10 for i in range(9)]

it_par_1_50 = it_par_1[2::7]
it_par_2_50 = it_par_2[2::7]
it_par_4_50 = it_par_4[2::7]
it_par_8_50 = it_par_8[2::7]

lines_par_1_50 = [it_par_1_50[i]*1*50 for i in range(9)]
lines_par_2_50 = [it_par_2_50[i]*2*50 for i in range(9)]
lines_par_4_50 = [it_par_4_50[i]*4*50 for i in range(9)]
lines_par_8_50 = [it_par_8_50[i]*8*50 for i in range(9)]

it_par_1_100 = it_par_1[3::7]
it_par_2_100 = it_par_2[3::7]
it_par_4_100 = it_par_4[3::7]
it_par_8_100 = it_par_8[3::7]

lines_par_1_100 = [it_par_1_100[i]*1*100 for i in range(9)]
lines_par_2_100 = [it_par_2_100[i]*2*100 for i in range(9)]
lines_par_4_100 = [it_par_4_100[i]*4*100 for i in range(9)]
lines_par_8_100 = [it_par_8_100[i]*8*100 for i in range(9)]

it_par_1_500 = it_par_1[4::7]
it_par_2_500 = it_par_2[4::7]
it_par_4_500 = it_par_4[4::7]
it_par_8_500 = it_par_8[4::7]

lines_par_1_500 = [it_par_1_500[i]*1*500 for i in range(9)]
lines_par_2_500 = [it_par_2_500[i]*2*500 for i in range(9)]
lines_par_4_500 = [it_par_4_500[i]*4*500 for i in range(9)]
lines_par_8_500 = [it_par_8_500[i]*8*500 for i in range(9)]

it_par_1_1000 = it_par_1[5::7]
it_par_2_1000 = it_par_2[5::7]
it_par_4_1000 = it_par_4[5::7]
it_par_8_1000 = it_par_8[5::7]

lines_par_1_1000 = [it_par_1_1000[i]*1*1000 for i in range(9)]
lines_par_2_1000 = [it_par_2_1000[i]*2*1000 for i in range(9)]
lines_par_4_1000 = [it_par_4_1000[i]*4*1000 for i in range(9)]
lines_par_8_1000 = [it_par_8_1000[i]*8*1000 for i in range(9)]

it_par_1_10000 = it_par_1[6::7]
it_par_2_10000 = it_par_2[6::7]
it_par_4_10000 = it_par_4[6::7]
it_par_8_10000 = it_par_8[6::7]

lines_par_1_10000 = [it_par_1_10000[i]*1*10000 for i in range(9)]
lines_par_2_10000 = [it_par_2_10000[i]*2*10000 for i in range(9)]
lines_par_4_10000 = [it_par_4_10000[i]*4*10000 for i in range(9)]
lines_par_8_10000 = [it_par_8_10000[i]*8*10000 for i in range(9)]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = [5, 10, 50, 100, 500, 1000, 10000]

plot_title = r"$80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=time_seq_dim[6], linestyle='--', linewidth=1.5, color='black', label=r'Sequential')
plt.scatter(x, time_par_2[42:49], color='orange')
plt.plot(x, time_par_2[42:49], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, time_par_4[42:49], color='red')
plt.plot(x, time_par_4[42:49], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, time_par_8[42:49], color='blue')
plt.plot(x, time_par_8[42:49], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RKAB_single_seq_extra_time_80000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[6], linestyle='--', linewidth=1.5, color='black', label=r'Sequential')
plt.scatter(x, lines_par_2[42:49], color='orange')
plt.plot(x, lines_par_2[42:49], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, lines_par_4[42:49], color='red')
plt.plot(x, lines_par_4[42:49], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, lines_par_8[42:49], color='blue')
plt.plot(x, lines_par_8[42:49], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Total Number of Used Rows')

filename_fig = "RKAB_single_seq_extra_lines_80000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r"$80000 \times 1000$"

fig = plt.figure(figsize=(10, 7))
# plt.axhline(y=it_seq_dim[6], linestyle='--', linewidth=1.5, color='black', label=r'Sequential')
plt.scatter(x, it_par_2[42:49], color='orange')
plt.plot(x, it_par_2[42:49], linewidth=1.5, color='orange', label=r'Threads = 2')
plt.scatter(x, it_par_4[42:49], color='red')
plt.plot(x, it_par_4[42:49], linewidth=1.5, color='red', label=r'Threads = 4')
plt.scatter(x, it_par_8[42:49], color='blue')
plt.plot(x, it_par_8[42:49], linewidth=1.5, color='blue', label=r'Threads = 8')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Block Size')
plt.ylabel(r'Iterations')

filename_fig = "RKAB_single_seq_extra_it_80000_1000"

# plt.show()
fig.savefig("plots/omp/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/omp/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()