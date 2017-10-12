# -*- coding: utf-8 -*-
        
class Dummy:
     def __init__(self, a,b):
        self.__a = a
        self.b=b
     def sum(self):
        return self.__a+ self.b
     def mul(self):
        return self.__a*self.b
class ClassVsObject:
    print("hello")
    if __name__ == "__main__":
        print("private")
        d1= Dummy(10,20)
        d2= Dummy(30,40)
        d3= Dummy(1,5)
        print("hello")
#        print(d1.__a)
        print(d1.sum())
        print(d2.sum())
        print(d3.mul())
        print(d1,d2,d3)
    def hello(self):
        return 3000
