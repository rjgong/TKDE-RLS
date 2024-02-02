import matplotlib.style
import matplotlib as mpl


matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True

XXX_NAME = "DAST"

# marker
MARKER_S1= "s"
MARKER_S2="."
MARKER_S3="v"
MARKER_S4="*"
MARKER_S5="d"
MARKER_S6="+"


# color
COLOR_S1="tab:blue"
COLOR_S2="tab:orange"
COLOR_S3="tab:green"
COLOR_S4="tab:red"
COLOR_S5="tab:purple"
COLOR_S6="tab:olive"

LINE_S1=":"
LINE_S2="--"
LINE_S3="-."
LINE_S4="-"
LINE_S5="--"
LINE_S6="--"

LEGEND_SIZE=40
LABEL_SIZE=42
TICK_SIZE=50
MARKER_SIZE=10

mpl.rcParams['lines.linewidth'] = 5

IS_DEBUG=False