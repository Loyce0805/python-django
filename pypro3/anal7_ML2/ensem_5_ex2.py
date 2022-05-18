'''
Created on 2022. 5. 12.
'''
# [Randomforest 문제2]
# 중환자 치료실에 입원 치료 받은 환자 200명의 생사 여부에 관련된 자료다.
# 종속변수 STA(환자 생사 여부)에 영향을 주는 주요 변수들을 이용해 검정 후에 해석하시오. 
# 모델 생성 후 입력자료 및 출력결과는 Django를 사용하시오.
# 예제 파일 : https://github.com/pykwon  ==>  patient.csv
# <변수설명>
#   STA : 환자 생사 여부 (0:생존, 1:사망)
#   AGE : 나이
#   SEX : 성별
#   RACE : 인종
#   SER : 중환자 치료실에서 받은 치료
#   CAN : 암 존재 여부
#   INF : 중환자 치료실에서의 감염 여부
#   CPR : 중환자 치료실 도착 전 CPR여부
#   HRA : 중환자 치료실에서의 심박수
import pandas as pd
df = pd.read_csv('../testdata/patient.csv')
# print(df.head(3))
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.shape) # (200, 11)

feature_df = df.drop(['STA'], axis = 1)
label_df = df['STA']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(feature_df, label_df, test_size = 0.2, random_state = 1)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
rfmodel = RandomForestClassifier().fit(x_train, y_train)
rfpredict = rfmodel.predict(x_test)
print('rf acc : {0:.5f}'.format(accuracy_score(y_test, rfpredict)))

# 참고 : 중요 변수 알아보기
print('특성(변수) 중요도 :\n{}'.format(rfmodel.feature_importances_))
import matplotlib.pyplot as plt
import numpy as np
def plot_feature_importances(rfmodel):   # 특성 중요도 시각화
    n_features = feature_df.shape[1]
    plt.barh(range(n_features), rfmodel.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), feature_df.columns)
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1, n_features)
    plt.show()
    plt.close()
plot_feature_importances(rfmodel)