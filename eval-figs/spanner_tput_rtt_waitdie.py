import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 5
namelist = ['20','40','60','80','100']

base = np.arange(size)
xxx = [
124.8+1128.0,
94.8+839.45,
77.15+726.4,
75.0+814.1,
80.85+817.15,
]
yyy = [
470.9+5065.6,
463.0+5166.75,
441.3+5045.85,
402.25+4564.1,
361.65+4341.9
]




xxx_break = [124.8,94.8,77.15,75.0,80.85]
yyy_break = [470.9,463.0,441.3,402.25,361.65]


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



ax.text(-0.1, (5686.50), "4.42x", fontsize=35)
ax.text(0.9, (5779.75), "6.03x", fontsize=35)
ax.text(1.9, (5637.15), "6.83x", fontsize=35)
ax.text(2.9, (5116.35), "5.59x", fontsize=35)
ax.text(3.9, (4853.55), "5.24x", fontsize=35)
ax.set_xlabel("Cross-region RTT (ms)", size=LABEL_SIZE)
ax.set_ylabel("Throughput (tx/s)", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 6600, 600), fontsize=TICK_SIZE)
plt.ylim((0, 6600))


name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')