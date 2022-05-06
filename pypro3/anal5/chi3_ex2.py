'''
Created on 2022. 4. 27.
'''
'''
카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
그렇다면 정말로 jikwon_jik과 jikwon_pay 간의 관련성이 없는지 분석. 가설검정하시오.
  예제파일 : MariaDB의 jikwon table 
  jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
  jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
  조건 : NA가 있는 행은 제외한다.
'''
#귀무가설 : A회사의 직급과 연봉은 관련이 없다. 독립이다.
#대립가설 : A회사의 직급과 연봉은 관련이 있다. 종속적이다.

import pandas as pd
import scipy.stats as stats
import MySQLdb
import pickle
import numpy as np

try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
    
except Exception as e:
    print('읽기 오류 : ',e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_jik, jikwon_pay from jikwon
        """
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(),columns=['직급','연봉']).dropna()
    #print(df.shape) #(30,2)
    #print(df.직급.unique()) #['이사' '부장' '과장' '대리' '사원']
    
    #cut으로
    bins = [1000,3000,5000,7000,10000]
    bins_label = [1,2,3,4]
    df["구간"] = pd.cut(df["연봉"], bins, right=False, labels=bins_label)
    print(df.head(3))
    
    #for문으로
    '''lst = []
    for tmp in df.연봉:
        if int(tmp)>=1000 and int(tmp)<=2999:
            lst.append(1)
        elif int(tmp)>=3000 and int(tmp)<=4999:
            lst.append(2)
        elif int(tmp)>=5000 and int(tmp)<=6999:
            lst.append(3)
        else:
            lst.append(4)
    df['구간'] = lst
    '''
    ctab = pd.crosstab(columns = df['직급'],index=df['구간'])
    print(ctab)

    # 카이제곱 검정
    chi2,p,_,_ = stats.chi2_contingency(observed = ctab)
    print(chi2,p) #37.40349394195548 0.00019211533885350577
    #해석 : 유의확률 p-value의 값이 0.00019로, 0.05 보다 작으므로, 귀무가설 기각. 
    #검정에 참여한 데이터는 필연적으로 발생한 것이다.
    #따라서, 직급과 연봉은 관련이 있다.

except Exception as e:
    print('오류 : ', e)
finally:
    cursor.close()
    conn.close()