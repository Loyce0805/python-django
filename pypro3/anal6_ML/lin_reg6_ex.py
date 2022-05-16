# 회귀분석 문제 3) 
# kaggle.com에서 carseats.csv 파일을 다운 받아 Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus']=False

df=pd.read_csv('../testdata/Carseats.csv')
print(df.head(2))
print(df.info())
print(df.corr())  # 상관관계 확인

lm = smf.ols(formula = 'Sales ~ Income + Advertising + Price + Age', data = df).fit()
print('요약 결과 : ', lm.summary())  # Income, Advertising, Price, Age 모두 < 0.05이므로 유의

print('---회귀분석모형의 적절성을 위한 조건 체크---------------')
# 잔차항
fitted = lm.predict(df)
residual = df['Sales'] - fitted
print(residual[:3])
print('잔차의 평균:', np.mean(residual))  # -8.057998712729386e-15

import seaborn as sns
print('선형성 : 예측값과 실제값의 잔차가 일정하게 분포')
sns.regplot(fitted, residual, lowess = True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0,0], '--', color='gray')
plt.show()    # 잔차가 일정하게 분포. 선형성을 만족.

print('정규성 : 잔차항이 정규분포를 따라야 한다. Quantile-Quantile Plot으로 확인')
import scipy.stats as stats
sr = stats.zscore(residual)
(x, y), _=stats.probplot(sr)
sns.scatterplot(x,y)
plt.plot([-3, 3],[-3, 3], '--', color='gray')
plt.show()  # 잔차항이 정규분포를 따르지 않음. 정규성

# shapiro test 확인
print('shapiro test :', stats.shapiro(residual))
# shapiro test : ShapiroResult(statistic=0.99492239, pvalue=0.21274073)
# pvalue=0.21274073 > 0.05 이므로 정규성을 만족


print('독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.')
# 잔차가 자기상관(인접 관측치의 오차가 상관되어있음)이 있는 지 확인
# Durbin-Watson: 1.931 : 2에 근접한 값. 독립성 만족(자기상관이 없다.)


print('등분산성 : 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.')
sr = stats.zscore(residual)
sns.regplot(fitted, np.sqrt(abs(sr)), lowess=True, line_kws={'color':'red'})
plt.show()  # 등분산성을 만족


print('다중공산성')
# VIF(분산 인플레 요인, 분산팽창계수) 값이 10을 넘으면 다중공선성이 발생하는 변수라고 할 수 있다.
from statsmodels.stats.outliers_influence import variance_inflation_factor
df2 = df[['Income','Advertising','Price','Age']]
print(df.shape[1])
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(df2.values, i) for i in range(df2.shape[1])]
print(vifdf)  # 모든 변수가 10을 넘지 않으므로 다중공선성 문제 발생안함


print('---------새로운 값으로 예측---------------------------')
new_df = pd.DataFrame({'Income':[35,62,24], 'Advertising':[6,3,11],'Price':[105,89,75], 'Age':[32,54,21]})
pred = lm.predict(new_df)
print('Sales 예측값 :\n', pred)