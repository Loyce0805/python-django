# 단순 Echo Server (1회용)

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)     # socket(AF_INET(소켓종류), SOCK_STREAM(소켓유형))
serverSock.bind(('127.0.0.1', 8888)) #'127.0.0.1'에 8888포트번호를 열어논다. 소켓을 주소에 바인딩. 튜플값만 가능
serverSock.listen(1)   # TCP리스너 요청 1에 1~5까지의 값을 줄 수 있음
print('server start ...')

conn, addr = serverSock.accept() # 클라이언트가 임의의 컴퓨터에서 연결요청이 들어오면 요청을 받아들임. 요청대기
print('client addr : ', addr)
print('from client message : ', conn.recv(1024).decode())   #클라이언트로부터 메세지를 받는데 그 메세지를 해석해서 출력(디코딩)
conn.close()
serverSock.close()