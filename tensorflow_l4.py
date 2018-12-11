# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:15:56 2018

@author: wangyu
"""

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
mnist = input_data.read_data_sets("E:/校内/研究/深度学习/src/learn1/MNIST_data/",one_hot=True)
sess = tf.InteractiveSession()
in_units = 784
h1_units = 300
W1 = tf.variable(tf.truncated_normal([in_units,h1_units],stddev = 0.1))
b1 = tf.variable(tf.zeros([h1_units]))
W2 = tf.variable(tf.zeros([in_units]))