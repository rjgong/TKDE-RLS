import matplotlib.pylab as plt
from matplotlib.pyplot import bar
import numpy as np
import sys 
import os.path
from config import *
from scipy.interpolate import make_interp_spline, BSpline
from matplotlib.ticker import FuncFormatter

fig, ax = plt.subplots(figsize=(20, 7))

labels = ['Spanner', 'Janus' , 'Slog', 'Tapir', 'MDCC']
data = [
    (18526/1000, 6184/1000, 4294/1000, 3453/1000, 2730/1000, 2287/1000),
    (70323/1000, 47957.3/1000, 30379.5/1000, 29233.12/1000, 24289.022/1000, 18999.92/1000),
    (50098.524/1000, 22816.624/1000, 11959.4/1000, 11554.3136/1000, 8313.558/1000, 6974.388/1000),
    (27965.18/1000, 23031.748/1000, 14615.28/1000, 11868.495/1000, 9658.033/1000, 7275.824/1000),
    (25492.391/1000, 15185.214/1000, 9414.113/1000, 6840.0265/1000, 5590.3235/1000, 4069.156/1000),
]
bar_data = [
    (-0.07, -0.07, -0.07, -0.07, -0.07, -0.07),
    (-0.09, -0.09, -0.09, -0.09, -0.09, -0.09),
    (-0.27, -0.29, -0.29, -0.09, -0.09, -0.09),
    (-0.09, -0.26, -0.54, -0.09, -0.09, -0.09), 
    (-0.18, -0.19, -0.23, -0.09, -0.09, -0.09),
]
num_apservers = ['0\% CRT Ratio', '5\% CRT Ratio', '10\% CRT Ratio', '15\% CRT Ratio', '20\% CRT Ratio', '25\% CRT Ratio']

x = np.arange(len(labels))  # the label locations
width = 0.12  # the width of the bars

for i in range(len(data[0])):
    rects = ax.bar(x - width*((len(data[0])-1)/2) + width*i, list(zip(*data))[i], width, label=num_apservers[i])
    # bar_label = list(zip(*bar_data))[i]
    # bar_label = [f'{l*100:.0f}\%' for l in bar_label]
    # ax.bar_label(rects, labels=bar_label, size=LABEL_SIZE*0.7, rotation = 45, weight="bold")

# ax.set_yscale('log')
ax.set_ylabel('Throughput (k txns/s)', size=LABEL_SIZE)
plt.xticks(x, fontsize=0.8*LABEL_SIZE)
plt.yticks(fontsize=TICK_SIZE)
plt.ylim((0, 80))
ax.set_xticklabels(labels, size=1.2*LABEL_SIZE, weight="bold") 
ax.legend(prop={'size': LABEL_SIZE*0.9}, ncol=3 )


fig.tight_layout()


plt.tight_layout()
name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')

