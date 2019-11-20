import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
#############################
####### Data X y1 y2
t = np.arange(0.0, 2.0, 0.01);
s1 = 1 + 1*np.sin(2*np.pi*t);
s2 = -1+np.cos(2*np.pi*t);
#############################
####### On an OFF control
COL='black'
COL='white'
IMSAVE=1;
#############################
####### SIZE

Line_width=4;
Marker_size=12;
Font_size_ratio=1.86;
Figure_ratio=5.0;
SMALL_SIZE = 8*Font_size_ratio;
MEDIUM_SIZE = 10*Font_size_ratio;
BIGGER_SIZE = 12*Font_size_ratio;
Figsize=(1.6188*Figure_ratio,1*Figure_ratio);

#############################
####### Initialize plot 
fig, ax1 = plt.subplots()

#############################
####### plot 
ax1.plot(t, s1, 'g-',linewidth=Line_width, markersize=Line_width)
ax1.plot(t, s2, 'r-',linewidth=Line_width, markersize=Line_width)

#############################
####### limit 
ax1.set_ylim((-3,3))
ax1.set_xlim((0,2))

#############################
####### label 
ax1.set_xlabel('X data', color=COL,fontsize=MEDIUM_SIZE)
ax1.set_ylabel('Y1 data', color=COL,fontsize=MEDIUM_SIZE)

#############################
####### tick 
ax1.tick_params(axis="x",which='both',direction="in",labelsize=SMALL_SIZE,colors=COL)
ax1.tick_params(axis="y",which='both',direction="in",labelsize=SMALL_SIZE,colors=COL)

#############################
####### spines color 
ax1.spines['left'].set_color(COL)
ax1.spines['right'].set_color(COL)
ax1.spines['top'].set_color(COL)
ax1.spines['bottom'].set_color(COL)

#############################
####### grid 
ax1.grid(b=True,which='minor',linestyle='-.',color=COL,alpha=0.1)
plt.minorticks_on()
ax1.grid(b=True,which='major',linestyle='-',color=COL,alpha=0.3)

ax1.xaxis.set_major_locator(MultipleLocator(0.5))
ax1.xaxis.set_minor_locator(AutoMinorLocator(2))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(2))


#############################
####### title 
plt.title(r'$\alpha > \beta$ as it gets, folks',color=COL,fontsize=BIGGER_SIZE)
#############################
####### legend 
legend = plt.legend([r'$\alpha > \beta$', "Train accuracy"], loc='upper right',facecolor=COL,edgecolor=None,framealpha=0,fontsize=SMALL_SIZE)
plt.setp(legend.get_texts(), color=COL)


############################
#######arror
textstr = '\n'.join((
    r'$\mu=%.2f$' % (1, ),
    r'$\mathrm{median}=%.2f$' % (2, ),
    r'$\sigma=%.2f$' % (3, )))

ax1.annotate(textstr,xy=(0.5, 0.5), xytext=(0, 0),arrowprops=dict(arrowstyle="->",color=COL),color=COL)

############################
#######text box
textstr = '\n'.join((
    r'$\mu=%.2f$' % (1, ),
    r'$\mathrm{median}=%.2f$' % (2, ),
    r'$\sigma=%.2f$' % (3, )))
props2 = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
props1 = dict(boxstyle=None, color='None')
ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=SMALL_SIZE,
        verticalalignment='top', bbox=props1,color=COL)

if IMSAVE:
	plt.savefig("testxy_text.png",transparent=True)

plt.show()
plt.close()
