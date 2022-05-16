''' Created on 2022. 5. 4. 5교시 ~ '''
# sklearn 모듈이 제공하는 PolynomialFeatures를 사용하여 다항식 항 추가
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from skimage.metrics.simple_metrics import mean_squared_error

x = np.array([258, 270, 294, 320, 342, 368, 396, 446, 480, 586])[:, np.newaxis]
print(x, x.shape)
y = np.array([236, 234, 253, 298, 314, 342, 360, 368, 391, 390])
print(y)

# plt.scatter(x, y)
# plt.show()

np.set_printoptions(precision=6, suppress=True) #과학적 표기법 없애기

# 선형 / 비선형 모델 작성 후 비교
lr = LinearRegression() #선형회귀용
pr = LinearRegression() #다항회귀용
polyf = PolynomialFeatures(degree=2)
x_quad = polyf.fit_transform(x)
print(x_quad)

# lr
lr.fit(x, y)
x_fit = np.arange(250, 600, 10)[:, np.newaxis]     # 새값으로 결과 예측    # [:, np.newaxis] 로 2차원으로 변형
y_lin_fit = lr.predict(x_fit)
print('결과 예측(lr) : ', y_lin_fit)    #시각화를 위한 참고 자료

# pr
pr.fit(x_quad, y)
y_quad_fit = pr.predict(polyf.fit_transform(x_fit))
print('결과 예측(pr) : ', y_quad_fit)

#시각화
plt.scatter(x, y, label='training points')
plt.plot(x_fit, y_lin_fit, label='linear fit', linestyle='--', c='red')
plt.plot(x_fit, y_quad_fit, label='quadratic fit', linestyle='-.', c='blue')
plt.legend()    # 각 선의 이름 표시
plt.show()

print()
# 두 모델 성능 점수 확인
y_lin_pred = lr.predict(x)
y_quad_pred = pr.predict(x_quad)
print('MSE 비교 : 선형모델:%.3f, 다항모델:%.3f'%(mean_squared_error(y, y_lin_pred), mean_squared_error(y, y_quad_pred)))
# --> MSE 비교 : 선형모델:570.885, 다항모델:58.294
print('결정계수 비교 : 선형모델:%.3f, 다항모델:%.3f'%(r2_score(y, y_lin_pred), r2_score(y, y_quad_pred)))
# --> 결정계수 비교 : 선형모델:0.831, 다항모델:0.983