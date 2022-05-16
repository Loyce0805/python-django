''' 
Created on 2022. 5. 2. 선형회귀분석(make_regression, LinearRegression, ols)
'''
# 회귀분석방법 확인 : 맛보기
# 잔차 제곱합이 최소가 되는 추세선을 만들고 이를 통해 feature(독립변수)가 label(종속변수, class)에 
# 얼마나 영향을 주는지 인과관계를 분석
# 두 개 이상의 변수는 상관관계가 있어야 하고, 나아가서는 인과관계가 있어야 한다.
# 정량적인 모델을 생성

import statsmodels.api as sm
from sklearn.datasets import make_regression # regression을 연습할 수 있는 모듈을 제공.
import numpy as np

np.random.seed(12)

# 모델 맛보기 1 : make_regression을 사용. model 생성은 안된다. 
x, y, coef = make_regression(n_samples=50, n_features=1, bias = 100, coef = True) # 표본수, 독립변수 수, y절편(default는 0), 기울기 coefficient(계수)를 출력하겠다. 
print(x)
print(y)
print(coef) # 기울기 : 89.47430739278907(동적), 절편 : 100     y(햇을 붙이면 예측값) = wx + b  y와 y햇의 차이가 최소가 될수록 좋다.
print('예측값 : ', coef * -1.70073563 + 100)
print('실제값 : ', -52.17214291)

print('예측값 : ', coef * -0.67794537 + 100)
print('실제값 : ', 39.34130801)

# scikitlearn은 feature는 2차원(matrix). label은 1차원(vector)도 되고 2차원(matrix)도 되지만 보통은 1차원(vector)
# 참고 : 머신러닝(기대학습)은 귀납적 추론방식을 따른다. 
# -> 수집된 데이터를 가지고 새로운 값을 예측한다. (연역적처럼 이미 정해져있는게 없다)


print('-----------------------')
xx = x
yy = y

# 모델 맛보기 2 : LinearRegression 사용. model 생성가능
from sklearn.linear_model import LinearRegression  # scikitlearn은 입력값(독립변수) matrix, 출력값(종속변수) vector
model = LinearRegression()  # LinearRegression 객체 생성
fit_model = model.fit(xx, yy) # linear 모델을 fitting(학습)하는 것. 최적의 선형회귀를 만든다. 
# -> 학습데이터로 모형 추정(training) : 절편, 기울기 얻음(최소제곱법을 이용)

print('slope : ', fit_model.coef_)  # slope(기울기) : [89.47430739]
print('bias : ', fit_model.intercept_)  # bias(절편) : 100.0 
# y = 89.47430739 * x + 100.0

print('모델이 예측한 값(수식사용) : ', 89.47430739 * -1.70073563 + 100.0)
y_new = fit_model.predict(xx[[0]]) # LinearRegression클래스의 predict 메소드를 사용 # matrix니까 [[]]사용 입력값이 매트릭스니까 예측값도 매트릭스를 이용.
print('모델이 예측한 값(method사용) : ', y_new[0])
print('미지의 x에 대한 새로운 예측값 : ', fit_model.predict([[66]]))   # 우리가 알고 싶은 값.
# -> matrix로 학습했기 때문에 입력값은 반드시 matrix로 넣어줘야 함

print('-----------------------')
# 모델 맛보기 3 : ols를 사용. model 생성가능 # Ordinary Least Squares
import statsmodels.formula.api as smf  # statsmodels는 DataFrame을 가지고 함.
import pandas as pd
x1 = xx.flatten()   # 차원 축소해서 matrix를 vector로 만듦.
y1 = yy
print(x1.shape, ' ', y.shape)   # (50,)    (50,)

data = np.array([x1, y1])
df = pd.DataFrame(data.T)
print(df.head(3))

model2 = smf.ols(formula = 'y1 ~ x1', data = df).fit() # 종속변수 : y1, 독립변수 : x1
print(model2.summary())
# Intercept : 100.0000, slope : 89.4743

# 예측값 확인 함수
print(x1[:2])   #[-1.70073563 -0.67794537]
new_df = pd.DataFrame({'x1':[-1.70073563, -0.67794537]})    # 기존자료로 예측값 확인
new_pred = model2.predict(new_df)
print('모델이 예측한 값(method) : \n', new_pred)

print()
# 전혀 새로운 독립변수에 대한 예측 결과 보기
new2_df = pd.DataFrame({'x1':[123, -2.345]})    # 새로운 자료로 예측값 확인
new2_pred = model2.predict(new2_df)
print('모델이 예측한 새로운 값(method) : \n', new2_pred)