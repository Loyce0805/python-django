# [로지스틱 분류분석 문제2] 
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("../testdata/bodycheck.csv")
print(data.head(2))

x = data[['게임', 'TV시청']]
y = data['안경유무']
print(set(y))  # {0, 1}

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

logi_model = LogisticRegression(C=0.01, random_state = 0)
result_logi = logi_model.fit(x_train, y_train)

y_pred= logi_model.predict(x_test)
print('예측값 : ', y_pred)
print('실제값 : ', y_test.values)

print('정확도 : %.5f'%accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

tmp1 = int(input('게임 시간 : '))
tmp2 = int(input('TV 시청 시간 : '))
predData = pd.DataFrame({'게임':[tmp1], 'TV시청':[tmp2]})
y_pred = logi_model.predict(predData)[0]
print('y_pred : ', y_pred)

if y_pred == 0:
    print('안경 착용 X')
else:
    print('안경 착용 O')