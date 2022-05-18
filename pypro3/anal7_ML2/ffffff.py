# titanic dataset으로 LogisticRegression, DecisionTreeClassifier, RandomForestClassifier 처리

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
print(df.head(2), df.shape)
df.drop(columns = ['PassengerId','Name','Ticket'], inplace = True)
pd.set_option('display.max_columns', None)
print(df.describe())
print(df.info())
print(df.isnull().sum()) #Age:177, Cabin:687, Embarked:2

# Null 처리 : 0 또는 평균 또는 제거 또는 임의의 값으로 대체
df['Age'].fillna(df['Age'].mean(), inplace = True)
df['Cabin'].fillna('N', inplace = True)
df['Embarked'].fillna('N', inplace = True)
print(df.isnull().sum())
print(df.head(2),df.shape) # (891, 9)

print()
# object type : Sex, Cabin, Embarked 얘네들의 상태를 별도 확인
print('Sex:', df['Sex'].value_counts())
print('Cabin:', df['Cabin'].value_counts())
df['Cabin'] = df['Cabin'].str[:1]
print('Embarked:', df['Embarked'].value_counts())
print(df.head(5))

# 성별이 생존확률에 어떤 영향을 가했는가?
print(df.groupby(['Sex','Survived'])['Survived'].count())
# 승객은 남자가 많지만 생존자는 여자가 많음을 알 수 있다.
print('여자 생존율:',233 / (81 + 233)) #0.742
print('남자 생존율:',109 / (468 + 109)) #0.188

'''# 시각화 : 성별 생존확률
sns.barplot(x='Sex', y='Survived', data=df, ci=95) #ci는 신뢰구간
plt.show()

# 시각화 : 성별 생존확률
sns.barplot(x='Pclass', y='Survived', hue = 'Sex', data=df, ci=95) #ci는 신뢰구간
plt.show()'''

# 나이별 생존 확률
# print(df['Age])
def age_category_func(age):
    msg=''
    if age <= -1: msg = 'unknown'
    elif age <= 5: msg = 'baby'
    elif age <= 18: msg = 'teenager'
    elif age <= 65: msg = 'adult'
    else: msg= 'elder' 
    return msg

df['Age_category'] = df['Age'].apply(lambda a: age_category_func(a))
#print(df)

'''# 시각화 : 성별 나이별 생존확률
sns.barplot(x='Age_category', y='Survived', hue='Sex',
             order=['unknown','baby','teenager','adult'], data=df, ci=95) #ci는 신뢰구간
plt.show()'''

del df['Age_category']


# Dummy 변수 : 문자열 -> 숫자 (범주형)
from sklearn import preprocessing

def label_incode_func(datas):
    cols = ['Cabin', 'Sex', 'Embarked']
    for c in cols:
        la = preprocessing.LabelEncoder().fit(datas[c])
        datas[c] = la.transform(datas[c])
    return datas

df = label_incode_func(df)
print(df.head(),type(df))
print(df['Cabin'].unique()) # 몇개로 나누어졌는지 확인 [7 2 4 6 3 0 1 5 8]
print(df['Sex'].unique()) # [1 0]
print(df['Embarked'].unique()) #[3 0 2 1]

# 데이터 가공
print()
from sklearn.model_selection import train_test_split
feature_df = df.drop(['Survived'], axis='columns')
label_df = df['Survived']

x_train, x_test, y_train, y_test = train_test_split(feature_df, label_df, test_size=0.2, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(712, 9) (179, 9) (712,) (179,)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

logmodel = LogisticRegression(solver = 'lbfgs', max_iter = 500).fit(x_train, y_train)
demodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier().fit(x_train, y_train)

logpredict = logmodel.predict(x_test)
print('LogisticRegression acc : {0:.5f}'.format(accuracy_score(y_test, logpredict)))
depredict = demodel.predict(x_test)
print('DecisionTreeClassifier acc : {0:.5f}'.format(accuracy_score(y_test, depredict)))
rfpredict = rfmodel.predict(x_test)
print('RandomForestClassifier acc : {0:.5f}'.format(accuracy_score(y_test, rfpredict)))

print('\n GridSearchCV----')
from sklearn.model_selection import GridSearchCV

# max_depth
# min_samples_split : 노드 분할 최소 샘플 수
# min_samples_leaf : 리프 노드 최소 샘플 수
# ...
params = {'max_depth':[2,3,5,10,15], 'min_samples_split':[2,3,5], 'min_samples_leaf':[1,5,8]}

# DecisionTreeClassifier
grid_clf = GridSearchCV(demodel, param_grid = params, scoring = 'accuracy', cv =5)
grid_clf.fit(x_train, y_train)
print(grid_clf.best_params_)
print(grid_clf.best_score_)
best_clf = grid_clf.best_estimator_ #최적의 모델 얻기
bestPredict = best_clf.predict(x_test)
print('DecisionTreeClassifier acc : {0:.5f}'.format(accuracy_score(y_test, bestPredict))) #0.80447

print('-------------')
#RandomForestClassifier
grid_clf2 = GridSearchCV(rfmodel, param_grid = params, scoring = 'accuracy', cv =5)
grid_clf2.fit(x_train, y_train)
print(grid_clf2.best_params_)
print(grid_clf2.best_score_)
best_clf2 = grid_clf2.best_estimator_ #최적의 모델 얻기
bestPredict2 = best_clf2.predict(x_test)
print('DecisionTreeClassifier acc : {0:.5f}'.format(accuracy_score(y_test, bestPredict2))) #0.78212