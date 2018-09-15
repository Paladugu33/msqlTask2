# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 19:40:41 2018

@author: hmohan
"""
import xlrd
import os
import pandas as pd
from datetime import datetime


xl= pd.ExcelFile('/home/hmohan/Desktop/inspections.xlsx')
#xl.sheet_names
fd1 = xl.parse('inspections')

xl= pd.ExcelFile('/home/hmohan/Desktop/violations.xlsx')
fd2 = xl.parse('violations')

fd=pd.merge(fd2,fd1,on=['serial_number'])

l=[]
try:
    for i in fd['facility_name']:
        l.append(i)
    
    l=set(l)
    l=list(l)
    l.sort()
    print('\n\n\n list of business name that have atleast one violation are:\n',l)
except Exception:
    error = Exception
    print (error)