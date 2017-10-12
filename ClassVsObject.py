# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:49:04 2017

@author: Reddy
"""



        
class Dummy:
     def __init__(self, a,b):
        self._a = a
        self.b=b
     def _sum(self):
        return self._a+ self.b
     def mul(self):
        return self._a*self.b
class ClassVsObject:
    print("hello")
    if __name__ == "__main__":
        print("private")
        d1= Dummy(10,20)
        d2= Dummy(30,40)
        d3= Dummy(1,5)
        print("hello")
        print(d1._a)
        print(d1._sum())
        print(d2._sum())
        print(d3.mul())
        print(d1,d2,d3)
    def hello(self):
        return 3000
