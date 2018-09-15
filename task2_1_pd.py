'''
Task of getting business name,address,code, city that have atleast one violation using pandas
'''



import xlrd
import os
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine


xl= pd.ExcelFile('/home/hmohan/Desktop/inspections.xlsx')
#xl.sheet_names
fd1 = xl.parse('inspections')

xl= pd.ExcelFile('/home/hmohan/Desktop/violations.xlsx')
fd2 = xl.parse('violations')

fd=pd.merge(fd2,fd1,on=['serial_number'])
df = pd.DataFrame()


df['name'] = fd['facility_name']
df['address'] = fd['facility_address']
df['code'] = fd['facility_zip'] 
df['city']= fd['facility_city']



engine = create_engine("mysql+mysqlconnector://root:admin@localhost/mydb")

con = engine.connect()
df.to_sql(name='previous_violations',con=con,if_exists='append')
con.close()
print ('table added')










