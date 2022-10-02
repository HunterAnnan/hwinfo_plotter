# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:28:59 2022

Tool for configuring the hwinfo_plot tool.

@author: Hunter.Annan
"""

import json

#think this needs to have some sort of "does a .json already exist...? If so,
#import it and use it as a starting point...

cfg_filename = 'cfg.json'

#look for an existing configuration: if it doesn't, set some defaults
try:
    with open(cfg_filename) as file_obj:
        cfg = json.load(file_obj)
except FileNotFoundError:
    cfg = {'filename' : None,
              }

# accept user input for filename & check for .csv extension
filename_temp = input('Enter the filename of the input CSV:\n')
if filename_temp.endswith('.csv'):
    config_raw['filename'] = filename_temp
else:
    config_raw['filename'] = str(filename_temp + '.csv')

# json.dumps(config_raw, indent=4)
#some sort of save? 