# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:34:32 2018

@author: wangyu
"""

import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #与服务端相同
try:
    sock.connect(('127.0.0.1',1052))
except socket.error as e:
    print(e)
    sys.exit(-1)
data_send = 'test'
sock.send(data_send.encode())
data_recv = sock.recv(98)
print('recieved len is %d the recv conent is %s'%(len(data_recv),data_recv.decode()))
sock.close()

