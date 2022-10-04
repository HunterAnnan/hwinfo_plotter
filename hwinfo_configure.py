# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:28:59 2022

Tool for configuring the hwinfo_plot tool.

@author: Hunter.Annan
"""

import json

#think this needs to have some sort of "does a .json already exist...? If so,
#import it and use it as a starting point...

def main():
    get_cfg()

def qproc(message_start):
    print(str(message_start)
          + ("; do you wish to proceed with configuration?")
          )

    # """Look for an existing config file: if none, set some defaults.\n
    # Returns a configuration dictionary, "cfg"."""
    
cfg_filename = 'cfg.json'

f_obj = open(cfg_filename)
cfg = json.load(f_obj)

try:
    with open(cfg_filename) as f_obj:
        cfg = json.load(f_obj)
except FileNotFoundError:
    cfg = {'filename' : None,
              }
else:
    qproc("Existing config file found")
print(cfg)
# return cfg


# accept user input for filename & check for .csv extension

# filename_temp = input('Enter the filename of the input CSV:\n')
# if filename_temp.endswith('.csv'):
#     cfg['filename'] = filename_temp
# else:
#     cfg['filename'] = str(filename_temp + '.csv')

cfg_file = open('cfg.json', 'w')

json.dump(cfg, cfg_file)
#some sort of save? 

# if __name__ == "__main__":
#     main()