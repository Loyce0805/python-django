''' 
Created on 2022. 5. 16.
'''
# sklearn이 지원하는 예측모델(연속형 데이터)

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score    # 위의 회귀분석모델들의 성능을 비교하기위한 것

adver = pd.read_csv('../testdata/Advertising.csv', usecols=[1,2,3,4])
print(adver.head(2))

x = np.array(adver.loc[:, 'tv':'newspaper'])    # tv, radio, newspaper만 x에 matrix로
print(x[:2])
y = np.array(adver.sales)
print(y[:2])

print()
print('- - Linear Regression - -')
lmodel = LinearRegression().fit(x, y)
lpred = lmodel.predict(x)
print('LinearRegression pred : ', lpred[:5])    # [20.52397441 12.33785482 12.30767078 17.59782951 13.18867186]
print('l_r2_scroe : ', r2_score(y, lpred))      # 0.8972106381789522
# --> 89.7% 정도의 설명력을 갖고 있다.

print()
print('- - KNeighbors Regressor - -')
kmodel = KNeighborsRegressor(n_neighbors=3).fit(x, y)
kpred = kmodel.predict(x)
print('KNeighborsRegressor pred : ', kpred[:5]) # [20.4  10.43333333  8.56666667  18.2  14.2]
print('k_r2_score : ', r2_score(y, kpred))      # 0.968012077694316

print()
print('- - RandomForest Regressor - -')
rmodel = RandomForestRegressor(n_estimators = 100, criterion='mse').fit(x, y)
#Regressor라서 criterion은 mse를 쓴다
rpred = rmodel.predict(x)
print('RandomForestRegressor pred : ', rpred[:5])    # [21.943  10.642  8.874 18.363  13.555]
print('rf_r2_scroe : ', r2_score(y, rpred))      # 0.9972658987811623    #사실상 과적합..

print()
print('- - XGB Regressor - -')
xmodel = XGBRegressor(n_estimators = 100, criterion='mse').fit(x, y)  
xpred = xmodel.predict(x)
print('XGBRegressor pred : ', xpred[:5])        # [22.095655  10.40437  9.302584  18.499216  12.9007015]
print('xgb_r2_scroe : ', r2_score(y, xpred))    # 0.9999996661140423