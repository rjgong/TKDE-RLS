import matplotlib.pylab as plt
import numpy as np
from config import *
import sys 
import os.path

xxx     = [
9372.7,
11563.1,
12583.9 ,
14911.3,
15195.4,
16950.6,
17275.5,
18323.2,
18581.0 ,
]
x     = [

10324.9 ,
12467.5 ,
13669.7 ,
14432.2 ,
14920.1 ,
15730.5 ,
17103.6 ,
18126.4 ,
19956.1 ,
19767.1
]
slogxx   = [
121.6,
130.0,
130.0,
138.0,
149.4,
176.2,
176.2,
192.9,
369.1,

]
slog  = [
104.9 ,
105.7 ,
121.6 ,
125.8 ,
142.6 ,
151.0 ,
159.4 ,
184.5 ,
285.2 ,
419.4


]

fig, ax = plt.subplots(figsize=(10,8.6))




lines = []
line = ax.plot(xxx, [a for a in slogxx], color=COLOR_S3, linestyle=LINE_S3, marker=MARKER_S3, markersize=MARKER_SIZE) #, marker=MARKER_SLAM)
lines.append(line[0])

line = ax.plot(x, [a for a in slog] , color="purple", linestyle=LINE_S4, marker=MARKER_S4, markersize=MARKER_SIZE) # , marker=MARKER_GOSSIP)
lines.append(line[0])




ax.set_xlabel("Total Tput (tx/s)", size=LABEL_SIZE)
ax.set_ylabel("99th tail latency (ms)", size=LABEL_SIZE)
plt.xlim((8000,22000))
# plt.yscale('log')
# ax.set_title("Throughput(limited to 30Mbps)")

plt.xticks(np.arange(8000, 22000, 3000), fontsize=TICK_SIZE * 0.8)
plt.yticks(np.arange(100, 500, 50), fontsize=TICK_SIZE * 0.8)
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
