# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:21:46 2022

Tool for plotting information recorded by HWiNFO. The expected input is a CSV file from HWiNFO.

This must be run in the same directory as hwinfo_import.py.

@author: Hunter.Annan
"""

import hwinfo_import as hwim

import pandas as pd
import matplotlib.pyplot as plt  #see https://matplotlib.org/
import matplotlib.dates as mdate
import time
import json
from pathlib import Path

def get_cfg_file():
    """Looks for 'cfg.json' and returns the configuration as a dict."""
    try:
        with open('cfg.json') as f_obj:
            cfg_dict = json.load(f_obj)
    except FileNotFoundError:
        print("No config file found. Please run the configuration tool.")
    return cfg_dict

def get_data_filename_from_cfg(cfg_dict):
    data_filename = cfg_dict['filename']
    print(data_filename)
    return data_filename

def direct_to_raw_data_folder(filename):
    filepath_str = "raw_data/" + filename
    filepath = Path(filepath_str)
    return filepath

date_fmt = mdate.DateFormatter('%H%M\n(%d %b)')

if __name__ == "__main__":

    #Find config file, identify data filename from it, then form a filepath.
    filepath = direct_to_raw_data_folder(
        get_data_filename_from_cfg(
            get_cfg_file(
                )
            )
        )
    
    # does load_data need to do whatever it does with parsing datatypes,
    # if the configurator has already run?
    data = hwim.load_data(filepath, 'all', silent=True)
    
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