'''
Created on 2022. 4. 28. 독립표본(two_sample) T검정(T-Test)
'''
# 두 집단 평균 차이 검정
# 두 집단의 가설검정 – 실습 시 분산을 알지 못하는 것으로 한정하겠다.
# ※ 선행 조건 : 정규성 & 등분산성 확인
# * 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.


# 실습1) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정
# 귀무가설 : 남녀 간의 파이썬 시험 평균의 차이가 없다.
# 대립가설 : 남녀 간의 파이썬 시험 평균의 차이가 있다.
import pandas as pd
from numpy import average
from scipy import stats

male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]
print(average(male), ' ', average(female))  # male:83.8 vs female:72.24

# 정규성, 등분산성 생략
two_sample = stats.ttest_ind(male, female)  # 두 개의 표본에 대해 독립표본 t검정을 실행. ind는 independence
print(two_sample)
# --> Ttest_indResult(statistic=1.233193127, pvalue=0.2525076844) # static은 검정통계량 t값. pvalue가 크니까 t값이 작다. 
# ★두 개의 집단의 평균의 차이는 ttest를 한다!
# 해석 : pvalue=0.2525076844 > 0.05 이므로 귀무가설 채택


print('***' * 20)
# 실습2) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv'
# 귀무가설 : 두 가지 교육방법에 따라 평균시험 점수에 차이가 없다.
# 대립가설 : 두 가지 교육방법에 따라 평균시험 점수에 차이가 있다.

data = pd.read_csv('../testdata/two_sample.csv')
print(data.head(3))

ms = data[['method', 'score']]
print(ms.head(3))

m1 = ms[ms['method'] == 1]  #교육방법1
m2 = ms[ms['method'] == 2]  #교육방법2

score1 = m1['score']    #교육방법1의 점수
score2 = m2['score']    #교육방법2의 점수
# print(score1)
# print(score2)

# 참고 : df.isnull().sum() -> null 값 확인 방법.

# sco1 = score1.fillna(0) #NaN을 0으로 채우기
# sco2 = score2.fillna(0) #NaN을 0으로 채우기
sco1 = score1.fillna(score1.mean()) #NaN을 평균으로 채우기
sco2 = score2.fillna(score2.mean()) #NaN을 평균으로 채우기

# 정규성 확인 : 0.05보다 같거나 크면 만족 
print(stats.shapiro(sco1)) # pvalue=0.36799
print(stats.shapiro(sco2)) # pvalue=0.67141

# 정규성 시각화
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.histplot(sco1, kde=True)
# sns.histplot(sco2, kde=True)
# plt.show()
# 정규성을 만족한다. 종모양에 가깝다.

# 등분산성 확인 : 0.05보다 같거나 크면 만족 | 모수검정 - levene(가장 많이 사용), fligner / 비모수검정 - bartlett(데이터의 갯수가 작을 때(30개 미만일 때))
print(stats.levene(sco1, sco2).pvalue) # 0.45684 # 모수 검정 제일 많이 씀.
print(stats.fligner(sco1, sco2).pvalue) # 0.44323
print(stats.bartlett(sco1, sco2).pvalue) # 0.26789 # 비모수 검정 얘도 많이 씀.

result = stats.ttest_ind(sco1, sco2, equal_var=True)    # 등분산성 만족할 때
# result = stats.ttest_ind(sco1, sco2, equal_var=False)    # 등분산성 만족 X
print('검정통계량t : %.5f, p-value : %.5f'%result)
# 검정통계량t : -0.19649, p-value : 0.84505
# 해석 : p-value: 0.84505 > 0.05 이므로 귀무가설 채택
# 두 가지 교육방법에 따른 평균시험 점수에 차이가 없다

# 참고 : 정규성 만족 못한 경우
# stats.mannwhitneyu(sco1, sco2) # 표본의 크기가 다를 때
# stats.wilcoxon(sco1, sco2) # 표본의 크기가 같을 때
