# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:28:59 2022

Tool for configuring the hwinfo_plot tool.

@author: Hunter.Annan
"""

import json
from pathlib import Path

import hwinfo_import as hwi

def get_cfg(cfg_filename):
    """Look for an existing config file: if none, set some defaults."""
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
    print("Existing config file found:")
    print(cfg)
    proceed_str = input("Would you like to reconfigure? Y/N:\n")
    proceed = False
    if proceed_str.lower() == "y":
        proceed = True
    elif proceed_str.lower() == "n":#
        print("Abandoning reconfiguration")
    else:
        print("Input not recognised: abandoning reconfiguration.")
    return proceed

# accept user input for filename & check for .csv extension

# filename_temp = input('Enter the filename of the input CSV:\n')
# if filename_temp.endswith('.csv'):
#     cfg['filename'] = filename_temp
# else:
#     cfg['filename'] = str(filename_temp + '.csv')

if __name__ == "__main__":
    filename = Path("raw_data/Owl_prime95.CSV") 
    cfg_filename = 'cfg.json'
    cfg, proceed = get_cfg(cfg_filename)
    if proceed == True:
        print("Proceeding")
        dict_temp = hwi.test_load_data(filename, var_types=['all'], silent=True)
        print(dict_temp)
        #some configuration happens here
        # json.dump(cfg, open(cfg_filename, 'w'))