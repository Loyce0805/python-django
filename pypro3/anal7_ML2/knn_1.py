''' 
Created on 2022. 5. 16.
'''
# KNN : 데이터로부터 거리가 가까운 k개의 다른 데이터의 레이블을 참조하여 분류를 진행.
#       (데이터 개수가 적을 때 분류가 잘 된다.)

train = [
    [5, 3, 2],
    [1, 3, 5],
    [4, 5, 7]
]

label = [0, 1, 1]

# 데이터 분포도 보기
import matplotlib.pyplot as plt
# plt.xlim([-1, 3])
# plt.ylim([0, 10])
# plt.plot(train, 'o')
# plt.show()

from sklearn.neighbors import KNeighborsClassifier
kmodel = KNeighborsClassifier(n_neighbors=3, weights='distance')
kmodel.fit(train, label)
pred = kmodel.predict(train)
print('pred : ', pred)  #[0 1 1]

print('- - - - - - - - - - - - - - - - - - - - - - - -')
from sklearn.datasets import load_breast_cancer
plt.rc('font', family='malgun gothic')
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, 
                                                    stratify = cancer.target,    # sampling 할 때 편향되는 걸 방지하기 위해서
                                                    random_state = 66)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(426, 30) (143, 30) (426,) (143,)

train_acc = []
test_acc = []
neighbors_set = range(1, 11)

for n_nei in neighbors_set:
    # classification model 만들기
    clf = KNeighborsClassifier(n_neighbors=n_nei)
    clf.fit(x_train, y_train)
    train_acc.append(clf.score(x_train, y_train))   # train 데이터의 정확도
    test_acc.append(clf.score(x_test, y_test))      # test 데이터의 정확도

import numpy as np
print(train_acc[:5])
print(test_acc[:5])
print('train 분류 정확도 평균 : ', np.mean(train_acc)) # 0.954225352112676
print('test 분류 정확도 평균 : ', np.mean(test_acc))   # 0.918881118881119

# train정확도와 test정확도의 접점 시각화
plt.plot(neighbors_set, train_acc, label='훈련 정확도')
plt.plot(neighbors_set, test_acc, label='검증 정확도')
plt.xlabel('k값')
plt.ylabel('정확도')
plt.legend()
plt.show()