import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 5
namelist = ['20','40','60','80','100']

base = np.arange(size)
xxx = [
6405,
4208,
3600,
3044,
2117
]
yyy = [
19906,
16835,
13394,
10694,
7252
]




xxx_break = [794,529,450,397,291]
yyy_break = [1429,1138,873,688,476]


total_width, n = 0.8, 2
width = total_width / n
base = base - (total_width - width) / 2
fig, ax = plt.subplots(figsize=(10,7))
hatch_tuple = [] 
bartuple=plt.bar(base, xxx,  facecolor='white', color='k',in_layout=True, edgecolor=COLOR_S1, width=width, lw=2, hatch='/', label='XXX')
hatch_tuple.append(bartuple[0])
bartuple=plt.bar(base + width, yyy,  facecolor='white', color='k',in_layout=True, edgecolor="purple", width=width, lw=2, hatch='|', label='YYY')
hatch_tuple.append(bartuple[0])

fig.tight_layout()
edge_tuple = []
bartuple = plt.bar(base, xxx,   color='none',in_layout=True, edgecolor='k', width=width, lw=2)
edge_tuple.append(bartuple[0])
bartuple = plt.bar(base+  width, yyy,   color='none',in_layout=True, edgecolor='k', width=width, lw=2)
edge_tuple.append(bartuple[0])



bottom_tuple = []

tmp = plt.bar(base, xxx_break, width=width, facecolor='white', color='k', in_layout=True, edgecolor=COLOR_S1, lw=2, hatch='.', label='XXX')
bottom_tuple.append(tmp)
plt.bar(base, xxx_break,   color='none', in_layout=True, edgecolor='k', width=width, lw=2)

tmp = plt.bar(base+width, yyy_break, width=width, facecolor='white', color='k', in_layout=True, edgecolor="purple", lw=2, hatch='.', label='YYY')
bottom_tuple.append(tmp)
plt.bar(base+width, yyy_break,   color='none', in_layout=True, edgecolor='k', width=width, lw=2)




ax.text(-0.1, (20056.00), "3.11x", fontsize=35)
ax.text(0.9, (16985.00), "4.00x", fontsize=35)
ax.text(1.9, (13544.00), "3.72x", fontsize=35)
ax.text(2.9, (10844.00), "3.51x", fontsize=35)
ax.text(3.9, (7402.00), "3.43x", fontsize=35)
ax.set_xlabel("Cross-region RTT (ms)", size=LABEL_SIZE)
ax.set_ylabel("Throughput (tx/s)", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 22500, 2500), fontsize=TICK_SIZE)
plt.ylim((0, 22500))


name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')