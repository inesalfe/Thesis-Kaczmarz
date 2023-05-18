import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/RK_SC_N.py

# filename = "outputs/seq/RK_seq_countSC.txt";

# with open(filename) as f:
#     lines = f.read().splitlines()

# file_size = len(lines)

# count_error = []
# count_res = []
# for i in range(37):
#     count_error.append(int(lines[i].split()[6]))
#     count_res.append(int(lines[i].split()[7]))

# indices = (0, 5, 11, 19, 28)
# count_50 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]
# indices = (1, 6, 12, 20, 29)
# count_100 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]
# indices = (2, 7, 13, 21, 30)
# count_200 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]
# indices = (3, 8, 14, 22, 31)
# count_500 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]
# indices = (4, 9, 15, 23, 32)
# count_750 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]
# indices = (10, 16, 24, 33)
# count_1000 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]
# indices = (17, 25, 34)
# count_2000 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]
# indices = (18, 26, 35)
# count_4000 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]
# indices = (27, 36)
# count_10000 = [100.0*float(count_res[i])/float(count_error[i]) for i in indices]

filename = "outputs/seq/RK_seq_SC.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

time = []
for i in range(74):
	time.append(float(lines[i].split()[2]))

time_SC = time[0::2]
time_no_SC = time[1::2]

indices = (0, 5, 11, 19, 28)
time_50 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_50 = [2000, 4000, 20000, 40000, 80000]

indices = (1, 6, 12, 20, 29)
time_100 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_100 = [2000, 4000, 20000, 40000, 80000]

indices = (2, 7, 13, 21, 30)
time_200 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_200 = [2000, 4000, 20000, 40000, 80000]

indices = (3, 8, 14, 22, 31)
time_500 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_500 = [2000, 4000, 20000, 40000, 80000]

indices = (4, 9, 15, 23, 32)
time_750 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_750 = [2000, 4000, 20000, 40000, 80000]

indices = (10, 16, 24, 33)
time_1000 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_1000 = [4000, 20000, 40000, 80000]

indices = (17, 25, 34)
time_2000 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_2000 = [20000, 40000, 80000]

indices = (18, 26, 35)
time_4000 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_4000 = [20000, 40000, 80000]

indices = (27, 36)
time_10000 = [100.0-100.0*time_no_SC[i]/time_SC[i] for i in indices]
x_10000 = [40000, 80000]

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

# plt.scatter(x_50, time_50, linewidth=1.5, color='yellow', label=r'$n = 50$')
# plt.plot(x_50, time_50, linewidth=1.5, color='yellow')
# plt.scatter(x_100, time_100, linewidth=1.5, color='orange', label=r'$n = 100$')
# plt.plot(x_100, time_100, linewidth=1.5, color='orange')
# plt.scatter(x_200, time_200, linewidth=1.5, color='red', label=r'$n = 200$')
# plt.plot(x_200, time_200, linewidth=1.5, color='red')
# plt.scatter(x_500, time_500, linewidth=1.5, color='magenta', label=r'$n = 500$')
# plt.plot(x_500, time_500, linewidth=1.5, color='magenta')
plt.scatter(x_750, time_750, linewidth=1.5, color='purple', label=r'$n = 750$')
plt.plot(x_750, time_750, linewidth=1.5, color='purple')
plt.scatter(x_1000, time_1000, linewidth=1.5, color='brown', label=r'$n = 1000$')
plt.plot(x_1000, time_1000, linewidth=1.5, color='brown')
plt.scatter(x_2000, time_2000, linewidth=1.5, color='blue', label=r'$n = 2000$')
plt.plot(x_2000, time_2000, linewidth=1.5, color='blue')
plt.scatter(x_4000, time_4000, linewidth=1.5, color='black', label=r'$n = 4000$')
plt.plot(x_4000, time_4000, linewidth=1.5, color='black')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Time w/o Stopping Criteria / Time w/ Stopping Criteria (\%)')

filename_fig = "RK_SC_N_time"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

# plot_title = r'RK - Overdetermined systems sampled from $N(\mu,\sigma)$'

# fig = plt.figure(figsize=(10, 7))

# # plt.scatter(x_50, count_50, linewidth=1.5, color='yellow', label=r'$n = 50$')
# # plt.plot(x_50, count_50, linewidth=1.5, color='yellow')
# # plt.scatter(x_100, count_100, linewidth=1.5, color='orange', label=r'$n = 100$')
# # plt.plot(x_100, count_100, linewidth=1.5, color='orange')
# plt.scatter(x_200, count_200, linewidth=1.5, color='red', label=r'$n = 200$')
# plt.plot(x_200, count_200, linewidth=1.5, color='red')
# plt.scatter(x_500, count_500, linewidth=1.5, color='magenta', label=r'$n = 500$')
# plt.plot(x_500, count_500, linewidth=1.5, color='magenta')
# plt.scatter(x_750, count_750, linewidth=1.5, color='purple', label=r'$n = 750$')
# plt.plot(x_750, count_750, linewidth=1.5, color='purple')
# plt.scatter(x_1000, count_1000, linewidth=1.5, color='brown', label=r'$n = 1000$')
# plt.plot(x_1000, count_1000, linewidth=1.5, color='brown')
# plt.scatter(x_2000, count_2000, linewidth=1.5, color='blue', label=r'$n = 2000$')
# plt.plot(x_2000, count_2000, linewidth=1.5, color='blue')
# plt.scatter(x_4000, count_4000, linewidth=1.5, color='black', label=r'$n = 4000$')
# plt.plot(x_4000, count_4000, linewidth=1.5, color='black')
# plt.grid()
# plt.legend(loc='upper right')
# # plt.title(plot_title)
# plt.yscale('log')
# plt.xscale('log')
# plt.xlabel(r'$m$')
# plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated (\%)')

# filename_fig = "RK_SC_N_count"

# plt.show()
# fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
# fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')