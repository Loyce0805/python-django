# 사용자 정의 모듈 작성 및 읽기
print('작업을 하다가 외부모듈 읽기')
print(dir())

list1 = [1, 3]
list2 = [2, 4]

import pack2.mymod1
pack2.mymod1.listHap(list1, list2)
# print(dir())

def listTot(*ar):
    print(ar)
    
    if __name__ == '__main__':
        print('이 파일이 메인이야~~')     #어디서 실행했느냐가 메인 응용 프로그램이 시작되는 파일에 임의적으로 이걸 적어줘서 가독성을 높인다. 이게 메인파일이라는걸 알려줌.
        

listTot(list1, list2)

print()
from pack2.mymod1 import kbs
kbs()

from pack2.mymod1 import mbc, price
mbc()
print('price : ', price)

print()
import other.mymod2
print(other.mymod2.Hap(5, 3))

from other.mymod2 import Cha
print(Cha(5, 3))

import mymod3                             # 아나콘다 3의 lip에다 모듈을 넣어놓으면 path가 이미 걸려있어서 패키지명 앞에 안붙여도 
print(mymod3.Gop(5, 3))              #PyDev interpreters Python interpreter -> 아래에서 libraries에 경로 있음 이왕이면 site-packages에다가 넣자

from mymod3 import Nanugi
print(Nanugi(5, 3))






