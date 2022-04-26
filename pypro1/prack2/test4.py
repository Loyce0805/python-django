from abc import *


class Employee(metaclass = ABCMeta):
    irum = "이름"
    nai = "나이"
    
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def data_print(self):
        pass
    
    def irumnai_print(self, irum, nai):
        print('이름:{}, 나이:{}'.format(self.irum, self.nai))


class Temporary(Employee):
    ilsu = 0
    ildang = 0

    def __init__(self, irum, nai, ilsu, ildang):
        self.irum = irum
        self.nai = nai
        self.ilsu = ilsu
        self.ildang = ildang

    def pay(self):
        pay = self.ilsu * self.ildang
        return pay

    def data_print(self):
        print('이름:{}, 나이:{}, 월급:{}'.format(self.irum, self.nai, self.pay()))
        
class Regular(Employee):
    salary = 0
    
    def __init__(self, irum, nai, salary):
        self.irum = irum
        self.nai = nai
        self.salary = salary
    
    def pay(self):
        pass
        
    def data_print(self):
        print('이름:{}, 나이:{}, 급여:{}'.format(self.irum, self.nai, self.salary))
        
class Salesman(Regular):
    sales = 0
    commission = 0
    
    def __init__(self, irum, nai, salary, sales, commission):
        self.irum = irum
        self.nai = nai
        self.salary = salary
        self.sales = sales
        self.commission=commission
        
    def sudang(self):
        sudang = self.sales * self.commission
        sudang2 = self.salary + sudang
        return sudang2
        
    def data_print(self):
       print('이름:{}, 나이:{}, 수령액:{}'.format(self.irum, self.nai, self.sudang()))
        


t = Temporary('홍길동', 24, 20, 100000)
t.data_print()
print()

r = Regular('이재인', 30, 5000)
r.data_print()
print()

s = Salesman('김구라', 48, 20000, 5000, 0.5)
s.data_print()
       
    
        
            
    
    