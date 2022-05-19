'''
Created on 2022. 5. 16. 계층적 군집분석 
'''
# 군집화
# iris_dataset

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(iris_df.head(3))

from scipy.spatial.distance import pdist, squareform

# dist_vec = pdist(iris_df.loc[0:4, ['sepal length (cm)', 'sepal width (cm)']], metric = 'euclidean')
dist_vec = pdist(iris_df.loc[:, ['sepal length (cm)', 'sepal width (cm)']], metric = 'euclidean')
print(dist_vec)
row_dist = pd.DataFrame(squareform(dist_vec))
print(row_dist)

print()
from scipy.cluster.hierarchy import linkage, dendrogram
row_cluster = linkage(dist_vec, method = 'complete')
print('row_cluster:', row_cluster)
df = pd.DataFrame(row_cluster, columns = ['id_1','id_2', '거리', 'cluster member'])
print(df)
print()
row_dend = dendrogram(row_cluster)
plt.tight_layout()
plt.ylabel('euclidean dist')
plt.show()