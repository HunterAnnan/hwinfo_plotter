# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:28:59 2022

Tool for configuring the hwinfo_plot tool.

@author: Hunter.Annan
"""

import json
from pathlib import Path

from hwinfo_import import test_load_data as get_vars

def get_cfg(cfg_filename):
    """Look for an existing config file: if none, set some defaults.
    Input: config filename
    Outputs: config file (dict) & proceed bool"""
    proceed = True
    try:
        with open(cfg_filename) as f_obj:
            cfg = json.load(f_obj)
    except FileNotFoundError:
        cfg = {'filename' : 'Test',
                  }
        print("No config file found. Defaults created:")
        print(cfg)
    else:
        proceed = q_reconfig(cfg)
    return cfg, proceed

def q_reconfig(existing_cfg_file):
    """Declares existing config file & asks user whether to proceed.
    Outputs proceed bool"""
    print("Existing config file found:")
    print(existing_cfg_file)
    proceed_str = input("Would you like to reconfigure? Y/N:\n")
    proceed = False
    if proceed_str.lower() == "y":
        proceed = True
        print("Proceeding with reconfiguration...")
    elif proceed_str.lower() == "n":#
        print("Abandoning reconfiguration")
    else:
        print("Input not recognised: abandoning reconfiguration.")
    return proceed

def q_cfg_item(configurable_item):
    proceed_str = input("Reconfigure " + configurable_item + "? Y/N:\n")
    proceed = False
    flag = True
    while flag == True:
        if proceed_str.lower() == "y":
            proceed = True
            print("Configuring " + configurable_item + "...")
            flag = False
        elif proceed_str.lower() == "n":
            print("Skipping configuration of " + configurable_item)
            flag = False
    return proceed

def cfg_input_CSV_filename():
    """Accept input filename for .csv & check if there is a .csv extension"""
    input_CSV_filename = input('Enter the filename of the input CSV:\n')
    if input_CSV_filename.lower().endswith('.csv'):
        cfg['filename'] = input_CSV_filename
    else:
        cfg['filename'] = str(input_CSV_filename + '.csv')

def cfg_vars_to_plot():
    full_vars_list = list(get_vars
                          (
                              input_filename, var_types=['all'], silent=True).keys()
                          )
    # full_vars_list = list(full_vars_dict.keys())
    print("\n  Available variables:")
    for i, var in enumerate(full_vars_list):
        print(i, var)
    ## Ask for some variables to plot (referenced by number) ...
    var_indices_str = input("\nInsert the variables you would like to plot, separated by commas:")
    vars_indices_list = map(int,
                            var_indices_str.replace(" ", "").split(",")
                            )
    ## ... then store as a list of variable names "vars_list" to be used later
    vars_list = []
    for var in vars_indices_list:
        vars_list.append(full_vars_list[var])
    cfg['vars'] = vars_list
    # feed the variables stored back to the user
    print("\nStoring the following variables for plotting:")
    for var in vars_list:
        print(var)

if __name__ == "__main__":
    cfg_filename = 'cfg.json'
    cfg, proceed = get_cfg(cfg_filename)
    
    if proceed == True:
        
        proceed = q_cfg_item("input filename")
        if proceed == True:
            cfg_input_CSV_filename() #adds new filename to .json
        
        #defines an input filename for cfg_vars_to_plot() to use
        input_filename = str("raw_data/" + cfg['filename'])
            
        proceed = q_cfg_item("variables")
        if proceed == True:
            cfg_vars_to_plot() #adds list of variables to plot to .json
        
        #some configuration happens here
        json.dump(cfg, open(cfg_filename, 'w'), indent=4)