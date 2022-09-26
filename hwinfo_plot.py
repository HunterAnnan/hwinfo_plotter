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
from pathlib import Path

#####
##### Routinely changeable inputs:
#####

filename = Path("raw_data/Owl_prime95.CSV")
date_fmt = mdate.DateFormatter('%H%M\n(%d %b)')

##Variable selector:     'all' is normally OK unless you have a large number
##                       columns/variables in your dataset
##
## T = Temperatures,         P = Power/Voltage,  C = Clock speeds,
## % = Usage/Residencies,    X = Ratios,         B = Bools
## all = all

var_types = ['all',
             # 'T',
             # 'P',
             # 'C'
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
# ax.scatter(data['Datetime'], data['Core Temperatures (avg) [°C]'], s=3, c='blue', label = 'CPU Avg Core Temperature')
# ax.scatter(data['Datetime'], data['Core Thermal Throttling (avg) [Yes/No]'], s=3, c='green', label = 'Therm Throt')
# ax.xaxis.set_major_formatter(date_fmt)
# ax.set_ylabel('Temperature / \N{DEGREE SIGN}C')
# ax2 = ax.twinx()
# ax2.scatter(data['Datetime'], data['Core Effective Clocks (avg) [MHz]'], s=3, c='red', label = 'Core Clocks')
# ax2.set_ylabel('Core Clocks / MHz')
# ax2.set_ylim(0, 2050)

# lines1, labels1 = ax.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# lines, labels = (lines1 + lines2), (labels1 + labels2)
# plt.legend(lines, labels, loc = 'lower right', scatterpoints = 7)

# plt.show()

end = time.time()
print("Plots completed in a further "
      + str(round(end-start, 4))
      + " seconds."
      )