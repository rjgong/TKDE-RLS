import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 6
namelist = ['0.5','0.6','0.7','0.8','0.9','1.0']

base = np.arange(size)
xxx = [
12147,
9556,
4970,
1785,
525,
105
]
yyy = [
27095,
26114,
19568,
13162,
10537,
9346
]




xxx_break = [1260,1050,630,280,70,12]
yyy_break = [2695,2555,1575,630,134,27]


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


ax.text(-0.1, (27245.00), "2.23x", fontsize=35)
ax.text(0.9, (26264.00), "2.73x", fontsize=35)
ax.text(1.9, (19718.00), "3.94x", fontsize=35)
ax.text(2.9, (13312.00), "7.37x", fontsize=35)
ax.text(3.9, (10687.00), "20.07x", fontsize=35)
ax.text(4.9, (9496.00), "89.01x", fontsize=35)
ax.set_xlabel("Zipf Coefficient", size=LABEL_SIZE)
ax.set_ylabel("Throughput (tx/s)", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 30000, 3000), fontsize=TICK_SIZE)
plt.ylim((0, 30000))

name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')