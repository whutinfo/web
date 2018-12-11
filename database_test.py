# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:30:57 2018

@author: wangyu
"""

import pymysql
conn = pymysql.connect(host='39.108.107.126', port=3306, database='test1', user='user', password='user', charset='utf8')
cursor = conn.cursor()
cursor.execute('SELECT * from student')
data = cursor.fetchone()
print('database version: %s' % data)
conn.close()