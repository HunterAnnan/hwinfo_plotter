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

def q_reconfig(cfg):
    """Declares existing config file & asks user whether to proceed.
    Outputs proceed bool"""
    print("Existing config file found:")
    print(cfg)
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

def q_cfg_item(item):
    proceed_str = input("Reconfigure " + item + "? Y/N:\n")
    proceed = False
    flag = True
    while flag == True:
        if proceed_str.lower() == "y":
            proceed = True
            print("Configuring " + item + "...")
            flag = False
        elif proceed_str.lower() == "n":
            print("Skipping configuration of " + item)
            flag = False
    return proceed

def cfg_input_filename():
    """Accept input filename for .csv & check if there is a .csv extension"""
    filename = input('Enter the filename of the input CSV:\n')
    if filename.endswith('.csv'):
        cfg['filename'] = filename
    else:
        cfg['filename'] = str(filename + '.csv')

if __name__ == "__main__":
    cfg_filename = 'cfg.json'
    cfg, proceed = get_cfg(cfg_filename)
    
    if proceed == True:
        filename = Path("raw_data/Owl_prime95.CSV")  #replace with some way to get this path...
        
        proceed = q_cfg_item("input filename")
        if proceed == True:
            cfg_input_filename() #adds new filename to .json
            
        proceed = q_cfg_item("variables")
        if proceed == True:
            vars_dict = get_vars(filename, var_types=['all'], silent=True)
            vars_list = vars_dict.keys()
            for i, var in enumerate(vars_list):
                print(i, var)
                
        #some configuration happens here
        json.dump(cfg, open(cfg_filename, 'w'))