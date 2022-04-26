# database 연동 프로그래밍
# LOCAL
# 개인용 database : sqlite3 - 파이썬에 기본 모듈로 제공
import sqlite3
print(sqlite3.sqlite_version)

print()
# conn = sqlite3.connect('exam.db')     # DB와 연결
conn = sqlite3.connect(':memory:')   # 실험용 - ram에 생성

try:
    cur = conn.cursor()               # SQL문 실행
    #속도는 char(10)이 빠르고 ram을 아끼는건 varchar(10)임. varchar는 10중에 5글자만 쓰면 5글자만 용량차지
    cur.execute("create table if not exists friends(name text, phone text, addr text)") # text는 아주 많은양의 데이터고 varchar는 데이터 정해져있음
    #cur.execute("""create table if not exists friends(name text, phone text, addr text)""")
    
    cur.execute("insert into friends values('홍길동', '111-1111', '서초1동')")
    cur.execute("insert into friends values(?, ?, ?)", ('신기루', '222-2222', '서초2동'))
    inputData = ('신선한', '333-2222', '서초2동')
    cur.execute("insert into friends values(?, ?, ?)", inputData)
    conn.commit()
    
    cur.execute("select * from friends")
    #print(cur.fetchone()) # 하나만 읽을거야
    print(cur.fetchall())
    
    print()
    cur.execute("select name, addr, phone from friends") # 다시 읽어줘야한다?
    for r in cur:
        print(r[0], r[1], r[2])
    

except Exception as e:
    print('err : ', e)
    conn.rollback()
finally:
    cur.close()
    conn.close()

