'''
Created on 2022. 4. 26. 카이검정
'''
# 교차분석(카이제곱, 카이스퀘어) 가설 검정
# 범주형 자료를 대상으로 교차빈도에 대한 기술통계량(검정통계량)을 제공해 줄 뿐 아니라 교차빈도에 대한
# 통계적 유의성을 검증해 주는 추론통계 분석 기법

import numpy as np
import pandas as pd
data = pd.read_csv("../testdata/pass_cross.csv", encoding='euc-kr')
print(data.head())

# 카이검정 : 두 개의 확률변수는 범주형
# 귀무가설(H0) : 벼락치기 공부하는 것과 합격여부는 관계가 없다.
# 대립가설(H1) : 벼락치기 공부하는 것과 합격여부는 관계가 있다.
# 귀무설정 : ...같다. 다르지 않다. 차이가 없다. 효과가 없다. 보수적으로 선언.
# 대립설정 : 귀무 가설과 반대로 설정

print(data.shape) #(50행, 4열)

print(data[(data['공부함'] == 1) & (data['합격'] == 1)].shape[0]) #공부해서 합격한 사람 18명 # shape[0]은 행, shape[1]은 열
print(data[(data['공부함'] == 1) & (data['불합격'] == 1)].shape[0]) #공부해서 불합격한 사람 7명

print('----- 빈도표 -----')
#ctab = pd.crosstab(index = data['공부함'], columns = data['합격'], margins = True)  
ctab = pd.crosstab(index = data['공부안함'], columns = data['불합격'], margins = True) # margins는 소계(총합)
ctab.columns = ['합격', '불합격', '행의 합']
ctab.index = ['공부함', '공부안함', '열의 합']
print(ctab) #ctab.to_html 해서 나중에 Django 프로젝트 할 때 웹으로 출력할 수 있다! df와 table은 가능.

# 교차분석 연습1 : 수식을 사용
# 관찰값 : 수집된 데이터 값
# 기댓값 : 어떤 확률을 가진 사건을 무한히 반복했을 때 얻을 수 있는 값의 평균으로서 기대할 수 있는 값
# 검정통계량 카이제곱 = 합(관측값 - 기대값)제곱 / 개디갮 : x축의 임의 지점 값을 구함. 임계치를 기준으로 가설을 판단할 때 사용.
# 기대도수 = 빈도표의 (각행의 주변합) * (각 열의 주변합) / 총합

chi2 = (18 - 15) ** 2 / 15 + (7 - 10) ** 2 / 10 + (12 - 15) ** 2 / 15 + (13 - 10) ** 2 / 10
# (빈도표(공부함 합격 수) - 기대도수표(공부함 합격 수)) ** 2 / 기대도수표(공부함 합격 수)) 이걸 셀당 구해서 다 더함.
print('카이제곱 값 : ', chi2) # 3.0 (x축 값이 3이므로 임계치 값을 구해서 귀무가설을 채택인지 기각인지 결정)
print('자유도(df) : ', (2 - 1) * (2 - 1)) # (행의 갯수 - 1) * (열의갯수 - 1)
# 카이제곱표를 통해 임계치 얻기 : df(자유도):1, α(알파값(유의수준)):0.05이므로 임계치(critical value)는 3.84 이다.
# 결론 : chi2값 3.0 < 임계치 3.84 이므로 귀무채택영역 내에 있어 귀무가설을 채택한다.
# 그러므로 벼락치기 공부하는 것과 합격여부는 관계가 없다.는 주장을 유지한다.

# 교차분석 연습2 : 모듈이 제공하는 p-value를 사용
import scipy.stats as stats

chi2, p, _, _ = stats.chi2_contingency(ctab) # stats.chi2_contingency(observed)  observed(관찰값)은 ctab
print('chi2:{}, p-value:{}'.format(chi2, p))
# 결론 : 유의수준(α알파) 0.05 < p-value:0.5578254003710748 이므로 귀무가설 채택  (신뢰구간 아무것도 얘기안하면 기본적으로 95%)
# 검정에 사용된 데이터는 우연히 발생된 데이터다. 귀무가설이 채택되면 우연히 발생된 데이터. 기각되면 필연적으로 발생된 데이터.