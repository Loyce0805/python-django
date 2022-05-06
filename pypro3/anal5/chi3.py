'''
Created on 2022. 4. 27. 카이제곱검정 : 이원카이제곱 - 교차분할표 이용
'''
# 이원카이제곱 - 교차분할표 이용
# : 두 개 이상의 변인(집단 또는 범주)을 대상으로 검정을 수행한다.
# 분석대상의 집단 수에 의해서 독립성 검정과 동질성 검정으로 나뉜다.
# 독립성(관련성) 검정
# - 동일 집단의 두 변인(학력수준과 대학진학 여부)을 대상으로 관련성이 있는가 없는가?
# - 독립성 검정은 두 변수 사이의 연관성을 검정한다.
# 실습 : 교육수준과 흡연율 간의 관련성 분석 : 'smoke.csv'

import pandas as pd
import scipy.stats as stats

data = pd.read_csv("../testdata/smoke.csv")
print(data.head(3))
print(data.tail(3))
print(data['education'].unique())  # [1 2 3]   # 교육수준 (독립변수 : 영향을 주는) - 범주형
print(data['smoking'].unique())    # [1 2 3]   # 흡연률   (종속변수 : 영향을 받는) - 범주형

# 귀무 : 교육수준과 흡연율은 관련이 없다. (독립이다. 별개다.)
# 대립 : 교육수준과 흡연율은 관련이 있다. (독립이 아니다.)

# 교차표 사용(변인이 2개(education, smoking))
ctab = pd.crosstab(index = data['education'], columns = data['smoking'])
# ctab = pd.crosstab(index = data['education'], columns = data['smoking'], normalize=True) # nomalize를 통해 비율로 출력 가능

ctab.index = ['대학원졸', '대졸', '고졸']
ctab.columns = ['과흡연', '보통', '노담']
print(ctab)  # 교육수준 별 흡연 인원 수 확인

chi_result = [ctab.loc['대학원졸'],ctab.loc['대졸'],ctab.loc['고졸']]
print(chi_result)
# chi2, p, ddof, exp = stats.chi2_contingency(chi_result)
chi2, p, ddof, exp = stats.chi2_contingency(ctab) # ctab을 써도 결과 똑같이 나온다.
print(chi2, p, ddof, exp)  # exp는 예측값인데 써먹을 데가 없어서  _로 놔둔다.
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, ddof))
# chi2:18.910915739853955, p:0.0008182572832162924, ddof:4

# 해석 : p:0.0008182572 < 0.05 이므로 귀무가설 기각, 대립가설 채택.
# 교육수준과 흡연률은 관련이 있다. (독립이 아니다.)

print('----------------------------')
# 실습) 국가전체와 지역에 대한 인종 간 인원수로 독립성 검정 실습
# 두 집단(국가전체 - national, 특정지역 - la)의 인종 간 인원수의 분포가 관련이 있는가?
# 귀무가설 : 국가전체와 지역에 대한 인종 간 인원수는 관련이 없다. (독립적이다)
# 대립가설 : 국가전체와 지역에 대한 인종 간 인원수는 관련이 있다. (독립적이지 않다)
national = pd.DataFrame(["white"] * 100000 + ["hispanic"] * 60000 +
                        ["black"] * 50000 + ["asian"] * 15000 + ["other"] * 35000)
la = pd.DataFrame(["white"] * 600 + ["hispanic"] * 300 + ["black"] * 250 +
                  ["asian"] * 75 + ["other"] * 150)
na_table = pd.crosstab(index=national[0], columns='count')
print(na_table)
la_table = pd.crosstab(index=la[0], columns='count')
print(la_table)

na_table['count_la'] = la_table['count']
print()
print(na_table)

chi2, p, df, _ = stats.chi2_contingency(na_table)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, ddof))
# 해석 : p:0.0011800 < 0.05 이므로 귀무 기각.
