''' 
Created on 2022. 4. 29. chi검정, t검정, Anova 총정리
'''
# jikwon 테이블의 자료로 chi2, t-test, anova 정리

import MySQLdb
import pickle
import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


try:
    with open('mydb.dat', mode= 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('읽기 오류 : ',e)

conn = MySQLdb.connect(**config)
cursor = conn.cursor()

print('교차분석(이원카이제곱검정 : 각 부서:범주형(독립)와 직원평가점수:범주형(종속) 간의 관련성 분석 ---')
# 귀무가설 : 각 부서와 직원평가점수 간에 관련이 없다.
# 대립가설 : 각 부서와 직원평가점수 간에 관련이 있다.

df = pd.read_sql("select * from jikwon", conn)
print(df.head(3))
buser = df['buser_num']
rating = df['jikwon_rating']

ctab = pd.crosstab(buser, rating)   # 이원카이제곱검정이라서 교차표
print(ctab)

chi, p, df, exp = stats.chi2_contingency(ctab)
print('chi:{}, p:{}, df:{}'.format(chi, p, df))
# chi(검정통계량):7.339285714285714, p:0.2906064076671985, df(자유도):6 # 카이제곱검정표에서 critical value(임계값)을 찾아서 아는 방법도 있다.
# p:0.290606 > 0.05 이므로 귀무가설 채택. 각 부서와 직원평가점수 간에 관련이 없다.

print()
print('평균차이분석(t-검정 : 10, 20번 부서:범주형(독립)와 평균 연봉:연속형(종속) 간의 관련성 분석 ---')
# 귀무가설(영가설, H0) : 두 부서 간 연봉 평균은 차이가 없다.
# 대립가설(연구가설, H1) : 두 부서 간 연봉 평균은 차이가 있다.

df_10 = pd.read_sql("select buser_num, jikwon_pay from jikwon where buser_num=10", conn)
df_20 = pd.read_sql("select buser_num, jikwon_pay from jikwon where buser_num=20", conn)
buser10 = df_10['jikwon_pay']
buser20 = df_20['jikwon_pay']
print('평균 : ', np.mean(buser10), ' ',np.mean(buser20))  # 평균 :  5414.28  VS  4908.33
t_result = stats.ttest_ind(buser10, buser20)    # 서로 다른 집단이 두 개이므로 1샘플 ttest가 아니다.
print(t_result)
# Ttest_indResult(statistic=0.4585177708256519, pvalue=0.6523879191675446)
# 해석 : pvalue=0.652387 > 0.05 이므로 귀무가설 채택. => 두 부서 간 연봉 평균은 차이가 없다.

print()
print('분산분석(ANOVA : 각 부서(요인1개:부서, 4그룹이 존재)(범주형:독립)와 평균연봉(연속형:종속) 간의 차이 분석 ---')
# 귀무가설 : 부서 간 평균연봉에 차이가 없다.
# 대립가설 : 부서 간 평균연봉에 차이가 있다.
df3 = pd.read_sql("select buser_num, jikwon_pay from jikwon", conn)
buser = df3['buser_num']
pay = df3['jikwon_pay']

gr1 = df3[df3['buser_num'] == 10]['jikwon_pay']
gr2 = df3[df3['buser_num'] == 20]['jikwon_pay']
gr3 = df3[df3['buser_num'] == 30]['jikwon_pay']
gr4 = df3[df3['buser_num'] == 40]['jikwon_pay']
# print(gr1)

# 시각화
import matplotlib.pyplot as plt
# plt.boxplot([gr1, gr2, gr3, gr4])
# plt.show()

# 방법1
f_sta, pv = stats.f_oneway(gr1, gr2, gr3, gr4)
print('f-value : ', f_sta)  # 0.41244077160708414
print('p-value : ', pv)     # 0.7454 > 0.05 이므로 귀무가설 채택.


print()
# 사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(df3.jikwon_pay, df3.buser_num, alpha=0.05) # 유의수준인 알파(0.05)
print(tukey)
'''
       Multiple Comparison of Means - Tukey HSD, FWER=0.05    
    ==========================================================
    group1 group2  meandiff p-adj    lower      upper   reject
    ----------------------------------------------------------
        10     20 -505.9524 0.9588 -3292.2114 2280.3066  False
        10     30  -85.7143 0.9998  -3217.199 3045.7705  False
        10     40  848.2143 0.9202 -2823.7771 4520.2056  False
        20     30  420.2381 0.9756 -2366.0209 3206.4971  False
        20     40 1354.1667 0.6937 -2028.2234 4736.5568  False
        30     40  933.9286  0.897 -2738.0628 4605.9199  False
    ----------------------------------------------------------
'''

tukey.plot_simultaneous()
plt.show()