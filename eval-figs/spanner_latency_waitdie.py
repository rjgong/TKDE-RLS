import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 3
namelist = ['Overall','IRTs','CRTs']

base = np.arange(size)
xxx = [
0.554,
0.402,
0.571
]
yyy = [
0.33,
0.06,
0.274
]




xxx_break = [0,0,0]
yyy_break = [0,0,0]


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



#ax.text(-0.1, (1702.92), "1.19x", fontsize=35)
#ax.text(0.9, (2025.30), "1.59x", fontsize=35)
#x.text(1.9, (3487.84), "3.45x", fontsize=35)
ax.set_xlabel("Transaction types", size=LABEL_SIZE)
ax.set_ylabel("Abort Rate", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 1, 0.1), fontsize=TICK_SIZE)
plt.ylim((0, 1))

lg = plt.legend(tuple(bottom_tuple), tuple([ "Spanner", "Spanner-RLS"]), fontsize=0.8*LEGEND_SIZE, loc='upper center',  columnspacing=0.5, borderpad=.4, edgecolor="black", fancybox=False, ncol=2, bbox_to_anchor=(0.5, 1.18))

name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')