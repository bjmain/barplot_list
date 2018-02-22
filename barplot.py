# bar_chart

import math
import matplotlib.pyplot as P
import numpy
import sys
#%matplotlib inline

#load data
d = [float(line.strip().split()[2]) for line in open("Cpipfilt_SNPs.idepth") if line.strip().split()[0]!="INDV"]
#import tick labels
xt = [line.strip().split()[0].split('_')[0] for line in open("Cpipfilt_SNPs.idepth") if line.strip().split()[0]!="INDV"]

ind = numpy.arange(len(d))+ 1  # the x locations for the groups

width = 0.25       # the width of the bars

fig, ax = P.subplots(1,1)
#b0 = ax.bar(ind+(1*width), d, width, color='k')
b1 = ax.bar(ind+(2*width), d, width, color='g')


ax.set_xticklabels( xt, fontsize=14, weight='bold',rotation = 90 )
ax.set_xticks (ind +.5 + width/2.)
ax.set_ylabel("average depth of coverage",weight='bold',fontsize=14)
#ax.set_yticks([.25,.50,.75])

#ax.set_xlim(1,7.25)
#ax.set_ylim(0,1)

#ax.legend()
#P.savefig("site_bm.png")
P.show()
