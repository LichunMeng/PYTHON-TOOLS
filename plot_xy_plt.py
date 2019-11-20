import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
t = np.arange(0.0, 2.0, 0.01);
s1 = 1 + 1*np.sin(2*np.pi*t);
s2 = -1+np.cos(2*np.pi*t);
Line_width=4;
Marker_size=12;
Font_size_ratio=1.86;
SMALL_SIZE = 8*Font_size_ratio;
MEDIUM_SIZE = 10*Font_size_ratio;
BIGGER_SIZE = 12*Font_size_ratio;
COL='black'
#COL='white'
IMSAVE=1;
ratio=5.0;
Figsize=(1.6188*ratio,1*ratio);
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE,)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.rc_context({'axes.edgecolor':COL, 'xtick.color':COL, 'ytick.color':COL, 'figure.facecolor':'none'})
plt.plot(t, s1,'r+',linewidth=Line_width, markersize=Line_width)
plt.plot(t, s2,'g*',linewidth=Line_width, markersize=Line_width)
plt.ylim((-3,3))
plt.xlim((0,2))
plt.xlabel('time (s)',color=COL)
plt.ylabel('voltage (mV)',color=COL)
plt.title(r'$\alpha > \beta$ as it gets, folks',color=COL)
plt.grid(b=True,which='minor',linestyle='-.',color=COL,alpha=0.1)
plt.minorticks_on()
plt.grid(b=True,which='major',linestyle='-',color=COL,alpha=0.3)
legend = plt.legend([r'$\alpha > \beta$', "Train accuracy"], loc='upper right',facecolor=COL,edgecolor=None,framealpha=0)
plt.setp(legend.get_texts(), color=COL)
ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(1))

# Change minor ticks to show every 5. (20/4 = 5)
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_minor_locator(AutoMinorLocator(2))

ax.tick_params(axis="y",which='both',direction="in")
ax.tick_params(axis="x",which='both',direction="in")
if IMSAVE:
	plt.savefig("test.png",transparent=True)
plt.show()
plt.close()
