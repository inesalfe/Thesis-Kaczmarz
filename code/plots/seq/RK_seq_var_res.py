import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/seq/RK_seq_var_res.py

filename = "outputs/seq/RK_seq_var_res.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

it = []
time = []
error_norm = []
count_error = []
count_res = []
res_norm_new = []
res_norm_old = []
res_avg_new = []
res_avg_old = []
for i in range(file_size):
	time.append(float(lines[i].split()[2]))
	it.append(int(lines[i].split()[3]))
	error_norm.append(float(lines[i].split()[4]))
	count_error.append(int(lines[i].split()[6]))
	count_res.append(int(lines[i].split()[7]))
	res_norm_new.append(float(lines[i].split()[8]))
	res_norm_old.append(float(lines[i].split()[9]))
	res_avg_new.append(float(lines[i].split()[10]))
	res_avg_old.append(float(lines[i].split()[11]))

time_order = time[0::2]
time_shuffle = time[1::2]
it_order = it[0::2]
it_shuffle = it[1::2]
error_norm_order = error_norm[0::2]
error_norm_shuffle = error_norm[1::2]
count_error_order = count_error[0::2]
count_error_shuffle = count_error[1::2]
count_res_order = count_res[0::2]
count_res_shuffle = count_res[1::2]
res_norm_new_order = res_norm_new[0::2]
res_norm_new_shuffle = res_norm_new[1::2]
res_norm_old_order = res_norm_old[0::2]
res_norm_old_shuffle = res_norm_old[1::2]
res_avg_new_order = res_avg_new[0::2]
res_avg_new_shuffle = res_avg_new[1::2]
res_avg_old_order = res_avg_old[0::2]
res_avg_old_shuffle = res_avg_old[1::2]

x_dim_1 = [4000, 2000, 1000, 500, 50]
x_dim_2 = [80000, 10000, 4000, 2000, 1000, 500, 50]
x_dim_3 = [80000, 10000, 4000, 2000, 1000, 500, 50]

time_order_dim_1 = time_order[0:5]
time_shuffle_dim_1 = time_shuffle[0:5]
time_order_dim_2 = time_order[5:12]
time_shuffle_dim_2 = time_shuffle[5:12]
time_order_dim_3 = time_order[12:]
time_shuffle_dim_3 = time_shuffle[12:]

it_order_dim_1 = it_order[0:5]
it_shuffle_dim_1 = it_shuffle[0:5]
it_order_dim_2 = it_order[5:12]
it_shuffle_dim_2 = it_shuffle[5:12]
it_order_dim_3 = it_order[12:]
it_shuffle_dim_3 = it_shuffle[12:]

error_norm_order_dim_1 = error_norm_order[0:5]
error_norm_shuffle_dim_1 = error_norm_shuffle[0:5]
error_norm_order_dim_2 = error_norm_order[5:12]
error_norm_shuffle_dim_2 = error_norm_shuffle[5:12]
error_norm_order_dim_3 = error_norm_order[12:]
error_norm_shuffle_dim_3 = error_norm_shuffle[12:]

count_error_order_dim_1 = count_error_order[0:5]
count_error_shuffle_dim_1 = count_error_shuffle[0:5]
count_error_order_dim_2 = count_error_order[5:12]
count_error_shuffle_dim_2 = count_error_shuffle[5:12]
count_error_order_dim_3 = count_error_order[12:]
count_error_shuffle_dim_3 = count_error_shuffle[12:]

count_res_order_dim_1 = count_res_order[0:5]
count_res_shuffle_dim_1 = count_res_shuffle[0:5]
count_res_order_dim_2 = count_res_order[5:12]
count_res_shuffle_dim_2 = count_res_shuffle[5:12]
count_res_order_dim_3 = count_res_order[12:]
count_res_shuffle_dim_3 = count_res_shuffle[12:]

res_norm_new_order_dim_1 = res_norm_new_order[0:5]
res_norm_new_shuffle_dim_1 = res_norm_new_shuffle[0:5]
res_norm_new_order_dim_2 = res_norm_new_order[5:12]
res_norm_new_shuffle_dim_2 = res_norm_new_shuffle[5:12]
res_norm_new_order_dim_3 = res_norm_new_order[12:]
res_norm_new_shuffle_dim_3 = res_norm_new_shuffle[12:]

res_norm_old_order_dim_1 = res_norm_old_order[0:5]
res_norm_old_shuffle_dim_1 = res_norm_old_shuffle[0:5]
res_norm_old_order_dim_2 = res_norm_old_order[5:12]
res_norm_old_shuffle_dim_2 = res_norm_old_shuffle[5:12]
res_norm_old_order_dim_3 = res_norm_old_order[12:]
res_norm_old_shuffle_dim_3 = res_norm_old_shuffle[12:]

res_avg_new_order_dim_1 = res_avg_new_order[0:5]
res_avg_new_shuffle_dim_1 = res_avg_new_shuffle[0:5]
res_avg_new_order_dim_2 = res_avg_new_order[5:12]
res_avg_new_shuffle_dim_2 = res_avg_new_shuffle[5:12]
res_avg_new_order_dim_3 = res_avg_new_order[12:]
res_avg_new_shuffle_dim_3 = res_avg_new_shuffle[12:]

res_avg_old_order_dim_1 = res_avg_old_order[0:5]
res_avg_old_shuffle_dim_1 = res_avg_old_shuffle[0:5]
res_avg_old_order_dim_2 = res_avg_old_order[5:12]
res_avg_old_shuffle_dim_2 = res_avg_old_shuffle[5:12]
res_avg_old_order_dim_3 = res_avg_old_order[12:]
res_avg_old_shuffle_dim_3 = res_avg_old_shuffle[12:]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
		 'axes.labelsize': 'xx-large',
		 'axes.titlesize': 'xx-large',
		 'xtick.labelsize': 'xx-large',
		 'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_1, time_shuffle_dim_1, linewidth=1.5, color='red')
plt.plot(x_dim_1, time_shuffle_dim_1, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $4000 \times 1000$')
plt.scatter(x_dim_1, time_order_dim_1, linewidth=1.5, color='red')
plt.plot(x_dim_1, time_order_dim_1, linewidth=1.5, color='red', label=r'Order - $4000 \times 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_res_4000_1000_time"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_1, it_shuffle_dim_1, linewidth=1.5, color='red')
plt.plot(x_dim_1, it_shuffle_dim_1, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $4000 \times 1000$')
plt.scatter(x_dim_1, it_order_dim_1, linewidth=1.5, color='red')
plt.plot(x_dim_1, it_order_dim_1, linewidth=1.5, color='red', label=r'Order - $4000 \times 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_res_4000_1000_it"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_1, error_norm_shuffle_dim_1, linewidth=1.5, color='red')
plt.plot(x_dim_1, error_norm_shuffle_dim_1, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $4000 \times 1000$')
plt.scatter(x_dim_1, error_norm_order_dim_1, linewidth=1.5, color='red')
plt.plot(x_dim_1, error_norm_order_dim_1, linewidth=1.5, color='red', label=r'Order - $4000 \times 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'$\|x^k-x^*\|$')

filename_fig = "RK_seq_var_res_4000_1000_error_norm"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_1, res_norm_old_order_dim_1, color='red', label=r'Order')
ax1.plot(x_dim_1, res_norm_old_shuffle_dim_1, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_1, res_norm_old_order_dim_1, color='red')
ax1.scatter(x_dim_1, res_norm_old_shuffle_dim_1, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Total Residual", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_1, res_norm_new_order_dim_1, color='blue', label=r'Order')
ax2.plot(x_dim_1, res_norm_new_shuffle_dim_1, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_1, res_norm_new_order_dim_1, color='blue')
ax2.scatter(x_dim_1, res_norm_new_shuffle_dim_1, color='blue')
ax2.set_ylabel("Partial Residual", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_4000_1000_res_norm"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_1, res_avg_old_order_dim_1, color='red', label=r'Order')
ax1.plot(x_dim_1, res_avg_old_shuffle_dim_1, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_1, res_avg_old_order_dim_1, color='red')
ax1.scatter(x_dim_1, res_avg_old_shuffle_dim_1, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Total Average Residual Entry", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_1, res_avg_new_order_dim_1, color='blue', label=r'Order')
ax2.plot(x_dim_1, res_avg_new_shuffle_dim_1, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_1, res_avg_new_order_dim_1, color='blue')
ax2.scatter(x_dim_1, res_avg_new_shuffle_dim_1, color='blue')
ax2.set_ylabel("Partial Average Residual Entry", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_4000_1000_res_avg"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_1, count_error_order_dim_1, color='red', label=r'Order')
ax1.plot(x_dim_1, count_error_shuffle_dim_1, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_1, count_error_order_dim_1, color='red')
ax1.scatter(x_dim_1, count_error_shuffle_dim_1, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Number of times the difference is computed", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_1, count_res_order_dim_1, color='blue', label=r'Order')
ax2.plot(x_dim_1, count_res_shuffle_dim_1, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_1, count_res_order_dim_1, color='blue')
ax2.scatter(x_dim_1, count_res_shuffle_dim_1, color='blue')
ax2.set_ylabel("Number of times the residual is computed", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_4000_1000_count"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_2, time_shuffle_dim_2, linewidth=1.5, color='red')
plt.plot(x_dim_2, time_shuffle_dim_2, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $80000 \times 1000$')
plt.scatter(x_dim_2, time_order_dim_2, linewidth=1.5, color='red')
plt.plot(x_dim_2, time_order_dim_2, linewidth=1.5, color='red', label=r'Order - $80000 \times 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_res_80000_1000_time"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_2, it_shuffle_dim_2, linewidth=1.5, color='red')
plt.plot(x_dim_2, it_shuffle_dim_2, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $80000 \times 1000$')
plt.scatter(x_dim_2, it_order_dim_2, linewidth=1.5, color='red')
plt.plot(x_dim_2, it_order_dim_2, linewidth=1.5, color='red', label=r'Order - $80000 \times 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_res_80000_1000_it"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_2, error_norm_shuffle_dim_2, linewidth=1.5, color='red')
plt.plot(x_dim_2, error_norm_shuffle_dim_2, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $80000 \times 1000$')
plt.scatter(x_dim_2, error_norm_order_dim_2, linewidth=1.5, color='red')
plt.plot(x_dim_2, error_norm_order_dim_2, linewidth=1.5, color='red', label=r'Order - $80000 \times 1000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'$\|x^k-x^*\|$')

filename_fig = "RK_seq_var_res_80000_1000_error_norm"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_2, res_norm_old_order_dim_2, color='red', label=r'Order')
ax1.plot(x_dim_2, res_norm_old_shuffle_dim_2, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_2, res_norm_old_order_dim_2, color='red')
ax1.scatter(x_dim_2, res_norm_old_shuffle_dim_2, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Total Residual", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_2, res_norm_new_order_dim_2, color='blue', label=r'Order')
ax2.plot(x_dim_2, res_norm_new_shuffle_dim_2, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_2, res_norm_new_order_dim_2, color='blue')
ax2.scatter(x_dim_2, res_norm_new_shuffle_dim_2, color='blue')
ax2.set_ylabel("Partial Residual", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_80000_1000_res_norm"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_2, res_avg_old_order_dim_2, color='red', label=r'Order')
ax1.plot(x_dim_2, res_avg_old_shuffle_dim_2, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_2, res_avg_old_order_dim_2, color='red')
ax1.scatter(x_dim_2, res_avg_old_shuffle_dim_2, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Total Average Residual Entry", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_2, res_avg_new_order_dim_2, color='blue', label=r'Order')
ax2.plot(x_dim_2, res_avg_new_shuffle_dim_2, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_2, res_avg_new_order_dim_2, color='blue')
ax2.scatter(x_dim_2, res_avg_new_shuffle_dim_2, color='blue')
ax2.set_ylabel("Partial Average Residual Entry", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_80000_1000_res_avg"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_2, count_error_order_dim_2, color='red', label=r'Order')
ax1.plot(x_dim_2, count_error_shuffle_dim_2, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_2, count_error_order_dim_2, color='red')
ax1.scatter(x_dim_2, count_error_shuffle_dim_2, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Number of times the difference is computed", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_2, count_res_order_dim_2, color='blue', label=r'Order')
ax2.plot(x_dim_2, count_res_shuffle_dim_2, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_2, count_res_order_dim_2, color='blue')
ax2.scatter(x_dim_2, count_res_shuffle_dim_2, color='blue')
ax2.set_ylabel("Number of times the residual is computed", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_80000_1000_count"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_3, time_shuffle_dim_3, linewidth=1.5, color='red')
plt.plot(x_dim_3, time_shuffle_dim_3, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $80000 \times 4000$')
plt.scatter(x_dim_3, time_order_dim_3, linewidth=1.5, color='red')
plt.plot(x_dim_3, time_order_dim_3, linewidth=1.5, color='red', label=r'Order - $80000 \times 4000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'Total Time (s)')

filename_fig = "RK_seq_var_res_80000_4000_time"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_3, it_shuffle_dim_3, linewidth=1.5, color='red')
plt.plot(x_dim_3, it_shuffle_dim_3, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $80000 \times 4000$')
plt.scatter(x_dim_3, it_order_dim_3, linewidth=1.5, color='red')
plt.plot(x_dim_3, it_order_dim_3, linewidth=1.5, color='red', label=r'Order - $80000 \times 4000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'Iterations')

filename_fig = "RK_seq_var_res_80000_4000_it"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.scatter(x_dim_3, error_norm_shuffle_dim_3, linewidth=1.5, color='red')
plt.plot(x_dim_3, error_norm_shuffle_dim_3, linewidth=1.5, color='red', linestyle='--', label=r'Shuffle - $80000 \times 4000$')
plt.scatter(x_dim_3, error_norm_order_dim_3, linewidth=1.5, color='red')
plt.plot(x_dim_3, error_norm_order_dim_3, linewidth=1.5, color='red', label=r'Order - $80000 \times 4000$')
plt.grid()
plt.legend()
# plt.title(plot_title)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'Number of rows')
plt.ylabel(r'$\|x^k-x^*\|$')

filename_fig = "RK_seq_var_res_80000_4000_error_norm"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_3, res_norm_old_order_dim_3, color='red', label=r'Order')
ax1.plot(x_dim_3, res_norm_old_shuffle_dim_3, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_3, res_norm_old_order_dim_3, color='red')
ax1.scatter(x_dim_3, res_norm_old_shuffle_dim_3, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Total Residual", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_3, res_norm_new_order_dim_3, color='blue', label=r'Order')
ax2.plot(x_dim_3, res_norm_new_shuffle_dim_3, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_3, res_norm_new_order_dim_3, color='blue')
ax2.scatter(x_dim_3, res_norm_new_shuffle_dim_3, color='blue')
ax2.set_ylabel("Partial Residual", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_80000_4000_res_norm"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_3, res_avg_old_order_dim_3, color='red', label=r'Order')
ax1.plot(x_dim_3, res_avg_old_shuffle_dim_3, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_3, res_avg_old_order_dim_3, color='red')
ax1.scatter(x_dim_3, res_avg_old_shuffle_dim_3, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Total Average Residual Entry", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_3, res_avg_new_order_dim_3, color='blue', label=r'Order')
ax2.plot(x_dim_3, res_avg_new_shuffle_dim_3, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_3, res_avg_new_order_dim_3, color='blue')
ax2.scatter(x_dim_3, res_avg_new_shuffle_dim_3, color='blue')
ax2.set_ylabel("Partial Average Residual Entry", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_80000_4000_res_avg"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots(figsize=(12,7))
ax1.plot(x_dim_3, count_error_order_dim_3, color='red', label=r'Order')
ax1.plot(x_dim_3, count_error_shuffle_dim_3, color='red', linestyle='--', label=r'Shuffle')
ax1.scatter(x_dim_3, count_error_order_dim_3, color='red')
ax1.scatter(x_dim_3, count_error_shuffle_dim_3, color='red')
ax1.set_xlabel(r'Number of rows')
ax1.set_ylabel("Number of times the difference is computed", color="red")
plt.grid()
plt.legend(loc='best')
ax2 = ax1.twinx()
ax2.plot(x_dim_3, count_res_order_dim_3, color='blue', label=r'Order')
ax2.plot(x_dim_3, count_res_shuffle_dim_3, color='blue', linestyle='--', label=r'Shuffle')
ax2.scatter(x_dim_3, count_res_order_dim_3, color='blue')
ax2.scatter(x_dim_3, count_res_shuffle_dim_3, color='blue')
ax2.set_ylabel("Number of times the residual is computed", color="blue")
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xscale('log')
ax2.set_xscale('log')
plt.legend(loc='best')

filename_fig = "RK_seq_var_res_80000_4000_count"

# plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
plt.close()