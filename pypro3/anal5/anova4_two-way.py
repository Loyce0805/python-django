'''
Created on 2022. 4. 29. ANOVA two-way(이원분산분석)
'''
# two-way anova(이원분산분석 - 요인이 2개)

import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import urllib.request
import matplotlib.pyplot as plt
import statsmodels.api as sm

plt.rc('font', family=('malgun gothic'))

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt"
data = pd.read_csv(urllib.request.urlopen(url))
print(data.head(3), data.shape) # (36, 3)

# data.boxplot(column ='머리둘레', by='태아수', grid=False)
# plt.show()

# 귀무가설 : 태아수와 관측자수는 태아의 머리둘레와 관련이 없다. (머리둘레의 평균과 차이가 없다)
# 대립가설 : 태아수와 관측자수는 태아의 머리둘레와 관련이 있다. (머리둘레의 평균과 차이가 있다)

# 상호 작용을 주지 않은 경우
reg = ols("data['머리둘레'] ~ C(data['태아수']) + C(data['관측자수'])", data=data).fit()
result = sm.stats.anova_lm(reg, typ=2)  # f_oneway는 있지만 f_twoway는 없으니까 anova_lm으로 해줘야함.
print(result)
'''
                         sum_sq    df            F        PR(>F)
    C(data['태아수'])   324.008889   2.0  2023.182239  1.006291e-32
    C(data['관측자수'])    1.198611   3.0     4.989593  6.316641e-03
    Residual           2.402222  30.0          NaN           NaN
'''

print()
# 상호 작용이 있는 경우. 이렇게 해줘야 함.
formula = "머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수) "
# data에 data를 넣었기 때문에 data['태아수']이렇게 안써줘도 된다.

reg2 = ols(formula, data=data).fit()
result2 = sm.stats.anova_lm(reg2, typ=2) 
# f_oneway는 있지만 f_twoway는 없으니까 anova_lm으로 해줘야함.
print(result2)
'''
                        sum_sq    df            F        PR(>F)
    C(태아수)          324.008889   2.0  2113.101449  1.051039e-27
    C(관측자수)           1.198611   3.0     5.211353  6.497055e-03
    C(태아수):C(관측자수)    0.562222   6.0     1.222222  3.295509e-01
    Residual          1.840000  24.0          NaN           NaN
'''
# PR(>F) =3.295509e-01 > 0.05 이므로 귀무가설을 채택.
# 태아수와 관측자수는 태아의 머리둘레와 관련이 없다.
