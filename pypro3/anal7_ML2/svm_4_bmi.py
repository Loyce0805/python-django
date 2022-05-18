'''
Created on 2022. 5. 13.
'''
# BMI 식을 이용해 dataset을 작성 후 SVM 분류 모델 생성

# BMI 식 = 몸무게(kg) / 키(m) * 키(m)
# 데이터 만들기
""" 
print(69 / ((177 / 100) * (177 / 100)))

# BMI 식을 이용해 무작위 자료 작성
import random

def calc_func(h, w):
    bmi = w / (h / 100) ** 2
    if bmi < 18.5 : return 'thin'
    if bmi < 25.0 : return 'normal'
    return 'fat'

print(calc_func(177, 69))

fp = open('bmi.csv', 'w', encoding = 'UTF-8')
fp.write('height,weight,label\n')
cnt = {'thin':0,'normal':0,'fat':0}
random.seed(12)
for i in range(50000):
    h = random.randint(150, 200)
    w = random.randint(35, 100)
    label = calc_func(h, w)
    cnt[label] += 1
    fp.write('{0},{1},{2}\n'.format(h,w,label))
    
fp.close()
"""

# SVM 분류 모델을 적용
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tbl = pd.read_csv('bmi.csv')
print(tbl.head(3))

label = tbl['label']

# weight, heigth를 정규화(0~1 사이에 들어오도록) 이래야 성능이 더 좋아진다. 표준화나 정규화를 해주면 분류모델의 성능이 좋아진다.
w = tbl['weight'] / 100
print(w[:3])
h = tbl['height'] / 200
print(h[:3])
wh = pd.concat([w, h], axis = 1) # w랑 h 합치기 axis = 1을 통해 열을 기준으로
print(wh.head(3), wh.shape)
print(label[:3], label.shape)
label = label.map({'thin':0,'normal':1,'fat':2}) # label의 String을 더미화 근데 굳이 더미화 안하고 문자로 해도 된다. 하지만 더미화가 더 자연스러움.
print(label[:3])

data_train, data_test, label_train, label_test = train_test_split(wh, label, random_state = 1)
print(data_train.shape, data_test.shape, label_train.shape, label_test.shape) # (37500, 2) (12500, 2) (37500,) (12500,)

# model = svm.SVC(C = 1).fit(data_train, label_train)
model = svm.LinearSVC(C = 1).fit(data_train, label_train)

pred = model.predict(data_test)
print('실제값 : ', label_test[:10].values)
print('예측값 : ', pred[:10])

print(metrics.accuracy_score(label_test, pred))
print(metrics.classification_report(label_test, pred))

# 시각화
tbl2 = pd.read_csv('bmi.csv', index_col = 2) # 인덱스 칼럼이 3번째에 있는 label
def scatter_func(lbl, color):
    b = tbl2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label=lbl)

scatter_func('fat', 'red')
scatter_func('normal', 'yellow')
scatter_func('thin', 'blue')
plt.legend()
plt.show()
