import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.pyplot import gca
import matplotlib.font_manager

# python3 plots/seq_sparse/RK_sparse.py

filename = "outputs/seq_sparse/RK_sparse.txt";

with open(filename) as f:
	lines = f.read().splitlines()

file_size = len(lines)

RK_full = []
RK_csr = []
ratio = []
for i in range(8):
	RK_full.append(float(lines[2*i].split()[2]))
	RK_csr.append(float(lines[2*i+1].split()[2]))
	ratio.append(RK_full[i]/RK_csr[i])

den = [1/10, 2/10, 5/10, 8/10, 1, 2, 3, 5]

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'larger',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig = plt.figure(figsize=(10, 7))

plt.grid()
plt.yscale('log')

plt.xlabel(r'Density (\%)')
plt.ylabel(r'$\mathrm{Ratio}_{CSR}$')

plt.plot(den, ratio, color='blue', linestyle='--', linewidth=1)
plt.scatter(den, ratio, color='blue')

filename_fig = "RK_sparse"

plt.show()
fig.savefig("plots/seq_sparse/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq_sparse/png/"+filename_fig+".png", bbox_inches='tight')