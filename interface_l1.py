# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:14:26 2018

@author: wangyu
"""

#import tkinter  as gui_test

import tkinter as gui_test

master = gui_test.Tk()

w = gui_test.Canvas(master, width=200, height=100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="#476042", width=3)
w.create_line(0, 100, 50, 80, fill="#476042", width=3)
w.create_line(150,20, 200, 0, fill="#476042", width=3)
w.create_line(150, 80, 200, 100, fill="#476042", width=3)

gui_test.mainloop()
