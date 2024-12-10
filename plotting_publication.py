# -*- coding: utf-8 -*-
"""
Any comments you want to add for documentation purposes.

"""

#
##########################
# Import python libraries
##########################
#
import numpy as np, numpy.ma as ma
import os
import random
import sys
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.gridspec import GridSpec
from textwrap import wrap
from matplotlib import rc # This sometimes gives problems
import csv
from random import randint

#
# Read data from the text file
#
x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6 = [], [],  [], [],  [], [],  [], [], [], [], [], []

# The following is one of the ways to read column data from a text file. You can change it as necessary
with open('filename.txt','r') as csvfile:
     for data in csvfile:
         row = data.split( )
         x1.append(float(row[0]))
         y1.append(float(row[1]))
csvfile.close()

# These are the parameters to use to get a publication quality figure.
mpl.rcParams['axes.linewidth'] = 1.2
mpl.rcParams['xtick.major.size'] = 6
mpl.rcParams['xtick.major.width'] = 1.2
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['xtick.minor.width'] = 1.2
mpl.rcParams['ytick.major.size'] = 6
mpl.rcParams['ytick.major.width'] = 1.2
mpl.rcParams['ytick.minor.size'] = 3
mpl.rcParams['ytick.minor.width'] = 1.2
mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['ytick.direction'] = 'out'
mpl.rcParams['font.size'] = 10
mpl.rcParams['mathtext.default'] = 'regular'
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10
mpl.rcParams['pdf.fonttype'] = 42 # new line
mpl.rcParams['legend.frameon'] = False
legend_properties = {'weight':'bold', 'size':8}
axisl_properties = {'family':'sans-serif','sans-serif':['Helvetica'], 'weight':'bold'}
label_properties = {'weight':'normal', 'size':10}

fig = plt.figure()
fig.set_size_inches(3.25, 3.25, forward=True)
ax1 = plt.Axes(fig, [0.115384615,0.230769231,0.769230769,0.769230769])
fig.add_axes(ax1)

# Other details about the figure!
ax1.errorbar(x1,y1,color='black',marker='None', linestyle='solid', label=r'label', elinewidth=1.3, capthick=1.3, capsize = 2.6, markerfacecolor='white', zorder = 1)
   
ax1.set_xlabel(r'xlabel', fontsize=15,fontweight='bold') # x-axis label
ax1.set_ylabel(r'ylabel',fontsize=15,fontweight='bold') # y-axis label

ax1.set_xlim(0,10) # x-axis limit (set limit according to your data)
ax1.set_ylim(0,10) # y-axis limit
ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))   # sets major tick spacing
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(2))   # sets minor tick spacing

ax1.set_xticklabels(ax1.get_xticks(), fontweight='bold', fontsize=10)
ax1.set_yticklabels(ax1.get_yticks(), fontweight='bold', fontsize=10)
ax1.tick_params(top=False)
ax1.tick_params(right=False)
ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f')) # set this based on your data (fraction vs integer number)
ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

ax1.legend(prop=legend_properties, numpoints = 1, bbox_to_anchor=(1.0, 0.98))
#ax1.set_title(f'%s' % str(title)) # if you want to add title to your figure
plt.savefig('fig.png', bbox_inches='tight', dpi=300)
plt.show()

#
#######
# End #
#######
#
