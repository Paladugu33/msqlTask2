# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:33:21 2018

@author: hmohan
"""

import mysql.connector

# CONNECTING TO DATABASE
database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database='mydb'
                                   )
#connect to cursor                       
cursor = database.cursor()

cursor.execute( """SELECT \
    DISTINCT \
    INSPECTIONS.facility_name as name \
    FROM VIOLATIONS\
    INNER JOIN INSPECTIONS ON INSPECTIONS.serial_number=VIOLATIONS.serial_number""")
myresult = cursor.fetchall()
lst=[]
for i in myresult:
    lst.append(i)
lst.sort()    
print (lst)