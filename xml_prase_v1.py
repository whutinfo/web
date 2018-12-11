# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 07:40:34 2018

@author: wangyu
"""
import xml.etree.cElementTree as ET

#    import xml.etree.cElementTree as ET
#    def __init__():
        
def read_xml_first():
    
    tree = ET.ElementTree(file="E:\src\deeplearn\sample.xml")
    root = tree.getroot()
    print(root.tag)
    return tree
    
    
def query_tag(name,tree):
    for ele in tree.iter(tag="book"): #遍历名称为book的节点
        print( ele.tag, ele.attrib    )

def query_tag_all(tree):
    for ele in tree.iter(): #遍历所有的节点
        print( ele.tag, ele.attrib    )
        
def all_fun1():
    obj1 =  read_xml_first()
    query_tag('book',obj1)
    print('...............')
    query_tag_all(obj1)