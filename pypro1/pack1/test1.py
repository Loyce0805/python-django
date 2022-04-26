'''
여러 줄
주석
'''

"""
여러 줄
주석
"""
# 한 줄 주석

print("환영합니다. python 세상")
print('환영합니다. "python" 세상');
a = "안녕" # 객체의 주소를 기억. 참조형 기억 장소
a = '반가워'
a = 10; b = 20.5
c = b   # 주소 치환
print(a, b, c)
print(id(a), id(b), id(c))
a = 10
b = 10
print(a == b, a is b) # == 값 비교 연산자, is 주소 비교 연산자
aa = [10]
bb = [10]
print(aa == bb, aa is bb) # ==는 True, is는 False