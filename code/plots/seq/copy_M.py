import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/copy_M.py

filename = "outputs/seq/RK_norep_rand.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

RK_norep_it_2000 = it[0:6]
RK_norep_time_2000 = time[0:6]
RK_norep_it_4000 = it[6:13]
RK_norep_time_4000 = time[6:13]
RK_norep_it_20000 = it[13:22]
RK_norep_time_20000 = time[13:22]
RK_norep_it_40000 = it[22:31]
RK_norep_time_40000 = time[22:31]
RK_norep_it_80000 = it[31:40]
RK_norep_time_80000 = time[31:40]

filename = "outputs/seq/RK_norep_rand_noshuffle.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

RK_norep_noshuffle_it_2000 = it[0:6]
RK_norep_noshuffle_time_2000 = time[0:6]
RK_norep_noshuffle_it_4000 = it[6:13]
RK_norep_noshuffle_time_4000 = time[6:13]
RK_norep_noshuffle_it_20000 = it[13:22]
RK_norep_noshuffle_time_20000 = time[13:22]
RK_norep_noshuffle_it_40000 = it[22:31]
RK_norep_noshuffle_time_40000 = time[22:31]
RK_norep_noshuffle_it_80000 = it[31:40]
RK_norep_noshuffle_time_80000 = time[31:40]

filename = "outputs/seq/RK_norep_rand_copy.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

RK_norep_copy_it_2000 = it[0:6]
RK_norep_copy_time_2000 = time[0:6]
RK_norep_copy_it_4000 = it[6:13]
RK_norep_copy_time_4000 = time[6:13]
RK_norep_copy_it_20000 = it[13:22]
RK_norep_copy_time_20000 = time[13:22]
RK_norep_copy_it_40000 = it[22:31]
RK_norep_copy_time_40000 = time[22:31]
RK_norep_copy_it_80000 = it[31:40]
RK_norep_copy_time_80000 = time[31:40]

filename = "outputs/seq/RK_norep_rand_noshuffle_copy.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

RK_norep_noshuffle_copy_it_2000 = it[0:6]
RK_norep_noshuffle_copy_time_2000 = time[0:6]
RK_norep_noshuffle_copy_it_4000 = it[6:13]
RK_norep_noshuffle_copy_time_4000 = time[6:13]
RK_norep_noshuffle_copy_it_20000 = it[13:22]
RK_norep_noshuffle_copy_time_20000 = time[13:22]
RK_norep_noshuffle_copy_it_40000 = it[22:31]
RK_norep_noshuffle_copy_time_40000 = time[22:31]
RK_norep_noshuffle_copy_it_80000 = it[31:40]
RK_norep_noshuffle_copy_time_80000 = time[31:40]

x_2000 = [50, 100, 200, 500, 750, 1000]
x_4000 = [50, 100, 200, 500, 750, 1000, 2000]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]
x_40000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]
x_80000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 2000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_2000, RK_norep_time_2000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling w/o copy)')
plt.scatter(x_2000, RK_norep_time_2000, linewidth=1.5, color='red')
plt.plot(x_2000, RK_norep_copy_time_2000, linewidth=1.5, color='red', linestyle='--', label=r'SRKWOR \\ (w/ shuffling w/ copy)')
plt.scatter(x_2000, RK_norep_copy_time_2000, linewidth=1.5, color='red')
plt.plot(x_2000, RK_norep_noshuffle_time_2000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling w/o copy)')
plt.scatter(x_2000, RK_norep_noshuffle_time_2000, linewidth=1.5, color='blue')
plt.plot(x_2000, RK_norep_noshuffle_copy_time_2000, linewidth=1.5, color='blue', linestyle='--', label=r'SRKWOR \\ (w/o shuffling w/ copy)')
plt.scatter(x_2000, RK_norep_noshuffle_copy_time_2000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "copy_M_time_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 4000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, RK_norep_time_4000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling w/o copy)')
plt.scatter(x_4000, RK_norep_time_4000, linewidth=1.5, color='red')
plt.plot(x_4000, RK_norep_copy_time_4000, linewidth=1.5, color='red', linestyle='--', label=r'SRKWOR \\ (w/ shuffling w/ copy)')
plt.scatter(x_4000, RK_norep_copy_time_4000, linewidth=1.5, color='red')
plt.plot(x_4000, RK_norep_noshuffle_time_4000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling w/o copy)')
plt.scatter(x_4000, RK_norep_noshuffle_time_4000, linewidth=1.5, color='blue')
plt.plot(x_4000, RK_norep_noshuffle_copy_time_4000, linewidth=1.5, color='blue', linestyle='--', label=r'SRKWOR \\ (w/o shuffling w/ copy)')
plt.scatter(x_4000, RK_norep_noshuffle_copy_time_4000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "copy_M_time_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 20000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_20000, RK_norep_time_20000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling w/o copy)')
plt.scatter(x_20000, RK_norep_time_20000, linewidth=1.5, color='red')
plt.plot(x_20000, RK_norep_copy_time_20000, linewidth=1.5, color='red', linestyle='--', label=r'SRKWOR \\ (w/ shuffling w/ copy)')
plt.scatter(x_20000, RK_norep_copy_time_20000, linewidth=1.5, color='red')
plt.plot(x_20000, RK_norep_noshuffle_time_20000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling w/o copy)')
plt.scatter(x_20000, RK_norep_noshuffle_time_20000, linewidth=1.5, color='blue')
plt.plot(x_20000, RK_norep_noshuffle_copy_time_20000, linewidth=1.5, color='blue', linestyle='--', label=r'SRKWOR \\ (w/o shuffling w/ copy)')
plt.scatter(x_20000, RK_norep_noshuffle_copy_time_20000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "copy_M_time_20000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 40000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_40000, RK_norep_time_40000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling w/o copy)')
plt.scatter(x_40000, RK_norep_time_40000, linewidth=1.5, color='red')
plt.plot(x_40000, RK_norep_copy_time_40000, linewidth=1.5, color='red', linestyle='--', label=r'SRKWOR \\ (w/ shuffling w/ copy)')
plt.scatter(x_40000, RK_norep_copy_time_40000, linewidth=1.5, color='red')
plt.plot(x_40000, RK_norep_noshuffle_time_40000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling w/o copy)')
plt.scatter(x_40000, RK_norep_noshuffle_time_40000, linewidth=1.5, color='blue')
plt.plot(x_40000, RK_norep_noshuffle_copy_time_40000, linewidth=1.5, color='blue', linestyle='--', label=r'SRKWOR \\ (w/o shuffling w/ copy)')
plt.scatter(x_40000, RK_norep_noshuffle_copy_time_40000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "copy_M_time_40000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 80000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_80000, RK_norep_time_80000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling w/o copy)')
plt.scatter(x_80000, RK_norep_time_80000, linewidth=1.5, color='red')
plt.plot(x_80000, RK_norep_copy_time_80000, linewidth=1.5, color='red', linestyle='--', label=r'SRKWOR \\ (w/ shuffling w/ copy)')
plt.scatter(x_80000, RK_norep_copy_time_80000, linewidth=1.5, color='red')
plt.plot(x_80000, RK_norep_noshuffle_time_80000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling w/o copy)')
plt.scatter(x_80000, RK_norep_noshuffle_time_80000, linewidth=1.5, color='blue')
plt.plot(x_80000, RK_norep_noshuffle_copy_time_80000, linewidth=1.5, color='blue', linestyle='--', label=r'SRKWOR \\ (w/o shuffling w/ copy)')
plt.scatter(x_80000, RK_norep_noshuffle_copy_time_80000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Total Time (s)')

filename_fig = "copy_M_time_80000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 2000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_2000, RK_norep_it_2000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling)')
plt.scatter(x_2000, RK_norep_it_2000, linewidth=1.5, color='red')
plt.plot(x_2000, RK_norep_noshuffle_it_2000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling)')
plt.scatter(x_2000, RK_norep_noshuffle_it_2000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "copy_M_it_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 4000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_4000, RK_norep_it_4000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling)')
plt.scatter(x_4000, RK_norep_it_4000, linewidth=1.5, color='red')
plt.plot(x_4000, RK_norep_noshuffle_it_4000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling)')
plt.scatter(x_4000, RK_norep_noshuffle_it_4000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "copy_M_it_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 20000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_20000, RK_norep_it_20000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling)')
plt.scatter(x_20000, RK_norep_it_20000, linewidth=1.5, color='red')
plt.plot(x_20000, RK_norep_noshuffle_it_20000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling)')
plt.scatter(x_20000, RK_norep_noshuffle_it_20000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "copy_M_it_20000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 40000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_40000, RK_norep_it_40000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling)')
plt.scatter(x_40000, RK_norep_it_40000, linewidth=1.5, color='red')
plt.plot(x_40000, RK_norep_noshuffle_it_40000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling)')
plt.scatter(x_40000, RK_norep_noshuffle_it_40000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "copy_M_it_40000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $m = 80000$'

fig = plt.figure(figsize=(10, 7))
plt.plot(x_80000, RK_norep_it_80000, linewidth=1.5, color='red', label=r'SRKWOR \\ (w/ shuffling)')
plt.scatter(x_80000, RK_norep_it_80000, linewidth=1.5, color='red')
plt.plot(x_80000, RK_norep_noshuffle_it_80000, linewidth=1.5, color='blue', label=r'SRKWOR \\ (w/o shuffling)')
plt.scatter(x_80000, RK_norep_noshuffle_it_80000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Iterations')

filename_fig = "copy_M_it_80000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()