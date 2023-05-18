import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import matplotlib.font_manager
import sys

# python3 plots/norms/hist_norms_dense_norm.py 80000 10000

if (len(sys.argv) != 3):
	exit()

M = int(sys.argv[1])
N = int(sys.argv[2])

filename_norms = "outputs/dense_norm_row_norms_" + str(M) + "_" + str(N) + ".txt"

with open(filename_norms) as f:
	lines = f.read().splitlines()

file_size = len(lines)

norms = np.zeros(file_size)
for i in range(file_size):
	norms[i] = float(lines[i])

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plot_title = str(M) + r" $\times$ " + str(N)

fig = plt.figure(figsize=(8, 6))
n_bins = 9
plt.hist(norms, bins=n_bins, color='grey', alpha=0.3)
plt.hist(norms, bins=n_bins, color='grey', edgecolor='black', fc='None', lw=3)
plt.grid()
plt.title(plot_title)
plt.ylabel(r'Count')
# plt.yscale('log')
plt.xlabel(r'Norm')

filename_fig = "plots/norms/Dense_norm_row_norms_" + str(M) + "_" + str(N)

plt.show()
fig.savefig(filename_fig+".pdf", bbox_inches='tight')
fig.savefig(filename_fig+".png", bbox_inches='tight')