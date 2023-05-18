import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys
from scipy.optimize import curve_fit
import matplotlib.colors as mcolors

# python3 plots/seq/RK_per_it_M_SC.py

filename = "outputs/seq/RK_seq_SC.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it_total = []
time_total = []
for i in range(file_size):
	it_total.append(int(lines[i].split()[3]))
	time_total.append(float(lines[i].split()[2]))

it = it_total[1::2]
time = time_total[1::2]
it_SC = it_total[0::2]
time_SC = time_total[0::2]

x_2000 = [50, 100, 200, 500, 750]
x_4000 = [50, 100, 200, 500, 750, 1000]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000]
x_40000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]
x_80000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

it_2000 = it[0:5]
time_2000 = time[0:5]
it_2000_SC = it_SC[0:5]
time_2000_SC = time_SC[0:5]
time_per_it_2000 = np.zeros(len(x_2000))
time_per_it_2000_SC = np.zeros(len(x_2000))
for i in range(len(x_2000)):
	time_per_it_2000[i] = time_2000[i] / it_2000[i]
	time_per_it_2000_SC[i] = time_2000_SC[i] / it_2000_SC[i]

it_4000 = it[5:11]
time_4000 = time[5:11]
it_4000_SC = it_SC[5:11]
time_4000_SC = time_SC[5:11]
time_per_it_4000 = np.zeros(len(x_4000))
time_per_it_4000_SC = np.zeros(len(x_4000))
for i in range(len(x_4000)):
	time_per_it_4000[i] = time_4000[i] / it_4000[i]
	time_per_it_4000_SC[i] = time_4000_SC[i] / it_4000_SC[i]

it_20000 = it[11:19]
time_20000 = time[11:19]
it_20000_SC = it_SC[11:19]
time_20000_SC = time_SC[11:19]
time_per_it_20000 = np.zeros(len(x_20000))
time_per_it_20000_SC = np.zeros(len(x_20000))
for i in range(len(x_20000)):
	time_per_it_20000[i] = time_20000[i] / it_20000[i]
	time_per_it_20000_SC[i] = time_20000_SC[i] / it_20000_SC[i]

it_40000 = it[19:28]
time_40000 = time[19:28]
it_40000_SC = it_SC[19:28]
time_40000_SC = time_SC[19:28]
time_per_it_40000 = np.zeros(len(x_40000))
time_per_it_40000_SC = np.zeros(len(x_40000))
for i in range(len(x_40000)):
	time_per_it_40000[i] = time_40000[i] / it_40000[i]
	time_per_it_40000_SC[i] = time_40000_SC[i] / it_40000_SC[i]

it_80000 = it[28:37]
time_80000 = time[28:37]
it_80000_SC = it_SC[28:37]
time_80000_SC = time_SC[28:37]
time_per_it_80000 = np.zeros(len(x_80000))
time_per_it_80000_SC = np.zeros(len(x_80000))
for i in range(len(x_80000)):
	time_per_it_80000[i] = time_80000[i] / it_80000[i]
	time_per_it_80000_SC[i] = time_80000_SC[i] / it_80000_SC[i]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def func(x, a, b):
    return a * x**b

popt, pcov = curve_fit(func, x_80000[4::], time_per_it_80000[4::])
popt_SC, pcov_SC = curve_fit(func, x_80000[4::], time_per_it_80000_SC[4::])

print(popt)
print(popt_SC)

# y1 = func(np.array(x_80000[4::]), popt[0], 1.01)
# y2 = func(np.array(x_80000[4::]), popt_SC[0], 1.01)

# print(1-y1/y2)

y1 = func(np.array(x_80000[4::]), *popt)
y2 = func(np.array(x_80000[4::]), *popt_SC)

fig = plt.figure(figsize=(10, 7))
plt.plot(x_80000[4::], y1, linestyle='--', linewidth=1.5, color='navy')
plt.plot(x_80000[4::], y2, linestyle='--', linewidth=1.5, color='dodgerblue')
plt.scatter(x_80000[4::], time_per_it_80000[4::], linewidth=1.5, marker='x', color='navy', s=50, label=r'w/o Stopping Criteria')
plt.scatter(x_80000[4::], time_per_it_80000_SC[4::], linewidth=1.5, color='dodgerblue', s=50, label=r'w/ Stopping Criteria')
# plt.plot(x_80000[4::], func(np.array(x_80000[4::]), *popt), linestyle='--', linewidth=1.5, color='navy')
# plt.plot(x_80000[4::], func(np.array(x_80000[4::]), *popt_SC), linestyle='--', linewidth=1.5, color='deepskyblue')
# plt.scatter(x_80000[4::], time_per_it_80000[4::], linewidth=1.5, marker='x', color='navy', s=50, label=r'w/o Stopping Criteria')
# plt.scatter(x_80000[4::], time_per_it_80000_SC[4::], linewidth=1.5, color='deepskyblue', s=50, label=r'w/ Stopping Criteria')
# plt.scatter(x_20000[4::], time_per_it_20000[4::], linewidth=1.5, color='red')
# plt.plot(x_20000[4::], time_per_it_20000[4::], linewidth=1.5, color='red', label=r'w/o SC - $m = 20000$')
# plt.scatter(x_40000[4::], time_per_it_40000[4::], linewidth=1.5, color='purple')
# plt.plot(x_40000[4::], time_per_it_40000[4::], linewidth=1.5, color='purple', label=r'w/o SC - $m = 40000$')
# plt.scatter(x_80000[4::], time_per_it_80000[4::], linewidth=1.5, color='blue')
# plt.plot(x_80000[4::], time_per_it_80000[4::], linewidth=1.5, color='blue', label=r'w/o SC - $m = 80000$')
# plt.scatter(x_20000[4::], time_per_it_20000_SC[4::], linewidth=1.5, color='red')
# plt.plot(x_20000[4::], time_per_it_20000_SC[4::], linewidth=1.5, color='red', linestyle='--', label=r'w/ SC - $m = 20000$')
# plt.scatter(x_40000[4::], time_per_it_40000_SC[4::], linewidth=1.5, color='purple')
# plt.plot(x_40000[4::], time_per_it_40000_SC[4::], linewidth=1.5, color='purple', linestyle='--', label=r'w/ SC - $m = 40000$')
# plt.scatter(x_80000[4::], time_per_it_80000_SC[4::], linewidth=1.5, color='blue')
# plt.plot(x_80000[4::], time_per_it_80000_SC[4::], linewidth=1.5, color='blue', linestyle='--', label=r'w/ SC - $m = 80000$')
plt.grid()
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Time per Iteration (s)')

filename_fig = "RK_per_it_M_SC_time"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')