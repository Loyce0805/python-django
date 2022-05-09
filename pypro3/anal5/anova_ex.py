'''
 Created on 2022. 4. 29. ANOVA quiz
'''
# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

import pandas as pd
import scipy.stats as stats

# 귀무가설 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.
# 대립가설 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 있다.

data = pd.read_csv('bread.csv')
data = data.fillna(data['quantity'].mean())
print(data.head(3))
print(data.describe())

result = data[['kind', 'quantity']]
k1 = result[result['kind']==1]
k2 = result[result['kind']==2]
k3 = result[result['kind']==3]
k4 = result[result['kind']==4]
print(k1)
q1 = k1['quantity']
q2 = k2['quantity']
q3 = k3['quantity']
q4 = k4['quantity']

print(stats.shapiro(q1).pvalue)
print(stats.shapiro(q2).pvalue)
print(stats.shapiro(q3).pvalue)
print(stats.shapiro(q4).pvalue)
print()

print(stats.levene(q1, q2, q3, q4).pvalue)  # 0.32689  등분산성이 있다.
print(stats.f_oneway(q1, q2, q3, q4))
# pvalue=0.8482436666841788 > 0.05이므로 귀무가설을 채택한다.


print('-------------------------------------------------')
# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
# 귀무 : 부서에 따른 연봉의 평균에 차이가 없다.
# 대립 : 부서에 따른 연봉의 평균에 차이가 없다.

import MySQLdb
import pickle
import csv

try:
    with open('mydb.dat', mode= 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('읽기 오류 : ',e)
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = '''
        select buser_name,jikwon_pay from jikwon inner join buser
        on buser_num = buser_no
    '''
    cursor.execute(sql)
       
    with open('jik_data.csv', mode = 'w', encoding = 'utf-8') as fobj:
        writer = csv.writer(fobj)
        for row in cursor:
            writer.writerow(row)
    
    df1 = pd.read_csv('jik_data.csv', header= None, 
                      names=['buser','pay'])
    print(df1.head(3))
    
    result = df1[['buser', 'pay']]
    b1 = result[result['buser']=='총무부']
    b2 = result[result['buser']=='영업부']
    b3 = result[result['buser']=='전산부']
    b4 = result[result['buser']=='관리부']
    #print(b1)
    
    p1 = b1['pay']
    p2 = b2['pay']
    p3 = b3['pay']
    p4 = b4['pay']
    
    print('정규성')
    print(stats.shapiro(p1).pvalue)
    print(stats.shapiro(p2).pvalue)
    print(stats.shapiro(p3).pvalue)
    print(stats.shapiro(p4).pvalue)
    print()
    print(stats.levene(p1, p2, p3, p4).pvalue)
    
    print(stats.kruskal(p1, p2, p3, p4))   # pvalue=0.6433438
    # pvalue > 0.05이므로 귀무가설을 채택한다.
    print(stats.f_oneway(p1, p2, p3, p4))  # pvalue=0.745442
    
except Exception as e:
    print('처리 오류:' ,e)
finally:
    cursor.close()
    conn.close()
