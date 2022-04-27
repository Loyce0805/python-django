'''
Created on 2022. 4. 21.

'''
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False  # 음수 값 깨짐 방지

try:
    with open('mydb.dat',mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결오류:',e)
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no,jikwon_name,buser_name,jikwon_pay,jikwon_jik
        from jikwon inner join buser
        on buser_num = buser_no
    """
    cursor.execute(sql)
    
    df = pd.DataFrame(cursor.fetchall(), columns=['사번','이름','부서명','연봉','직급'])
    # print(df)
# - DataFrame의 자료를 파일로 저장
    # with open('jik_data2.csv',mode='w',encoding="UTF-8") as fobj:
    #     write = csv.writer(fobj)
    #     for r in cursor:
    #         write.writerow(r)

# - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    df = pd.read_sql(sql, conn)
    df.columns = ['번호','이름','부서','연봉','직급']
    print(df)
    print('부서명별 연봉의 합', df.groupby(['부서'])['연봉'].sum())
    print('부서명별 연봉의 최대값', df.groupby(['부서'])['연봉'].max())
    print('부서명별 연봉의 최소값', df.groupby(['부서'])['연봉'].min())
    
    # print('부서명별 연봉의 최소값 :',df.groupby(['부서'])['연봉'].mean())
# - 부서명, 직급으로 교차테이블을 작성(crosstab)
    ctab = pd.crosstab(df['부서'],df['직급'], margins=True)
    print(ctab)
    
# - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    print('df.index :', df.index)  # RangeIndex(start=0, stop=30, step=1)
    for i in range(1, len(df.index) - 1):
        sql2 = """
        select gogek_no,gogek_name,gogek_tel  
        from gogek inner join jikwon
        on gogek_damsano=jikwon_no
        where jikwon_no={}
        """.format(str(df.index[i]))
        #print(sql2)
        cursor.execute(sql2)
        result = cursor.fetchone()
        if result == None:
            print(df['이름'][i + 1], '담당고객 X')
        else:
            print(df['이름'][i + 1], '직원담당고객')
            df2 = pd.read_sql(sql2, conn)
            df2.columns = ['고객번호','고객명','고객전화']
            df2.set_index('고객번호', inplace = True)
            print(df2)
    
# - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    jik_ypay = df.groupby(['부서'])['연봉'].mean()
    print(jik_ypay, type(jik_ypay)) # Series

    plt.barh(range(len(jik_ypay)), jik_ypay,alpha = 0.5)
    plt.xlabel('연봉')
    plt.yticks([0,1,2,3], labels=['관리부', '영업부', '전산부', '총무부'])
    plt.ylabel('부서별')
    plt.show()

except Exception as e:
    print('처리오류:',e)
finally:
    cursor.close()
    conn.close()