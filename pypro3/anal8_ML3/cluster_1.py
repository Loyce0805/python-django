'''
Created on 2022. 5. 16. 군집분석(Clustering) 비지도 학습
'''
# 군집분석(Clusterung) : 비지도학습
# 계층적 군집 분석 : 특정 알고리즘에 의해 데이터들을 연결하여 계층적으로 군집(클러스터)을 형성
# 응집형 : 자료 하나를 군집으로 간주하고 가까운 군집끼리 연결해가는 방법(상향식)
# 분리형 : 전체 자료를 하나의 큰 군집으로 간주하고, 유의한 부분을 분리해가는 방법(하향식)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

np.random.seed(123)
var = ['X', 'Y']
labels = ['점0','점1','점2','점3','점4']
x = np.random.random_sample([5, 2]) * 10
df = pd.DataFrame(x, columns = var, index = labels)
print(df)

# plt.scatter(x[:, 0], x[:, 1], s=50, c='blue', marker='o')
# plt.grid(True)
# plt.show()

from scipy.spatial.distance import pdist, squareform
dist_vec = pdist(df, metric = 'euclidean') # 유클리디안 거리계산법이 기본
print(dist_vec)

# 거리벡터를 사각형 형식으로 출력
row_dist = pd.DataFrame(squareform(dist_vec), columns=labels, index=labels)
print(row_dist)

# 계층적 군집분석 : 특정 알고리즘에 의해 데이터들을 연결하여 계층적으로 군집(클러스터)을 형성
from scipy.cluster.hierarchy import linkage
row_cluster = linkage(dist_vec, method = 'ward') # single(최단연결법), average(완결연결법), ...

df = pd.DataFrame(row_cluster, columns = ['클러스터id_1','클러스터id_2', '거리', '클러스터 멤버수'])
print(df)

from scipy.cluster.hierarchy import dendrogram
row_dend = dendrogram(row_cluster, labels = labels)
plt.tight_layout()
plt.ylabel('유클리드 거리')
plt.show()

