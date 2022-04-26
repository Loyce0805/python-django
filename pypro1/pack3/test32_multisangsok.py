# 다중상속
# 복스의 클래스를 상속가능 : 순서가 중요
class Donkey:
    data = '당나귀 만세'
    
    def skill(self):
        print('당나귀 : 짐 나르기')
        
        
class Horse:
    def skill(self):
        print('말 : 달리기')
        
    def hobby(self):
        print('프로그램 짜기')
        
class Mule1(Donkey, Horse):
    pass
mu1 = Mule1()
print(mu1.data)
mu1.skill()             # 먼저 나온 클래스에 우선순위가 있음. 그래서 당나귀:짐나르기가 나온다
mu1.hobby()

print()
class Mule2(Horse, Donkey):
    def play(self):
        print('노새 고유 메소드')
        
    def hobby(self):
        print('노새는 걷기를 좋아함')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data, super().data)         #self는 mule2를 뒤지고 없으면 부모. super는 처음부터 부모
        
mu2 = Mule2()
mu2.skill()                   # Horse를 먼저 적었기 때문에 Horse의 스킬이 나옴.
mu2.hobby()
mu2.play()
mu2.showHobby()














