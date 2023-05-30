import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq_norm/Variations_RK_rand_all_norm_M.py

filename = "outputs/seq_norm/RK_norm.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
	it.append(int(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

RK_it_2000 = it[0:6]
RK_time_2000 = time[0:6]
RK_it_4000 = it[6:13]
RK_time_4000 = time[6:13]
RK_it_20000 = it[13:22]
RK_time_20000 = time[13:22]
RK_it_40000 = it[22:31]
RK_time_40000 = time[22:31]
RK_it_80000 = it[31:40]
RK_time_80000 = time[31:40]

filename = "outputs/seq_norm/RK_rand_norm.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

RK_rand_it_2000 = it[0:6]
RK_rand_time_2000 = time[0:6]
RK_rand_it_4000 = it[6:13]
RK_rand_time_4000 = time[6:13]
RK_rand_it_20000 = it[13:22]
RK_rand_time_20000 = time[13:22]
RK_rand_it_40000 = it[22:31]
RK_rand_time_40000 = time[22:31]
RK_rand_it_80000 = it[31:40]
RK_rand_time_80000 = time[31:40]

filename = "outputs/seq_norm/RK_cyclic_norm.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

RK_cyclic_it_2000 = it[0:6]
RK_cyclic_time_2000 = time[0:6]
RK_cyclic_it_4000 = it[6:13]
RK_cyclic_time_4000 = time[6:13]
RK_cyclic_it_20000 = it[13:22]
RK_cyclic_time_20000 = time[13:22]
RK_cyclic_it_40000 = it[22:31]
RK_cyclic_time_40000 = time[22:31]
RK_cyclic_it_80000 = it[31:40]
RK_cyclic_time_80000 = time[31:40]

filename = "outputs/seq_norm/RK_norep_rand_noshuffle_norm.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

RK_norep_rand_noshuffle_it_2000 = it[0:6]
RK_norep_rand_noshuffle_time_2000 = time[0:6]
RK_norep_rand_noshuffle_it_4000 = it[6:13]
RK_norep_rand_noshuffle_time_4000 = time[6:13]
RK_norep_rand_noshuffle_it_20000 = it[13:22]
RK_norep_rand_noshuffle_time_20000 = time[13:22]
RK_norep_rand_noshuffle_it_40000 = it[22:31]
RK_norep_rand_noshuffle_time_40000 = time[22:31]
RK_norep_rand_noshuffle_it_80000 = it[31:40]
RK_norep_rand_noshuffle_time_80000 = time[31:40]

x_2000 = [50, 100, 200, 500, 750, 1000]
x_4000 = [50, 100, 200, 500, 750, 1000, 2000]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]
x_40000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]
x_80000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 2000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_2000, RK_time_2000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_2000, RK_time_2000, linewidth=1.5, color='green')
plt.scatter(x_2000, RK_cyclic_time_2000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_2000, RK_cyclic_time_2000, linewidth=1.5, color='orange')
plt.scatter(x_2000, RK_rand_time_2000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_2000, RK_rand_time_2000, linewidth=1.5, color='blue')
plt.scatter(x_2000, RK_norep_rand_noshuffle_time_2000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_2000, RK_norep_rand_noshuffle_time_2000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_rand_all_norm_M_time_2000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 2000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_2000, RK_it_2000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_2000, RK_it_2000, linewidth=1.5, color='green')
plt.scatter(x_2000, RK_cyclic_it_2000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_2000, RK_cyclic_it_2000, linewidth=1.5, color='orange')
plt.scatter(x_2000, RK_rand_it_2000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_2000, RK_rand_it_2000, linewidth=1.5, color='blue')
plt.scatter(x_2000, RK_norep_rand_noshuffle_it_2000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_2000, RK_norep_rand_noshuffle_it_2000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_rand_all_norm_M_it_2000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 4000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, RK_time_4000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_4000, RK_time_4000, linewidth=1.5, color='green')
plt.scatter(x_4000, RK_cyclic_time_4000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_4000, RK_cyclic_time_4000, linewidth=1.5, color='orange')
plt.scatter(x_4000, RK_rand_time_4000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_4000, RK_rand_time_4000, linewidth=1.5, color='blue')
plt.scatter(x_4000, RK_norep_rand_noshuffle_time_4000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_4000, RK_norep_rand_noshuffle_time_4000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_rand_all_norm_M_time_4000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 4000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, RK_it_4000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_4000, RK_it_4000, linewidth=1.5, color='green')
plt.scatter(x_4000, RK_cyclic_it_4000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_4000, RK_cyclic_it_4000, linewidth=1.5, color='orange')
plt.scatter(x_4000, RK_rand_it_4000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_4000, RK_rand_it_4000, linewidth=1.5, color='blue')
plt.scatter(x_4000, RK_norep_rand_noshuffle_it_4000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_4000, RK_norep_rand_noshuffle_it_4000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_rand_all_norm_M_it_4000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 20000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, RK_time_20000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_20000, RK_time_20000, linewidth=1.5, color='green')
plt.scatter(x_20000, RK_cyclic_time_20000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_20000, RK_cyclic_time_20000, linewidth=1.5, color='orange')
plt.scatter(x_20000, RK_rand_time_20000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_20000, RK_rand_time_20000, linewidth=1.5, color='blue')
plt.scatter(x_20000, RK_norep_rand_noshuffle_time_20000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_20000, RK_norep_rand_noshuffle_time_20000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_rand_all_norm_M_time_20000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 20000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_20000, RK_it_20000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_20000, RK_it_20000, linewidth=1.5, color='green')
plt.scatter(x_20000, RK_cyclic_it_20000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_20000, RK_cyclic_it_20000, linewidth=1.5, color='orange')
plt.scatter(x_20000, RK_rand_it_20000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_20000, RK_rand_it_20000, linewidth=1.5, color='blue')
plt.scatter(x_20000, RK_norep_rand_noshuffle_it_20000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_20000, RK_norep_rand_noshuffle_it_20000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_rand_all_norm_M_it_20000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 40000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_40000, RK_time_40000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_40000, RK_time_40000, linewidth=1.5, color='green')
plt.scatter(x_40000, RK_cyclic_time_40000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_40000, RK_cyclic_time_40000, linewidth=1.5, color='orange')
plt.scatter(x_40000, RK_rand_time_40000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_40000, RK_rand_time_40000, linewidth=1.5, color='blue')
plt.scatter(x_40000, RK_norep_rand_noshuffle_time_40000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_40000, RK_norep_rand_noshuffle_time_40000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_rand_all_norm_M_time_40000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 40000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_40000, RK_it_40000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_40000, RK_it_40000, linewidth=1.5, color='green')
plt.scatter(x_40000, RK_cyclic_it_40000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_40000, RK_cyclic_it_40000, linewidth=1.5, color='orange')
plt.scatter(x_40000, RK_rand_it_40000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_40000, RK_rand_it_40000, linewidth=1.5, color='blue')
plt.scatter(x_40000, RK_norep_rand_noshuffle_it_40000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_40000, RK_norep_rand_noshuffle_it_40000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_rand_all_norm_M_it_40000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 80000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000, RK_time_80000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_80000, RK_time_80000, linewidth=1.5, color='green')
plt.scatter(x_80000, RK_cyclic_time_80000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_80000, RK_cyclic_time_80000, linewidth=1.5, color='orange')
plt.scatter(x_80000, RK_rand_time_80000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_80000, RK_rand_time_80000, linewidth=1.5, color='blue')
plt.scatter(x_80000, RK_norep_rand_noshuffle_time_80000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_80000, RK_norep_rand_noshuffle_time_80000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_rand_all_norm_M_time_80000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(0,1)$ with $m = 80000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_80000, RK_it_80000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_80000, RK_it_80000, linewidth=1.5, color='green')
plt.scatter(x_80000, RK_cyclic_it_80000, linewidth=1.5, color='orange', label=r'CK')
plt.plot(x_80000, RK_cyclic_it_80000, linewidth=1.5, color='orange')
plt.scatter(x_80000, RK_rand_it_80000, linewidth=1.5, color='blue', label=r'SRK')
plt.plot(x_80000, RK_rand_it_80000, linewidth=1.5, color='blue')
plt.scatter(x_80000, RK_norep_rand_noshuffle_it_80000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_80000, RK_norep_rand_noshuffle_it_80000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_rand_all_norm_M_it_80000"

# plt.show()
fig.savefig("plots/seq_norm/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_norm/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()