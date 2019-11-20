import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
#############################
####### Data X y1 y2
t = np.arange(0.0, 2.0, 0.1);
s1 = 1 + 1*np.sin(2*np.pi*t);
err = (-1+np.cos(2*np.pi*t))/3;
#############################
####### On an OFF control
COL='black'
#COL='white'
IMSAVE=1;
#############################
####### SIZE

Line_width=2;
Marker_size=4;
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
ax1.errorbar(t, s1, err,fmt='-o',elinewidth=Line_width/2,capsize=4,color='r',linestyle='-',linewidth=Line_width, markersize=Marker_size)

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
if IMSAVE:
	plt.savefig("testxy.png",transparent=True)
plt.show()
plt.close()
