'''
Created on 2022. 5. 3. ols(Ordinary Least Squares)(최소제곱법)
'''
# ols(Ordinary Least Squares) 사용 : 최소제곱법. 가장 기본적인 결정론적 선형회귀방법. 불확실성이 있다.

import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("../testdata/drinking_water.csv")
print(df.head(3))
print(df.corr()) # 피어슨상관분석으로 두 변수의 상관관계 분석
# -> 상관관계가 있으니 회귀분석을 사용할 수 있다. 하지만 인과관계는 설명할 수 없다.
# -> 회귀분석 : "만족도와 적절성은 인과관계가 있다" 라는 가정 하에
# 귀무가설과 대립가설을 걸고 갈 수 있다.
model = smf.ols(formula = '만족도 ~ 적절성', data = df).fit() # 만족도(종속변수) 적절성(독립변수)
# fit()은 추세선을 무작위로 그어보면서 잔차(residual)(예측값과 실측값의 차이)가 최소가 되는 선을 찾기위해 Debugging
print(model.summary())
"""
==============================================================================
Dep. Variable:                    만족도   R-squared:                       0.588
Model:                            OLS   Adj. R-squared:                  0.586
Method:                 Least Squares   F-statistic:                     374.0
Date:                Wed, 11 May 2022   Prob (F-statistic):           2.24e-52
Time:                        22:22:00   Log-Likelihood:                -207.44
No. Observations:                 264   AIC:                             418.9
Df Residuals:                     262   BIC:                             426.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.7789      0.124      6.273      0.000       0.534       1.023
적절성            0.7393      0.038     19.340      0.000       0.664       0.815
==============================================================================
Omnibus:                       11.674   Durbin-Watson:                   2.185
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               16.003
Skew:                          -0.328   Prob(JB):                     0.000335
Kurtosis:                       4.012   Cond. No.                         13.4
==============================================================================
"""
# SSE(some of square error) : (실제값-예측값)**2, SSR(some of square residual) = 평균을 뺀 모든 값을 더해서 제곱 SST = SSE + SSR 
# 결정계수 : 상관계수(r)의 제곱 또는 1 - SSE/SST -> 독립변수가 종속변수의 분산을 얼마정도 설명하는가 설명된 분산/종속변수의 전체분산
# 독립변수가 2개일때는 수정된 결정계수를 본다. (Adj R-squared)
# 이 모델은 p-value에 의해 유의한 모델이고 독립변수가 종속변수의 분산을 58%정도 설명하고 있다 라고 할 수 있다.
# coef와 std err에 의해 t값이 나온다. 그 t값에 의해 F-statistic 값이 나오고 그 F값에 의해 나오는게 Prob(p-value)이다. p-value는 모델의 유의미를 판단.
# AIC 값은 독립변수의 갯수에 따라 바뀌고 작을 수록 좋다. 독립변수가 1개일땐 의미가 없다. 독립변수의 갯수가 많으면 AIC 값이 모델의 성능을 결정.
# A반에 국어 영어 수학이 과학점수에 영향을 준다. 국어가 과학에 영향을 미치는 모델, 국어/영어가 영향, 국어/영어/수학이 영향 이 3개의 모델을 AIC값을 비교해서 성능을 알 수 있다.
# BIC 값도 모델의 성능을 비교. AIC와 마찬가지로 독립변수의 갯수를 몇개를 하는게 적절한지.
# t값 : 표준오차로 w(기울기)를 나눈다. 0.7393/0.038(std) 이걸 가지고 p-value를 구한다.

# 표준오차 : 표본평균들의 표준편차.
# 표준오차가 적으면 참에서 가깝다. 모집단과 표본의 차이가 적다는 얘기. 분산의 설명력이 높다. 상관관계가 높다. 우연일 가능성이 낮다. p-value < 0.05
# 표준오차가 크면 참에서 멀다. 모집단과 표본의 차이가 크다. 분산의 설명력이 낮다. 상관관계가 낮다. 우연일 가능성이 높다. p-value > 0.05
print(0.766853**2)

print('결정계수 : ', model.rsquared) # 설명력 : 회귀분석 모델의 성능을 이야기할때 사용. 
# SSE(some of square error) : (실제값-예측값)**2, SSR(some of square residual) = 평균을 뺀 모든 값을 더해서 제곱 SST = SSE + SSR 
# 결정계수 : 상관계수(r)의 제곱 또는 1 - SSE/SST -> 독립변수가 종속변수의 분산을 얼마정도 설명하는가 설명된 분산/종속변수의 전체분산
# 독립변수가 2개일때는 수정된 결정계수를 본다. (Adj R-squared)
# 이 모델은 p-value에 의해 유의한 모델이고 독립변수가 종속변수의 분산을 58%정도 설명하고 있다 라고 할 수 있다.
print('p-value : ', model.pvalues)
# coef와 std err에 의해 t값이 나온다. 그 t값에 의해 F-statistic 값이 나오고 그 F값에 의해 나오는게 Prob(p-value)이다. p-value는 모델의 유의미를 판단.
print('예측값 : ', model.predict()[:5])
print('실제값 : ', df.만족도[:5].values)


# 시각화
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1)    #1 써주면 1차식.
plt.plot(df.적절성, df.적절성*slope + intercept, 'b')
plt.show()