# 클래스는 새로운 타입을 만든다.
class Singer:
    title_song = '화이팅 코리아'
    
    def sing(self):
        msg = "노래는 "
        print(msg, self.title_song, '랄라라 ~~~')
        
    def hello(self):
        msg = "안녕하세요~"
        print(msg, "저에요")
    # ...
    
# -------아래 내용은 별도의 모듈을 만들었다고 가정 ----------------
bts = Singer()
bts.hello()
bts.sing()

print()
blackpink = Singer()      #singer 클래스 타입의 생성자를 부르는 것
blackpink.hello()
blackpink.sing()
blackpink.title_song = "마지막처럼"
blackpink.sing()
blackpink.co = 'SM'
print('blackpink 소속사 : ', blackpink.co)

# print('bts 소속사 : ', bts.co)    # sm이라고 소속사를 안정해줘가지고 오류뜸.
bts.sing()    # title 송 없어서 아직 화이팅 코리아

print()
print(id(bts), id(blackpink))
print(type(bts), type(blackpink))


#포함관계와 상속관계로 클래스를 갖다 쓸 수 있음. 