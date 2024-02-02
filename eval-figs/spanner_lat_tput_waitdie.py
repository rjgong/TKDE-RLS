import matplotlib.pylab as plt
import numpy as np
from config import *
import sys 
import os.path

xxx     = [200,1398.6125,1500.225,1685.7625,2055.3625,2301.275,2724.0875,3037.5875,3359.3,3600.9,4097.5,4501.525,4597.4375,4638.4125,4654.4,4681.9625]
x     = [200,617.54,1117.54,1127.54,1127.98,1165.98]
slogxx   = [0.58,0.6123,0.607,0.6098,0.6113,0.6125,0.6208,0.6265,0.6402,0.6495,0.6992,0.8005,0.997,1.51,1.7325,2.1585]
slog  = [0.6,0.6,0.612,1,1.6328,3.495]

fig, ax = plt.subplots(figsize=(10,8.6))




lines = []
line = ax.plot(xxx, [a for a in slogxx], color=COLOR_S3, linestyle=LINE_S3, marker=MARKER_S3, markersize=MARKER_SIZE) #, marker=MARKER_SLAM)
lines.append(line[0])

line = ax.plot(x, [a for a in slog] , color="purple", linestyle=LINE_S4, marker=MARKER_S4, markersize=MARKER_SIZE) # , marker=MARKER_GOSSIP)
lines.append(line[0])




ax.set_xlabel("Total Tput (tx/s)", size=LABEL_SIZE)
ax.set_ylabel("90th tail latency (ms)", size=LABEL_SIZE)
plt.xlim((0,5000))
# plt.yscale('log')
# ax.set_title("Throughput(limited to 30Mbps)")

plt.xticks(fontsize=TICK_SIZE * 0.8)
plt.yticks(np.arange(0, 6, 0.5), fontsize=TICK_SIZE * 0.8)
ax.grid(linestyle='--', which= 'major')
#ax.set_xscale('log')
lines2= []
lines2.append(lines[1])

lines2.append(lines[0])
lg = plt.legend(tuple(lines2), tuple([ "Spanner", "Spanner-RLS"]), fontsize=0.8*LEGEND_SIZE, loc='upper center',  columnspacing=0.5, borderpad=.4, edgecolor="black", fancybox=False, ncol=2, bbox_to_anchor=(0.5, 1.2))

if IS_DEBUG:
	plt.show()
plt.tight_layout()

name = os.path.basename(sys.argv[0])[:-2] + 'pdf'
plt.savefig(name, bbox_inches='tight')
