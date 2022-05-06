'''
Created on 2022. 4. 27.
'''
# 이원카이제곱
# 동질성 검정 - 두 집단의 분포가 동일한가? 다른 분포인가? 를 검증하는 방법이다. 두 집단 이상에서 각 범주(집단) 간의 비율이 서로
# 동일한가를 검정하게 된다. 두 개 이상의 범주형 자료가 동일한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다.

# 동질성 검정실습1) 교육방법에 따른 교육생들의 만족도 분석 - 동질성 검정 survey_method.csv
# 귀무 : 교육방법에 따른 교육생들의 만족도에 차이가 없다. 동질이다. 분포가 같다.
# 대립 : 교육방법에 따른 교육생들의 만족도에 차이가 있다. 동질이 아니다. 분포가 다르다. 

import pandas as pd
import scipy.stats as stats

data = pd.read_csv("../testdata/survey_method.csv")
print(data.head(5))
print(data['method'].unique())  # [1 2 3]
print(data['survey'].unique())  # [1 2 3 4 5]

# 교차표
ctab = pd.crosstab(index = data['method'], columns = data['survey'])
ctab.columns = ['매우만족', '만족', '보통', '불만족', '매우불만족']
ctab.index = ['방법1', '방법2', '방법3']
print(ctab)

chi2, p, df, _ = stats.chi2_contingency(ctab)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, df))
# 해석 : p: 0.586457 > 0.05로 귀무 채택!
# 교육방법에 따른 교육생들의 만족도에 차이가 없다.



print('--------------------')
# 동질성 검정 실습2) 연령대별 sns 이용률의 동질성 검정
# 20대에서 40대까지 연령대별로 서로 조금씩 그 특성이 다른 SNS 서비스들에 대해 
# 이용 현황을 조사한 자료를 바탕으로 연령대별로 홍보전략을 세우고자 한다.
# 연령대별로 이용 현황이 서로 동일한지 검정해 보도록 하자.
# 귀무가설 : 연령대별로 sns 이용률은 동일하다.
# 대립가설 : 연령대별로 sns 이용률은 동일하지 않다.
data2 = pd.read_csv("../testdata/snsbyage.csv")
print(data2.head(5), len(data2)) #데이터 길이 1439
print(data2['age'].unique()) #[1 2 3]
print(data2['service'].unique()) #['F' 'T' 'K' 'C' 'E']
# 교차표
ctab2 = pd.crosstab(index = data2['age'], columns = data2['service'])
print(ctab2)

chi2, p, df, _ = stats.chi2_contingency(ctab2)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, df))
# 해석 : p:1.167906420e-18 < 0.05로 귀무가설 기각 (p값이 거의 0에 가까운 값으로, 0.05보다 작다.)
# 연령대별로 sns 이용률은 동일하지 않다.

print('-------------------------------------')
# 만약에 snsbyage.csv 데이터가 모집단이라면 표본 추출 후 가설검정을 진행한다.
sample_data = data2.sample(n=500, replace=False) #replace=False면 비복원추출, True면 복원추출
print(sample_data.head(3), len(sample_data))

ctab3 = pd.crosstab(index = sample_data['age'], columns = sample_data['service'])
print(ctab3)

chi2, p, df, _ = stats.chi2_contingency(ctab3)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, df))
# 해석 : p:6.996082771e-06 < 0.05 이므로 귀무가설 기각 (p값이 거의 0에 가깝다)