# 로또 생성기 : 클래스의 포함
import random

class LottoBall:
    def __init__(self, num):
        self.num = num
        
class LottoMachine:
    def __init__(self):
        self.ballList = []

        for i in range(1, 46):
            self.ballList.append(LottoBall(i))     # 클래스의 포함
                    
    def selectBall(self):
        # 섞기 전
        for a in range(45):
            print(self.ballList[a].num, end = ' ')
        
            random.shuffle(self.ballList)
        # 섞기 후
        print()
        for i in range(45):
            self.ballList.append(LottoBall(i))    
            
        return self.ballList[0:6]
     
            
class LottoUi:
    def __init__(self):
        self.machine = LottoMachine()      #   #   클래스의 포함
        
    def playLotto(self):
        input("로또 번호 뽑기를 시작하려면 엔터키를 누르세요")
        selectBalls = self.machine.selectBall()
        print()
        print("당첨번호 : ")
        for ball in selectBalls:
            print('%d '%ball.num)    # 한줄에 => print(ball.num, end = ' ')
        
if __name__ == '__main__':
    # aa = LottoUi().
    # aa.playLotto()
    LottoUi().playLotto()    # 위 두 코드를 합쳐서 한거다.

        
        
        
        
        
        
        
        
        