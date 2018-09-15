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

cursor.execute("select name,COUNT(*) from pre_vio GROUP BY name")

myresult = cursor.fetchall()
print (myresult)