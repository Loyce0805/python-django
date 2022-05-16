''' Created on 2022. 5. 3. 3교시~ '''
# iris dataset으로 선형회귀분석
# 상관관계가 약한 경우와 강한 경우로 분석 모델을 작성해서 비교

import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns   #iris가 seaborn에 있음
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head(3), iris.shape)
print(iris.corr(method='pearson'))

# 단순 선형회귀
# 1. 상관관계가 약한 두 변수
result1 = smf.ols(formula = 'sepal_length ~ sepal_width', data = iris).fit()
print('요약결과1: \n', result1.summary())
print('R squared : ', result1.rsquared)
print('p-value : ', result1.pvalues[1])
# 1모델은 의미 없는 모델!
print('실제 값 : ', iris.sepal_length[:5].values)
print('예측 값 : ', result1.predict()[:5])
# plt.scatter(iris.sepal_length, iris.sepal_width)
# plt.show()

print('-----2번째-------')
# 1. 상관관계가 강한 두 변수
result2 = smf.ols(formula = 'sepal_length ~ petal_length', data = iris).fit()
print('요약결과2: \n', result2.summary())
print('R squared : ', result2.rsquared) #R squared :  0.759954645772515
print('p-value : ', result2.pvalues[1]) #p-value :  1.0386674194499307e-47 < 0.05
# 2모델은 의미 있는 모델!
print('실제 값 : ', iris.sepal_length[:5].values)
print('예측 값 : ', result2.predict()[:5])

# 새로운 값(petal_length)로 미지의 sepal_length 값을 얻고 싶어!!
new_data = pd.DataFrame({'petal_length':[1.1, 0.5, 5.0]})
y_pred = result2.predict(new_data)
print('new_data로 예측 결과 : ', y_pred.values)

print()
print('----------------------')
# 다중 선형회귀 : 독립변수 복수 --> Adj. R-squared를 봐야한다!!!
# result3 = smf.ols(formula = 'sepal_length ~ petal_length+petal_width+sepal_width', data=iris).fit()
# print('요약결과2 : ', result3.summary())

# 여러 개의 독립변수는 join을 사용
column_select = "+".join(iris.columns.difference(['sepal_length', 'species']))
print(column_select)
result3 = smf.ols(formula = 'sepal_length ~ ' + column_select, data=iris).fit()
print('요약결과2 : ', result3.summary())