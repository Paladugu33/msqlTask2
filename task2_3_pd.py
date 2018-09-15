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
df = pd.DataFrame()

try:
    df['name'] = fd['facility_name']
    df['address'] = fd['facility_address']
    df['code'] = fd['facility_zip'] 
    df['city']= fd['facility_city']
except Exception:
    print ('data frame is not occuring')

#print ("business name, address, code, city :\n",df)

try:
    print(df.groupby('name')['name'].count())
except Exception:
    print ('grouping is failed and the error is :')
    error = Exception
    print (error)







