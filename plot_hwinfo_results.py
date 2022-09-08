# -*- coding: utf-8 -*-
"""
Tool for plotting information recorded by HWiNFO. The expected input is a CSV file from HWiNFO.

You can explore variables using the varlist_... functions

By default, this tool will create plots for...

@author: Hunter.Annan
"""

import pandas as pd
#import numpy as np
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
#     for i, val in enumerate(data.iloc[1:1,:]):
#         if val.isdigit():
#             data.iloc[i] = astype(data.iloc[i])
        #neeeeeds review

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
    df = df.convert_dtypes(convert_string=False) #needs replacing with a function...
    df = clean_dates(df)
    
    return df

def varlist_temp(data, silent=False):
    '''Data exploring:\n
    Adds variables of particular interest that can be read from the .CSV to a
    dictionary with matched datatypes. Use silent=False to print the variables.'''
    dict_tempvars = {}
    for i, val in enumerate(data.columns[:]):
        if u'\N{DEGREE SIGN}' in str(val):
            dict_tempvars[val] = type(data.iloc[i, 1])
            if silent == True:
                print(i)
    print(dict_tempvars)
            
def varlist_power(data):
    '''Data exploring:\n
    Lists all of the power & voltage variables that can be read from the csv'''
    for i in data.columns[:]:
        if '[w]' in str(i).lower():
            print(i)
            
def varlist_bool(data):
    '''Data exploring:\n
    Lists some boolean indicators that can be read from the csv'''
    for i in data.columns[:]:
        if 'no' in str(i).lower() or 'yes' in str(i).lower():
            print(data.head(0)[i].name)

#define user-selectable input variables
filename = 'raw_data\Owl_prime95.CSV'

data = load_data(filename)

# print(data.dtypes)
# print(data.iloc[0:1])
# varlist_bool(data)

