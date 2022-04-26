from abc import *


class Employee(metaclass=ABCMeta):
    irum='이름'
    nai='nai'
    @abstractclassmethod
    def pay(self):
        pass
    
    @abstractclassmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print('이름:{}, 나이:{}'.format(self.irum, self.nai))

class Temporary(Employee):
    ilsu=0
    ildang=0
    
    def __init__(self,irum, nai,ilsu, ildang):
        self.irum= irum
        self.nai= nai
        self.ilsu= ilsu
        self.ildang=ildang
    
    
    def pay(self):
        pay=self.ilsu*self.ildang
        return pay
   
    def data_print(self):
        print('이름:{}, 나이:{}, 월급:{}'.format(self.irum, self.nai, self.pay()))

class Regular(Employee):
    
    def __init__(self,irum, nai,salary):
        self.irum= irum
        self.nai= nai
        self.salary= salary
    
    def pay(self):
        return self.salary
   
    def data_print(self):
        print('이름:{}, 나이:{}, 급여:{}'.format(self.irum, self.nai, self.pay()))

class Salesman(Regular):
    
    def __init__(self,irum, nai, salary, sales, commission):
        self.irum= irum
        self.nai= nai
        self.salary= salary
        self.sales=sales
        self.commission=commission
    
    def pay(self):
        pay= self.salary+ (self.sales*self.commission)
        return pay
    
    def data_print(self):
        print('이름:{}, 나이:{}, 수령액:{}'.format(self.irum, self.nai, int(self.pay())))
t= Temporary('sul',24,10,15000)
t.data_print() 
print()
r= Regular('minsu', 24, 2000000)
r.data_print()
print()
s= Salesman('bada', 21, 2000000, 5000000, 0.25)
s.data_print()