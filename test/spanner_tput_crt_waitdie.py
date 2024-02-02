import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys 
from config import *
size = 5
namelist = [
# '0\%',
'5\%','10\%','15\%','20\%','25\%']

base = np.arange(size)
xxx = [
68.43+1351.32,
94.63+916.14,
117.74+738.1,
133.31+595.33,
140.8+471.41
]
yyy = [
313.525+7907.9,
377.2+4512.0,
455.025+3344.775,
458.2+2392.75,
464.95+1835.125
]




xxx_break = [
68.43,94.63,117.74,133.31,140.8]
yyy_break = [
313.525,377.2,455.025,458.2,464.95]


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


ax.text(-0.1, (8421.42), "5.79x", fontsize=35)
ax.text(0.9, (5089.20), "4.84x", fontsize=35)
ax.text(1.9, (3999.80), "4.44x", fontsize=35)
ax.text(2.9, (3050.95), "3.91x", fontsize=35)
ax.text(3.9, (2500.07), "3.76x", fontsize=35)
ax.set_xlabel("CRT Ratio (\%)", size=LABEL_SIZE)
ax.set_ylabel("Throughput (tx/s)", size=LABEL_SIZE)
plt.xticks(base + 0.5 * width, labels=namelist, fontsize=TICK_SIZE)
plt.yticks(np.arange(0, 10000, 1000), fontsize=TICK_SIZE)
plt.ylim((0, 10000))


name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')