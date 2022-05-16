''' Created on 2022. 5. 4. 3교시 ~ '''
# linearRegression으로 선형회귀모델 - mtcars dataset

import statsmodels.api
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
print(mtcars.corr(method='pearson'))

print()
# hp가 mpg에 영향을 준다, 라고 가정하고 모델을 생성!
x = mtcars[['hp']].values
print(x[:5])
y = mtcars['mpg'].values
print(y[:5])

# plt.scatter(x, y)
# plt.show()

# 원래는 train / test 로 분리해야 하나 생략
lmodel = LinearRegression().fit(x, y)
print('회귀계수(slope) : ', lmodel.coef_)   #[-0.06822828]
print('회귀계수(intercept) : ', lmodel.intercept_)  #30.098860539622496

pred = lmodel.predict(x)
print('예측값 : ', np.round(pred[:5], 1))
print('실제값 : ', y[:5])
# 예측값 :  [22.6 22.6 23.8 22.6 18.2]
# 실제값 :  [21.  21.  22.8 21.4 18.7]

# 모델 성능 평가
print('RMSE : ', mean_squared_error(y, pred))   #13.989822298268805
print('r2_score : ', r2_score(y, pred))     #0.602437341423934    #60% 정도의 설명력

print()
# 새로운 데이터로 예측
new_hp = [[110]]
new_pred = lmodel.predict(new_hp)
print('%s 마력인 경우 예상연비는 약 %s 입니다.'%(new_hp[0][0], new_pred[0]))
# --> 110 마력인 경우 예상연비는 약 22.593749951750496 입니다.