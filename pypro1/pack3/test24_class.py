# class : 메소드(함수)나 변수 등을 포함한 별도의 집합체(객체, 개체, Object) - 객체 중심의 프로그래밍이 가능

class Car:
    handle = 0
    speed = 0
    
    def __init__(self, na, sp):
        self.name = na
        self.speed = sp #셀프한테 간다.
        
    def showData(self):
        km = '킬로미터'
        msg = '속도 : ' + str(self.speed) + km + " 확인한 사람 : " + self.name
        return msg
    
print(Car.handle)             # 원형 클래스의 멤버를 출력. prototype 값 출력
print()
car1 = Car('tom', 10)           # 생성자를 통한 객체 생성
print(car1.handle, car1.name, car1.speed)
car1.color = ' 검정'
print(car1.color)
print()
car2 = Car('james', 20)
print(car2.handle, car2.name, car2.speed)
car2.color = ' 그린'
print(car2.color)
# print(car2.color)   car1에 검정만 넣어놔서 다른데는 컬러가 없다
# print(Car.color)
print()
print(car1.showData())

ss = car2.showData()
print(ss)

print()
print('주소 : ', id(Car), id(car1), id(car2))
print(car1.__dict__)
print(car2.__dict__)

car1.speed = 80
print(car1.showData())
print(car2.showData())

Car.handle = '한 개'
print(car1.handle)
print(car2.handle)











  
  
    







