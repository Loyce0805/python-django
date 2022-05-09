'''
Created on 2022. 4. 28. 단일표본(one_sample) T검정(T-Test)
'''

# 평균차이분석
# 두 집단 이하의 평균 또는 비율 차이 검정
# t분포는 표본평균을 이용해 정규분포의 평균을 해석할 때 사용한다.
# 독립변수 : 범주형, 종속변수 : 연속형

# 단일 모집단의 평균에 대한 가설검정(one samples t-test)
# 하나의 집단에 대한 표본평균이 예측된 평균(모집단의 평균)과 같은지를 검정.
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 연습 1) 어느 남성 집단의 평균 키는 177이다.(모집단의 평균키가 177) 남성 집단의 표본 데이터를 추출해 평균차이 검정.
# 귀무 : 남성 집단의 평균 키는 177이다.
# 대립 : 남성 집단의 평균 키는 177이 아니다. (양측 검정)
# 대립 : 남성 집단의 평균 키는 177 보다 크다(작다). (단측 검정)

one_sample = [167.0, 182.7, 169.6, 176.8, 185.0]
print(np.array(one_sample).mean()) # 176.219997 vs 177 평균에 차이가 있는가? 통계적으로 검정
# 데이터의 정규성 확인
print(stats.shapiro(one_sample))   # pvalue=0.540051 > 0.05 이므로 정규성 만족(이때는 0.05보다 커야함.)(정규성이 만족하지 않으면 데이터가 적어서 그런거니 데이터를 늘린다.)

# 검정 수행
result = stats.ttest_1samp(one_sample, popmean=177) # popmean = 모집단평균
print('t값:%.3f, p-value:%.3f'%result) # t값:-0.221, p-value:0.836
# 해석 : p-value:0.836 > 0.05 이므로 귀무가설 채택(남성 집단의 평균 키는 177이다.)

print()
result2 = stats.ttest_1samp(one_sample, popmean=165) # 모집단의 평균 키가 165
print('t값:%.3f, p-value:%.3f'%result2) # t값:3.185, p-value:0.033
# 해석 : p-value:0.033 > 0.05 이므로 귀무가설 기각(남성 집단의 평균 키는 177이 아니다.)

print('-------------------------')
# 실습 예제 2) A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정)
# A중학교 1학년 1반 학생들의 국어 시험결과는 늘 평균이 80점이라고 알려져 있다.

# 귀무가설 : A중학교 1학년 1반 학생들의 국어 시험결과 평균은 80점이다.
# 대립가설 : A중학교 1학년 1반 학생들의 국어 시험결과 평균은 80점이 아니다.(80보다 크다, 80보다 작다)
data = pd.read_csv("../testdata/student.csv")
print(data.head(3))
print(data['국어'].mean())  # 72.9 VS 80 차이가 있느냐?
# print(data.describe()) 로도 평균점수 확인 가능

print(stats.shapiro(data.국어)) # pvalue=0.012959 < 0.05 정규성 만족하지 않는다. 따라서 데이터를 가공하거나 더 수집하거나 해야한다. 
# ShapiroResult(statistic=0.872416, pvalue=0.012959) 
print(stats.ttest_1samp(data.국어, popmean=80))
# Ttest_1sampResult(statistic=-1.3321801667713213, pvalue=0.19856051824785262)
# pvalue=0.1985605 > 0.05 이므로 귀무가설 채택. 수집된 데이터는 우연히 발생된 자료이다. 72.9랑 80이랑 차이가 없다고 봄.

print('\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# 실습 예제 3) 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.

# 귀무가설 : 여아 신생아 몸무게의 평균은 2800(g)이다.
# 대립가설 : 여아 신생아 몸무게의 평균은 2800(g)보다 크다.

data = pd.read_csv("../testdata/babyboom.csv")
print(data.head(3), len(data)) # gender:1 여아 gender:2 남아
fdata = data[data.gender == 1]
print(fdata.head(3), len(fdata))
print(np.mean(fdata.weight))  # 3132 vs 2800 차이가 있는가?

# 정규성 확인
#print(stats.shapiro(fdata.iloc[:, 2])) # ShapiroResult(statistic=0.8702830076217651, pvalue=0.017984798178076744)
print(stats.shapiro(fdata.weight)) # ShapiroResult(statistic=0.8702830076217651, pvalue=0.017984798178076744)
# p-value = 0.017984 정규성을 만족하지 않는다.

# 시각화
sns.distplot(fdata.iloc[:, 2], kde = True) # kde=True 밀도 곡선도 같이 보기.
plt.show()

stats.probplot(fdata.iloc[:, 2], plot = plt) # R에서 봤던 Q-Q plot 정규성을 확인할 때 Q-Q plot을 쓸 수도 있다.
plt.show()

print(stats.ttest_1samp(fdata.weight, popmean = 2800))
# Ttest_1sampResult(statistic=2.233187669387536, pvalue=0.03926844173060218)
# p-value = 0.0392 < 0.05 이므로 귀무가설을 기각하고 대립가설을 채택(기존에 알려진 2800g보다 평균 몸무게가 증가했다.)















