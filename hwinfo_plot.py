# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:21:46 2022

Tool for plotting information recorded by HWiNFO. The expected input is a CSV file from HWiNFO.

This must be run in the same directory as hwinfo_import.py.

@author: Hunter.Annan
"""

import hwinfo_import as hwim

# import pandas as pd
import matplotlib.pyplot as plt  #see https://matplotlib.org/
import matplotlib.dates as mdate
import time

#####
##### Routinely changeable inputs:
#####

filename = 'raw_data\E2000_lowramtest.CSV'
date_fmt = mdate.DateFormatter('%H%M\n(%d %b)')

##Variable selector:     'all' is normally OK unless you have a large number
##                       columns/variables in your dataset
##
## T = Temperatures,         P = Power/Voltage,
## % = Usage/Residencies,    X = Ratios,         B = Bools
## all = all]

var_types = ['all',
             # 'T',
             # 'P',
             # '%',
             # 'X',
             # 'B'
             ]

#####
##### End of routinely changeable inputs
#####

## Import data from the above .CSV file
## Use silent = False to see a list of mapped variables
data = hwim.load_data(filename, var_types, silent=False)

start = time.time()


# plt.close('all')
# plt.rc('font', size=20)

# fig, ax = plt.subplots()
# ax.scatter(data['Datetime'], data['Virtual Memory Load [%]'], s=3, c='blue', label = 'Virtual Memory')
# ax.xaxis.set_major_formatter(date_fmt)
# ax.set_ylabel('Memory Load / %')
# ax.scatter(data['Datetime'], data['Physical Memory Load [%]'], s=3, c='red', label = 'Physical Memory')
# ax.scatter(data['Datetime'], data['Page File Usage [%]'], s=3, c='green', label = 'Page File Usage')

# lines, labels = ax.get_legend_handles_labels()
# plt.legend(lines, labels, loc = 'upper right', scatterpoints = 7)

# plt.show()


end = time.time()
print("Plots completed in a further "
      + str(round(end-start, 4))
      + " seconds."
      )