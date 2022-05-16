'''
Created on 2022. 5. 2. 상관관계 분석
'''
# 상관관계 분석
# 두 개 이상의 확률변수(연속형) 간에 어떤 관계가 있는지 분석하는 것
# 공분산을 표준화 한 것을 피어슨상관계수(r)라고 한다.
# 공분산은 x가 증가할 때 y도 감소한다는 것을 알려준다.
# 상관계수를 사용하면 공분산의 한계를 극복할 수 있다.
# 변수 간의 힘의 방향뿐만 아니라 힘의 크기까지 구체적으로 표현할 수 있다.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

df = pd.DataFrame({'id1':(1,2,3,4,5), 'id2':(2,3,-1,7,9)})
print(df)
print(df.cov())     # 공분산. covariance 하나에 대해서만 평균에서 얼만큼 떨어진지 알고 싶으면 분산을 사용한다.
print(df.corr())    # 상관계수. 피어슨 상관계수가 일반적.(corr) ★상관계수 수식정도는 알고 있자. 개념을 아는게 좋다.

# plt.scatter(df.id1, df.id2)
# plt.show()

print()
# 파일 자료를 읽어서 상관분석
data = pd.read_csv("../testdata/drinking_water.csv")
print(data.head(3), len(data))
print(data.info())  # 요약구조
print(data.describe()) # 요약통계량

# 공분산
print('공분산')
print(np.cov(data.친밀도, data.적절성))   # numpy는 두 개씩밖에 못 본다
print(np.cov(data.친밀도, data.만족도))
print(data.cov()) # pandas의 dataframe으로 보면 numpy와 다르게 한번에 다 볼 수 있다.
# 상관계수
print('상관계수')
print(np.corrcoef(data.친밀도, data.적절성))
print(np.corrcoef(data.친밀도, data.만족도))
print(data.corr())  # pandas의 dataframe. method 안 써주면 'pearson'이 디폴트 값이다.
print(data.corr(method='pearson'))  # 피어슨 상관계수를 구한다. 정규성, 연속형(등간, 비율 척도)
# print(data.corr(method='spearman')) # 서열척도, 비선형(정규성을 따르지 않는다.)
# print(data.corr(method='kendall'))  # 서열척도, 비선형(정규성을 따르지 않는다.)

print()
print('--만족도의 상관계수만 보기--(한 가지만 따로 보기)')
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))


print()
#시각화
print('----- 시각화 -----')
# data.plot(kind = 'scatter', x='만족도', y='적절성') # 산점도 확인
# plt.show()
#
# from pandas.plotting import scatter_matrix
# attr = ['친밀도', '적절성', '만족도']
# scatter_matrix(data[attr]) # scatter_marix를 통해 산점도와 히스토그램을 같이 보여준다.
# plt.show()

# hitmap
import seaborn as sns
# sns.heatmap(data.corr()) # 상관계수를 히트맵으로. 흐릴수록 상관관계가 강한 것.
# plt.show()

''' heatmap에 텍스트 표시 추가사항 적용해 보기 '''
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()