# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:13:52 2018

@author: wangyu
"""

#https://www.cnblogs.com/aland-1415/p/7309457.html
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',1057))
sock.listen(5)
conn,address = sock.accept()
if  conn:
    print('connect a client',address)
while True :
    data1 = conn.recv(100)
    
    if not data1:
        break
    print(data1)
    data = 'anydata'
    conn.send(data.encode())
sock.close()
