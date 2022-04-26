# 상속
class Person:
    say = '난 사람이야'
    nai = 20
    __abc = 'good'     # private    __를 붙이면 private 현재 클래스에서만 유효
    
    def __init__(self, nai):       #클래스의 멤버에 초기값을 주기 위해 생성자를 씀. 파이썬은 다 public이라 getter setter 없어도 됨
        print('Person 생성자')
        self.nai = nai
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))     #self를 this와 비교하면 된다.
        
    def hello(self):
        print('안녕')
        print(self.__abc)
        
    @staticmethod  
    def sbs(tel):
        print('sbs _ static method ', tel)
        
print(Person.say, Person.nai)   #Person.printInfo와 hello는 안됨 self를 만족 못시켜서?
p = Person(22)
p.printInfo()
p.hello()

print('***' * 10)
class Employee(Person):
    say = '일하는 동물'                               #부모의 멤버는 자식의 멤버에 의해 은닉화
    subject = '근로자'
    
    def __init__(self):
        print('Employee 생성자~~~')
        
    def printInfo(self):                                           # method override
        print('Employee 클래스 내의 printInfo')
        
    def eprintInfo(self):
        self.printInfo()
        super().printInfo()
        print(self.say, super().say)
        self.hello()

        
e = Employee()
print(e.say, e.nai)
print(e.subject)
e.printInfo()
e.eprintInfo()

print('---' * 10)
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)        # Bound method call
        
    def wprintInfo(self):
        super().printInfo()
        
w = Worker('25')
print(w.say, w.nai)
w.printInfo()
w.wprintInfo()

print('~~~' * 10)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        Worker.__init__(self, nai)            #unBound method call
        
    def wprintInfo(self):                  # 메소드 오버라이딩
        print('Programmer 내에 작성된 wprintinfo')
        
    def hello2(self):
        print(super().__abc)

        
pr = Programmer(33)
print(pr.say, pr.nai)
pr.printInfo()
pr.wprintInfo()

print()
p.hello()
# pr.hello2() # err __abc가 private이기 때문에 그 클래스에서만 사용 가능하다.
w.sbs('111-1111')
pr.sbs('222-2222')

print('클래스 타입----' )
a = 10
print(type(a))
print(type(pr))
print(Programmer.__bases__)
print(Worker.__bases__)
print(Person.__bases__)    # 최상위 superclass는 object. 클래스임을 오브젝이 알려줌. 최상위는 object







