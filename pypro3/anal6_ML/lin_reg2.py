''' 
Created on 2022. 5. 2. 선형회귀분석(linregress)
'''
# 모델 맛보기 4 : linregress를 사용. model 생성 OOOO

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IQ에 따른 시험성적 값 예측
score_iq = pd.read_csv("../testdata/score_iq.csv")
print(score_iq.info())  # 구조 확인
print(score_iq.head(3), score_iq.shape) # (150, 6)

x = score_iq.iq # feature(독립변수)
y = score_iq.score  # label(종속변수, class)

# 상관관계 확인
print(np.corrcoef(x, y)[0,1])    # numpy로 확인   
print(score_iq.corr())      # pandas로 확인 # 0.882220

# plt.scatter(x, y)
# plt.show()


# 선형회귀분석
model = stats.linregress(x, y)  # LinregressResult(slope=0.6514309527270075, ...
print(model)
print('x slope : ', model.slope)
print('y intercept: ', model.intercept)
print('pvalue : ', model.pvalue)
# x slope :  0.6514309527270075
# y intercept :  -2.8564471221974657
# pvalue :  2.8476895206683644e-50 < 0.05 이므로 유의한 모델이다(인과관계가 있다.)
# y = model.slope * x + model.intercept
print('IQ에 따른 점수 예측 : ', model.slope * 140 + model.intercept)   # 88.34388625958358
print('IQ에 따른 점수 예측 : ', model.slope * 120 + model.intercept)   # 75.31526720504343

# linregress는 predict을 지원하지 않음
# -> 그래서 numpy의 polyval([slope, bias], x)을 이용.

print('IQ에 따른 점수 예측 : ', np.polyval([model.slope, model.intercept], 140))   # 88.34388625958358
print()
newdf = pd.DataFrame({'iq':[55,66,77,88,150]})
print('새로운 점수 예측 : ', np.polyval([model.slope, model.intercept], newdf).flatten())  # flatten으로 차원축소 matrix -> vector
# 새로운 점수 예측 :  [32.97225528 40.13799576 47.30373624 54.46947672 94.85819579]