# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:14:13 2018

@author: wangyu
"""

# 服务端实例
import socket
import select
import queue

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setblocking(False)   #设置为非阻塞服务
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('127.0.0.1',20178))
sock.listen(10)
rlists = [sock]
wlists = []
msg_que = {}
timeout = 20

while rlists:
    rs,ws,es = select.select(rlists,wlists,rlists,timeout)
    if not (rs or ws or es):
        print('timeout...')
        break
    for s in rs:
        if s is sock:
            conn,address = s.accept()
            conn.setblocking(False)
            rlists.append(conn)
            msg_que[conn] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print(data)
                msg_que[s].put(data)
                if s not in wlists:
                    wlists.append(s)
            else:
                if s in wlists:
                    wlists.remove(s)
                rlists.remove(s)
                s.close()
                del msg_que[s]
    for s in ws:
        try:
            msg = msg_que[s].get_nowait()
        except queue.Empty:
            wlists.remove(s)
    for s in es:
        print('except ',s.getpeername())
        if s in rlists:
            rlists.remove(s)
        if s in wlists:
            wlists.remove(s)
        s.close()
        del msg_que[s]