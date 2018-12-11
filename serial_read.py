# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:56:43 2018

@author: wangyu
"""

import serial
from time import sleep

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data

if __name__ == '__main__':
    serial = serial.Serial('COM5', 9600, timeout=0.5)  #/dev/ttyUSB0
#    serial.Serial.BAUDRATES = 9600;
#    serial.Serial.parity = serial.PARITY_EVEN;
    
    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")

    while True:
        data =recv(serial)
        if data != b'' :
            print("receive : ",data)
            serial.write(data) #数据写回
#--------------------- 
#作者：itas109 
#来源：CSDN 
#原文：https://blog.csdn.net/itas109/article/details/78874165 
#版权声明：本文为博主原创文章，转载请附上博文链接！