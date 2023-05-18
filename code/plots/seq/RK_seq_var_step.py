import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/RK_seq_var_step.py

filename = "outputs/seq/RK_seq_var_step.txt";

with open(filename) as f:
    lines = f.read().splitlines()

file_size = len(lines)

count_error = []
count_res = []
error_norm = []
time = []
it = []
for i in range(file_size):
    count_error.append(int(lines[i].split()[6]))
    count_res.append(int(lines[i].split()[7]))
    error_norm.append(float(lines[i].split()[4]))
    time.append(float(lines[i].split()[2]))
    it.append(int(lines[i].split()[3]))

count_error_2000_50 = count_error[0:5]
count_error_2000_500 = count_error[5:10]
count_error_4000_50 = count_error[10:15]
count_error_4000_500 = count_error[15:20]
count_error_4000_1000 = count_error[20:25]
count_error_80000_50 = count_error[25:30]
count_error_80000_500 = count_error[30:35]
count_error_80000_1000 = count_error[35:40]
count_error_80000_4000 = count_error[40:45]
count_error_80000_10000 = count_error[45:50]

count_res_2000_50 = count_res[0:5]
count_res_2000_500 = count_res[5:10]
count_res_4000_50 = count_res[10:15]
count_res_4000_500 = count_res[15:20]
count_res_4000_1000 = count_res[20:25]
count_res_80000_50 = count_res[25:30]
count_res_80000_500 = count_res[30:35]
count_res_80000_1000 = count_res[35:40]
count_res_80000_4000 = count_res[40:45]
count_res_80000_10000 = count_res[45:50]

error_norm_2000_50 = error_norm[0:5]
error_norm_2000_500 = error_norm[5:10]
error_norm_4000_50 = error_norm[10:15]
error_norm_4000_500 = error_norm[15:20]
error_norm_4000_1000 = error_norm[20:25]
error_norm_80000_50 = error_norm[25:30]
error_norm_80000_500 = error_norm[30:35]
error_norm_80000_1000 = error_norm[35:40]
error_norm_80000_4000 = error_norm[40:45]
error_norm_80000_10000 = error_norm[45:50]

time_2000_50 = time[0:5]
time_2000_500 = time[5:10]
time_4000_50 = time[10:15]
time_4000_500 = time[15:20]
time_4000_1000 = time[20:25]
time_80000_50 = time[25:30]
time_80000_500 = time[30:35]
time_80000_1000 = time[35:40]
time_80000_4000 = time[40:45]
time_80000_10000 = time[45:50]

it_2000_50 = it[0:5]
it_2000_500 = it[5:10]
it_4000_50 = it[10:15]
it_4000_500 = it[15:20]
it_4000_1000 = it[20:25]
it_80000_50 = it[25:30]
it_80000_500 = it[30:35]
it_80000_1000 = it[35:40]
it_80000_4000 = it[40:45]
it_80000_10000 = it[45:50]

x = [15, 20, 100, 1000, 10000]

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
plt.scatter(x, count_error_80000_50, linewidth=1.5, color='yellow', label=r'$80000 \times 50$')
plt.plot(x, count_error_80000_50, linewidth=1.5, color='yellow')
plt.scatter(x, count_error_80000_500, linewidth=1.5, color='orange', label=r'$80000 \times 500$')
plt.plot(x, count_error_80000_500, linewidth=1.5, color='orange')
plt.scatter(x, count_error_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, count_error_80000_1000, linewidth=1.5, color='red')
plt.scatter(x, count_error_80000_4000, linewidth=1.5, color='purple', label=r'$80000 \times 4000$')
plt.plot(x, count_error_80000_4000, linewidth=1.5, color='purple')
plt.scatter(x, count_error_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x, count_error_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|x^{(k)}-x^*\|$ is calculated')

filename_fig = "RK_seq_var_step_count_error_M_80000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_res_80000_50, linewidth=1.5, color='yellow', label=r'$80000 \times 50$')
plt.plot(x, count_res_80000_50, linewidth=1.5, color='yellow')
plt.scatter(x, count_res_80000_500, linewidth=1.5, color='orange', label=r'$80000 \times 500$')
plt.plot(x, count_res_80000_500, linewidth=1.5, color='orange')
plt.scatter(x, count_res_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, count_res_80000_1000, linewidth=1.5, color='red')
plt.scatter(x, count_res_80000_4000, linewidth=1.5, color='purple', label=r'$80000 \times 4000$')
plt.plot(x, count_res_80000_4000, linewidth=1.5, color='purple')
plt.scatter(x, count_res_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x, count_res_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated')

filename_fig = "RK_seq_var_step_count_res_M_80000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, error_norm_80000_50, linewidth=1.5, color='yellow', label=r'$80000 \times 50$')
plt.plot(x, error_norm_80000_50, linewidth=1.5, color='yellow')
plt.scatter(x, error_norm_80000_500, linewidth=1.5, color='orange', label=r'$80000 \times 500$')
plt.plot(x, error_norm_80000_500, linewidth=1.5, color='orange')
plt.scatter(x, error_norm_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, error_norm_80000_1000, linewidth=1.5, color='red')
plt.scatter(x, error_norm_80000_4000, linewidth=1.5, color='purple', label=r'$80000 \times 4000$')
plt.plot(x, error_norm_80000_4000, linewidth=1.5, color='purple')
plt.scatter(x, error_norm_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x, error_norm_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

filename_fig = "RK_seq_var_step_error_norm_M_80000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, time_80000_50, linewidth=1.5, color='yellow', label=r'$80000 \times 50$')
plt.plot(x, time_80000_50, linewidth=1.5, color='yellow')
plt.scatter(x, time_80000_500, linewidth=1.5, color='orange', label=r'$80000 \times 500$')
plt.plot(x, time_80000_500, linewidth=1.5, color='orange')
plt.scatter(x, time_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, time_80000_1000, linewidth=1.5, color='red')
plt.scatter(x, time_80000_4000, linewidth=1.5, color='purple', label=r'$80000 \times 4000$')
plt.plot(x, time_80000_4000, linewidth=1.5, color='purple')
plt.scatter(x, time_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x, time_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_step_time_M_80000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, it_80000_50, linewidth=1.5, color='yellow', label=r'$80000 \times 50$')
plt.plot(x, it_80000_50, linewidth=1.5, color='yellow')
plt.scatter(x, it_80000_500, linewidth=1.5, color='orange', label=r'$80000 \times 500$')
plt.plot(x, it_80000_500, linewidth=1.5, color='orange')
plt.scatter(x, it_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, it_80000_1000, linewidth=1.5, color='red')
plt.scatter(x, it_80000_4000, linewidth=1.5, color='purple', label=r'$80000 \times 4000$')
plt.plot(x, it_80000_4000, linewidth=1.5, color='purple')
plt.scatter(x, it_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x, it_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_step_it_M_80000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_error_4000_50, linewidth=1.5, color='yellow', label=r'$4000 \times 50$')
plt.plot(x, count_error_4000_50, linewidth=1.5, color='yellow')
plt.scatter(x, count_error_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, count_error_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, count_error_4000_1000, linewidth=1.5, color='red', label=r'$4000 \times 1000$')
plt.plot(x, count_error_4000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|x^{(k)}-x^*\|$ is calculated')

filename_fig = "RK_seq_var_step_count_error_M_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_res_4000_50, linewidth=1.5, color='yellow', label=r'$4000 \times 50$')
plt.plot(x, count_res_4000_50, linewidth=1.5, color='yellow')
plt.scatter(x, count_res_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, count_res_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, count_res_4000_1000, linewidth=1.5, color='red', label=r'$4000 \times 1000$')
plt.plot(x, count_res_4000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated')

filename_fig = "RK_seq_var_step_count_res_M_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, error_norm_4000_50, linewidth=1.5, color='yellow', label=r'$4000 \times 50$')
plt.plot(x, error_norm_4000_50, linewidth=1.5, color='yellow')
plt.scatter(x, error_norm_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, error_norm_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, error_norm_4000_1000, linewidth=1.5, color='red', label=r'$4000 \times 1000$')
plt.plot(x, error_norm_4000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

filename_fig = "RK_seq_var_step_error_norm_M_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, time_4000_50, linewidth=1.5, color='yellow', label=r'$4000 \times 50$')
plt.plot(x, time_4000_50, linewidth=1.5, color='yellow')
plt.scatter(x, time_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, time_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, time_4000_1000, linewidth=1.5, color='red', label=r'$4000 \times 1000$')
plt.plot(x, time_4000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_step_time_M_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, it_4000_50, linewidth=1.5, color='yellow', label=r'$4000 \times 50$')
plt.plot(x, it_4000_50, linewidth=1.5, color='yellow')
plt.scatter(x, it_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, it_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, it_4000_1000, linewidth=1.5, color='red', label=r'$4000 \times 1000$')
plt.plot(x, it_4000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_step_it_M_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_error_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, count_error_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, count_error_2000_500, linewidth=1.5, color='orange', label=r'$2000 \times 500$')
plt.plot(x, count_error_2000_500, linewidth=1.5, color='orange')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|x^{(k)}-x^*\|$ is calculated')

filename_fig = "RK_seq_var_step_count_error_M_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_res_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, count_res_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, count_res_2000_500, linewidth=1.5, color='orange', label=r'$2000 \times 500$')
plt.plot(x, count_res_2000_500, linewidth=1.5, color='orange')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated')

filename_fig = "RK_seq_var_step_count_res_M_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, error_norm_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, error_norm_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, error_norm_2000_500, linewidth=1.5, color='orange', label=r'$2000 \times 500$')
plt.plot(x, error_norm_2000_500, linewidth=1.5, color='orange')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

filename_fig = "RK_seq_var_step_error_norm_M_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, time_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, time_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, time_2000_500, linewidth=1.5, color='orange', label=r'$2000 \times 500$')
plt.plot(x, time_2000_500, linewidth=1.5, color='orange')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_step_time_M_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, it_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, it_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, it_2000_500, linewidth=1.5, color='orange', label=r'$2000 \times 500$')
plt.plot(x, it_2000_500, linewidth=1.5, color='orange')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_step_it_M_2000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_error_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, count_error_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, count_error_4000_50, linewidth=1.5, color='orange', label=r'$4000 \times 50$')
plt.plot(x, count_error_4000_50, linewidth=1.5, color='orange')
plt.scatter(x, count_error_80000_50, linewidth=1.5, color='red', label=r'$80000 \times 50$')
plt.plot(x, count_error_80000_50, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|x^{(k)}-x^*\|$ is calculated')

filename_fig = "RK_seq_var_step_count_error_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_res_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, count_res_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, count_res_4000_50, linewidth=1.5, color='orange', label=r'$4000 \times 50$')
plt.plot(x, count_res_4000_50, linewidth=1.5, color='orange')
plt.scatter(x, count_res_80000_50, linewidth=1.5, color='red', label=r'$80000 \times 50$')
plt.plot(x, count_res_80000_50, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated')

filename_fig = "RK_seq_var_step_count_res_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, error_norm_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, error_norm_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, error_norm_4000_50, linewidth=1.5, color='orange', label=r'$4000 \times 50$')
plt.plot(x, error_norm_4000_50, linewidth=1.5, color='orange')
plt.scatter(x, error_norm_80000_50, linewidth=1.5, color='red', label=r'$80000 \times 50$')
plt.plot(x, error_norm_80000_50, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

filename_fig = "RK_seq_var_step_error_norm_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, time_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, time_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, time_4000_50, linewidth=1.5, color='orange', label=r'$4000 \times 50$')
plt.plot(x, time_4000_50, linewidth=1.5, color='orange')
plt.scatter(x, time_80000_50, linewidth=1.5, color='red', label=r'$80000 \times 50$')
plt.plot(x, time_80000_50, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_step_time_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, it_2000_50, linewidth=1.5, color='yellow', label=r'$2000 \times 50$')
plt.plot(x, it_2000_50, linewidth=1.5, color='yellow')
plt.scatter(x, it_4000_50, linewidth=1.5, color='orange', label=r'$4000 \times 50$')
plt.plot(x, it_4000_50, linewidth=1.5, color='orange')
plt.scatter(x, it_80000_50, linewidth=1.5, color='red', label=r'$80000 \times 50$')
plt.plot(x, it_80000_50, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_step_it_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_error_2000_500, linewidth=1.5, color='yellow', label=r'$2000 \times 500$')
plt.plot(x, count_error_2000_500, linewidth=1.5, color='yellow')
plt.scatter(x, count_error_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, count_error_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, count_error_80000_500, linewidth=1.5, color='red', label=r'$80000 \times 500$')
plt.plot(x, count_error_80000_500, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|x^{(k)}-x^*\|$ is calculated')

filename_fig = "RK_seq_var_step_count_error_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_res_2000_500, linewidth=1.5, color='yellow', label=r'$2000 \times 500$')
plt.plot(x, count_res_2000_500, linewidth=1.5, color='yellow')
plt.scatter(x, count_res_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, count_res_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, count_res_80000_500, linewidth=1.5, color='red', label=r'$80000 \times 500$')
plt.plot(x, count_res_80000_500, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated')

filename_fig = "RK_seq_var_step_count_res_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, error_norm_2000_500, linewidth=1.5, color='yellow', label=r'$2000 \times 500$')
plt.plot(x, error_norm_2000_500, linewidth=1.5, color='yellow')
plt.scatter(x, error_norm_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, error_norm_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, error_norm_80000_500, linewidth=1.5, color='red', label=r'$80000 \times 500$')
plt.plot(x, error_norm_80000_500, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

filename_fig = "RK_seq_var_step_error_norm_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, time_2000_500, linewidth=1.5, color='yellow', label=r'$2000 \times 500$')
plt.plot(x, time_2000_500, linewidth=1.5, color='yellow')
plt.scatter(x, time_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, time_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, time_80000_500, linewidth=1.5, color='red', label=r'$80000 \times 500$')
plt.plot(x, time_80000_500, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_step_time_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, it_2000_500, linewidth=1.5, color='yellow', label=r'$2000 \times 500$')
plt.plot(x, it_2000_500, linewidth=1.5, color='yellow')
plt.scatter(x, it_4000_500, linewidth=1.5, color='orange', label=r'$4000 \times 500$')
plt.plot(x, it_4000_500, linewidth=1.5, color='orange')
plt.scatter(x, it_80000_500, linewidth=1.5, color='red', label=r'$80000 \times 500$')
plt.plot(x, it_80000_500, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_step_it_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_error_4000_1000, linewidth=1.5, color='orange', label=r'$4000 \times 1000$')
plt.plot(x, count_error_4000_1000, linewidth=1.5, color='orange')
plt.scatter(x, count_error_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, count_error_80000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|x^{(k)}-x^*\|$ is calculated')

filename_fig = "RK_seq_var_step_count_error_N_1000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, count_res_4000_1000, linewidth=1.5, color='orange', label=r'$4000 \times 1000$')
plt.plot(x, count_res_4000_1000, linewidth=1.5, color='orange')
plt.scatter(x, count_res_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, count_res_80000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated')

filename_fig = "RK_seq_var_step_count_res_N_1000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, error_norm_4000_1000, linewidth=1.5, color='orange', label=r'$4000 \times 1000$')
plt.plot(x, error_norm_4000_1000, linewidth=1.5, color='orange')
plt.scatter(x, error_norm_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, error_norm_80000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

filename_fig = "RK_seq_var_step_error_norm_N_1000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, time_4000_1000, linewidth=1.5, color='orange', label=r'$4000 \times 1000$')
plt.plot(x, time_4000_1000, linewidth=1.5, color='orange')
plt.scatter(x, time_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, time_80000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_step_time_N_1000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
plt.scatter(x, it_4000_1000, linewidth=1.5, color='orange', label=r'$4000 \times 1000$')
plt.plot(x, it_4000_1000, linewidth=1.5, color='orange')
plt.scatter(x, it_80000_1000, linewidth=1.5, color='red', label=r'$80000 \times 1000$')
plt.plot(x, it_80000_1000, linewidth=1.5, color='red')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_step_it_N_1000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()