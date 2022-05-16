# 회귀분석 문제 1) scipy.stats.linregress(), statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량 대한 데이터는 아래와 같다.
#  - 지상파 시청 시간을 입력하면(input) 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 10시간 초과는 이상치로 한다. 

from scipy import stats
import numpy as np
import pandas as pd

data = pd.read_csv('../testdata/watchingTv.csv', header=None)
data.columns = ['지상파', '종편', '운동']

print(data.지상파.mean())
data = data.fillna(data.지상파.mean())
data.drop(data[data['운동']>10].index, inplace = True)
print(data, type(data))

x = data.지상파
y = data.운동

model = stats.linregress(x, y)
print(model)
print('x-slope : ', model.slope)
print('y-intercept : ', model.intercept)
print('p-value : ', model.pvalue)

number = int(input("숫자를 입력하세요 : "))
print(number)
print('지상파 시청 시간에 따른 예측 운동시간 : ', model.slope * number + model.intercept)