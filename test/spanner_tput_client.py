import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 6
namelist = ['16','32','64','128','256','512']

base = np.arange(size)
xxx = [
1452,
2600,
3911,
3653,
3536,
3793
]
yyy = [
1686,
3395,
7962,
11569,
14614,
14882
]




xxx_break = [163,304,491,468,468,538]
yyy_break = [16,31,60,81,96,98]


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




ax.text(-0.1, (1886.00), "1.16x", fontsize=35)
ax.text(0.9, (3595.00), "1.31x", fontsize=35)
ax.text(1.9, (8162.00), "2.04x", fontsize=35)
ax.text(2.9, (11769.00), "3.17x", fontsize=35)
ax.text(3.9, (14814.00), "4.13x", fontsize=35)
ax.text(4.9, (15082.00), "3.92x", fontsize=35)
ax.set_xlabel("Clients per Shard", size=LABEL_SIZE)
ax.set_ylabel("Throughput (tx/s)", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 20000, 2000), fontsize=TICK_SIZE)
plt.ylim((0, 20000))


name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')