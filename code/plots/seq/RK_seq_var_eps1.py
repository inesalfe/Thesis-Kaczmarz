import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/RK_seq_var_eps1.py

filename = "outputs/seq/RK_seq_var_eps1.txt";

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

count_error_4000_50 = count_error[0:4]
count_error_4000_500 = count_error[4:8]
count_error_4000_1000 = count_error[8:12]
count_error_80000_50 = count_error[12:16]
count_error_80000_500 = count_error[16:20]
count_error_80000_1000 = count_error[20:24]
count_error_80000_4000 = count_error[24:28]
count_error_80000_10000 = count_error[28:30]

count_res_4000_50 = count_res[0:4]
count_res_4000_500 = count_res[4:8]
count_res_4000_1000 = count_res[8:12]
count_res_80000_50 = count_res[12:16]
count_res_80000_500 = count_res[16:20]
count_res_80000_1000 = count_res[20:24]
count_res_80000_4000 = count_res[24:28]
count_res_80000_10000 = count_res[28:30]

error_norm_4000_50 = error_norm[0:4]
error_norm_4000_500 = error_norm[4:8]
error_norm_4000_1000 = error_norm[8:12]
error_norm_80000_50 = error_norm[12:16]
error_norm_80000_500 = error_norm[16:20]
error_norm_80000_1000 = error_norm[20:24]
error_norm_80000_4000 = error_norm[24:28]
error_norm_80000_10000 = error_norm[28:30]

time_4000_50 = time[0:4]
time_4000_500 = time[4:8]
time_4000_1000 = time[8:12]
time_80000_50 = time[12:16]
time_80000_500 = time[16:20]
time_80000_1000 = time[20:24]
time_80000_4000 = time[24:28]
time_80000_10000 = time[28:30]

it_4000_50 = it[0:4]
it_4000_500 = it[4:8]
it_4000_1000 = it[8:12]
it_80000_50 = it[12:16]
it_80000_500 = it[16:20]
it_80000_1000 = it[20:24]
it_80000_4000 = it[24:28]
it_80000_10000 = it[28:30]

x = [1E-10, 1E-15, 1E-20, 1E-25]
x2 = [1E-20, 1E-25]

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
plt.scatter(x2, count_error_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x2, count_error_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|x^{(k)}-x^*\|$ is calculated')

filename_fig = "RK_seq_var_eps1_count_error_M_80000"

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
plt.scatter(x2, count_res_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x2, count_res_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'\# Times $\|Ax^{(k)}-b\|$ is calculated')

filename_fig = "RK_seq_var_eps1_count_res_M_80000"

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
plt.scatter(x2, error_norm_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x2, error_norm_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

filename_fig = "RK_seq_var_eps1_error_norm_M_80000"

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
plt.scatter(x2, time_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x2, time_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_eps1_time_M_80000"

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
plt.scatter(x2, it_80000_10000, linewidth=1.5, color='blue', label=r'$80000 \times 10000$')
plt.plot(x2, it_80000_10000, linewidth=1.5, color='blue')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Step Size')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_eps1_it_M_80000"

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

filename_fig = "RK_seq_var_eps1_count_error_M_4000"

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

filename_fig = "RK_seq_var_eps1_count_res_M_4000"

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

filename_fig = "RK_seq_var_eps1_error_norm_M_4000"

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

filename_fig = "RK_seq_var_eps1_time_M_4000"

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

filename_fig = "RK_seq_var_eps1_it_M_4000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_count_error_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_count_res_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_error_norm_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_time_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_it_N_50"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_count_error_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_count_res_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_error_norm_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_time_N_500"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(11, 7))
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

filename_fig = "RK_seq_var_eps1_it_N_500"

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

filename_fig = "RK_seq_var_eps1_count_error_N_1000"

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

filename_fig = "RK_seq_var_eps1_count_res_N_1000"

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

filename_fig = "RK_seq_var_eps1_error_norm_N_1000"

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

filename_fig = "RK_seq_var_eps1_time_N_1000"

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

filename_fig = "RK_seq_var_eps1_it_N_1000"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()