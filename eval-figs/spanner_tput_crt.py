import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 6
namelist = [
'0\%',    '5\%','10\%','15\%','20\%','25\%']

base = np.arange(size)
xxx = [
18526,
6184,
4294,
3453,
2730,
2287
]
yyy = [
18226,
18226,
17596,
14866,
11762,
9895
]




xxx_break = [
0,
396,560,676,700,723]
yyy_break = [
0,
700,1283,1540,1587,1703]


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


# ax.text(-0.1, (27595), "2.23x", fontsize=35)
ax.text(0.9, (18426.00), "2.95x", fontsize=35)
ax.text(1.9, (17796.00), "4.10x", fontsize=35)
ax.text(2.9, (15066.00), "4.31x", fontsize=35)
ax.text(3.9, (11962.00), "4.31x", fontsize=35)
ax.text(4.9, (10095.00), "4.33x", fontsize=35)
ax.set_xlabel("CRT Ratio (\%)", size=LABEL_SIZE)
ax.set_ylabel("Throughput (tx/s)", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 20000, 2000), fontsize=TICK_SIZE)
plt.ylim((0, 20000))


name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')