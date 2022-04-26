# class

kor = 100

def abc():
    print('함수라고 해')
    
class MyClass:
    kor = 90                              # 멤버변수
    
    def abc(self):
        print('난 메소드야~')
        
    def show(self):
        # kor = 88
        print(self.kor)         #self 는 kor =  90이다     self는 java의 this와 같단다.
        print(kor)                # kor 은 kor = 100이다    지역변수 일 수도 있지만 없으면 모듈로 간다.
        self.abc()                #self.abc 호출하면 멤버메소드
        abc()                       #abc() 호출하면 모듈의 전역메소드 호출  (지역메소드가 없으니까)
        
my = MyClass()
my.show()

print('-----------------')
class OurClass:
    a = 1
    
print(OurClass.a)

our1 = OurClass()
print(our1.a)

our2 = OurClass()
print(our2.a)
our2.b = 2
print(our2.b)


# print(our1.b)   # our1.b에 할당된 값이 없다?
