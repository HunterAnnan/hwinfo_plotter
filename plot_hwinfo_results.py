# -*- coding: utf-8 -*-
"""
Tool for plotting information recorded by HWiNFO64. The expected input is a CSV file from HWiNFO64.

You can explore variables using the varlist_... functions

By default, this tool will create plots for...

@author: Hunter.Annan
"""

import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt  #see https://matplotlib.org/

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
    df["Datetime"] = pd.to_datetime((df["Date"] + " " + df["Time"]), format='%d.%m.%Y %H:%M:%S.%f')
    df.drop(columns = ['Date', 'Time'])
    return df

def load_data(filename):
    '''Loads csv data into a pandas dataframe, then cleans it up
    
    input expected: HWiNFO .CSV export'''
    
    #encoding may differ between HWiNFO64 versions: ANSI is correct for v.7.26.
    print('Reading .CSV import')
    df_temp = pd.read_csv(filename, encoding='ANSI', low_memory=False)
    df_temp = clean_footer(df_temp)
    #after removing problem cols/rows, we re-interpret object types:
    df_temp = df_temp.infer_objects()
    df_temp = clean_dates(df_temp)
    
    return df_temp

def varlist_temp(data):
    '''Data exploring:\n
    Adds variables of particular interest that can be read from the .CSV to a
    dictionary with matched datatypes. Use silent=False to print the variables.'''
    for i in data.columns[:]:
        if u'\N{DEGREE SIGN}' in str(i):
            print(i)
            
def varlist_power(data):
    '''Data exploring:\n
    Lists all of the power & voltage variables that can be read from the csv'''
    for i in data.columns[:]:
        if '[w]' in str(i).lower():
            print(i)
            
def varlist_bool(data):
    '''Data exploring:\n
    Lists some boolean indicators that can be read from the csv'''
    for i in data.iloc[1:1,:]:
        if 'no' in str(i).lower() or 'yes' in str(i).lower():
            print(data.head(0)[i].name)

#define user-selectable input variables
filename = 'raw_data\Owl_prime95.CSV'

data = load_data(filename)
print(data)
#print(data['Datetime'])
#print(data['Core 0 VID [V]'])
#print(type(data['Core 0 VID [V]'][0]))

