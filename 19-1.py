# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 09:21:23 2017

@author: Administrator
"""

#class Person:
#    def __init__(self, name):
#        self.name = name
#    def sayHi(self):
#        print 'Hello, my name is', self.name
#p = Person('Swaroop')
#p.sayHi()


#class Singleton(object):
#    __instance = None                       # 定义实例
#
#    def __init__(self):
#        pass
#
#    def __new__(cls, *args, **kwd):         # 在__init__之前调用
#        if Singleton.__instance is None:    # 生成唯一实例
#            Singleton.__instance = object.__new__(cls, *args, **kwd)
#        return Singleton.__instance
#aa = Singleton()





#!/usr/bin/env python

class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'
        self.hr = hr
        self.min = min

    def __str__(self):
        'Time60 - string representation'
        return '%d:%d' % (self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        'Time60 - overloading the addition operator'
        return self.__class__(self.hr + other.hr,
            self.min + other.min)

    def __iadd__(self, other):
        'Time60 - overloading in-place addition'
        self.hr += other.hr
        self.min += other.min
        return self


mon = Time60(10,15)
tue = Time60(20,55)
print mon + tue






