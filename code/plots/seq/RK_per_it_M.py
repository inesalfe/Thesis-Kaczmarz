import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/RK_per_it_M.py

filename = "outputs/seq/RK.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
	it.append(int(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

it_2000 = it[0:6]
time_2000 = time[0:6]
time_per_it_2000 = np.zeros(6)
for i in range(6):
	time_per_it_2000[i] = time_2000[i] / it_2000[i]
x_2000 = [50, 100, 200, 500, 750, 1000]

it_4000 = it[6:13]
time_4000 = time[6:13]
time_per_it_4000 = np.zeros(6)
for i in range(6):
	time_per_it_4000[i] = time_4000[i] / it_4000[i]
x_4000 = [50, 100, 200, 500, 750, 1000]

it_20000 = it[13:22]
time_20000 = time[13:22]
time_per_it_20000 = np.zeros(6)
for i in range(6):
	time_per_it_20000[i] = time_20000[i] / it_20000[i]
x_20000 = [50, 100, 200, 500, 750, 1000]

it_40000 = it[22:31]
time_40000 = time[22:31]
time_per_it_40000 = np.zeros(6)
for i in range(6):
	time_per_it_40000[i] = time_40000[i] / it_40000[i]
x_40000 = [50, 100, 200, 500, 750, 1000]

it_80000 = it[32:40]
time_80000 = time[32:40]
time_per_it_80000 = np.zeros(6)
for i in range(6):
	time_per_it_80000[i] = time_80000[i] / it_80000[i]
x_80000 = [50, 100, 200, 500, 750, 1000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r'RK - Overdetermined systems sampled from $N(\mu,\sigma)$'

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
plt.scatter(x_2000, time_per_it_2000, linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000, time_per_it_2000, linewidth=1.5, color='yellow')
plt.scatter(x_4000, time_per_it_4000, linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000, time_per_it_4000, linewidth=1.5, color='orange')
plt.scatter(x_20000, time_per_it_20000, linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000, time_per_it_20000, linewidth=1.5, color='red')
plt.scatter(x_40000, time_per_it_40000, linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000, time_per_it_40000, linewidth=1.5, color='purple')
plt.scatter(x_80000, time_per_it_80000, linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000, time_per_it_80000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
# start, end = ax.get_ylim()
# ax.yaxis.set_ticks(np.arange(start, end, 20))
plt.yticks([4E-6, 1E-5, 2E-5, 8E-5], (r'$4 \times 10^{-6}$', r'$10^{-5}$', r'$2 \times 10^{-5}$', r'$8 \times 10^{-5}$') )
# ax.yaxis.set_major_locator(plt.MultipleLocator(10))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
plt.xlabel(r'$n$')
plt.ylabel(r'Time per Iteration (s)')

filename_fig = "RK_per_it_M_time"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')