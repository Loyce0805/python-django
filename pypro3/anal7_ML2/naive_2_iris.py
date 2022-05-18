''' Created on 2022. 5. 9. 6교시 ~ '''
# http://okminseok.blogspot.com/2017/09/ml-xgboost.html
# sklearn 모듈이 지원하는 분류 모델 사용
# 다항분류 : 출력시 softmax 함수를 사용 - 결과가 확률값으로 출력되며 가장 큰값의 인덱스를 분류 범주값으로 적용

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler    #표준화 지원
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

iris = datasets.load_iris()
# print(iris.DESCR)
print(iris.keys())

print()
print(np.corrcoef(iris.data[:, 2], iris.data[:, 3]))    #0.9628

print()
x = iris.data[:, [2, 3]]    # petal.length, petal.width
y = iris.target
print(x[:3])    #[[1.4 0.2],  [1.4 0.2],  [1.3 0.2]]
print(y[:3], set(y))    #[0 0 0], set(y)={0, 1, 2}

print()
# train / test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)     #(105, 2) (45, 2) (105,) (45,)

'''
# 학습 데이터의 크기의 차이가 심하면 스케일링(크기 표준화 또는 정규화)
# 독립변수를 스케일링 하면 모델이 안정성, 수렴 속도 향상, 오버플로우/언더플로우 등의 방지에 효과적이다
print(x_train[:3])
sc = StandardScaler()   #표준화    # 독립변수의 편차가 클 때는 표준화를 하면 분석 결과가 잘 나온다.
sc.fit(x_train) # x_train 데이터를 표준화
sc.fit(x_test)  # x_test 데이터를 표준화
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])
# 스케일링 원상복귀
inver_x_train = sc.inverse_transform(x_train)
print(inver_x_train[:3])
'''

# model
# model = LogisticRegression(C = 100.0, random_state = 0, solver='lbfgs', multi_class='auto')
# C 속성: L2규제(모델에 패널티 적용) <-- C 값이 작을수록 더 강한 규제 적용
# <- solver='lbfgs', multi_class='auto' 이렇게 적으면 softmax를 지원하게 설정됨.

# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(criterion='entropy', n_estimators=500, random_state = 1, n_jobs = 4) # n_jobs = 2 듀얼 4 쿼드코어 1 싱글코어

# import xgboost as xgb
# model = xgb.XGBClassifier(boost='gbtree', n_estimators=500, random_state = 1)

# from sklearn import svm
# # model = svm.SVC(C=1) # 과적합을 해결하기 위해 C를 조절.
# model = svm.LinearSVC(C = 100) # SVC의 개량종. 속도가 향상

# model
# 2022.05.16 1교시
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
print(model)
model.fit(x_train, y_train) # 학습 진행


# 분류 예측
y_pred = model.predict(x_test)
print('예측 값 :  ', y_pred)
print('실제 값 : ', y_test)
print('총 갯수 :%d, 오류수:%d'%(len(y_test), (y_test != y_pred).sum()))

print()
print('분류 정확도 확인 1')    ##0.978
print('%.3f'% accuracy_score(y_test, y_pred))
print('분류 정확도 확인 2')    #0.9777777777777777
con_mat = pd.crosstab(y_test, y_pred, rownames=['예측치'], colnames=['관측치'])
print(con_mat)
print((con_mat[0][0] + con_mat [1][1] + con_mat[2][2]) / len(y_test))
print('분류 정확도 확인 3')
print('test : ', model.score(x_test, y_test))       #test :  0.9777777777777777
print('train : ', model.score(x_train, y_train))    #train :  0.9619047619047619

# 모델 저장 후 읽기
import pickle
pickle.dump(model, open('cla_model.sav', mode='wb'))
del model
read_model = pickle.load(open('cla_model.sav', mode='rb'))

print('\n새로운 값으로 예측 - petal.lenght, petal.width 만 참여')
print(x_test[:3])
new_data = np.array([[5.1, 2.4], [0.3, 0.3], [3.4, 0.2]])
# sc.fit(new_data)    #표준화 후 모델을 학습한 경우
# new_data = sc.transform(new_data)

new_pred = read_model.predict(new_data)
print('예측 결과 : ', new_pred)

# * 붓꽃 자료에 대한 로지스틱 회귀 결과를 차트로 그리기 *

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import font_manager, rc
plt.rc('font', family='malgun gothic')      
plt.rcParams['axes.unicode_minus']= False

def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')  # 점 표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])


    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    
    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 인자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)   # Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    
    # X를 xx, yy가 축인 그래프 상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    
    X_test = X[test_idx, :]

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], c=cmap(idx), marker=markers[idx], label=cl)

    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c=[], linewidth=1, marker='o', s=80, label='testset')


    plt.xlabel('꽃잎 길이')
    plt.ylabel('꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()


x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=read_model, test_idx=range(105, 150), title='scikit-learn제공')