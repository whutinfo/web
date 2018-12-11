# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 07:40:34 2018

@author: wangyu
"""
import xml.etree.cElementTree as ET
class xml_parse_test():
#    import xml.etree.cElementTree as self.ET
#    def __init__(self):
        
    def read_xml_first(self):
        
        self.tree = ET.ElementTree(file="E:\src\deeplearn\sample.xml")
        root = self.tree.getroot()
        print(root.tag)
        return self.tree
        
        
    def query_tag(self,name,tree):
        for ele in tree.iter(tag="book"): #遍历名称为book的节点
            print( ele.tag, ele.attrib    )
    
    def query_tag_all(self,tree):
        for ele in tree.iter(): #遍历所有的节点
            print( ele.tag, ele.attrib)
            
    def all_fun1(self):
        self.obj1 =  self.read_xml_first()
        self.query_tag('book',self.obj1)
        print('...............')
        self.query_tag_all(self.obj1)