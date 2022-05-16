# 회귀분석 문제 5)
# Kaggle 지원 dataset으로 회귀분석 모델(LinearRegression)을 작성하시오.
# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset
# feature : Temperatura Media (C) : 평균 기온(C)
#           Precipitacao (mm) : 강수(mm)
# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

'''Index(['Data', 'Temperatura Media (C)', 'Temperatura Minima (C)',
       'Temperatura Maxima (C)', 'Precipitacao (mm)', 'Final de Semana',
       'Consumo de cerveja (litros)'],
      dtype='object')'''

df = pd.read_csv('../testdata/Consumo_cerveja.csv',
                 usecols=['Temperatura Media (C)','Precipitacao (mm)','Consumo de cerveja (litros)'])
df.dropna(inplace=True)
df.columns = ['기온','강수','소비량']
df['기온'] = df['기온'].apply(lambda x: x.replace(',', '.'))
df['강수'] = df['강수'].apply(lambda x: x.replace(',', '.'))

print(df.head(1))
# print(df.corr(method = 'pearson'))

print()
# 모델을 생성한후 예측값 얻기
x = df[['기온', '강수']]
y = df[['소비량']]

lmodel = LinearRegression().fit(x, y)
pred = lmodel.predict(x)
print('예측값 :', np.round(pred[:5]).T) # [[31. 30. 29. 28. 28.]]
print('실제값 :', np.round(y[:5]).T) # 25.0  29.0  31.0  30.0  29.0

print()
# 모델 성능 평가
print('MSE : ', mean_squared_error(y, pred)) # 12.093133754991651
print('r2 score : ', r2_score(y, pred)) # 0.37339445073731026 37% 

print()
# 새로운 값으로 예측
new_params = [[30,10]]
new_pred = lmodel.predict(new_params)
print('기온이 %s, 강수량이 %s 경우에 맥주 소비량은 약 %s'%(new_params[0][0],new_params[0][1], new_pred[0]))