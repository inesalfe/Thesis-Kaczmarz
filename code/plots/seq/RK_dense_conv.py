import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.pyplot import gca
import matplotlib.font_manager

# python3 plots/seq/RK_dense_conv.py

with open("errors/seq/RK_converg_80000_1000.txt") as f:
	lines = f.read().splitlines()

file_size = len(lines)

RK_it = np.zeros(file_size)
RK_error = np.zeros(file_size)
for i in range(file_size):
	RK_it[i] = int(i+1)
	RK_error[i] = float(lines[i])

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

plt.grid()
plt.yscale('log')

plt.xlabel(r'Iterations')
plt.ylabel(r'$\|x^{(k)}-x^*\|$')

plt.plot(RK_it, RK_error, linewidth=1.5, color='blue')

filename_fig = "conv_RK"

plt.show()
fig.savefig("plots/seq/pdf/"+filename_fig+".pdf", bbox_inches='tight')
fig.savefig("plots/seq/png/"+filename_fig+".png", bbox_inches='tight')
