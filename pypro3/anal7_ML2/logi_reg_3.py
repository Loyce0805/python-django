''' 
Created on 2022. 5. 9.
'''
# LogisticRegression 클래스 사용
# pima-indians-diabetes dataset 사용

''' Pregnancies: 임신 횟수
    Glucose: 포도당 부하 검사 수치
    BloodPressure: 혈압(mm Hg)
    SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm)
    Insulin: 혈청 인슐린(mu U/ml)
    BMI: 체질량지수(체중(kg)/키(m))^2
    DiabetesPedigreeFunction: 당뇨 내력 가중치 값
    Age: 나이
    Outcome: 클래스 결정 값(0 또는 1) '''

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/pima-indians-diabetes.data.csv"
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkindThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv(url, names=names)
print(df.head(3), df.shape)     # (768, 9)

arr = df.values
x = arr[:, 0:8]     # x 값은 matrix 형식   # [[  6.    148.     72.     35.      0.     33.6     0.627  50.   ] ...
print(x[:3], x.shape)
y = arr[:, 8]       # y 값은 vector 형식    # [1. 0. 1.]    # scikitlearn이 요구하는 형식이다.
print(y[:3], y.shape)

x_train, x_test, y_train, y_test= model_selection.train_test_split(x, y, 
                                                                   test_size = 0.33, random_state=7)
# random_state=7 : 난수값 지정해서 샘이랑 같은 값 얻으려고 정하는 것.. 실제 분석할 때는 지정할 필요 없음
print(x_train.shape, x_test.shape)  # (514, 8) (254, 8)

"""
model = LogisticRegression()
model.fit(x_train, y_train)
print('예측값 : ', model.predict(x_test[:5]))  #예측값 :  [0. 1. 1. 0. 0.]
print('실제값 : ', y_test[:5])                 #실제값 :  [0. 1. 1. 0. 1.]
print('예측과 실제가 일치하지 않는 갯수 : ', (model.predict(x_test) != y_test).sum()) #254개 중 54개 틀림
# LinearRegression에서는 score가 있다!!! accuracy_score() 대신 쓸 수 있음.
print('test로 분류 정확도 : ', model.score(x_test, y_test))       #0.787401    #모델 성능이 좋지는 않음..
print('train으로 분류 정확도 : ', model.score(x_train, y_train))   #0.774319
# ==> train과 test의 분류 정확도가 크지 않아야 함. train의 값이 너무 크면 과적합이 발생한 것임..!

from sklearn.metrics import accuracy_score
pred = model.predict(x_test)
print('분류 정확도 : ', accuracy_score(y_test, pred))    #0.787401

# 모델의 분류 성능이 목표치에 도달했다면 모델을 저장 후 저장된 모델로 분류 결과를 예측한다.
pickle.dump(model, open('pima_model.sav', mode='wb'))
# -->> 모델을 만들어서 저장했으므로 더이상 학습시킬 필요가 없음!!
"""

model = pickle.load(open('pima_model.sav', 'rb'))
print('test로 분류 정확도 : ', model.score(x_test, y_test))

print(x_test[:1])   # 분류를 원하는 새로운 데이터라고 가정하자
print('분류 예측 : ', model.predict(x_test[:1]))