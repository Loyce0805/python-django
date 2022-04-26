# 자원의 재활용을 목적으로 클래스의 상속 - 다형성

class Animal:
    def __init__(self):                               #(생성자)
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')
        
    # ... 
    
class Dog(Animal):                              #java였으면 Dog에 ()를 붙이는게 extends
    #public Dog(){                                  #java였으면 이렇게 부모클래스를 불러야 하지만 안그래도됨.
    #   super()
    #}
    def __init__(self):                 #자식의 생성자가 있으면 자식거만 호출된다. 하지만 생성자가 없으면 부모클래스껄 호출한다.
        #super()   자바라면 이게 있었겠지.
        print('Dog 생성자')
    
    def my(self):
        print('난 댕댕이라고 해요')

dog1 = Dog()
dog1.my()
dog1.move()

print()
class Horse(Animal):
    pass

horse = Horse()
horse.move()