import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/Variations_RK_quasirand_all_N.py

filename = "outputs/seq/RK.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
	it.append(int(lines[i].split()[3]))
	time.append(float(lines[i].split()[2]))

indices = (0, 6, 13, 22, 31)
RK_it_50 = [it[i] for i in indices]
RK_time_50 = [time[i] for i in indices]
indices = (1, 7, 14, 23, 32)
RK_it_100 = [it[i] for i in indices]
RK_time_100 = [time[i] for i in indices]
indices = (2, 8, 15, 24, 33)
RK_it_200 = [it[i] for i in indices]
RK_time_200 = [time[i] for i in indices]
indices = (3, 9, 16, 25, 34)
RK_it_500 = [it[i] for i in indices]
RK_time_500 = [time[i] for i in indices]
indices = (4, 10, 17, 26, 35)
RK_it_750 = [it[i] for i in indices]
RK_time_750 = [time[i] for i in indices]
indices = (5, 11, 18, 27, 36)
RK_it_1000 = [it[i] for i in indices]
RK_time_1000 = [time[i] for i in indices]
indices = (12, 19, 28, 37)
RK_it_2000 = [it[i] for i in indices]
RK_time_2000 = [time[i] for i in indices]
indices = (20, 29, 38)
RK_it_4000 = [it[i] for i in indices]
RK_time_4000 = [time[i] for i in indices]
indices = (21, 30, 39)
RK_it_10000 = [it[i] for i in indices]
RK_time_10000 = [time[i] for i in indices]

filename = "outputs/seq/RK_norep_rand_noshuffle.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

indices = (0, 6, 13, 22, 31)
RK_norep_rand_noshuffle_it_50 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_50 = [time[i] for i in indices]
indices = (1, 7, 14, 23, 32)
RK_norep_rand_noshuffle_it_100 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_100 = [time[i] for i in indices]
indices = (2, 8, 15, 24, 33)
RK_norep_rand_noshuffle_it_200 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_200 = [time[i] for i in indices]
indices = (3, 9, 16, 25, 34)
RK_norep_rand_noshuffle_it_500 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_500 = [time[i] for i in indices]
indices = (4, 10, 17, 26, 35)
RK_norep_rand_noshuffle_it_750 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_750 = [time[i] for i in indices]
indices = (5, 11, 18, 27, 36)
RK_norep_rand_noshuffle_it_1000 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_1000 = [time[i] for i in indices]
indices = (12, 19, 28, 37)
RK_norep_rand_noshuffle_it_2000 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_2000 = [time[i] for i in indices]
indices = (20, 29, 38)
RK_norep_rand_noshuffle_it_4000 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_4000 = [time[i] for i in indices]
indices = (21, 30, 39)
RK_norep_rand_noshuffle_it_10000 = [it[i] for i in indices]
RK_norep_rand_noshuffle_time_10000 = [time[i] for i in indices]

filename = "outputs/seq/RK_quasirand.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

indices = (0, 6, 13, 22, 31)
RK_quasirand_it_50 = [it[i] for i in indices]
RK_quasirand_time_50 = [time[i] for i in indices]
indices = (1, 7, 14, 23, 32)
RK_quasirand_it_100 = [it[i] for i in indices]
RK_quasirand_time_100 = [time[i] for i in indices]
indices = (2, 8, 15, 24, 33)
RK_quasirand_it_200 = [it[i] for i in indices]
RK_quasirand_time_200 = [time[i] for i in indices]
indices = (3, 9, 16, 25, 34)
RK_quasirand_it_500 = [it[i] for i in indices]
RK_quasirand_time_500 = [time[i] for i in indices]
indices = (4, 10, 17, 26, 35)
RK_quasirand_it_750 = [it[i] for i in indices]
RK_quasirand_time_750 = [time[i] for i in indices]
indices = (5, 11, 18, 27, 36)
RK_quasirand_it_1000 = [it[i] for i in indices]
RK_quasirand_time_1000 = [time[i] for i in indices]
indices = (12, 19, 28, 37)
RK_quasirand_it_2000 = [it[i] for i in indices]
RK_quasirand_time_2000 = [time[i] for i in indices]
indices = (20, 29, 38)
RK_quasirand_it_4000 = [it[i] for i in indices]
RK_quasirand_time_4000 = [time[i] for i in indices]
indices = (21, 30, 39)
RK_quasirand_it_10000 = [it[i] for i in indices]
RK_quasirand_time_10000 = [time[i] for i in indices]

filename = "outputs/seq/RK_quasirand_sobol.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
for i in range(40):
    it.append(int(lines[i].split()[3]))
    time.append(float(lines[i].split()[2]))

indices = (0, 6, 13, 22, 31)
RK_quasirand_sobol_it_50 = [it[i] for i in indices]
RK_quasirand_sobol_time_50 = [time[i] for i in indices]
indices = (1, 7, 14, 23, 32)
RK_quasirand_sobol_it_100 = [it[i] for i in indices]
RK_quasirand_sobol_time_100 = [time[i] for i in indices]
indices = (2, 8, 15, 24, 33)
RK_quasirand_sobol_it_200 = [it[i] for i in indices]
RK_quasirand_sobol_time_200 = [time[i] for i in indices]
indices = (3, 9, 16, 25, 34)
RK_quasirand_sobol_it_500 = [it[i] for i in indices]
RK_quasirand_sobol_time_500 = [time[i] for i in indices]
indices = (4, 10, 17, 26, 35)
RK_quasirand_sobol_it_750 = [it[i] for i in indices]
RK_quasirand_sobol_time_750 = [time[i] for i in indices]
indices = (5, 11, 18, 27, 36)
RK_quasirand_sobol_it_1000 = [it[i] for i in indices]
RK_quasirand_sobol_time_1000 = [time[i] for i in indices]
indices = (12, 19, 28, 37)
RK_quasirand_sobol_it_2000 = [it[i] for i in indices]
RK_quasirand_sobol_time_2000 = [time[i] for i in indices]
indices = (20, 29, 38)
RK_quasirand_sobol_it_4000 = [it[i] for i in indices]
RK_quasirand_sobol_time_4000 = [time[i] for i in indices]
indices = (21, 30, 39)
RK_quasirand_sobol_it_10000 = [it[i] for i in indices]
RK_quasirand_sobol_time_10000 = [time[i] for i in indices]

x_50 = [2000, 4000, 20000, 40000, 80000]
x_100 = [2000, 4000, 20000, 40000, 80000]
x_200 = [2000, 4000, 20000, 40000, 80000]
x_500 = [2000, 4000, 20000, 40000, 80000]
x_750 = [2000, 4000, 20000, 40000, 80000]
x_1000 = [2000, 4000, 20000, 40000, 80000]
x_2000 = [4000, 20000, 40000, 80000]
x_4000 = [20000, 40000, 80000]
x_10000 = [20000, 40000, 80000]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=50$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_50, RK_time_50, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_50, RK_time_50, linewidth=1.5, color='green')
plt.scatter(x_50, RK_quasirand_time_50, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_50, RK_quasirand_time_50, linewidth=1.5, color='orange')
plt.scatter(x_50, RK_quasirand_sobol_time_50, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_50, RK_quasirand_sobol_time_50, linewidth=1.5, color='blue')
plt.scatter(x_50, RK_norep_rand_noshuffle_time_50, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_50, RK_norep_rand_noshuffle_time_50, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=50$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_50, RK_it_50, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_50, RK_it_50, linewidth=1.5, color='green')
plt.scatter(x_50, RK_quasirand_it_50, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_50, RK_quasirand_it_50, linewidth=1.5, color='orange')
plt.scatter(x_50, RK_quasirand_sobol_it_50, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_50, RK_quasirand_sobol_it_50, linewidth=1.5, color='blue')
plt.scatter(x_50, RK_norep_rand_noshuffle_it_50, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_50, RK_norep_rand_noshuffle_it_50, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=100$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_100, RK_time_100, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_100, RK_time_100, linewidth=1.5, color='green')
plt.scatter(x_100, RK_quasirand_time_100, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_100, RK_quasirand_time_100, linewidth=1.5, color='orange')
plt.scatter(x_100, RK_quasirand_sobol_time_100, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_100, RK_quasirand_sobol_time_100, linewidth=1.5, color='blue')
plt.scatter(x_100, RK_norep_rand_noshuffle_time_100, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_100, RK_norep_rand_noshuffle_time_100, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_100"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=100$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_100, RK_it_100, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_100, RK_it_100, linewidth=1.5, color='green')
plt.scatter(x_100, RK_quasirand_it_100, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_100, RK_quasirand_it_100, linewidth=1.5, color='orange')
plt.scatter(x_100, RK_quasirand_sobol_it_100, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_100, RK_quasirand_sobol_it_100, linewidth=1.5, color='blue')
plt.scatter(x_100, RK_norep_rand_noshuffle_it_100, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_100, RK_norep_rand_noshuffle_it_100, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_100"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=200$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_200, RK_time_200, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_200, RK_time_200, linewidth=1.5, color='green')
plt.scatter(x_200, RK_quasirand_time_200, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_200, RK_quasirand_time_200, linewidth=1.5, color='orange')
plt.scatter(x_200, RK_quasirand_sobol_time_200, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_200, RK_quasirand_sobol_time_200, linewidth=1.5, color='blue')
plt.scatter(x_200, RK_norep_rand_noshuffle_time_200, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_200, RK_norep_rand_noshuffle_time_200, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_200"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=200$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_200, RK_it_200, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_200, RK_it_200, linewidth=1.5, color='green')
plt.scatter(x_200, RK_quasirand_it_200, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_200, RK_quasirand_it_200, linewidth=1.5, color='orange')
plt.scatter(x_200, RK_quasirand_sobol_it_200, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_200, RK_quasirand_sobol_it_200, linewidth=1.5, color='blue')
plt.scatter(x_200, RK_norep_rand_noshuffle_it_200, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_200, RK_norep_rand_noshuffle_it_200, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_200"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=500$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_500, RK_time_500, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_500, RK_time_500, linewidth=1.5, color='green')
plt.scatter(x_500, RK_quasirand_time_500, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_500, RK_quasirand_time_500, linewidth=1.5, color='orange')
plt.scatter(x_500, RK_quasirand_sobol_time_500, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_500, RK_quasirand_sobol_time_500, linewidth=1.5, color='blue')
plt.scatter(x_500, RK_norep_rand_noshuffle_time_500, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_500, RK_norep_rand_noshuffle_time_500, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=500$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_500, RK_it_500, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_500, RK_it_500, linewidth=1.5, color='green')
plt.scatter(x_500, RK_quasirand_it_500, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_500, RK_quasirand_it_500, linewidth=1.5, color='orange')
plt.scatter(x_500, RK_quasirand_sobol_it_500, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_500, RK_quasirand_sobol_it_500, linewidth=1.5, color='blue')
plt.scatter(x_500, RK_norep_rand_noshuffle_it_500, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_500, RK_norep_rand_noshuffle_it_500, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=750$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_750, RK_time_750, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_750, RK_time_750, linewidth=1.5, color='green')
plt.scatter(x_750, RK_quasirand_time_750, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_750, RK_quasirand_time_750, linewidth=1.5, color='orange')
plt.scatter(x_750, RK_quasirand_sobol_time_750, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_750, RK_quasirand_sobol_time_750, linewidth=1.5, color='blue')
plt.scatter(x_750, RK_norep_rand_noshuffle_time_750, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_750, RK_norep_rand_noshuffle_time_750, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_750"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=750$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_750, RK_it_750, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_750, RK_it_750, linewidth=1.5, color='green')
plt.scatter(x_750, RK_quasirand_it_750, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_750, RK_quasirand_it_750, linewidth=1.5, color='orange')
plt.scatter(x_750, RK_quasirand_sobol_it_750, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_750, RK_quasirand_sobol_it_750, linewidth=1.5, color='blue')
plt.scatter(x_750, RK_norep_rand_noshuffle_it_750, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_750, RK_norep_rand_noshuffle_it_750, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_750"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=1000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, RK_time_1000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_1000, RK_time_1000, linewidth=1.5, color='green')
plt.scatter(x_1000, RK_quasirand_time_1000, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_1000, RK_quasirand_time_1000, linewidth=1.5, color='orange')
plt.scatter(x_1000, RK_quasirand_sobol_time_1000, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_1000, RK_quasirand_sobol_time_1000, linewidth=1.5, color='blue')
plt.scatter(x_1000, RK_norep_rand_noshuffle_time_1000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_1000, RK_norep_rand_noshuffle_time_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_1000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=1000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_1000, RK_it_1000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_1000, RK_it_1000, linewidth=1.5, color='green')
plt.scatter(x_1000, RK_quasirand_it_1000, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_1000, RK_quasirand_it_1000, linewidth=1.5, color='orange')
plt.scatter(x_1000, RK_quasirand_sobol_it_1000, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_1000, RK_quasirand_sobol_it_1000, linewidth=1.5, color='blue')
plt.scatter(x_1000, RK_norep_rand_noshuffle_it_1000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_1000, RK_norep_rand_noshuffle_it_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_1000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=2000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_2000, RK_time_2000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_2000, RK_time_2000, linewidth=1.5, color='green')
plt.scatter(x_2000, RK_quasirand_time_2000, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_2000, RK_quasirand_time_2000, linewidth=1.5, color='orange')
plt.scatter(x_2000, RK_quasirand_sobol_time_2000, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_2000, RK_quasirand_sobol_time_2000, linewidth=1.5, color='blue')
plt.scatter(x_2000, RK_norep_rand_noshuffle_time_2000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_2000, RK_norep_rand_noshuffle_time_2000, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=2000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_2000, RK_it_2000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_2000, RK_it_2000, linewidth=1.5, color='green')
plt.scatter(x_2000, RK_quasirand_it_2000, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_2000, RK_quasirand_it_2000, linewidth=1.5, color='orange')
plt.scatter(x_2000, RK_quasirand_sobol_it_2000, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_2000, RK_quasirand_sobol_it_2000, linewidth=1.5, color='blue')
plt.scatter(x_2000, RK_norep_rand_noshuffle_it_2000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_2000, RK_norep_rand_noshuffle_it_2000, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=4000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, RK_time_4000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_4000, RK_time_4000, linewidth=1.5, color='green')
plt.scatter(x_4000, RK_quasirand_time_4000, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_4000, RK_quasirand_time_4000, linewidth=1.5, color='orange')
plt.scatter(x_4000, RK_quasirand_sobol_time_4000, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_4000, RK_quasirand_sobol_time_4000, linewidth=1.5, color='blue')
plt.scatter(x_4000, RK_norep_rand_noshuffle_time_4000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_4000, RK_norep_rand_noshuffle_time_4000, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=4000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_4000, RK_it_4000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_4000, RK_it_4000, linewidth=1.5, color='green')
plt.scatter(x_4000, RK_quasirand_it_4000, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_4000, RK_quasirand_it_4000, linewidth=1.5, color='orange')
plt.scatter(x_4000, RK_quasirand_sobol_it_4000, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_4000, RK_quasirand_sobol_it_4000, linewidth=1.5, color='blue')
plt.scatter(x_4000, RK_norep_rand_noshuffle_it_4000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_4000, RK_norep_rand_noshuffle_it_4000, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=10000$'

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_10000, RK_time_10000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_10000, RK_time_10000, linewidth=1.5, color='green')
plt.scatter(x_10000, RK_quasirand_time_10000, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_10000, RK_quasirand_time_10000, linewidth=1.5, color='orange')
plt.scatter(x_10000, RK_quasirand_sobol_time_10000, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_10000, RK_quasirand_sobol_time_10000, linewidth=1.5, color='blue')
plt.scatter(x_10000, RK_norep_rand_noshuffle_time_10000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_10000, RK_norep_rand_noshuffle_time_10000, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$m$')
plt.ylabel(r'Total Time (s)')

filename_fig = "Variations_RK_quasirand_all_N_time_10000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

plot_title = r'Overdetermined systems sampled from $N(\mu,\sigma)$ with $n=10000$'

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
plt.scatter(x_10000, RK_it_10000, linewidth=1.5, color='green', label=r'RK')
plt.plot(x_10000, RK_it_10000, linewidth=1.5, color='green')
plt.scatter(x_10000, RK_quasirand_it_10000, linewidth=1.5, color='orange', label=r'SRK - Halton')
plt.plot(x_10000, RK_quasirand_it_10000, linewidth=1.5, color='orange')
plt.scatter(x_10000, RK_quasirand_sobol_it_10000, linewidth=1.5, color='blue', label=r'SRK - Sobol')
plt.plot(x_10000, RK_quasirand_sobol_it_10000, linewidth=1.5, color='blue')
plt.scatter(x_10000, RK_norep_rand_noshuffle_it_10000, linewidth=1.5, color='red', label=r'SRKWOR')
plt.plot(x_10000, RK_norep_rand_noshuffle_it_10000, linewidth=1.5, color='red')
plt.grid()
plt.legend(loc='upper right')
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.yticks([6E5, 1E6, 2E6, 6E6, 1E7], [r"$6 \times 10^5$", r"$10^6$", r"$2 \times 10^6$", r"$6 \times 10^6$", r"$10^7$"] )
plt.xlabel(r'$m$')
plt.ylabel(r'Iterations')

filename_fig = "Variations_RK_quasirand_all_N_it_10000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()