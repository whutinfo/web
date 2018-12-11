
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 00:38:18 2018

@author: wangyu
"""

#! /usr/bin/python
#-* coding: utf-8 -*
# __author__ ="tyomcat"

import threading
import time
#import os
import socket
import select
import queue
class socket_cli_Trans():
    
    '''
    实现对客户端的socket链接，并接受和发送数据，实现数据的通信过程。请注意这次是实现二进制的模式下的数据通信。
    '''    
    def __init__(self,ipaddr,port):
        self.ipaddr = ipaddr
        self.port = port
#        self.sock_handle = 0
#        self.sock = 0
    def init_Connect_Type(self,conn_type):
        if conn_type == 1:
            self.sock_handle = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.sock_handle = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#    def connect_Srv(self):
#        self.sock = self.sock_handle.connect((self.ipaddr,self.port))
#    '''
            
    def connect_Srv(self):
        try:
            self.sock = self.sock_handle.connect((self.ipaddr,self.port))
        except (socket.error) as e:
            print(e)
            

    def test(self):
        print('connect')
        
    def send_data(self,send_data):
        self.sock_handle.send(send_data)
#        if not self.sock_handle:
#            self.sock_handle.send(send_data)
#        else:
#            print('cant send data')
        

        
        
        
    def recv_data_thread(self):
        while True:
            recv_buf = self.recv_data(self.data_len)
            if len(recv_buf) <= 2:
                break
            else:
                self.data_buf = recv_buf
                print(recv_buf)
        self.conn_close()
        
    def recv_data(self,data_len):
        data_buf = ''
        data_buf = self.sock_handle.recv(data_len)
        return data_buf
#        if not self.sock_handle:
#            
#            
#        else:
#            print('sock dont recv data')
        return data_buf
    def conn_close(self):
        self.sock_handle.close()
            
    def recv_data_thread_trans(self,data_len):
        self.data_len = data_len
        self.socket_cli_thread = threading.Thread(target=self.recv_data_thread,args=())
        self.socket_cli_thread.start()        
#        self.socket_cli_thread.join()
        
        
'''
socket服务器端的功能
'''        
class socket_srv_Trans(socket_cli_Trans):
    '''
    实现服务器端的数据收取功能
    '''
   
    def __init__(self,ipaddr,port):
        self.ipaddr = ipaddr
        self.port = port
#        self.sock_handle = 0
#        self.sock = 0
    def init_Connect_Type(self,conn_type,listen_cnt):
        if conn_type == 1:
            self.sock_handle = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock_handle.setblocking(False)
            self.sock_handle.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            self.sock_handle.bind((self.ipaddr,self.port))
            self.sock_handle.listen(listen_cnt)
        else:
            self.sock_handle = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            
    '''
    初始化线程的基本参数
    '''        
    def multi_accept_Init(self):
        self.rlists = [self.sock_handle]
        self.wlists = []
        self.timeout = 20
        self.msg_que = {}
#        self.sock_handle.accept()
#    def connect_Srv(self):
#        self.sock = self.sock_handle.connect((self.ipaddr,self.port))
#    '''
#            
#    def connect_Srv(self):
#        try:
#            self.sock = self.sock_handle.connect((self.ipaddr,self.port))
#        except (socket.error) as e:
#            print(e)
            

#    def test(self):
#        print('connect')
        
    def send_data(self,send_data):
        self.sock_handle.send(send_data)
#        if not self.sock_handle:
#            self.sock_handle.send(send_data)
#        else:
#            print('cant send data')
        

        
        
        
    def recv_data_thread(self):

        while self.rlists:
            self.rs,self.ws,self.es = select.select(self.rlists,self.wlists,self.rlists,self.timeout)
            if not (self.rs or self.ws or self.es):
                print('timeout...')
                break
            for s in self.rs:
                if s is self.sock_handle:
                    conn,address = s.accept()
                    conn.setblocking(False)
                    self.rlists.append(conn)
                    self.msg_que[conn] = queue.Queue()
                else:
                    data = s.recv(self.data_len)
                    if data:
                        print(data)
                        self.msg_que[s].put(data)
                        if s not in self.wlists:
                            self.wlists.append(s)
                    else:
                        if s in self.wlists:
                            self.wlists.remove(s)
                        self.rlists.remove(s)
                        self.s.close()
                        del self.msg_que[s]
            for s in self.ws:
                try:
                    self.msg_que[s].get_nowait()
                except queue.Empty:
                    self.wlists.remove(s)
            for s in self.es:
                print('except ',s.getpeername())
                if s in self.rlists:
                    self.rlists.remove(s)
                if s in self.wlists:
                    self.wlists.remove(s)
                s.close()
                del self.msg_que[s]
        
#    def recv_data(self,data_len):
#        data_buf = ''
#        data_buf = self.sock_handle.recv(data_len)
#        return data_buf
#        if not self.sock_handle:
#            
#            
#        else:
#            print('sock dont recv data')
#        return data_buf
    def conn_close(self):
        self.sock_handle.close()
            
    def recv_data_thread_trans(self,data_len):
        self.data_len = data_len
        self.socket_cli_thread = threading.Thread(target=self.recv_data_thread,args=())
        self.socket_cli_thread.start()        
#        self.socket_cli_thread.join()
        
#        
#    def set_srv_Param2Listen(self,conn_type,sel_cnt):
#        super(socket_srv_Trans,self).init_Connect_Type(conn_type)
#        
#        super(socket_srv_Trans,self).sock_handle.listen(sel_cnt)
    
    
#    
#    def srv_Accept_Connect(self):
#        try:
#            self.conn_handle,self.conn_address = self.conn_handle.accept()
#        except (socket.error) as e:
#            print(e)
            
            



def open_srv():
#    socket_test_srv = socket_srv_Trans('127.0.0.1',2001)
#    socket_test_srv.set_srv_Param2Listen(5,1)
    socket_test_cli = socket_cli_Trans('127.0.0.1',2001)
    data1 = 'test'
    socket_test_cli.init_Connect_Type(1)
    socket_test_cli.connect_Srv();
    socket_test_cli.send_data(data1.encode())
#    while True:
#        recv_data = socket_test_cli.recv_data(20)
#        if len(recv_data) <= 2:
#            break
#    socket_test_cli.conn_close()    
    socket_test_cli.recv_data_thread_trans(10)


def open_srv_listen():
    socket_srv_test = socket_srv_Trans('127.0.0.1',2001)
    socket_srv_test.init_Connect_Type(1,10)
    socket_srv_test.multi_accept_Init()
    socket_srv_test.recv_data_thread_trans(20)
    
    
if __name__ == "__main__": 
#    open_srv()
    open_srv_listen()
    while True:
        time.sleep(1)
        print('wait the message')
    



'''
def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()
        if i!=0:
            i=i-1
            print( "窗口:",tid,",剩余票数:",i)
            time.sleep(1)
        else:
            print( "Thread_id",tid,"No more tickets")
            os._exit(0)
        lock.release()
        time.sleep(1)

i = 100
lock=threading.Lock()

for k in range(10):

    new_thread = threading.Thread(target=booth,args=(k,))
    new_thread.start()
'''

#
#import socket
#class socket_cli_trans():
#    
#	def  __init__(self,ipaddr,port):
#		self.ipaddr = ipaddr
#		self.port = port
#	def Init_SocketType(self,socketType):
#        
#		if socketType == 1: #表示是TCP模式
#			self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#		else:
#			self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#        
#            
#    def conn_srv(self):
#        self.sock.connect((self.ipaddr,self.port))
#
#        try:
#            self.sock.connect((self.ipaddr,self.port))
#        except socket.error as e:
#            print(e)
    
     
#	def  conn_srv(self):
#		try:
#            self.sock.connect((self.ipaddr,self.port))
#       except socket.error as e:
#            print(e)
#                
        

		

