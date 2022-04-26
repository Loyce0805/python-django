# 메소드 오버라이드 : 다형성

class Parent:
    def printData(self):        
        pass                             # 부모로서만 의미를 가질거라 내용이 없어. printdata라는 메소드를 오버라이드 하길 바래
    
class Child1(Parent):
    def printData(self):
        print('Child에서 override')
        
class Child2(Parent):
    def printData(self):
        print('Child2에서 재정의')
        print('부모 메소드와 이름은 같으나 기능이 다름')
        
    def abc(self):
        print('Child2 고유 메소드')
    
c1 = Child1()
c1.printData()
print()
c2 = Child2()
c2.printData()
c2.abc()

print('\n다형성 ---')     #스프링은 무조건 다형성
# par = Parent()   #자바는 부모 객체변수에게 자식의 주소를 치환하고 해야하는데 파이썬은 아니다.
par = c1
par.printData()
print()
par = c2
par.printData()

print()
plist = [c1, c2]
for a in plist:
    a.printData()
