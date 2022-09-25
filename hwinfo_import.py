# -*- coding: utf-8 -*-
"""
Tool for importing information recorded by HWiNFO. The expected input is a CSV file from HWiNFO.

@author: Hunter.Annan
"""

import pandas as pd
# import matplotlib.pyplot as plt  #see https://matplotlib.org/
# import matplotlib.dates as mdate
import time

#suppress pandas PerformanceWarning
from warnings import simplefilter
simplefilter(action="ignore",category=pd.errors.PerformanceWarning)

def load_data(filename, var_types=['all'], silent=True):
    '''Loads csv data into a pandas dataframe, then cleans it up\n
    Input expected: HWiNFO .CSV export'''
    print('Reading .CSV import')
    start = time.time()
    try: #latin_1 (ISO-8859-1) seems to be the correct encoding for HWiNFO 7.26; other versions may differ
        df = pd.read_csv(filename, encoding='latin_1', dtype='object', low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(filename, dtype='object', low_memory=False)
    df = clean_footer(df) #should be handled by read_csv, but 'c' engine doesn't allow skipfooter
    ## after removing problem cols/rows, we re-interpret object types:
    df = clean_dates(df) #dates & times to datetime64
    dict_vars={}
    dict_vars = build_varlist(df,
                              dict_vars, 
                              silent=silent, 
                              var_types=var_types
                              )
    df = df.astype(dict_vars) #convert dtypes using above-built dict
    ## record & report time to run
    end = time.time()
    print("Data loaded & variables mapped in "
          + str(round(end-start, 4))
          + " seconds."
          )
    return df

def clean_footer(df):
    '''Remove the footer rows (2 by default) and NaN column (1 by default)\n
    N.B. This is a "dumb" function! If the .CSV format changes, this will need
    changing as well.'''
    print('Cleaning excess rows and columns')
    df = df.iloc[
        :-2, #remove a specified number of final rows (footers)
        :-1] #remove a specified number of final columns (NaNs)
    return df

def clean_dates(df):
    '''Replaces date & time strings with a datetime column.'''
    print('Cleaning date formatting')    
    df["Datetime"] = pd.to_datetime((df["Date"] + " " + df["Time"]), 
                                    format='%d.%m.%Y %H:%M:%S.%f'
                                    )
    df.drop(columns = ["Date", "Time"], inplace = True)
    return df

def build_varlist(df, dict_vars, var_types=['all'], convert_bools=True, silent=True):
    '''Builds a list of variables from import .CSV in a dictionary with matched datatypes. 
    Use convert_bools=False to keep bool values as str.
    Use silent=False to print the variables.'''
    print("Building a list of variables & mapping data types")
    if 'all' in var_types or 'T' in var_types:
            varlist_temp(df, dict_vars, silent)
    if 'all' in var_types or 'P' in var_types:
            varlist_power(df, dict_vars, silent)
    if 'all' in var_types or '%' in var_types:
        varlist_usage(df, dict_vars, silent)
    if 'all' in var_types or 'X' in var_types:
        varlist_ratios(df, dict_vars, silent)
    if 'all' in var_types or 'B' in var_types:
        varlistfix_bool(df, dict_vars, convert_bools, silent)
    print("Variable list built; data types mapped")
    return dict_vars

def varlist_temp(df, dict_vars, silent=True):
    '''Temperature data: 
    Add temperature variables from import .CSV to a dict with matched datatypes.\n
    Use silent=False to print the variables.'''
    print("...mapping temperature variables")
    for i, val in enumerate(df.columns[:]):
        if u'\N{DEGREE SIGN}' in str(val):
            if df.iloc[0,i].isdigit():
                dict_vars[val] = "int64"
            else:
                dict_vars[val] = "float64"
            if silent == False:
                print(val)
            
def varlist_power(df, dict_vars, silent=True):
    '''Power & Voltage data: 
    Add power & voltage variables from import .CSV to a dict with matched datatypes.\n
    Use silent=False to print the variables.'''
    print("...mapping power & voltage variables")
    for i, val in enumerate(df.columns[:]):
        if '[w]' in str(val).lower() or '[v]' in str(val).lower():
            if df.iloc[0,i].isdigit():
                dict_vars[val] = "int64"
            else:
                dict_vars[val] = "float64"
            if silent == False:
                print(val)
                
def varlist_usage(df, dict_vars, silent=True):
    '''Usage data: 
    Add usage (% & byte) variables from import .CSV to a dict with matched datatypes.\n
    Use silent=False to print the variables.'''
    print("...mapping usage variables")
    for i, val in enumerate(df.columns[:]):
        if ('%' in str(val) or 
            '[kb]' in str(val).lower() or
            '[mb]' in str(val).lower() or 
            '[gb]' in str(val).lower()
            ):
            if df.iloc[0,i].isdigit():
                dict_vars[val] = "int64"
            else:
                dict_vars[val] = "float64"
            if silent == False:
                print(val)
                
def varlist_ratios(df, dict_vars, silent=True):
    '''Usage data: 
    Add ratio variables (CPU core & memory, normally) from import .CSV
    to a dict with matched datatypes.\n
    Use silent=False to print the variables.'''
    print("...mapping CPU core & memory ratio variables")
    for i, val in enumerate(df.columns[:]):
        if '[x]' in str(val):
            if df.iloc[0,i].isdigit():
                dict_vars[val] = "int64"
            else:
                dict_vars[val] = "float64"
            if silent == False:
                print(val)
            
def varlistfix_bool(df, dict_vars, convert_bools=True, silent=True):
    '''Boolean data: 
    Add boolean variables from import .CSV to a dict with matched datatypes.
    Additionally convert string bools to actual boolean values.\n
    Use convert_bools=False to keep bool values as str.
    Use silent=False to print the variables.'''
    print("...mapping boolean variables")
    for i, val in enumerate(df.columns[:]):
        if 'no' in str(val).lower() and 'yes' in str(val).lower():
            dict_vars[val] = 'bool'
            if convert_bools == True:
                df[val] = df[val].replace({'Yes': True, 'No': False})
            if silent == False:
                print(val)