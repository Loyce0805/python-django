# 두 개의 가전제품 클래스의 부모 클래스를 만들고 메소드를 오버라이드 하길 기대!

class ElecProduct:
    volume = 0
    
    def volumeControl(self, volume):
        pass
    
class ElectTv(ElecProduct):
    def volumeControl(self, volume):         # 오버라이딩이 옵션. 강요X
        self.volume += volume
        print('TV 소리 크기 :  ', self.volume)
    
class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        vol = volume
        self.volume += vol
        print('라디오 소리 크기 :  ', self.volume)
        
    def showProduct(self):
        print('라디오 만세')
        
tv = ElectTv()
tv.volumeControl(5)
tv.volumeControl(-2)
print()
radio = ElecRadio()
radio.volumeControl(7)
radio.showProduct()

print('다형성 ----')
product = tv
product.volumeControl(10)
product = radio
product.volumeControl(10)

        
        
        