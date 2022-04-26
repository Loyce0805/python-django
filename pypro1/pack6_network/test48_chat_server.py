# 멀티 채팅 서버 : socket, thread를 이용

import socket
import threading


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('121.134.105.61', 5555))
ss.listen(5)
print('채팅 서버 서비스 시작...')

users = [] # 채팅 접속 컴의 건수만큼 소켓을 만들어서 여기에 담는다.

def chatUser(conn):
    name = conn.recv(1024)
    data = '^_^ ' + name.decode('UTF_8') + ' 님 입장 ^^' 
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('UTF_8'))   # 모든 접속자에게 접속한 채팅명을 전송
        
        while True:   # 수다는 이 부분에서 떠는거임. 수다메세지를 받아 모든 접속자에게 전송
            msg = conn.recv(1024)
            data = name.decode('UTF_8') + '님 메세지 : ' + msg.decode('UTF_8')
            print(data)      # 이걸로 서버에서도 채팅 나오게 함
            for p in users:
                p.send(data.encode('UTF_8'))
            
    except:
        users.remove(conn)    # 채팅을 종료한 클라이언트 소켓을 users = []에서 제거
        data = name.decode('UTF_8') + '님이 도망갔습니다 ㅠㅠ'
        print(data)
        
        if users:
            for p in users:
                p.send(data.encode('UTF_8'))
        else:
            print('exit')
            
    
while True:
    conn, addr = ss.accept()   # client가 커넥트하는 순간 얘로 들어옴. addr을 안쓸거면 _로 대체 가능. conn이 소켓
    users.append(conn) # 그 conn을 user = []에 담는다. 얘로 소켓이 들어옴.
    th = threading.Thread(target = chatUser, args=(conn,))
    th.start()
    
    