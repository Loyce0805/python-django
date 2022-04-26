# 원격 데이터 베이스 연동
import MySQLdb

# conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
# print(conn)
# conn.close

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config) # packing연산자에서 dict 타입은 **을 쓴다.
    cursor = conn.cursor()
    """
    print('insert-----')
    #isql = "insert into sangdata(code, sang, su, dan) values(10, '신상', 5, 5000)"
    #isql = "insert into sangdata(code, sang, su, dan) values(%s, %s, %s, %s)"
    isql = "insert into sangdata values(%s, %s, %s, %s)"
    sql_data = (10, '신상', 5, 5000)   
    #sql_data = 10, '신상', 5, 5000    # 가독성을 위해 이거보단 괄호있는 위에꺼 추천
    cursor.execute(isql, sql_data)
    conn.commit()
    """
    
    """
    print('update-----')
    usql = "update sangdata set sang=%s, su=%s where code=%s" # where절 무조건 넣어야 함 안그러면 큰일남.
    sql_data = ('얼죽아', 30, 10)
    cou = cursor.execute(usql, sql_data) #cou는 update 했을때 return값임
    print('cou : ', cou)
    conn.commit()
    """
    """
    print('delete-----')
    input_code = '10'
    #dsql = "delete from sangdata where code=" + input_code  # secure coding 가이드라인에 위배됨. 해킹당하기 딱 좋음.
    
    #dsql = "delete from sangdata where code=%s"
    # cou = cursor.execute(dsql, (input_code,))
    
    dsql = "delete from sangdata where code='{0}'".format(input_code)
    cou = cursor.execute(dsql)           # tuple 값으로 input_code를 넣어줘야한다고 함 / input_code는 위에 format에서 들어가니 안들어가도 됨.
    conn.commit()
    if cou > 0:
        print('삭제 성공')
    else:
        print('삭제 실패')
    """
    
    print('select-----')
    sql = "select code, sang, su, dan from sangdata" # 이왕이면 sql문장은 큰따옴표 권장
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        #print(data)                                         #원래 이렇게 하는데 아래처럼 해도 됨
        print('%s %s %s %s'%data)
    """    
    print()
    for data in cursor:
        print(data[0], data[1], data[2], data[3])

    print()
    for (code, sang, su, dan) in cursor:    #가독성을 위해 아래가 아니라 위를 추천
        print(code, sang, su, dan)

    print()
    for (a, kbs, mbc, dan) in cursor:           #커서를 이용하기 때문에 컬럼명이 아닌 변수이다.
        print(a, kbs, mbc, dan)
    """
except Exception as e:
    print('err : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()