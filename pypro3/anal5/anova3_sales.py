'''
Created on 2022. 4. 29. Anova
'''
# data.go.kr 사이트에서 어느 음식점 매출데이터와 날씨 데이터를 이용하여 온도 높낮이에 따른 매출액 평균의 차이를 검정

# 온도가 높을 때, 보통일 때, 낮을 때의 매출액

# 귀무가설 : 매출액은 온도에 의해 영향을 받지 않는다.
# 대립가설 : 매출액은 온도에 의해 영향을 받는다.

import numpy as np
import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt

# 자료 읽기1
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv",
                         dtype={'YMD':'object'}) #wt_data랑 병합하려고 연월일은 object로 타입 변환!
print(sales_data.head(3))
print(sales_data.info())

print()
# 자료 읽기2
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-', ''))    #map()은 함수를 실행하는 함수!
# 위 코드 실행 결과 --> 2018-06-01 => 20180601
print(wt_data.head(3))
print(wt_data.info())

print()
# 두 파일을 병합
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm') #sales가 기준이니까 left-outer join
print(frame.head(5), len(frame))
print(frame.columns)

data = frame.iloc[:, [0, 1, 7, 8]]  #모든행, 열 'YMD', 'AMT', 'maxTa', 'sumRn'
print(data.head(3), len(data))  #328일치 데이터
print(data.isnull().sum())  #결측치 없음

print()
# 일별 최고온도를 구간 설정
print(data.maxTa.describe())
# plt.boxplot(data.maxTa)
# plt.show()

# 3구간으로 구간 나누기
data['ta_gubun'] = pd.cut(data.maxTa, bins = [-5, 8, 24, 37], labels = [0, 1, 2]) # -5~8미만이 0, 8~24미만은 1, 24~37미만은 2
print(data.head(3), ' ', data['ta_gubun'].unique())

# 상관분석
print(data.corr())  # maxTa와 AMT는 음의 상관관계.

x1 = np.array(data[data.ta_gubun == 0].AMT) # 낮을 때 매출액
x2 = np.array(data[data.ta_gubun == 1].AMT) # 보통일 때 매출액
x3 = np.array(data[data.ta_gubun == 2].AMT) # 높을 때 매출액
print(x1[:3])
print(x2[:3])
print(x3[:3])

# 등분산성
print(stats.levene(x1, x2, x3)) # pvalue=0.03900 < 0.05 이므로 등분산성 X.

# 정규성
print(stats.ks_2samp(x1, x2).pvalue)    #9.28938415079017e-09
print(stats.ks_2samp(x1, x3).pvalue)    #1.198570472122961e-28
print(stats.ks_2samp(x2, x3).pvalue)    #1.4133139103478243e-13    # --> 3그룹 다 정규성 만족 못함.

print()
# 세 그룹의 온도별 매출액 평균
spp = data.loc[:, ['AMT', 'ta_gubun']]
print(spp.groupby('ta_gubun').mean())
'''                   AMT
    ta_gubun              
    0         1.032362e+06
    1         8.181069e+05
    2         5.537109e+05
'''
print()
print(pd.pivot_table(spp, index=['ta_gubun'], aggfunc='mean'))
'''                    AMT
    ta_gubun              
    0         1.032362e+06
    1         8.181069e+05
    2         5.537109e+05
'''
print(spp[:3])
'''     AMT ta_gubun
    0      0        2
    1  18000        1
    2  50000        1
'''
sp = np.array(spp)
group1 = sp[sp[:, 1] == 0, 0]
group2 = sp[sp[:, 1] == 1, 0]
group3 = sp[sp[:, 1] == 2, 0]

# 매출액 시각화
# plt.boxplot([group1, group2, group3])
# plt.show()

# 일원분산분석
print(stats.f_oneway(group1, group2, group3))
# F_onewayResult(statistic=99.1908012029983, pvalue=2.360737101089604e-34)
# pvalue = 2.360737101089604e-34 < 0.05 이므로 귀무가설 기각
# 매출액은 온도에 영향을 받는다.

print()
# 정규성 만족 X
print(stats.kruskal(group1, group2, group3))  # kruscal-Wallis test 사용
# KruskalResult(statistic=132.7022591443371, pvalue=1.5278142583114522e-29)
# pvalue = 1.5278142583114522e-29 < 0.05 이므로 귀무가설 기각.
# 매출액은 온도에 영향을 받는다.

print()
# 등분산성 만족 X
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(data = data, dv='AMT', between='ta_gubun'))
# pvalue = 7.907874e-35 < 0.05 이므로 귀무가설 기각. 
# 매출액은 온도에 영향을 받는다.
'''
     Source  ddof1     ddof2           F         p-unc       np2
0  ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038
'''
# 해석 : 날씨(온도_더움, 보통, 추움)에 의해 매출에 영향이 있다.


# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_result = pairwise_tukeyhsd(endog = spp['AMT'], groups = spp['ta_gubun'], alpha = 0.05)
print(turkey_result)
'''
           Multiple Comparison of Means - Tukey HSD, FWER=0.05       
=================================================================
group1 group2   meandiff   p-adj    lower        upper     reject
-----------------------------------------------------------------
     0      1 -214255.4486   0.0  -296755.647 -131755.2503   True
     0      2 -478651.3813  -0.0 -561484.4539 -395818.3088   True
     1      2 -264395.9327  -0.0 -333326.1167 -195465.7488   True
-----------------------------------------------------------------
'''
turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()