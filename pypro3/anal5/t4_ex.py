# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.

import numpy as np
from scipy import stats
import pandas as pd
import MySQLdb
import pickle

try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('읽기 오류 : ', e)
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select buser_name,jikwon_pay 
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql)
    
    df = pd.DataFrame(cursor.fetchall(), 
                       columns = ['부서명','연봉'])
    #print(df.groupby(['부서명']).mean(['연봉']))
    df.groupby(['부서명']).apply(lambda x: x.fillna(x.groupby(['부서명']).mean())) # 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.(?)
    print(df)

    # 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
    # 귀무 : 총무부, 영업부 직원의 연봉의 평균에 차이가 없다.
    # 대립 : 총무부, 영업부 직원의 연봉의 평균에 차이가 있다.
    
    buser1 = df[df['부서명']=='총무부'].연봉
    buser2 = df[df['부서명']=='영업부'].연봉
    print(np.average(buser1),' ',np.average(buser2)) # 5414.285714285715   4908.333333333333

    # 정규성 검증
    print(stats.shapiro(buser1).pvalue) # 0.02604489028453827 < 0.05 불만족
    print(stats.shapiro(buser2).pvalue) # 0.02560843899846077 < 0.05 불만족

    # 등분산성 검증
    print(stats.levene(buser1, buser2).pvalue) # 0.915044305043978 > 0.05 만족
        
    two_sample = stats.mannwhitneyu(buser1, buser2)

    print(two_sample) # MannwhitneyuResult(statistic=51.0, pvalue=0.47213346080125185)
    # pvalue=0.4721 > 0.05 귀무가설 채택.
    # 총무부, 영업부 직원의 연봉의 평균에 차이가 없다.
except Exception as e:
    print('오류 : ', e)
finally:
    cursor.close()
    conn.close()

print()

# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
#    중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
#    기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

exam1 = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
exam2 = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(stats.shapiro(exam1).pvalue)  # 0.3681465 > 0.05
print(stats.shapiro(exam2).pvalue)  # 0.1930028 > 0.05
print(np.mean(exam1), ' ', np.mean(exam2))  # 74.16   81.66
print(stats.ttest_rel(exam1, exam2))
# Ttest_relResult(statistic=-2.6281127723493993, pvalue=0.023486192540203194)
# 해석 : pvalue=0.023486192540203194 < 0.05 귀무가설 기각.
# 학업능력이 변화했다.