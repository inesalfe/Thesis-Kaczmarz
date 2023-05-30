import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/RK_cond1_M.py

filename = "outputs/seq/RK_seq_eps1.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

count_error = []
for i in range(file_size):
    count_error.append(int(lines[i].split()[6]))

count_error_before = count_error[0::2]
count_error_after = count_error[1::2]

count_2000_error_before = count_error_before[0:5]
count_4000_error_before = count_error_before[5:11]
count_20000_error_before = count_error_before[11:19]
count_40000_error_before = count_error_before[19:28]
count_80000_error_before = count_error_before[28:37]

count_2000_error_after = count_error_after[0:5]
count_4000_error_after = count_error_after[5:11]
count_20000_error_after = count_error_after[11:19]
count_40000_error_after = count_error_after[19:28]
count_80000_error_after = count_error_after[28:37]

count_2000 = [100.0*float(count_2000_error_after[i])/float(count_2000_error_before[i]) for i in range(len(count_2000_error_after))]
count_4000 = [100.0*float(count_4000_error_after[i])/float(count_4000_error_before[i]) for i in range(len(count_4000_error_after))]
count_20000 = [100.0*float(count_20000_error_after[i])/float(count_20000_error_before[i]) for i in range(len(count_20000_error_after))]
count_40000 = [100.0*float(count_40000_error_after[i])/float(count_40000_error_before[i]) for i in range(len(count_40000_error_after))]
count_80000 = [100.0*float(count_80000_error_after[i])/float(count_80000_error_before[i]) for i in range(len(count_80000_error_after))]

filename = "outputs/seq/RK_seq_eps1.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))

time_before = time[0::2]
time_after = time[1::2]

x_2000 = [50, 100, 200, 500, 750]
x_4000 = [50, 100, 200, 500, 750, 1000]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000]
x_40000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]
x_80000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

time_2000_before = time_before[0:5]
time_4000_before = time_before[5:11]
time_20000_before = time_before[11:19]
time_40000_before = time_before[19:28]
time_80000_before = time_before[28:37]

time_2000_after = time_after[0:5]
time_4000_after = time_after[5:11]
time_20000_after = time_after[11:19]
time_40000_after = time_after[19:28]
time_80000_after = time_after[28:37]

time_2000 = [100.0*time_2000_after[i]/time_2000_before[i] for i in range(len(time_2000_after))]
time_4000 = [100.0*time_4000_after[i]/time_4000_before[i] for i in range(len(time_4000_after))]
time_20000 = [100.0*time_20000_after[i]/time_20000_before[i] for i in range(len(time_20000_after))]
time_40000 = [100.0*time_40000_after[i]/time_40000_before[i] for i in range(len(time_40000_after))]
time_80000 = [100.0*time_80000_after[i]/time_80000_before[i] for i in range(len(time_80000_after))]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r'RK - Overdetermined systems sampled from $N(\mu,\sigma)$'

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], time_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], time_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], time_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], time_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], time_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], time_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], time_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], time_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], time_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], time_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Time After / Time Before (\%)')

filename_fig = "RK_cond1_M_time"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

plot_title = r'RK - Overdetermined systems sampled from $N(\mu,\sigma)$'

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], count_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], count_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], count_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], count_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], count_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], count_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], count_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], count_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], count_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], count_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'\# $\|x^{(k)}-x^{*}\|$_{after} / $\|x^{(k)}-x^{*}\|_{before}$ (\%)')

filename_fig = "RK_cond1_M_count"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')