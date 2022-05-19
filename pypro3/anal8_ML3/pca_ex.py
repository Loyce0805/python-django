'''
Created on 2022. 5. 17. 주성분분석(PCA)
'''
# PCA(주성분 분석) : 원본 데이터의 feature 갯수에 비해 작은 주성분으로 원본 데이터의 총 변동성(variance)을 대부분 설명할 수 있는 분석기법
# 중요한 칼람만 뽑는게 feature selection. 여기서는 feature extension


import numpy as np
import pandas as pd

x1 = [95, 91, 66, 94, 68]
x2 = [56, 27, 25, 1, 9]
x3 = [57, 34, 9, 79, 4]
x = np.stack((x1,x2,x3), axis = 0)
print(x)

print('표준화 ----') # 표준화 정규화를 통해 모델 성능이 좋아진다.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_std = scaler.fit_transform(x)
print(x_std[:3])
print(scaler.inverse_transform(x_std))  # 원복을 해줘야 의미가 있다.

print('\nPCA ----------')
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
print(pca.fit_transform(x_std))
print(pca.inverse_transform(pca.fit_transform(x_std)))

print(scaler.inverse_transform(pca.inverse_transform(pca.fit_transform(x_std))))

print('--wine dataset으로 분류 모델(Randomforest)---------')

from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics
from sklearn.model_selection import train_test_split
import pandas as pd

datas = pd.read_csv("../testdata/wine.csv", header = None)
print(datas.head(3))
x = np.array(datas.iloc[:, 0:12])   # matrix
y = np.array(datas.iloc[:, 12])     # vector
print(x[:2])
print(y[:2], set(y))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 1)
model = RandomForestClassifier(n_estimators = 100, criterion='entropy').fit(x_train, y_train)
pred = model.predict(x_test)
print('acc : ', sklearn.metrics.accuracy_score(y_test, pred))

print('주성분 분석 후 feature의 수를 줄여 Randomforest 진행 ---')
pca = PCA(n_components = 3)
print(x[:2])
print(pca.fit_transform(x)[:2])  # 12개 전체로 1개의 feature를 만든거다. 앞에꺼부터 나눠서 만든거 아님.

x_pca = pca.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x_pca, y, test_size = 0.25, random_state = 1)
model2 = RandomForestClassifier(n_estimators = 100, criterion='entropy').fit(x_train, y_train)
pred2 = model2.predict(x_test)
print('acc2 : ', sklearn.metrics.accuracy_score(y_test, pred2))



