import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 6
namelist = ['0.5','0.6','0.7','0.8','0.9','1.0']

base = np.arange(size)
xxx = [
1309.4571+11780.6,
446.6214+4039.8143,
164.9214+1548.5,
53.7+553.5786,
17.7071+244.3714,
6.3+148.8071
]
yyy = [
2739.3944+24724.1556,
1766.2056+16272.5778,
708.3222+7246.6944,
220.5667+3132.0722,
63.2167+1742.2278,
11.55+477.5556
]




xxx_break = [1309.4571,446.6214,164.9214,53.7,17.7071,6.3]
yyy_break = [2739.3944,1766.2056,708.3222,220.5667,63.2167,11.55]


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


ax.text(-0.1, (27663.55), "2.10x", fontsize=35)
ax.text(0.9, (18238.78), "4.02x", fontsize=35)
ax.text(1.9, (8155.02), "4.64x", fontsize=35)
ax.text(2.9, (3552.64), "5.52x", fontsize=35)
ax.text(3.9, (2005.44), "6.89x", fontsize=35)
ax.text(4.9, (689.11), "3.15x", fontsize=35)
ax.set_xlabel("Zipf Coefficient", size=LABEL_SIZE)
ax.set_ylabel("Throughput (tx/s)", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 30000, 3000), fontsize=TICK_SIZE)
plt.ylim((0, 30000))

name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')