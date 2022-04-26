# 커피 자판기 프로그램

class CoinIn:   # 계산만 진행
    def __init__(self, coin):
        self.coin = coin
        
    def culc(self, cupCount):
        coff = int(200)
        total = cupCount * coff
        if self.coin < total:
            print('요금이 부족합니다.')
        else:
            # 잔돈 계산
            change = self.coin - total
            print('커피 {}잔과 잔돈 {}원'.format(cupCount, change))

class Machine:  # 입력과 출력 진행
    def __init__(self):
        # 동전과 잔 수 입력 받기
        self.coin = int(input('동전을 입력하세요 : '))
        self.cupCount = int(input('몇 잔을 원하세요? : '))
        
    def showData(self):
        # 객체 생성(들어간 동전에 대한 객체)
        inCoin = CoinIn(self.coin)
        # 생성된 객체에 대한 계산값 출력
        inCoin.culc(self.cupCount)
    
if __name__ == '__main__':
    Machine().showData()
