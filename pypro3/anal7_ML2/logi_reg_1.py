''' 
Created on 2022. 5. 9.
'''
# 로지스틱 회귀분석(Logistci Linear Regression)
# 분류 모델 : 이항분류가 기본
# 독립변수: 연속형, 종속변수 : 범주형
# 출력된 연속형 자료를 logit 변환해 sigmoid function 함수로 0~1 사이의 실수 값이 나오도록 한 후 0.5를 기준으로 분류
import math

def sigmoidFunc(x):
    return 1/(1+math.exp(-x))

print(sigmoidFunc(3))
print(sigmoidFunc(1))
print(sigmoidFunc(-2))
print(sigmoidFunc(-5))
#--------------------

# mtcars dataset으로 분류 작업
import statsmodels.api as sm

mtcarData = sm.datasets.get_rdataset('mtcars')
print(mtcarData.keys())
mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
print(mtcars['am'].unique())    # [1 0]    수동 또는 자동
mtcar = mtcars.loc[:, ['mpg', 'hp', 'am']]

# 연비와 마력수에 따른 변속기 분류
# 모델 작성 방법1 : logit()
import statsmodels.formula.api as smf
import numpy as np
formula = 'am ~ mpg + hp'
result = smf.logit(formula = formula, data=mtcar).fit()
print(result)
print(result.summary())
'''                  coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept    -33.6052     15.077     -2.229      0.026     -63.156      -4.055
    mpg            1.2596      0.567      2.220      0.026       0.147       2.372
    hp             0.0550      0.027      2.045      0.041       0.002       0.108
'''
# print('예측값 : ', result.predict())

pred = result.predict(mtcar[:10])
# print('예측값 : ', pred.values)
print('예측값 : ', np.around(pred.values))
print('실제값 : ', mtcar['am'][:10].values)
print()
conf_tab = result.pred_table()  # 빈도수 구하는 테이블을 confusion matrix라고 함
print('confusion matrix(혼동 행렬) : \n', conf_tab)
# 모델의 분류 정확도(accuracy)
print('정확도1 : ', (16 + 10) / len(mtcar))
print('정확도2 : ', (conf_tab[0][0] + conf_tab[1][1]) / len(mtcar))

# tensorflow는 confusion matrix가 없으므로 아래 방법을 써야 함
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcar)
print('정확도3 : ', accuracy_score(mtcar['am'], np.around(pred2)))

print()
print('모델 작성 방법2 : glm()')
# 모델 작성 방법2 : glm() - generalized linear model, 일반화된 선형 모델
result2 = smf.glm(formula = formula, data=mtcar, family = sm.families.Binomial()).fit() # 이항분포
print(result2)
print(result2.summary())
pred2 = result.predict(mtcar[:10])

print('예측값 : ', np.around(pred2.values))
print('예측값 : ', np.rint(pred2.values))
print('실제값 : ', mtcar['am'][:10].values)
pred3 = result2.predict(mtcar)
print('정확도 : ', accuracy_score(mtcar['am'], np.around(pred3)))


print('- - 새로운 연비와 마력수에 대한 분류 결과 - -')
# 1. 기존 값 일부 수정
newdf = mtcar.iloc[:2].copy()
# print(newdf)
newdf['mpg'] = [10, 30]
newdf['hp'] = [100, 130]
new_pred = result2.predict(newdf)
print('new_pred : ', new_pred.values)
print('new_pred : ', np.rint(new_pred.values))

print()
# 2. 별도 작성
import pandas as pd
newdf2 = pd.DataFrame({'mpg':[10, 35, 50, 5], 'hp':[80, 100, 120, 50]})
new_pred2 = result2.predict(newdf2)
print('new_pred2 : ', np.rint(new_pred2.values))