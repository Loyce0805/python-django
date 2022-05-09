'''
Created on 2022. 4. 29. Anova(분산분석)
'''
# ANOVA(분산분석)
# 세 집단 이상의 평균의 차이를 검정
# 전제조건 : 독립성(집단은 서로 독립적이어야 한다.), 
#          정규성(각 집단은 정규분포를 이루어야 한다.), 
#          불편성(등분산성)(분산이 일정해야 한다. 편향이 없어야 한다. 패턴이 일정해야 한다.)
# 독립변수 : 범주형, 종속변수 : 연속형
# f-value = 그룹간 분산 / 그룹내분산 (F 값이 커지면 p 값이 작은거니까 우연히 발생한 것이 아니라 필연적이고 귀무가설 기각. F 값이 작으면 우연히 발생.)
# 집단 간 분산이 집단 내 분산보다 충분히 큰 것인가를 파악하는 것. 
# 종속변수의 변화(분산) 폭이 독립변수에 의해 주로 기인하는지를 파악하는 것.

# ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 
# 나누어진 각 집단 내의 분산으로 나누고 요인에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.
# * 서로 독립인 세 집단의 평균 차이 검정 *

# 하나의 요인에 속한 집단이 복수 : 일원분산분석(One-way ANOVA)
# 실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv'
# 귀무가설 : 세 가지 교육방법에 따른 교육생 실기시험의 평균에 차이가 없다.
# 대립가설 : 세 가지 교육방법에 따른 교육생 실기시험의 평균에 차이가 있다.

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols  # 선형회귀
import statsmodels.api as sm

data = pd.read_csv('../testdata/three_sample.csv')
print(data.head(3), len(data))
print(data.describe())
print(data.info())

# boxplot으로 이상치를 확인하기
import matplotlib.pyplot as plt
# plt.boxplot(data.score)
# plt.hist(data.score)
# plt.show()

data = data.query('score < = 100')  # 이상치 제거
print(data.describe())  # max(score) = 100으로
# plt.hist(data.score)
# plt.show()

# 등분산(불편성) 확인 : 만족하면 anova, 만족하지 않으면 welch_anova
# 등분산을 만족하지 않으면 데이터 가공을 생각할 수도 있다 - 표준화, 정규화, transformation(자연log를 씌움)
result = data[['method', 'score']]
# print(result)
m1 = result[result['method'] == 1] # method1
m2 = result[result['method'] == 2] # method2
m3 = result[result['method'] == 3] # method3
score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print('등분산성 확인 : ', stats.levene(score1, score2, score3).pvalue)    # 0.113228506 >0.05 만족

# 정규성 확인
print(stats.shapiro(score1))    #ShapiroResult(statistic=0.9447869658470154, pvalue=0.1746741086244583)
print(stats.shapiro(score2))    #ShapiroResult(statistic=0.9591007232666016, pvalue=0.33189886808395386)
print(stats.shapiro(score3))    #ShapiroResult(statistic=0.9333066940307617, pvalue=0.1155870258808136)
print(stats.ks_2samp(score1, score2))   #KstestResult(statistic=0.24725274725274726, pvalue=0.3096879629846001)
print(stats.ks_2samp(score1, score3))   #KstestResult(statistic=0.18269230769230768, pvalue=0.7162094473752455)
print(stats.ks_2samp(score2, score3))   #KstestResult(statistic=0.17261904761904762, pvalue=0.7724081666033108)

# 독립성 확인 : 상관관계 등으로 확인

print()
# 교육방법별 건수 : 교차표
data2 = pd.crosstab(index = data['method'], columns='count')
data2.index = ['방법1', '방법2', '방법3']
print(data2)

# 교육방법별 만족여부 건수 : 교차표
data3 = pd.crosstab(data.method, data.survey)
data3.index = ['방법1', '방법2', '방법3']
data3.columns = ['만족', '불만족']
print(data3)    # .to_html 하면 html 코드로 출력 가능

# f통계량을 얻기 위해 회귀분석 모델을 사용
lm = ols("data['score'] ~  C(data['method'])", data = data).fit()  # score가 종속변수, method가 독립변수. fit()으로 학습을 시켜준다.
# C(독립변수) : 독립변수가 범주형임을 알려주기 위해 독립변수에 C를 두른다.
table = sm.stats.anova_lm(lm, typ=1)    # typ, type 둘 다 가능.
print(table) # 분산 분석표. 보고서 만들 때 꼭 필요. 중요.
# typ=1일 때
#                      df        sum_sq     mean_sq         F    PR(>F)    # df:자유도, sum_sq:제곱합, mean_sq:처리제곱평균, F:검정통계량 
# C(data['method'])   2.0     28.907967   14.453984  0.062312  0.939639    # 처리한 것
# Residual(오차)      75.0  17397.207418  231.962766       NaN       NaN    # 오차
# sum_sq를 df로 나눈 값이 mean_sq
# F 통계량 : 14.453 / 231.96(오차의 평균)
# -> C의 mean_sq를 Residual의 mean_sq로 나눈 게 C의 F 값이다.
# F 값이 작으면 P 값이 커지고, F 값이 커지면 P 값이 작아진다.

# typ=2일 때
#                          sum_sq    df         F    PR(>F)
# C(data['method'])     28.907967   2.0  0.062312  0.939639
# Residual           17397.207418  75.0       NaN       NaN
#
# typ=3일 때
#                           sum_sq    df           F        PR(>F)
# Intercept          118057.846154   1.0  508.951710  3.695277e-35
# C(data['method'])      28.907967   2.0    0.062312  9.396386e-01
# Residual            17397.207418  75.0         NaN           NaN

# p-value : 0.939639 > 0.05 이므로 귀무가설 채택.
# 세 가지 교육방법에 따른 교육생 실기시험의 평균에 차이가 없다.
import numpy as np
print(np.mean(score1), np.mean(score2), np.mean(score3))
# 67.38, 68.35, 68.87

print()
# 사후 검정(Post Hoc Text)
# 분산분석은 세 개 이상의 집단의 평균에 차이 유무만을 알려줌 
# 차이가 난다고 하면 : 세 개 이상의 집단 각각의 집단 간 평균의 차이를 알고 싶은 경우 사후검정 실시.
from statsmodels.stats.multicomp import pairwise_tukeyhsd   # tukey를 가장 많이 사용함. (dunnett, duncan도 있음)
tukey_result = pairwise_tukeyhsd(data.score, groups = data.method)
print(tukey_result)
# 
#     Multiple Comparison of Means - Tukey HSD, FWER=0.05
#     ===================================================
#     group1 group2 meandiff p-adj  lower   upper  reject
#     ---------------------------------------------------
#          1      2   0.9725   0.9  -8.946  10.891  False 유의미한 차이가 있으면 reject가 True
#          1      3   1.4904   0.9 -8.8184 11.7992  False
#          2      3   0.5179   0.9 -9.6127 10.6484  False
#     ---------------------------------------------------
# 
#
tukey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
# reject이 True가 되려면 겹치지 않아야 함. 평균차이가 없다는 뜻이다.