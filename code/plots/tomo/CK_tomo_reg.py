import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/tomo/CK_tomo_reg.py ct_gaussian 19558 16384 1 30000000
# 12760000 0.493655
# python3 plots/tomo/CK_tomo_reg.py ct_gaussian 19558 16384 2 30000000
# 5140000 0.95464
# python3 plots/tomo/CK_tomo_reg.py ct_gaussian 19558 16384 3 30000000
# 2230000 1.63661
# python3 plots/tomo/CK_tomo_reg.py ct_gaussian 19558 16384 4 30000000
# 720000 2.92048

# python3 plots/tomo/CK_tomo_reg.py ct_poisson 19558 16384 1 30000000
# 900000 2.49948
# python3 plots/tomo/CK_tomo_reg.py ct_poisson 19558 16384 2 30000000
# 1870000 1.72374
# python3 plots/tomo/CK_tomo_reg.py ct_poisson 19558 16384 3 30000000
# 2230000 1.41428
# python3 plots/tomo/CK_tomo_reg.py ct_poisson 19558 16384 4 30000000
# 2050000 1.4959

# python3 plots/tomo/CK_tomo_reg.py ct_gaussian 19558 16384 1 10000000
# 9850000 0.49933
# python3 plots/tomo/CK_tomo_reg.py ct_gaussian 19558 16384 2 10000000
# 5140000 0.95464
# python3 plots/tomo/CK_tomo_reg.py ct_gaussian 19558 16384 3 10000000
# 2230000 1.63661
# python3 plots/tomo/CK_tomo_reg.py ct_gaussian 19558 16384 4 10000000
# 720000 2.92048

# python3 plots/tomo/CK_tomo_reg.py ct_poisson 19558 16384 1 10000000
# 900000 2.49948
# python3 plots/tomo/CK_tomo_reg.py ct_poisson 19558 16384 2 10000000
# 1870000 1.72374
# python3 plots/tomo/CK_tomo_reg.py ct_poisson 19558 16384 3 10000000
# 2230000 1.41428
# python3 plots/tomo/CK_tomo_reg.py ct_poisson 19558 16384 4 10000000
# 2050000 1.4959

if (len(sys.argv) != 6):
	exit()

data_set = sys.argv[1]
M = int(sys.argv[2])
N = int(sys.argv[3])
seed = int(sys.argv[4])
max_it = int(sys.argv[5])

if (data_set == "ct_gaussian"):
	error_folder = "errors/tomo_gauss_reg/"
	output_foler = "_gauss/"
elif (data_set == "ct_poisson"):
	error_folder = "errors/tomo_poisson_reg/"
	output_foler = "_poisson/"
else:
	exit()

filename = error_folder + "CK_error_" + str(M) + "_" + str(N) + "_" + str(seed) + "_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_error = []
error = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_error.append(int(lines[i].split()[0]))
		error.append(float(lines[i].split()[1]))

filename = error_folder + "CK_res_" + str(M) + "_" + str(N) + "_" + str(seed) + "_" + str(max_it) + ".txt"

with open(filename) as f:
	lines = f.read().splitlines()
file_size = len(lines)
it_res = []
res = []
for i in range(file_size):
	curr_it = int(lines[i].split()[0])
	if (curr_it < max_it):
		it_res.append(int(lines[i].split()[0]))
		res.append(float(lines[i].split()[1]))

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
         'axes.labelsize': 'xx-large',
         'axes.titlesize': 'xx-large',
         'xtick.labelsize': 'xx-large',
         'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax1 = plt.subplots(figsize=(10,7))

ax1.plot(it_res, res, color='blue', label=r'$\|Ax^{(k)}-b\|$')
ax1.set_ylabel("Residual", color="blue")

ax1.set_xlabel(r'Iterations')
plt.grid()
ax2 = ax1.twinx()
ax2.set_ylabel("Error", color="red")
ax1.set_yscale('log')
ax2.set_yscale('log')

ax2.plot(it_error, error, color='red', label=r'$\|x^{(k)}-\overline{x}\|$')

ax2.scatter(it_error[error.index(min(error))], min(error), color='red', label=r'Minimum - $\|x^{(k)}-\overline{x}\|$')
print(it_error[error.index(min(error))], end=' ')
print(min(error))

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='best')

filename_fig = "CK_tomo_reg_" + str(M) + "_" + str(N) + "_" + str(seed) + "_" + str(max_it)

# plt.show()
fig.savefig("plots/tomo/pdf"+output_foler+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/tomo/png"+output_foler+filename_fig+".png", bbox_inches='tight')
plt.close()