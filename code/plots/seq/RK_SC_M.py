import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/RK_SC_M.py

# filename = "outputs/seq/RK_seq_countSC.txt";

# with open(filename) as f:
#     lines = f.read().splitlines()

# file_size = len(lines)

# count_error = []
# count_res = []
# for i in range(37):
#     count_error.append(int(lines[i].split()[6]))
#     count_res.append(int(lines[i].split()[7]))

# count_2000_error = count_error[0:5]
# count_4000_error = count_error[5:11]
# count_20000_error = count_error[11:19]
# count_40000_error = count_error[19:28]
# count_80000_error = count_error[28:37]

# count_2000_res = count_res[0:5]
# count_4000_res = count_res[5:11]
# count_20000_res = count_res[11:19]
# count_40000_res = count_res[19:28]
# count_80000_res = count_res[28:37]

# count_2000 = [100.0*float(count_2000_res[i])/float(count_2000_error[i]) for i in range(len(count_2000_res))]
# count_4000 = [100.0*float(count_4000_res[i])/float(count_4000_error[i]) for i in range(len(count_4000_res))]
# count_20000 = [100.0*float(count_20000_res[i])/float(count_20000_error[i]) for i in range(len(count_20000_res))]
# count_40000 = [100.0*float(count_40000_res[i])/float(count_40000_error[i]) for i in range(len(count_40000_res))]
# count_80000 = [100.0*float(count_80000_res[i])/float(count_80000_error[i]) for i in range(len(count_80000_res))]

filename = "outputs/seq/RK_seq_SC.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(74):
	time.append(float(lines[i].split()[2]))

time_SC = time[0::2]
time_no_SC = time[1::2]

x_2000 = [50, 100, 200, 500, 750]
x_4000 = [50, 100, 200, 500, 750, 1000]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000]
x_40000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]
x_80000 = [50, 100, 200, 500, 750, 1000, 2000, 4000, 10000]

time_2000_SC = time_SC[0:5]
time_4000_SC = time_SC[5:11]
time_20000_SC = time_SC[11:19]
time_40000_SC = time_SC[19:28]
time_80000_SC = time_SC[28:37]

time_2000_no_SC = time_no_SC[0:5]
time_4000_no_SC = time_no_SC[5:11]
time_20000_no_SC = time_no_SC[11:19]
time_40000_no_SC = time_no_SC[19:28]
time_80000_no_SC = time_no_SC[28:37]

time_2000 = [100.0-100.0*time_2000_no_SC[i]/time_2000_SC[i] for i in range(len(time_2000_no_SC))]
time_4000 = [100.0-100.0*time_4000_no_SC[i]/time_4000_SC[i] for i in range(len(time_4000_no_SC))]
time_20000 = [100.0-100.0*time_20000_no_SC[i]/time_20000_SC[i] for i in range(len(time_20000_no_SC))]
time_40000 = [100.0-100.0*time_40000_no_SC[i]/time_40000_SC[i] for i in range(len(time_40000_no_SC))]
time_80000 = [100.0-100.0*time_80000_no_SC[i]/time_80000_SC[i] for i in range(len(time_80000_no_SC))]

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
# plt.scatter(x_2000[3::], time_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
# plt.plot(x_2000[3::], time_2000[3::], linewidth=1.5, color='yellow')
# plt.scatter(x_4000[3::], time_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
# plt.plot(x_4000[3::], time_4000[3::], linewidth=1.5, color='orange')
# plt.scatter(x_20000[3::], time_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
# plt.plot(x_20000[3::], time_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[5::], time_40000[5::], linewidth=1.5, color='red', label=r'$m = 40000$')
plt.plot(x_40000[5::], time_40000[5::], linewidth=1.5, color='red')
plt.scatter(x_80000[5::], time_80000[5::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[5::], time_80000[5::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Time of Stopping Criteria / Total Time (\%)')

filename_fig = "RK_SC_M_time"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r'RK - Overdetermined systems sampled from $N(\mu,\sigma)$'

# fig = plt.figure(figsize=(10, 7))
# plt.scatter(x_2000[3::], count_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
# plt.plot(x_2000[3::], count_2000[3::], linewidth=1.5, color='yellow')
# plt.scatter(x_4000[3::], count_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
# plt.plot(x_4000[3::], count_4000[3::], linewidth=1.5, color='orange')
# plt.scatter(x_20000[3::], count_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
# plt.plot(x_20000[3::], count_20000[3::], linewidth=1.5, color='red')
# plt.scatter(x_40000[3::], count_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
# plt.plot(x_40000[3::], count_40000[3::], linewidth=1.5, color='purple')
# plt.scatter(x_80000[3::], count_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
# plt.plot(x_80000[3::], count_80000[3::], linewidth=1.5, color='blue')
# plt.grid()
# plt.legend()
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$n$')
# plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated (\%)')

# filename_fig = "RK_SC_M_count"

# plt.show()
# fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')