'''
Created on 2022. 4. 19. 12시부터 시작

'''
# 함수
from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[1.4, np.nan], [7, 4.5], [np.NaN, np.NAN], [0.5, -1]])
df.columns = ['one', 'two']   # column명을 나중에 추가
print(df)
print(df.drop(1))  # drop으로 1행 날림
print(df.isnull())   # NaN탐지(null 값이 있으면 True로 나온다.)
print(df.notnull())   # Nan탐지(Null 값이 아닌 것만 True로 나온다.)
print(df.dropna())    # NaN이 있는 행 제거  (now='any') 와 동일
print(df.dropna(how='any'))    # 열 값 중 하나라도 NaN이 있으면 그 행을 삭제
print(df.dropna(how='all'))    # 열 값 모두가 NaN인 경우 그 행 삭제
print(df.dropna(subset=['one']))    # column명이 one인 column에 NaN 값이 있으면 해당 행 삭제
print(df.dropna(axis='rows'))    # NaN이 포함된 행 삭제
print(df.dropna(axis='columns')) # NaN이 포함된 열 삭제

print()
print(df.fillna(0))    # NaN 값을 0으로 채워준다. 평균 또는 대표값으로도 채울 수 있다.

print('-----')
print(df)
print(df.sum())   # 열의 합
print(df.sum(axis=0))  # 열의 합

print(df.mean(axis=1))   # 행의 평균

print()
print(df.idxmax())   # 가장 큰 값의 index를 반환
print(df.max())   # 가장 큰 값을 반환  # axis=0 들어간것과 똑같다. 
print()
print(df.describe())  # 요약 통계량  R에서는 summary와 똑같다.
print(df.info())   # 중요

words = Series(['봄', '여름', '봄'])
print(words.describe())
# words.info() # AttributeError: 'Series' object has no attribute 'info'



