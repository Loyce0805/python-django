# 완성 제품의 부품 클래스로 핸들을 만듬

class PohamHandle:
    quantity = 0    # 회전량
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
        
    def RightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'        
    
    # ...
        
        
        
        