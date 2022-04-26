from pandas import DataFrame
from pandas import Series
import numpy as np

# pandas 문제 1)
#   a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
#      np.random.randn(9, 4)
#   b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
#   c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용

df = DataFrame(np.random.randn(9,4))
df.columns=['no1', 'no2', 'no3', 'no4']
print(df)
print()
print(df.mean(axis=0))


df=DataFrame(np.arange(4).reshape(4,1), index=['a','b','c','d'], columns=['numbers'])
print(df)
val = Series([10,20,30,40], index=['a','b','c','d'])
df['numbers'] = val
print(df)