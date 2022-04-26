# 완성차 : 여러 개의 부품 클래스를 이용해 완성차를 생산

import pack3.test27_handle

class PohamCar:
    turnShowMessage = "정지"
    
    def __init__(self, ownerName):       #self가 참조하고 있는 포함카 인스턴스에 만들어진다. 이게 생성자
        self.ownerName = ownerName    # 얘로 인해서
        self.handle = pack3.test27_handle.PohamHandle()         #클래스의 포함 관계 ownerName처럼 self가 포함핸들을 가지게됨.# 포함 핸들 객체를 생성해서 주는거임. self가 가지고 있는 객체에는 PohamHandle이 들어감.
        #클래스가 또다른 클래스를 자기꺼인양 갖다 쓰는거 그게 포함이다.생성자를 통해서
        
    def TurnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.RightTurn(q)     # 점이 2개 이상 나왔으면 포함 관계구나. self.handle.RightTurn
        elif q < 0:
            self.turnShowMessage = self.handle.LeftTurn(q)
        elif q == 0:
            self.turnShowMessage = '직진'
            self.handle.quantity = 0
            
if __name__ == '__main__':
    tom = PohamCar('미스터 톰')
    tom.TurnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + str(tom.handle.quantity))
    
    tom.TurnHandle(0)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + str(tom.handle.quantity))
    
    print()
    sujan = PohamCar('미스 수잔')
    sujan.TurnHandle(-10)
    print(sujan.ownerName + '의 회전량은 ' + sujan.turnShowMessage + str(sujan.handle.quantity))
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        