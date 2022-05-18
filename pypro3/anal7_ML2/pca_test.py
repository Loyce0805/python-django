'''
Created on 2022. 5. 13. 주성분 분석(pca)
https://angeloyeo.github.io/2019/07/27/PCA.html
'''
# 주성분 분석(PCA) : 데이터 차원 축소
# 원래 데이터 분산을 최대한 보존하는 새로운 축을 찾고, 그 축에 데이터를 사영(projection) 시키는 방법(직교) 사용

# iris data를 사용해서 차원축소

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.rc('font', family='malgun gothic')
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.data[:2])
n = 10
x = iris.data[:n, :2]
print('차원 축소 전 : ', x, x.shape, type(x))
print(x.T)

"""
# 시각화
plt.plot(x.T, 'o:')
plt.xticks(range(2), ['꽃받침 길이', '꽃받침 폭'])
plt.xlabel('특성의 종류')
plt.ylabel('특성 값')
plt.title('붓꽃 크기 특성')
plt.legend(['표본 {}'.format(i + 1) for i in range(n)])
plt.grid()
plt.show()
"""
"""
# x 축에는 꽃받침 길이, y 축에는 꽃받침 폭으로 산점도 출력
df = pd.DataFrame(x)
ax = sns.scatterplot(df[0], df[1], data=df, marker = 's', s=100, color=['b'])
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.03, '표본{}'.format(i + 1))
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('붓꽃 크기 특성(2차원)')
plt.axis('equal')
plt.show()
"""
"""
# 두 개의 열의 값 패턴이 매우 유사함을 알 수 있다. 그러므로 차원축소 가능. ==> PCA
pca1 = PCA(n_components = 1) # 변환 차원 수 # n_components는 주성분 성분의 갯수. 2개를 1개로 만드는거니까 1을 준다.
x_low = pca1.fit_transform(x) # 비지도 학습이라 x값 하나만 가지고 한다. target은 지정하지 않는다. 특징행렬은 낮은 타원의 근사행렬로 변환.
print('x_low', x_low, ' ', x_low.shape) # (10, 1)

# 차원 축소 값 원복하기.
x2 = pca1.inverse_transform(x_low)
print('원복 값', x2, ' ', x2.shape) # (10, 2)  주성분 분석값 원복 결과 [5.1 3.5] ==> [5.06676112 3.53108532] 근사행렬이기 때문에 같은 값이 아니다.
print('원래 값 : ', x[0, :])
print('주성분 값 : ', x_low[0])
print('원복 값 : ', x2[0, :])


# x 축에는 꽃받침 길이, y 축에는 꽃받침 폭으로 산점도 출력
df = pd.DataFrame(x)
ax = sns.scatterplot(df[0], df[1], data=df, marker = 's', s=100, color=['b'])
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.03, '표본{}'.format(i + 1))
    plt.plot([x[i, 0], x2[i, 0]], [x[i, 1], x2[i, 1]], 'k--')

plt.plot(x2[:, 0],x2[:, 1], 'o-', color='y', markersize = 10)
plt.plot(x2[:, 0].mean(),x2[:, 1].mean(), 'D', color='r', markersize = 10)

plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('붓꽃 크기 특성(2차원)')
plt.axis('equal')
plt.show()
"""

# iris 4개의 열을 두 개로 축소
x = iris.data
print(x[:2])
pca2 = PCA(n_components = 2)
x_low2 = pca2.fit_transform(x)
print('x_low2', x_low2, ' ', x_low2.shape)
print(pca2.explained_variance_ratio_) # 변동성 비율
print('원래 값 : ', x[0, :])
print('주성분 값 : ', x_low2[0]) # 근사행렬로 변환했을 때 원본 값의 0.92461872% 설명함 <- 변동성 비율을 확인함으로써 
x_trans = pca2.inverse_transform(x_low2)
print('원복 값 : ', x_trans[0, :])

print()
iris1 = pd.DataFrame(x, columns=['sepal_length','sepal_width','petal_length','petal_with'])
print(iris1.head(5))
print()
iris2 = pd.DataFrame(x_low2, columns=['var1','var2'])
print(iris2.head(5))
