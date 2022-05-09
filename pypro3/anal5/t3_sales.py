'''
Created on 2022. 4. 28. 2개의 데이터를 하나로 합쳐서 사용하기.
'''
# data.go.kr 사이트에서 어느 음식점 매출데이터와 날씨 데이터를 이용하여
# 강수 여부에 따른 매출의 평균에 차이를 검정.(비가 올 때와 안 올때 매출의 차이를 검정)

# 비가 올 때의 매출액
# 비가 안올 때의 매출액

# 귀무가설 : 강수 여부에 따른 매출액에 차이가 없다.
# 대립가설 : 강수 여부에 따른 매출액에 차이가 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats

# 자료 읽기1
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv"
                         , dtype={'YMD':'object'}) # data type 맞춰주기
print(sales_data.head(3))
print(sales_data.info())

print()
# 자료 읽기2
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-','')) # tm의 - 를 없애주기. # 2018-06-01 => 20180601
print(wt_data.head(3))
print(wt_data.info())

print()
# 두 파일을 날짜로 병합
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')
print(frame.head(5))
print(len(frame))
print(frame.columns)

data = frame.iloc[:, [0, 1, 7, 8]] # 'YMD'연월일, 'AMT'매출액, 'maxTa'최고기온, 'sumRn'강수량
print(data.head(3), len(data)) # 328개의 RAW
print(data.isnull().sum()) # null(결측치) 값 확인 -> 결측치 없음

print('독립표본 t검정 --강수 여부에 따른 매출액의 평균에 차이가 있는가? ----------------')
print(data['sumRn'] > 0) # 여기선 True, False 값

# data['rain_yn'] = (data['sumRn'] > 0).astype(int) # 비옴:1, 비안옴:0
# print(data.head(3))

# print(True * 1, False * 1)  # 1 0
data['rain_yn'] = (data.loc[:, ('sumRn')] > 0) * 1 # 비옴:1, 비안옴:0
print(data.head(3))

# 시각화
import matplotlib.pyplot as plt

sp = np.array(data.iloc[:, [1, 4]])  # 1이 0열, 4가 1열이 된다.
print(sp[:3]) # [[    0     0][18000     1][50000     0]]
tg1 = sp[sp[:, 1] == 0, 0] # 비 안올 때 매출액
tg2 = sp[sp[:, 1] == 1, 0] # 비 올 때 매출액
print(tg1[:3])
print(tg2[:3])

# plt.plot(tg1)
# plt.show()
# plt.plot(tg2)
# plt.show()

# 두 집단의 각 평균
print('비 안올 때 : ',np.mean(tg1), ' ', '비 올 때 : ', np.mean(tg2)) # 761040.2542 VS 757331.5217

# plt.boxplot([tg1, tg2], notch = True, meanline = True, showmeans=True)
# plt.show() 

# 정규성 확인
print(len(tg1), len(tg2))
print(stats.shapiro(tg1).pvalue) # 0.0560494 > 0.05 로 정규성 만족
print(stats.shapiro(tg2).pvalue) # 0.8827397 > 0.05 로 정규성 만족

# 등분산성
print(stats.levene(tg1, tg2).pvalue) # 0.7123452 > 0.05 등분산성 만족

print(stats.ttest_ind(tg1, tg2, equal_var = True)) # 등분산성 만족하니까 equal_var는 True
# Ttest_indResult(statistic=0.10109828602924716, pvalue=0.919534587722196)
# 해석 : pvalue=0.9195 > 0.05 이므로 귀무가설 채택
# 이 음식점은 강수량에 따른 매출액의 평균의 차이는 없다.
