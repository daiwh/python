__author__ = 'wenhai.dai'
#-*-  encode:utf-8  -*-
import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1', user='root', password='root', database='mytest')
cursor = conn.cursor()
cursor.execute("insert into user values(1,'daidai','daiwenhai')")
conn.commit()
cursor.close()
conn.close()


