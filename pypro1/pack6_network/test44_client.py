# 단순 Client
import socket
from _socket import AF_INET, SOCK_STREAM

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 종류랑 소켓유형에 socket.을 안붙여도 작동함.
clientSock.connect(('121.134.105.61', 7878))
clientSock.send('안녕 서버님'.encode(encoding = 'UTF_8'))
re_msg = clientSock.recv(1024).decode()
print('수신 자료 : ', re_msg)
clientSock.close()
