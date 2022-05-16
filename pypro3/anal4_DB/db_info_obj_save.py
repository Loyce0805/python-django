# DB 연결 정보를 객체로 저장
import pickle

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

with open(file = 'mydb.dat', mode = 'wb') as obj:
    pickle.dump(config, obj)