# -*- coding: utf-8 -*-
"""
Tool for plotting information recorded by HWiNFO. The expected input is a CSV file from HWiNFO.

You can explore variables using the varlist_... functions

By default, this tool will create plots for...

@author: Hunter.Annan
"""

import pandas as pd
# import numpy as np
#import matplotlib.pyplot as plt  #see https://matplotlib.org/

#suppress pandas PerformanceWarning
from warnings import simplefilter
simplefilter(action="ignore",category=pd.errors.PerformanceWarning)

def clean_footer(df):
    '''Remove the footer rows (2 by default) and NaN column (1 by default)'''
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
    df.drop(columns = ["Date", "Time"])
    return df

# def clean_dtypes(df):
#     '''Try some different dtypes and ... [needs completing]'''
#     for i, val in enumerate(df.iloc[0:1, -5:]):
#         if df.iloc[0,i].lower() == 'yes' or df.iloc[0,i].lower() == 'no':
            
#     return df

def load_data(filename):
    '''Loads csv data into a pandas dataframe, then cleans it up\n
    Input expected: HWiNFO .CSV export'''
    print('Reading .CSV import')
    try: #ANSI is the correct encoding for HWiNFO 7.26; other versions may differ
        df = pd.read_csv(filename, encoding='ANSI', low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(filename, low_memory=False)
    df = clean_footer(df)
    #after removing problem cols/rows, we re-interpret object types:
    df = clean_dates(df)
    df = df.convert_dtypes()
    # df = clean_dtypes(df)
    
    return df

def varlist_temp(df, dict_vars, silent=True):
    '''Data exploring: Temperature\n
    Adds variables of particular interest that can be read from the .CSV to a
    dictionary with matched datatypes. Use silent=False to print the variables.'''
    for i, val in enumerate(data.columns[:]):
        if u'\N{DEGREE SIGN}' in str(val):
            if df.iloc[0,i].isdigit():
                dict_vars[val] = "int64"
            else:
                dict_vars[val] = "float64"
            if silent == False:
                print(val)
            
def varlist_power(df, dict_vars, silent=True):
    '''Data exploring: Power\n
    Adds variables of particular interest that can be read from the .CSV to a
    dictionary with matched datatypes. Use silent=False to print the variables.'''
    for i, val in enumerate(df.columns[:]):
        if '[w]' in str(val).lower() or '[v]' in str(val).lower():
            if df.iloc[0,i].isdigit():
                dict_vars[val] = "int64"
            else:
                dict_vars[val] = "float64"
            if silent == False:
                print(val)
            
def varlist_bool(df, dict_vars, silent=True):
    '''Data exploring:\n
    Lists some boolean indicators that can be read from the csv'''
    for i, val in enumerate(df.columns[:]):
        if 'no' in str(val).lower() and 'yes' in str(val).lower():
            dict_vars[val] = 'bool'
            if silent == False:
                print(val)

def varlist_usage(df, dict_vars, silent=True):
    for i, val in enumerate(data.columns[:]):
        if '%' in str(val) or '[mb]' in str(val).lower() or '[gb]' in str(val).lower():
            if df.iloc[0,i].isdigit():
                dict_vars[val] = "int64"
            else:
                dict_vars[val] = "float64"
            if silent == False:
                print(val)

def build_varlist(df, silent=True):
    dict_vars = {}
    varlist_temp(df, dict_vars, silent)
    varlist_power(df, dict_vars, silent)
    varlist_bool(df, dict_vars, silent)
    varlist_usage(df, dict_vars, silent)
    print(dict_vars)

#define user-selectable input variables
filename = 'raw_data\Owl_prime95.CSV'

data = load_data(filename)

# print(data.dtypes)
# print(data.iloc[0:1])

build_varlist(data)