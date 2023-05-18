import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/RK_seq_paramsSC_M.py

filename = "outputs/seq/RK_seq_paramsSC.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

count_error = []
count_res = []
error_norm = []
error_avg = []
error_first_avg = []
res_norm = []
res_avg = []
for i in range(file_size):
    count_error.append(int(lines[i].split()[5]))
    count_res.append(int(lines[i].split()[6]))
    error_norm.append(float(lines[i].split()[7]))
    error_avg.append(float(lines[i].split()[9]))
    error_first_avg.append(float(lines[i].split()[8]))
    res_norm.append(float(lines[i].split()[10]))
    res_avg.append(float(lines[i].split()[11]))

count_error_2000 = count_error[0:5]
count_error_4000 = count_error[5:11]
count_error_20000 = count_error[11:19]
count_error_40000 = count_error[19:28]
count_error_80000 = count_error[28:37]

count_res_2000 = count_res[0:5]
count_res_4000 = count_res[5:11]
count_res_20000 = count_res[11:19]
count_res_40000 = count_res[19:28]
count_res_80000 = count_res[28:37]

error_norm_2000 = error_norm[0:5]
error_norm_4000 = error_norm[5:11]
error_norm_20000 = error_norm[11:19]
error_norm_40000 = error_norm[19:28]
error_norm_80000 = error_norm[28:37]

error_avg_2000 = error_avg[0:5]
error_avg_4000 = error_avg[5:11]
error_avg_20000 = error_avg[11:19]
error_avg_40000 = error_avg[19:28]
error_avg_80000 = error_avg[28:37]

error_first_avg_2000 = error_first_avg[0:5]
error_first_avg_4000 = error_first_avg[5:11]
error_first_avg_20000 = error_first_avg[11:19]
error_first_avg_40000 = error_first_avg[19:28]
error_first_avg_80000 = error_first_avg[28:37]

res_norm_2000 = res_norm[0:5]
res_norm_4000 = res_norm[5:11]
res_norm_20000 = res_norm[11:19]
res_norm_40000 = res_norm[19:28]
res_norm_80000 = res_norm[28:37]

res_avg_2000 = res_avg[0:5]
res_avg_4000 = res_avg[5:11]
res_avg_20000 = res_avg[11:19]
res_avg_40000 = res_avg[19:28]
res_avg_80000 = res_avg[28:37]

x_2000 = [50, 100, 200, 500, 750]
x_4000 = [50, 100, 200, 500, 750, 1000]
x_20000 = [50, 100, 200, 500, 750, 1000, 2000, 4000]
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

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], count_error_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], count_error_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], count_error_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], count_error_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], count_error_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], count_error_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], count_error_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], count_error_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], count_error_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], count_error_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'\# Times $\|x^{(k)}-x^*\|$ is calculated')

filename_fig = "RK_seq_paramsSC_M_count_error"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], count_res_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], count_res_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], count_res_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], count_res_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], count_res_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], count_res_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], count_res_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], count_res_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], count_res_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], count_res_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated')

filename_fig = "RK_seq_paramsSC_M_count_res"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], error_norm_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], error_norm_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], error_norm_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], error_norm_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], error_norm_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], error_norm_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], error_norm_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], error_norm_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], error_norm_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], error_norm_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

filename_fig = "RK_seq_paramsSC_M_error_norm"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], error_avg_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], error_avg_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], error_avg_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], error_avg_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], error_avg_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], error_avg_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], error_avg_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], error_avg_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], error_avg_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], error_avg_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Average of $\left|x^{(k)}-x^*\right|$')

filename_fig = "RK_seq_paramsSC_M_error_avg"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], error_first_avg_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], error_first_avg_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], error_first_avg_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], error_first_avg_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], error_first_avg_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], error_first_avg_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], error_first_avg_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], error_first_avg_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], error_first_avg_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], error_first_avg_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'First value of average of $\left|x^{(k)}-x^{(k-1)}\right|$')

filename_fig = "RK_seq_paramsSC_M_error_first_avg"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], res_norm_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], res_norm_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], res_norm_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], res_norm_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], res_norm_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], res_norm_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], res_norm_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], res_norm_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], res_norm_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], res_norm_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'$\|Ax^{(k)}-b\|$')

filename_fig = "RK_seq_paramsSC_M_res_norm"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')

fig = plt.figure(figsize=(11, 7))
plt.scatter(x_2000[3::], res_avg_2000[3::], linewidth=1.5, color='yellow', label=r'$m = 2000$')
plt.plot(x_2000[3::], res_avg_2000[3::], linewidth=1.5, color='yellow')
plt.scatter(x_4000[3::], res_avg_4000[3::], linewidth=1.5, color='orange', label=r'$m = 4000$')
plt.plot(x_4000[3::], res_avg_4000[3::], linewidth=1.5, color='orange')
plt.scatter(x_20000[3::], res_avg_20000[3::], linewidth=1.5, color='red', label=r'$m = 20000$')
plt.plot(x_20000[3::], res_avg_20000[3::], linewidth=1.5, color='red')
plt.scatter(x_40000[3::], res_avg_40000[3::], linewidth=1.5, color='purple', label=r'$m = 40000$')
plt.plot(x_40000[3::], res_avg_40000[3::], linewidth=1.5, color='purple')
plt.scatter(x_80000[3::], res_avg_80000[3::], linewidth=1.5, color='blue', label=r'$m = 80000$')
plt.plot(x_80000[3::], res_avg_80000[3::], linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'Average of $\left|Ax^{(k)}-b\right|$')

filename_fig = "RK_seq_paramsSC_M_res_avg"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')