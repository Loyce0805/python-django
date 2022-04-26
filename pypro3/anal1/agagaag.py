import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

conn = MySQLdb.connect(**config)
cursor = conn.cursor()
sql = """
select buser_name, jikwon_gen, jikwon_pay
from jikwon inner join buser on buser_no=buser_num
"""
cursor.execute(sql)

# 제시1) "buser_name, buser_name, jikwon_pay" column을 읽어 DataFrame을 작성한 후 처음 2행만 출력하시오.
# 출력 결과
#    부서 성별    연봉
# 0  총무부  남  9900
# 1  영업부  여  8800

df1 = pd.DataFrame(cursor.fetchall(), columns=['부서', '성별', '연봉'])
print(df1.head(2))

# 제시2) pivot_table을 사용해 성별 연봉의 평균을 출력한다.
# 출력 결과
      # 연봉
# 성별     
# 남  5980
# 여  4630
print(df1.pivot_table(['연봉'], index=['성별'], aggfunc=np.mean))

# 제시3) 성별(남, 여) 연봉의 평균으로 시각화를 한다

jik_ypay = df1.groupby(['성별'])['연봉'].mean()
print(jik_ypay.index)
jik_ypay.plot.bar(x=jik_ypay.index, y = jik_ypay, color=['k','r'])
plt.show()

# 제시4) 부서명, 성별로 교차 테이블을 작성한다.
# 출력 결과
# 성별  남  여
# 부서     
# 관리부  2  2
# 영업부  4  8
# 전산부  3  4
# 총무부  6  1

print(pd.crosstab(df1['부서'], df1['성별']))
