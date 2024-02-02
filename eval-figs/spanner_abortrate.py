import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 4
namelist = ['avg','50\%','90\%','99\%']

base = np.arange(size)
xxx = [
237,13,805,993
]

yyy = [
13,0.43,1.4,403
]

zzz = [
432,352,962,1066
]

nnn = [
368,
111,
981,
1064
    
]



total_width, n = 0.8, 4
width = total_width / 4
base = base - (total_width) / 4
fig, ax = plt.subplots(figsize=(10,7))
hatch_tuple = [] 
bartuple=plt.bar(base, xxx,  facecolor='white', color='k',in_layout=True, edgecolor="red", width=width, lw=2, hatch='//', label='XXX')
hatch_tuple.append(bartuple[0])
bartuple=plt.bar(base + width, yyy,  facecolor='white', color='k',in_layout=True, edgecolor="green", width=width, lw=2, hatch='||', label='YYY')
hatch_tuple.append(bartuple[0])
bartuple=plt.bar(base + 2*width, zzz,  facecolor='white', color='k',in_layout=True, edgecolor="orange", width=width, lw=2, hatch='\\\\', label='YYY')
hatch_tuple.append(bartuple[0])
bartuple=plt.bar(base + 3*width, nnn,  facecolor='white', color='k',in_layout=True, edgecolor="blue", width=width, lw=2, hatch='..', label='YYY')
hatch_tuple.append(bartuple[0])


fig.tight_layout()
edge_tuple = []
bartuple = plt.bar(base, xxx,   color='none',in_layout=True, edgecolor='k', width=width, lw=2)
edge_tuple.append(bartuple[0])
bartuple = plt.bar(base+  width, yyy,   color='none',in_layout=True, edgecolor='k', width=width, lw=2)
edge_tuple.append(bartuple[0])
bartuple = plt.bar(base+ 2*width, zzz,   color='none',in_layout=True, edgecolor='k', width=width, lw=2)
edge_tuple.append(bartuple[0])
bartuple = plt.bar(base+ 3*width, nnn,   color='none',in_layout=True, edgecolor='k', width=width, lw=2)
edge_tuple.append(bartuple[0])

bottom_tuple = []


ax.set_xlabel("Tail Latency", size=LABEL_SIZE)
ax.set_ylabel("Latency (ms)", size=LABEL_SIZE)
plt.xticks(base + width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 1200, 200), fontsize=TICK_SIZE)
plt.ylim((0, 1200))

lg = plt.legend(tuple(hatch_tuple), tuple(["Spanner IRT", "Spanner-RLS IRT", "Spanner CRT", "Spanner-RLS CRT"]), fontsize=0.8*LEGEND_SIZE, loc='upper center',  columnspacing=0.5, borderpad=.4, edgecolor="black", fancybox=False, ncol=2, bbox_to_anchor=(0.5, 1.28))

name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')