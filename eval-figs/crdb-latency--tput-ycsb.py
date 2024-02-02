import matplotlib.pylab as plt
import numpy as np
from config import *
import sys 
import os.path

xxx     = [
2140.5,
3537.0,
4221.2,
4722.3,
6514.4,
7214.8,
8156.0,
9651.6,
11955.5,
12790.2,
14620.4,
15102.0,
16001.9,
17801.9,
18501.9
]
x     = [
3756.5,
5166.6,
6465.7,
8386.7,
9295.1,
10568.8,
12470.6,
13775.2,
15934.1,
17829.7,
18997.9,
20067.9
]
slogxx   = [
22.0,
24.1,
26.3,
27.6,
30.3,
31.6,
32.5,
35.7,
37.5,
37.7,
37.7,
37.7,
42.4,
48.4,
104.9
]
slog  = [
17.9,
17.8,
17.8,
17.8,
18.1,
22.1,
24.3,
27.5,
29.4,
34.3,
39.7,
65.0
]

fig, ax = plt.subplots(figsize=(10,8.6))




lines = []
line = ax.plot(xxx, [a for a in slogxx], color=COLOR_S3, linestyle=LINE_S3, marker=MARKER_S3, markersize=MARKER_SIZE) #, marker=MARKER_SLAM)
lines.append(line[0])

line = ax.plot(x, [a for a in slog] , color="purple", linestyle=LINE_S4, marker=MARKER_S4, markersize=MARKER_SIZE) # , marker=MARKER_GOSSIP)
lines.append(line[0])




ax.set_xlabel("Total Tput (tx/s)", size=LABEL_SIZE)
ax.set_ylabel("99th tail latency (ms)", size=LABEL_SIZE)
plt.xlim((0,22000))
# plt.yscale('log')
# ax.set_title("Throughput(limited to 30Mbps)")

plt.xticks(np.arange(0, 22000, 5000), fontsize=TICK_SIZE * 0.8)
plt.yticks(np.arange(10, 110, 10), fontsize=TICK_SIZE * 0.8)
ax.grid(linestyle='--', which= 'major')
#ax.set_xscale('log')
lines2= []
lines2.append(lines[1])

lines2.append(lines[0])
lg = plt.legend(tuple(lines2), tuple([ "CRDB", "CRDB-RLS"]), fontsize=0.8*LEGEND_SIZE, loc='upper center',  columnspacing=0.5, borderpad=.4, edgecolor="black", fancybox=False, ncol=2, bbox_to_anchor=(0.5, 1.2))

if IS_DEBUG:
	plt.show()
plt.tight_layout()

name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')
