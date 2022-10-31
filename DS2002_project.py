#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:58:37 2022

@author: lucywang
"""

import json
import requests
import pandas
import os
import csv
import pandas as pd

os.getcwd()


try:
    #retreive local file
    file = pd.read_csv("avocado.csv") #reads data file --> path to csv file from current directory
    file2 = file.rename(columns={"Unnamed: 0": "index"}) #rename first column that is unnamed
      
    try:
        #modify number of columns
        file2 = file2.drop(['year'], axis=1) #drop year columns 
        file2[['Year', 'Month', 'Day']] = file2['Date'].str.split('-', expand=True) #expand date column into three rows: year, month, day
        file2 = file2.drop(['Date'], axis=1) #drop original date column
    
    except:
        print("cannot drop/expand columns")
    
    #summary of data file
    print("Number of rows: " + str(file2.shape[0])) #print number of records
    
    print("Number of columns: " + str(file2.shape[1])) #print number of columns
    
    des = file2.describe() #summary statistics of data
    print(des)

except:
    print("cannot read file")


