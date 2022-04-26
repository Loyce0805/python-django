# Pandas : 고 수준의 자료구조(Series, DataFame)를 지원. 
# 데이터분석용 자료 관리를 위한 다양한 함수 제공
# 축약 연산, SQL 처리, 시계열 데이터 처리, 시각화...

import pandas as pd
from pandas import Series
import numpy as np


# Series : 일련의 데이터를 담을 수 있는 1차원 배열과 비슷한 자료 구조를 가지며, 색인을 지원함.

obj = Series([3, 7, -5, 4])
# list, tuple type 가능. TypeError : 'set type is unordered
print(obj, type(obj))

obj2 = Series([3, 7, -5, 4], index = ['a', 'b', 'c', 'd'])
# 생성시 색인을 지정
print(sum(obj2), obj2.sum(), np.sum(obj2))    #python의 함수, pandas의 함수, numpy의 함수 pandas를 권장
print(obj2.values)    # [ 3 7 -5 4]
print(obj2.index)

# 인덱싱, 슬라이싱
print(obj2)
print(obj2[1])
print(obj2['b'])
print(obj2[['b']])

print(obj2[['a', 'b']])
print(obj2['a' : 'b'])

print(obj2[2])
print(obj2[1:4])
print(obj2[[2, 1]])
print(obj2 > 1)
print('a' in obj2)

print('----------------------')
# dict type으로 Series 객체 생성
names = {'mouse' : 5000, 'keyboard':25000, 'monitor':'550000'}
print(names)
obj3 = Series(names)
print(obj3)
obj3.index = ['마우스', '키보드', '모니터']  # index명을 바꿈
print(obj3)
print(obj3['마우스'])
print()
obj3.name = '상품가격'    # Series에 name을 붙일 수 있다.   Name: 상품가격, dtype: object
print(obj3)

print('\n~~~DataFarame~~~~~~~~~~~~~~~~~~~~~~~')
# DataFrame : 표 모양(2차원)의 자료구조로 여러개의 칼럼(열)을 갖는다.
from pandas import DataFrame
df = DataFrame(obj3)
print(df, type(df))   # <class 'pandas.core.frame.DataFrame'>

data = {
    'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
    'nai':[23, 25, 33, 30, 35],
    }
print(data, type(data))

frame = DataFrame(data)
print(frame, type(frame))

print(frame['irum'], type(frame['irum']))
print(frame.irum)
print()
print(DataFrame(data, columns=['juso', 'irum', 'nai']))
print()
frame2 = DataFrame(data, columns=['irum', 'nai', 'juso', 'tel'], index = ['a', 'b', 'c', 'd', 'e'])
# frame2.columns = ['irum', 'nai', 'juso', 'tel'])
# frame2.index = ['a', 'b', 'c', 'd', 'e']
print(frame2)

frame2['tel'] = "111-1111" # 모든 행에 적용
print(frame2)

val = Series(['222-2222', '333-3233', '444-4444'], index = ['b', 'c', 'e'])
print(val)
frame2['tel'] = val
print(frame2)

print(frame2.T)   # transpose 전치 - 행열의 위치를 변경

print(frame2.values)   # values를 추출하면 2차원(matrix가 됨.) 중첩리스트.
print()
print(frame2.values[0,1])   # 23만 나옴
print()
print(frame2.values[0:2])   # 0~1번째 values의 값 다 보여줌

print()
frame3 = frame2.drop('d')   # 행 삭제  axis = 0
# frame3 = frame2.drop('d', axis = 0)
print(frame3)

frame4 = frame2.drop('tel', axis = 1)  # 그냥 'tel'만 쓰면 행에서 찾기 떄문에 오류뜬다 axis = 1 로 열 삭제를 표현해야함.
print(frame4)

print()
print(frame2)
print(frame2.sort_index(axis=0, ascending=False)) # ascending=False로 행단위로 거꾸로 바꿔버림
print(frame2.sort_index(axis=1, ascending=True))  # 열단위   sort?
print(frame2.rank(axis = 0))   # 순서를 보여준다.

print()
print(frame2['juso'].value_counts())

print()
data = {
    'juso' : ['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon' : [23, 25, 15]
    }
fr = DataFrame(data)
print(fr)

result1 = Series([ju.split()[0] for ju in fr.juso])
print(result1.values)
print(result1.value_counts())

result2 = Series([ju.split()[1] for ju in fr.juso])
print(result2)