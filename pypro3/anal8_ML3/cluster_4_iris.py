'''
Created on 2022. 5. 16.
'''
# iris dataset으로 분류모델을 작성. 지도학습(K-NN), 비지도학습(K-Means)

from sklearn.datasets import load_iris

iris = load_iris()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size = 0.25, random_state = 42)

print(x_train[:2])
print(y_train[:2])

print('지도학습 : K최근접이웃알고리즘')
from sklearn.neighbors import KNeighborsClassifier
knnModel = KNeighborsClassifier(n_neighbors = 3)
knnModel.fit(x_train, y_train) # feature, label 주니까 지도학습

predict_label = knnModel.predict(x_test)
print('예측값 : ', predict_label[:3])

from sklearn.metrics import accuracy_score
print('acc : ', accuracy_score(y_test, predict_label))

print()
print('비지도학습 : K평균 군집 알고리즘')
from sklearn.cluster import KMeans
kmeansModel = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
kmeansModel.fit(x_train)  # label이 없음

print(kmeansModel.labels_)
print('0 cluster : ', y_train[kmeansModel.labels_ == 0])
print('0 cluster : ', y_train[kmeansModel.labels_ == 1])
print('0 cluster : ', y_train[kmeansModel.labels_ == 2])

print()
import numpy as np
new_input = np.array([[1.1, 2.3, 1.5, 1.5]])
clu_pred = kmeansModel.predict(new_input)
print(clu_pred)
