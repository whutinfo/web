# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:02:32 2018

@author: wangyu
"""
#周雅雯
#总类：动物
class Animal(object):
    def __init__(self , name,foot,eye,lung):
        self.name = name
        self.eye = eye
        
    
    def getEye(self,value):
        self.eye=value
        
    

#有足动物
class HaveFoot(Animal):
    
    def __init__(self,name,foot,eye,lung):
        super(HaveFoot,self).__init__(name,eye)
        self.__foot=foot
        
    def set_foot(self,value):
        self.__foot=value
        
    def getFoot(self):
        return self.__foot
    

#无足动物
class NoFoot(Animal):
    __foot=0
    def FootNumber(self):
        return self.__foot

#海生动物
class SeaAnimal(Animal):
    __lung=0
    def LungNumber(self):
        return self.__lung


#陆生动物
class LandAnimal(Animal):
    def __init__(self,name,foot,eye,lung):
        super(LandAnimal,self).__init__(name,foot,eye)
        self.__lung=lung
        
    def set_lung(self,value):
        self.__lung=value
        
    def getLung(self):
        return self.__lung
#鲸鱼
class Whale(NoFoot,SeaAnimal):
    def __init__(self,name):
        self.name=name
        self.eye=2
        
#章鱼
class Devilfish(HaveFoot,SeaAnimal):
    def __init__(self,name):
        self.name=name
        self.eye=2
        self.set_foot(8)


#马
class Horse(HaveFoot,LandAnimal):
    def __init__(self,name):
        self.name=name
        self.eye=2
        self.set_foot(4)
        self.set_lung(1)

        
#牛
class Cow(HaveFoot,LandAnimal):
    def __init__(self,name):
        self.name=name
        self.eye=2
        self.set_foot(4)
        self.set_lung(1)



#人
class Human(HaveFoot,LandAnimal):
    def __init__(self,name):
        self.name=name
        self.eye=2
        self.set_foot(2)
        self.set_lung(1)
    # coding = utf-8

class Animal():
	def __init__(self,name):
		self.name = name
		self.eye = 2
		self.mouse = 1




#林慧宁
class Animal_with_legs(Animal):
	def __init__(self,name,legs,nums):
		super.__init__(self,name)
		self.legs = legs * nums
		print("%s has %d legs"%(self.name,self.legs))
	def get_legnums(self):
		return self.legs


class Animal_without_legs(Animal):
	def __init__(self,name):
		super.__init__(self,name)
		self.legs = 0
		print("%s has no legs"%self.name)
	def get_legnums(self):
		super.get_legnums()
		return 0

if __name__ == '__main__':
	Yang = Animal_with_legs('yang',2,10)
	ZhangYu = Animal_with_legs('zhangyu',8,5)
	Jingyu = Animal_without_legs('jingyu')
	leg_total = Yang.get_legnums() + ZhangYu.get_legnums() + Jingyu.get_legnums()






















'''
夏琪
'''


class Animal(object):  
    def __init__(self):
        self.name=''
        self.eye=''
        self.mouth=''
     #### 设置各属性 ####    
    def set_eye(self,value):
        self.eye=value 
    def set_mouth(self,value):
        self.mouth=value
        ###用封装成方法获得相应信息
    def get_eye(self):
        return self.eye
    def get_mouth(self):
        return self.mouth
    def move(self):####行动
        print('The animal is moving slowly')
    def sleep(self):####睡觉
        print('The animal is sleeping')

        
#无足动物
class Apod(Animal): 
    __foot=0#不能更改 
    def get_foot(self):
        return self.__foot 
    def set_color(self,value):
        self.color=value
    def get_color(self):
        return self.color
#有足动物
class Footed_Animal(Animal):
    ##继承eye,mouth属性，设置值的方法，和获取的方法
    def __init__(self):
       # super 指的是 MRO 中的下一个类
        super(Footed_Animal,self).__init__()
        self.__foot=''
    def set_foot(self,value):
        self.__foot=value
    def get_foot(self):
        return self.__foot
    def set_color(self,value):
        self.color=value
    def get_color(self):
        return self.color
    
#鲸鱼
class Whale(Apod):
    def __init__(self):
        super(Whale,self).__init__()
        
 #已经是比较具体的一个类了，眼睛嘴巴可以直接给确定值
        self.eye=2  
        self.mouth=1

#章鱼
class Octopus(Footed_Animal):
    def __init__(self):
        super(Octopus,self).__init__()
        self.eye=2  
        self.mouth=1
        self.set_foot(8)
    def spit(self):###章鱼吐墨
        print('It spits ink')
#马
class Horse(Footed_Animal):
    def __init__(self):
        super(Horse,self).__init__()
        self.eye=2  
        self.mouth=1
        self.set_foot(4)

#牛
class Cow(Footed_Animal):
     def __init__(self):
        super(Cow,self).__init__()
        self.eye=2  
        self.mouth=1
        self.set_foot(4)
    
#羊
class Sheep(Footed_Animal):
     def __init__(self):
        super(Sheep,self).__init__()
        self.eye=2  
        self.mouth=1
        self.set_foot(4)

#人
class People(Footed_Animal):
     weight=''
     score=''
     def __init__(self):
        super(People,self).__init__()
        self.eye=2  
        self.mouth=1
        self.set_foot(2)
     def set_score(self,value):
         self.score=value
     def get_score(self):
         return self.score
     
def getSum(animal,x):
    if hasattr(animal,'get_foot'):
        sum=animal.get_foot()*x
        return sum
    
whale=Whale()
octopus=Octopus()
horse=Horse()
sheep=Sheep()
people=People()
WSum=getSum(whale,10)
OSum=getSum(octopus,10)
HSum=getSum(horse,2)
SSum=getSum(sheep,3)
total=WSum+OSum+HSum+SSum
print('10个鲸鱼有%s条腿\n10个章鱼有%s条腿\n2个马有%s条腿\n3个羊有%s条腿'%(WSum,OSum,HSum,SSum))
print('共有%s条腿'%total)
