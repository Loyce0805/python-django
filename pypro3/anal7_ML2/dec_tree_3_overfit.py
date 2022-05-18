'''
Created on 2022. 5. 10. 과적합(overfitting)방지
'''
# scikit-learn 모듈(라이브러리)이 지원하는 과적합 방지 함수(메소드)의 이해
# iris dataset

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score # 분류 정확도


iris = load_iris()
print(iris.keys())
train_data = iris.data
train_label = iris.target   # 종속변수 : class, label 독립변수 : feature
print(train_data[:3])
print(train_label[:3])

# 분류 모델
dt_clf = DecisionTreeClassifier()  # sklearn의 다른 분류모델을 써도 됨.
dt_clf.fit(train_data, train_label)
pred = dt_clf.predict(train_data)
print('예측값 : ', pred)
print('실제값 : ', train_label)
print('분류 정확도 : ', accuracy_score(train_label, pred))   # 꼭 (실제값, 예측값) 순서로 집어넣어야함.
# 분류 정확도(accuracy)가 100%. 찝찝하다. : 과적합 문제 발생
# 모의고사 문제와 본고사 문제가 똑같은거랑 마찬가지.
# 모델의 포용성을 위해 과적합 문제를 해결하는 방안을 찾아야 한다.

# ※참고 : 과적합 방지로 데이터 수를 늘릴 수 있다.

print('--- 과적합 방지 목적 처리 1 --') # 과적합을 방지하는 것을 목적으로 처리하기.
# train / test split 해보자. (보통 7 : 3, or 8 : 2)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, 
                                                    test_size = 0.3, random_state = 121)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (105, 4) (45, 4) (105,) (45,)
dt_clf.fit(x_train, y_train)   # 모델학습은 train data
pred2 = dt_clf.predict(x_test) # 모델 평가는 test data
print('예측값 : ', pred2)
print('실제값 : ', y_test)
print('분류 정확도 : ', accuracy_score(y_test, pred2))   # 0.9555 데이터에 대한 분류 데이터가 95~6% 맞춘다. 약 4~5%정도는 틀릴 수도 있다. 약간의 포용성을 준거.
# 추론통계는 모든 환경에서 100%가 될 수 없다. 100%를 원하지 않는다.


print('\n--- 과적합 방지 목적 처리 2 ---')
# 교차검증 : train / test split을 했으나 여전히 과적합일 때 -> 교차검증을 해보자.(k-fold)
# 모델 학습 시 데이터의 편중을 방지하고자 학습 데이터를 쪼개서 학습과 평가를 병행하는 것. (train 도중에 train데이터를 쪼갠다.)
# 본고사를 치르기 전에 모의고사를 여러 번 보는 것
# 교차검증 중 가장 보편적인 방법으로 k-fold가 있다.
from sklearn.model_selection import KFold # 데이터의 양이 많지 않을 때 KFold. train 했는데 과적합 나왔거나 그냥 하거나.
import numpy as np
features = iris.data # 독립
label = iris.target  # 종속
dt_clf = DecisionTreeClassifier(criterion = 'entropy', random_state = 123)
kfold = KFold(n_splits = 5) # 5겹. 얼마주는지는 자기 마음이다.
cv_acc = [] # 학습할때마다 학습과 검정을 같이 하는데 그 때마다 accuracy 체크해서 담아주기.
print('iris shape : ', features.shape) # (150, 4) target이 빠져서
# 전체 행 수가 150, 학습데이터: 4/5(120개(train)), 검증데이터: 1/5(30개(test))로 분할해 가며 학습을 진행. 하나를 validation 나머지를 train 함으로서 accuracy 확인.

n_iter = 0
for train_index, test_index in kfold.split(features):
    '''
    print('n_iter : ', n_iter)
    print('train_index : ', len(train_index))
    print('test_index : ', len(test_index))
    n_iter += 1
    '''
    xtrain, xtest = features[train_index], features[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    n_iter += 1
    
    # 반복할 때 마다 정확도 측정
    acc = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수 : {0}, 교차검증 정확도 : {1}, 학습데이터 크기 : {2}, 학습데이터 크기 : {3}'.format(n_iter, acc, train_size, test_size))
    print('반복수 : {0}, validation data index : {1} '.format(n_iter, test_index))
    cv_acc.append(acc)

print('평균 검증 정확도 : ', np.mean(cv_acc))  # 0.91999


# KFold는 편향된 데이터에서는 잘 안나올 수 있다.
print('\n--- 과적합 방지 목적 처리 2-1 ---')
# 대출 사기 데이터인 경우 정상과 사기 데이터가 비율적으로 편향된 경우가 많다. 이메일, 강우 여부
# 위와 같은 불균형 데이터인 경우는 KFold 보다는 StratifiedKFold를 사용한다.
from sklearn.model_selection import StratifiedKFold
skfold = StratifiedKFold(n_splits = 5)
cv_acc = []
n_iter = 0

for train_index, test_index in skfold.split(features, label):  # kfold를 skfold로, features뒤에 label 추가
    xtrain, xtest = features[train_index], features[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    n_iter += 1
    
    # 반복할 때 마다 정확도 측정
    acc = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수 : {0}, 교차검증 정확도 : {1}, 학습데이터 크기 : {2}, 학습데이터 크기 : {3}'.format(n_iter, acc, train_size, test_size))
    print('반복수 : {0}, validation data index : {1} '.format(n_iter, test_index))
    cv_acc.append(acc)

print('평균 검증 정확도 : ', np.mean(cv_acc))  # 0.9534  # 하지만 iris는 편향되지 않은 데이터라 skfold랑은 안맞는다. 편향된 데이터에 주로 사용.

print('\n--- 과적합 방지 목적 처리 2-2 ---')
# scikitlearn의 KFold대신 cross_val_score를 이용하면 교차검증을 쉽게 할 수 있다.
from sklearn.model_selection import cross_val_score

data = iris.data
label = iris.target

score = cross_val_score(dt_clf, data, label, scoring='accuracy', cv = 5) # estimator는 모델(dt_clf(DecisionTreeClassifier())
print('교차 검증별 정확도 : ', np.round(score, 3))
print('평균 검증정확도 : ', np.round(np.mean(score), 3)) # train validation을 쪼갠거다. test는 따로 있다.


print('\n--- 과적합 방지 목적 처리 3 ---')
# GridSearchCV : 교차검증과 최적의 속성(하이퍼 파라미터)을 위한 튜닝을 한 번에 처리
from sklearn.model_selection import GridSearchCV # ★이거 중요한 녀석이라고 한다.

# 여러 개의 속성 값 중 max_depth, min_samples_split 에 대해서 최적의 값 찾기
parameters = {'max_depth':[1, 2, 3], 'min_samples_split':[2, 3]}

grid_tree = GridSearchCV(dt_clf, param_grid = parameters, cv = 3, refit = True) # refit은 재학습을 시키는 것. kford를 이해해야 cv를 안다.
grid_tree.fit(x_train, y_train)

import pandas as pd
scores_df = pd.DataFrame(grid_tree.cv_results_) # results 뒤에 _(언더바)를 하나 붙여줘야한다.
pd.set_option('max_columns', None) # 모든 칼럼을 다 보는거
print(scores_df)

print('GridSearchCV 최적 파라미터 : ', grid_tree.best_params_)
print('GridSearchCV 최고 정확도 : ', grid_tree.best_score_)
# dt_clf = DecisionTreeClassifier(..., max_depth = 3, min_samples_split = 2, ...)

# GridSearchCV가 제공하는 최적의 파라미터로 모델(DecisionTreeClassifier) 생성
estimator = grid_tree.best_estimator_
print(estimator)
pred = estimator.predict(x_test)  # train으로 학습했으니 test로 검정
print(pred)
print('모델 성능(정확도) : ', accuracy_score(y_test, pred))
# 과적합 방지 목적도 있지만, 최적의 파라미터를 얻을 수 있다. 굉장히 중요함

