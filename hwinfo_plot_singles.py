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
import json
from pathlib import Path

def get_cfg_file():
    """Looks for 'cfg.json' and returns the configuration as a dict."""
    try:
        with open('cfg.json') as f_obj:
            config_dict = json.load(f_obj)
    except FileNotFoundError:
        print("No config file found. Please run the configuration tool.")
    else:
        print("Configuration file loaded successfully")
        return config_dict

def get_data_filename_from_cfg(config_dict):
    data_filename = config_dict['filename']
    return data_filename

def direct_to_raw_data_folder(filename):
    filepath_str = "raw_data/" + filename
    filepath = Path(filepath_str)
    return filepath

def get_vars_to_plot_from_cfg(config_dict):
    vars_list = config_dict['variables']
    return vars_list

#hardcoded v bad
date_fmt = mdate.DateFormatter('%H%M\n(%d %b)')

if __name__ == "__main__":

    config_dict = get_cfg_file()

    #Find config file, identify data filename from it, then form a filepath.
    data_filepath = direct_to_raw_data_folder(
        get_data_filename_from_cfg(
            config_dict
            )
        )
    
    #Get a list of variables to plot
    vars_list = get_vars_to_plot_from_cfg(config_dict)
    
    #Load in and clean the data to be plotted
    ## does load_data need to do whatever it does with parsing datatypes,
    ## if the configurator has already run? i.e. is 'all' needed here?
    data = hwim.load_data(data_filepath, 'all', silent=True)
    
    start = time.time()
    
    plt.close('all')
    plt.rc('font', size=20)
    
    for var in vars_list:
        fig, ax = plt.subplots()
        ax.scatter(data['Datetime'], data[var], s=3)
        ax.xaxis.set_major_formatter(date_fmt)
        ax.set_ylabel(var)
        plt.tight_layout()
        plt.show()
    
    end = time.time()
    print("Plots completed in a further "
          + str(round(end-start, 4))
          + " seconds."
          )