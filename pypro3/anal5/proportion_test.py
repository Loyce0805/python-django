'''  
Created on 2022. 4. 29. Proportion(비율검정)
'''
# 추론통계 분석 중 비율검정
# - 비율검정 특징
# : 집단의 비율이 어떤 특정한 값과 같은지를 검증.
# : 비율 차이 검정 통계량을 바탕으로 귀무가설의 기각여부를 결정.

import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# one-sample
# A회사에는 100명 중에 45명이 흡연을 한다. 국가 통계를 보니 국민 흡연율은 35%라고 한다.
# 비율이 같냐?
# 귀무가설 : A회사의 흡연율과 국민 흡연율은 비율이 같다.
# 대립가설 : A회사의 흡연율과 국민 흡연율은 비율이 다르다.
count = np.array([45])
nobs = np.array([100])
val = 0.35

z, p = proportions_ztest(count = count, nobs=nobs, value=val) # 비율을 구하기 때문에 z를 쓴다.
print(z)    # [2.01007563]
print(p)    # [0.04442318] < 0.05 이므로 귀무가설 기각. A회사의 흡연율과 국민 흡연율은 비율이 다르다.


# two-sample
# A회사 사람들 300명 중 100명이 커피를 마시고, B회사 사람들 400명 중 170명이 커피를 마셨다.
# 비율이 같냐? (비율 동일 여부 확인)
# 귀무가설 : 두 회사의 커피를 마시는 비율은 같다.
# 대립가설 : 두 회사의 커피를 마시는 비율은 같지 않다.

count1 = np.array([100, 170])
nobs1 = np.array([300, 400])
z, p = proportions_ztest(count=count1, nobs=nobs1, value=0) # 비율이 제시되지 않았기 때문에 value=0으로 설정한다.
print(z)    # -2.4656701201792273
print(p)    # 0.01367 < 0.05 이므로 귀무가설 기각. 두 회사의 커피를 마시는 비율은 같지 않다.