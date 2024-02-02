import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 6
namelist = ['2','5','15','25','35','45']

base = np.arange(size)
xxx = [
129.24+1171.98,
116.37+1065.98,
89.82+877.05,
87.82+868.77,
99.56+1006.95,
98.13+1010.28
]
yyy = [
154.3125+1398.6125,
189.5375+1685.7625,
300.25+3037.5875,
383.4125+4097.5,
411.2375+4597.4375,
388.5125+4681.9625
]




xxx_break = [129.24,116.37,89.82,87.82,99.56,98.13]
yyy_break = [154.3125,189.5375,300.25,383.4125,411.2375,388.5125]


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


ax.text(-0.1, (1752.92), "1.19x", fontsize=35)
ax.text(0.9, (2075.30), "1.59x", fontsize=35)
ax.text(1.9, (3537.84), "3.45x", fontsize=35)
ax.text(2.9, (4680.91), "4.68x", fontsize=35)
ax.text(3.9, (5208.68), "4.53x", fontsize=35)
ax.text(4.9, (5270.47), "4.57x", fontsize=35)
ax.set_xlabel("Clients per Shard", size=LABEL_SIZE)
ax.set_ylabel("Throughput (tx/s)", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 6000, 500), fontsize=TICK_SIZE)
plt.ylim((0, 6000))


name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')