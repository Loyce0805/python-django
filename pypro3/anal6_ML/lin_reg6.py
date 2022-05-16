''' Created on 2022. 5. 3. 5교시~ '''
# Advertising.csv : 여러 매체를 통한 광고비 판매량 추정치 얻기

import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

advdf = pd.read_csv('../testdata/Advertising.csv', usecols=[1,2,3,4]) #Advertising.csv는 kaggle에 있는 데이터임.
print(advdf.head(3), advdf.shape)   #200행 4열

print('상관계수(r) : ', advdf.loc[:, ['sales', 'tv']].corr())   #0.782224
print('상관계수(r) : ', advdf.loc[:, ['sales', 'newspaper']].corr())    #0.228299
print('상관계수(r) : ', advdf.loc[:, ['sales', 'radio']].corr())    #0.576223

print()
print('--단순선형회귀--')
lm = smf.ols(formula = 'sales ~ tv', data=advdf).fit()
print(lm.summary())
print('설명력 : ', lm.rsquared)    #0.611875050850071
print('p값 : ', lm.pvalues[1])   #1.406300e-35
# 미지의 입력값에 대한 결과를 얻기 위해 하는 것들임~~~

# 시각화
'''
plt.scatter(advdf.tv, advdf.sales)
plt.xlabel('tv')
plt.ylabel('sales')
x = pd.DataFrame({'tv':[advdf.tv.min(), advdf.tv.max()]})
y_pred =lm.predict(x)
plt.plot(x, y_pred, c='red')
plt.show() '''

print()
# 미지의 tv 광고비에 따른 상품 판매량 추정
x_new = pd.DataFrame({'tv':[220.12, 55.66, 10]})
pred_new = lm.predict(x_new)
print('상품 판매량 추정치 : ', pred_new.values)

print('------')
print(advdf.corr()) # sales와의 상관관계: tv > radio > newspaper
# lm_mul = smf.ols(formula = 'sales ~ tv + radio + newspaper', data=advdf).fit()
# print(lm_mul.summary(0))    #Adj. R-squared: 0.896 | p-values:1.58e-96 < 0.05 이므로 유의한 모델이다!
# ---- 6교시 ----
# newspaper의 p-value는 0.860로 > 0.05 이므로 독립변수에서 제거를 고려

lm_mul = smf.ols(formula = 'sales ~ tv + radio', data=advdf).fit()
print(lm_mul.summary(0))    #Adj. R-squared: 0.896 | p-values: 4.83e-98<0.05 이므로 유의한 모델이다!
# newspaper를 제외해도 Adj.R-squared는 동일하므로 모델의 성능에 영향을 주지 못하는 변수이다!
# tv 하나만 독립변수로 설정했을 때 설명력은 0.611875. AIC는 1042.
# tv와 radio 두 개를 독립변수로 설정했을 때 설명력은 0.896, AIC는 778.4로 모델의 성능이 더 좋아졌다고 볼 수 있음.

print()
""" 새로운 독립변수 값으로 종속변수 sales를 예측해서 추정치를 얻기 """
x_new2 = pd.DataFrame({'tv':[220.12, 55.66, 10], 'radio':[30.3, 40.4, 50.5]})
pred_new2 = lm.predict(x_new2)
print('상품 판매량 추정치2 : ', pred_new2.values)

print()
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
print('***** 선형회귀분석의 기존 가정 충족 조건 *****')
""" . 선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다.
    . 정규성 : 잔차항이 정규분포를 따라야 한다.
    . 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
    . 등분산성 : 그룹간의 분산이 유사해야 한다. 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.
    . 다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다. """

# 잔차항 구하기 (실제값 - 예측값)
fitted = lm_mul.predict(advdf.iloc[:, 0:2]) #모든 행, tv:radio만 건 것
# print(fitted)    #예측값
residual = advdf['sales'] - fitted  # 잔차!!!!!!!!
print(np.mean(residual))    #잔차의 평균은 1.1430856261540611e-14 으로 0에 근사한다.

print('선형성 ---- 예측값과 잔차의 분포가 유사하다.')
import seaborn as sns
# sns.regplot(fitted, residual, lowess = True, line_kws = {'color':'red'})   #선형회귀모델의 적합성를 그릴 때 사용. - 잔차의 추세선을 시각화
# plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color='gray')
# plt.show()
# --> 선형성을 만족하지 못함.(추세선이 비선형이다) : 이럴 경우에는 다'항'회귀 모델이 추천된다.(PolynomialFeatures)


print('\n정규성 ---- 잔차가 정규분포를 따르는지 확인. Q-Q plot을 사용한다')
import scipy.stats

# sr = scipy.stats.zscore(residual)
# (x, y), _ = scipy.stats.probplot(sr)
# sns.scatterplot(x, y)
# plt.plot([-3, 3], [-3, 3], '--', color='gray')
# plt.show()
# --> 정규성을 만족하지 않음. : 데이터에 대해 표준화, 정규화, log를 씌우는 등의 작업을 시도해봐야 한다.

# 정규성은 shapiro로 볼 수도 있음
print('shapifo test : ', scipy.stats.shapiro(residual))
#shapifo test :  ShapiroResult(statistic=0.9180378317832947, pvalue=4.190036317908152e-09)
#pvalue=4.190036317908152e-09 < 0.05 이므로 정규성을 만족하지 못함

print('\n독립성 ---- 잔차가 자기상관을 따르는지 확인. (따르면 안 됨) | 0 =< Durbin-Watson =< 4. 2에 근사하면 만족')
#독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
# Durbin-Watson: 2.081    : 독립성은 만족

#-----------7교시----------

print('\n등분산성 ---- 잔차의 분산이 일정해야 함') #시각화로 볼 수 있다
# sr = scipy.stats.zscore(residual)
# sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws = {'color':'red'})
# plt.show()
# 등분산성 만족 못함. : 비선형인지 확인, 이상값, 확인, 정규성 확인
# 정규성은 만족하나 등분산성은 만족하지 못한 경우 가중회귀(weighted regression)분석

print('\n다중공산성 ---- 독립변수들 간에 강한 상관관계 확인')
from statsmodels.stats.outliers_influence import variance_inflation_factor
# VIF(Variable Inflation Factors : 분산 팽창 계수) 값 확인 : 10을 넘으면 다중공산성이 의심됨.
print(variance_inflation_factor(advdf.values, 1))   # tv 12.570312383503682
print(variance_inflation_factor(advdf.values, 2))   # radio 3.1534983754953845
vifdf = pd.DataFrame()  #DataFrame으로 확인하기
vifdf['vif_value'] = [variance_inflation_factor(advdf.values, i) for i in range(1, 3)]
print(vifdf)

print("\n참고 : 극단치(이상치) 확인 - Cook'sDistance") 
from statsmodels.stats.outliers_influence import OLSInfluence   #새로운 모듈!
cd, _ = OLSInfluence(lm_mul).cooks_distance #극단값을 나타내는 지표 반환
print(cd.sort_values(ascending=False).head())   #극단치 확인

import statsmodels.api as sm
sm.graphics.influence_plot(lm_mul, criterion='cooks')
plt.show()

print(advdf.iloc[[130, 5, 35, 178, 126]])