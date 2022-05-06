'''
Created on 2022. 4. 27.
'''
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
# 예제파일 : cleanDescriptive.csv
# 칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
# 조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
# 귀무가설 : 부모학력 수준이 자녀의 진학여부와 관련이 없다.(독립이다.)
# 대립가설 : 부모학력 수준이 자녀의 진학여부와 관련이 있다.(독립이 아니다.)

import pandas as pd
import scipy.stats as stats
data = pd.read_csv("../testdata/cleanDescriptive.csv").dropna(subset=['level', 'pass'])
pd.set_option('display.max_columns', 500)
print(data.head(3))
print(data.columns)
print(data.shape)    # (248,14) -> (225,14)
print(data.describe())
print(data['level'].unique())    # [1. 2. 3.]
print(data['pass'].unique())     # [1. 2.]

# 교차표
ctab = pd.crosstab(index = data['level'], columns = data['pass'])
ctab.index = ['고졸','대졸','대학원졸']
ctab.columns = ['합격', '불합격']
print(ctab)

# 카이제곱 검정
chi2, p, df, _ = stats.chi2_contingency(observed = ctab)
print(chi2, p)  # 2.7669512025956684 0.25070568406521365
print(df)
# 해석 : 유의확률(p-value) 0.250705 > 0.05 이므로 귀무가설 채택. 검정에 참여한 데이터는 우연히 발생한 것이다.
# 부모학력 수준이 자녀의 진학여부와 관련이 없다.  독립이다.