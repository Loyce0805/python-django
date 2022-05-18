'''
Created on 2022. 5. 12.
'''
# [XGBoost 문제] 
# kaggle.com이 제공하는 'glass datasets'
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.
# RI    Na    Mg    Al    Si    K    Ca    Ba    Fe    
#  Type                          ...
# glass.csv 파일을 읽어 분류 작업을 수행하시오.

import numpy as np
import pandas as pd
import xgboost as xgb
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics._classification import classification_report
from xgboost import plot_importance
import matplotlib.pyplot as plt

plt.rc('font', family="malgun gothic")

print(xgb.__version__)

data = pd.read_csv('../testdata/glass.csv')
pd.set_option('display.max_columns', None)
print(data['Type'].unique())
# print(data.head(10), data.shape) # (214, 10)
# print(data.info())
# print(data.describe)
# print(data.columns)
# print(data.isnull().sum())
x_feature = data.drop(['Type'], axis = 1)
y_label = data['Type']
from sklearn import preprocessing
# lab = LabelEncoder()
# y_label = pd.Series(lab.fit_transform(y_label))
y_label = preprocessing.LabelEncoder().fit(y_label).transform(y_label)
# print(x_feature)
# print(y_label)
x_train, x_test, y_train, y_test = train_test_split(x_feature, y_label, test_size=0.2, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (171, 9) (43, 9) (171,) (43,)

xgbmodel = xgb.XGBClassifier(boost='gbtree', max_depth = 3, n_estimators=500, random_state=1).fit(x_train, y_train)
pred = xgbmodel.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10])

from sklearn.metrics import accuracy_score
print('분류 정확도 : ', accuracy_score(y_test, pred))
print('분류 보고서 : ', classification_report(y_test, pred))

# 시각화
fig, ax = plt.subplots(figsize = (10, 12))
plot_importance(xgbmodel, ax = ax)
plt.show()