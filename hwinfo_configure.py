# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:28:59 2022

Tool for configuring the hwinfo_plot tool.

@author: Hunter.Annan
"""

import json

#think this needs to have some sort of "does a .json already exist...? If so,
#import it and use it as a starting point...

config_raw = {'filename' : None,
              }

# accept user input for filename & check for .csv extension
filename_temp = input('Enter the filename of the input CSV:\n')
if filename_temp.endswith('.csv'):
    config_raw['filename'] = filename_temp
else:
    config_raw['filename'] = str(filename_temp + '.csv')

# json.dumps(config_raw, indent=4)
#some sort of save? 