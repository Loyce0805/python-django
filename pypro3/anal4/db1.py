'''Created on 2022. 4. 21. 3교시~ '''
# Local Database 연동 후 DataFrame 으로 저장
import sqlite3

sql = "create table if not exists mytab(product varchar(10), maker varchar(10), weight real, price integer)"
# mytab이라는 테이블이 없으면 만드는 거임.

conn=sqlite3.connect(":memory:")    # ram 상에서만 1회용으로 연습
#conn=sqlite3.connect("testdb") # 원래는 db명을 줄 수 있음.
conn.execute(sql)
conn.commit()

stmt = 'insert into mytab values(?,?,?,?)'
data1 = ('신상1', '롯데리아', 45, 5000)
conn.execute(stmt, data1)
data2 = ('신상2', '맥도날드', 55, 5500)
conn.execute(stmt, data2)

cursor = conn.execute("select * from mytab")
rows = cursor.fetchall()
for a in rows:
    print(a)

#DataFrame으로 만들기
import pandas as pd
df1 = pd.DataFrame(rows, columns=['product', 'maker', 'weight', 'price'])
print(df1)

print('-------------')
df2 = pd.read_sql("select * from mytab", conn) #("sql 구문", 커넥션 개체)
print(df2)
# print(df2.to_html())    #웹에 적용할 수 있는 형태로 만들어짐.

print()
# DataFrame을 DB로 저장
print('---DataFrame을 DB로 저장---')
data = {
    'product':['연필', '볼펜'],
    'maker':['모나미', '모나미'],
    'weight':[1.5, 2.3],
    'price':[500, 1000]
}
frame = pd.DataFrame(data)
print(frame)
print()
frame.to_sql('mytab', con=conn ,if_exists='append', index=False)
df3 = pd.read_sql("select * from mytab", conn)
print(df3)                                    # 연필과 볼펜이 추가됨
print(pd.read_sql("select count(*) as count from mytab", conn)) 