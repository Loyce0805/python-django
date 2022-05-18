'''
Created on 2022. 5. 12.
'''
# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# dataset은 winequality-red.csv 
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv
# Input variables (based on physicochemical tests):
#  1 - fixed acidity
#  2 - volatile acidity
#  3 - citric acid
#  4 - residual sugar
#  5 - chlorides
#  6 - free sulfur dioxide
#  7 - total sulfur dioxide
#  8 - density
#  9 - pH
#  10 - sulphates
#  11 - alcohol
#  Output variable (based on sensory data):
#  12 - quality (score between 0 and 10)

import pandas as pd

df = pd.read_csv('../testdata/winequality-red.csv')
pd.set_option('display.max_columns', 12)
# print(df.head(3))
# print(df.describe())
# print(df.info())
# print(df.isnull().sum()) # 만약 있다면 df['column명'].fillna로 평균이나 0 또는 제거하거나 임의 값으로 대체하기

# 만약 문자열의 데이터가 있다면 숫자로 변경해줘야 한다.
# sklearn의 preprocessing을 이용하여 labelencoding해주기

from sklearn.model_selection import train_test_split
feature_df = df.drop(['quality'], axis = 1)
label_df = df['quality']
# print(feature_df.shape)
# print(label_df)

x_train, x_test, y_train, y_test = train_test_split(feature_df, label_df, test_size = 0.2, random_state = 1)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

logmodel = LogisticRegression(solver = 'lbfgs', max_iter = 10000).fit(x_train, y_train)
decmodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier().fit(x_train, y_train)

logpredict = logmodel.predict(x_test)
print('log acc : {0:.5f}'.format(accuracy_score(y_test, logpredict)))
decpredict = decmodel.predict(x_test)
print('dec acc : {0:.5f}'.format(accuracy_score(y_test, decpredict)))
rfpredict = rfmodel.predict(x_test)
print('rf acc : {0:.5f}'.format(accuracy_score(y_test, rfpredict)))

print('특성(변수) 중요도 :\n{}'.format(rfmodel.feature_importances_))

import matplotlib.pyplot as plt
import numpy as np
def plot_feature_importances(model):   # 특성 중요도 시각화
    n_features = feature_df.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), feature_df.columns)
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1, n_features)
    plt.show()
    plt.close()
plot_feature_importances(rfmodel)

print('\nGridSearchCV ----')
from sklearn.model_selection import GridSearchCV

params = {'max_depth':[2,3,5,10,15], 'min_samples_split':[2,3,5], 'min_samples_leaf':[1,5,8]}

grid_clf = GridSearchCV(rfmodel, param_grid = params, scoring='accuracy', cv=5)
grid_clf.fit(x_train, y_train)
print(grid_clf.best_params_)
print(grid_clf.best_score_)
best_clf = grid_clf.best_estimator_
bestpredict = best_clf.predict(x_test)
print('rf acc : {0:.5f}'.format(accuracy_score(y_test,bestpredict)))





