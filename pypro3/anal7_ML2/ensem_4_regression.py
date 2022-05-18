'''
Created on 2022. 5. 11.
'''
# sklearn 모듈의 분류 모델의 상당수는 출력결과가 연속형인 예측 처리도 가능
# RandomForest는 대표적 앙상블 배깅 기법.
# 병렬식. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score

boston = load_boston()

dfx = pd.DataFrame(boston.data, columns = boston.feature_names)
dfy = pd.DataFrame(boston.target, columns = ['MEDV'])
df = pd.concat([dfx, dfy], axis = 1) # axis = 1 은 행기준
print(df.head(3), df.shape) # (506, 14)

print(df.corr())

cols = ['MEDV', 'RM', 'LSTAT']
# sns.pairplot(df[cols])
# plt.show()

x = df[['LSTAT']]
y = df['MEDV']

import numpy as np
# 실습1 : DecisionTreeRegressor
model = DecisionTreeRegressor(criterion = 'mse').fit(x, y)
print('predict : ', model.predict(x)[:5])
print('real : ', np.array(y[:5]))
print('결정계수(R2) : ', r2_score(y, model.predict(x))) # 독립변수가 종속변수의 분산을 얼마나 설명할 수 있느냐

print('----------------')
# 실습2 : RandomForestRegressor
model2 = RandomForestRegressor(n_estimators = 1000, criterion = 'mse', random_state = 123).fit(x, y)
print('predict : ', model2.predict(x)[:5])
print('real : ', np.array(y[:5]))
print('결정계수(R2) : ', r2_score(y, model2.predict(x))) # 독립변수가 종속변수의 분산을 얼마나 설명할 수 있느냐
