# 사번과 이름을 입력하여 로그인에 성공하면 사번과 직원 이름을 받기
#사번, 직원명, 부서명, 부서전화, 연봉, 성별 출력

import MySQLdb
"""
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
"""
import pickle
with open('mydb.dat', 'rb') as obj:
    config = pickle.load(obj)
    
def rala():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        jikwon_no = input('사번 입력 : ')
        jikwon_name = input('이름 입력 : ')
        sql = """
            select jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen
            from jikwon inner join buser on buser_num=buser_no
            where jikwon_no={} and jikwon_name='{}'   #string type으로 들어가야 해서 jikwon_name에 작은따옴표 붙이기
        """.format(jikwon_no, jikwon_name)
        
        cursor.execute(sql)
        datas = cursor.fetchall()
        
        if len(datas) == 0:                                #사번과 이름이 format형식으로 들어가지 못해 데이터를 못읽어오면 0개
            print('존재하지 않습니다.')
            return                                                  #return으로 빠져나오기
        for jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen in datas:
            print('입력완료')
            print('{}, {}, {}, {}, {}'.format(jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen))
        
    except Exception as e:
        print('err : ', e)        
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    rala()