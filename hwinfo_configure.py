# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:28:59 2022

Tool for configuring the hwinfo_plot tool.

@author: Hunter.Annan
"""

import json

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
        cfg = {'filename' : None,
               'variables' : None,
               'variables_(multi)' : None
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
    for key, val in existing_cfg_file.items():
        print(f"{key.title() + ':  ':<20}" + str(val))
    proceed_str = input("Would you like to reconfigure? Y/N:\n")
    proceed = False
    if proceed_str.lower() == "y":
        proceed = True
        print("Proceeding with reconfiguration...")
    elif proceed_str.lower() == "n":
        print("Abandoning reconfiguration")
    else:
        print("Input not recognised: abandoning reconfiguration.")
    return proceed

def q_cfg_item(configurable_item):
    proceed = False
    flag = True
    while flag == True:
        proceed_str = input("Reconfigure " + configurable_item + "? Y/N:\n")
        if proceed_str.lower() == "y":
            proceed = True
            print("Configuring " + configurable_item + "...")
            flag = False
        elif proceed_str.lower() == "n":
            print("Skipping configuration of " + configurable_item)
            flag = False
        else:
            print("\nInvalid input.")
    return proceed

def cfg_input_CSV_filename():
    """Accept input filename for .csv & check if there is a .csv extension"""
    input_CSV_filename = input('Enter the filename of the input CSV:\n')
    if input_CSV_filename.lower().endswith('.csv'):
        cfg['filename'] = input_CSV_filename
    else:
        cfg['filename'] = str(input_CSV_filename + '.csv')

def get_available_variables():
    full_vars_list = list(get_vars
                          (
                              input_filename, var_types=['all'], silent=True).keys()
                          )
    print("\n  Available variables:")
    for i, var in enumerate(full_vars_list):
        print(i, var)
    return full_vars_list

def cfg_vars_for_single_var_plot():
    full_vars_list = get_available_variables()
    ## Ask for some variables to plot (referenced by number) ...
    var_indices_str = input("\nSingle-variable plots:" +
                            "\n Enter the variable(s) you would like from the list above." +
                            "\n Use the index numbers, separated by commas (,):\n"
                            )
    vars_indices_list = map(int,
                            var_indices_str.replace(" ", "").split(",")
                            )
    ## ... then store as a list of variable names "vars_list" to be used later
    vars_list = []
    for var in vars_indices_list:
        vars_list.append(full_vars_list[var])
    cfg['variables'] = vars_list
    # feed the variables stored back to the user
    if len(vars_list) == 1:
        print("\nStoring the following variable for plotting:")
    else:
        print("\nStoring the following variables for plotting:")
    for var in vars_list:
        print(var)
        
def cfg_vars_for_multi_var_plot():
    full_vars_list = get_available_variables()
    ## Ask for some variables to plot (referenced by number) ...
    var_indices_str = input("\nMulti-variable plots:" +
                            "\n Enter the variable(s) you would like from the list above." +
                            "\n Use the index numbers, separating variables with commas (,)" +
                            "\n and separating plots with forward slashes (/):\n"
                            ) 
    vars_indices_list = list(map(str,
                                 var_indices_str.replace(" ", "").split("/")
                                 )
                             )
    plots_list = [ [] for _ in range(len(vars_indices_list)) ]
    for plot_index, plot_vars in enumerate(vars_indices_list):
        vars_indices_list[plot_index] = list(map(int,
                                        vars_indices_list[plot_index].replace(" ", "").split(",")
                                        )
                                    )
        for var in vars_indices_list[plot_index]:
            print(full_vars_list[var])
            plots_list[plot_index].append(full_vars_list[var])
    cfg['variables_(multi)'] = plots_list
    # feed the variables stored back to the user
    if len(plots_list) == 1:
        print("\nStoring variable(s) for the plot:")
    else:
        print("\nStoring variables for " + str(len(plots_list)) + " plots:")
    for i, plot in enumerate(plots_list):
        print(" Plot " + str(i) + ":")
        for var in plot:
            print("  " + var)

if __name__ == "__main__":
    cfg_filename = 'cfg.json'
    cfg, proceed = get_cfg(cfg_filename)
    
    if proceed == True:
        
        proceed = q_cfg_item("input filename")
        if proceed == True:
            cfg_input_CSV_filename() #adds new filename to .json
        
        #defines an input filename for cfg_vars_to_plot() to use
        input_filename = str("raw_data/" + cfg['filename'])
          
        proceed = q_cfg_item("variables for single-variable plots")
        if proceed == True:
            cfg_vars_for_single_var_plot() #adds list of variables to plot to .json
        
        proceed = q_cfg_item("variables for multi-variable plots")
        if proceed == True:
            cfg_vars_for_multi_var_plot() #adds list of variables to plot to .json
        
        #some configuration happens here
        json.dump(cfg, open(cfg_filename, 'w'), indent=4)