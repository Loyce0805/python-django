'''
Created on 2022. 5. 13. Quiz
'''
# [SVM 분류 문제] 심장병 환자 데이터를 사용하여 분류 정확도 분석 연습
# https://www.kaggle.com/zhaoyingzhu/heartcsv
# https://github.com/pykwon/python/tree/master/testdata_utf8         Heartcsv
#
# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
# 임의의 값을 넣어 분류 결과를 확인하시오.     
# 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ
#
# feature 칼럼 : 문자 데이터 칼럼은 제외
# label 칼럼 : AHD(중증 심장질환)
#
# 데이터 예)
#
# "","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"
# "1",63,1,"typical",145,233,1,2,150,0,2.3,3,0,"fixed","No"
# "2",67,1,"asymptomatic",160,286,0,2,108,1,1.5,2,3,"normal","Yes"
# ...

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../testdata/Heart.csv')
print(data.head(2))
pd.set_option('display.max_columns', None)
data['Ca'].fillna(0, inplace = True)
label_df = data['AHD']
feature_df = data.drop(columns =['Unnamed: 0' ,'ChestPain', 'Thal', 'AHD'])
print(feature_df)
from sklearn.preprocessing import LabelEncoder
label_df = LabelEncoder().fit_transform(label_df)
print(label_df)

# 정규화
feature_df['Age'] = feature_df['Age'] / 100
feature_df['RestBP'] = feature_df['RestBP'] / 100
feature_df['Chol'] = feature_df['Chol'] / 100
feature_df['MaxHR'] = feature_df['MaxHR'] / 100

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
feature_df_train, feature_df_test, label_df_train, label_df_test = train_test_split(feature_df, label_df, test_size = 0.3, random_state = 42)

# 위쪽은 C parameter를 1로 한 것이고, 아래는 100으로 한 것입니다. 앞선 포스트에서 설명했듯이 C를 작게 하면 훈련 데이터의 분류를 부정확하게 하는 대신 (= decision boundary를 곧게 그리는 대신) Margin을 크게 합니다. C를 크게 하면 Margin을 작게 하는 대신 훈련 데이터의 분류를 정확하게 (= decision boundray를 굴곡있게) 합니다.
# 상황에 따라 C를 적절하게 선택해줘야 합니다. Noise가 많은 데이터라면 C를 작게 하는 것이 좋고, Noise가 별로 없는 데이터라면 C를 크게 하는 것이 좋습니다.
model = SVC(C = 1).fit(feature_df_train, label_df_train)
pred = model.predict(feature_df_test)
print('실제값 : ', label_df_test[:10])
print('예측값 : ', pred[:10])

from sklearn import metrics
print(metrics.accuracy_score(label_df_test, pred))
print(metrics.classification_report(label_df_test, pred))
