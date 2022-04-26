# 단순 Client Server
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8888))
clientSock.send('안녕 반가워'.encode(encoding = 'UTF_8', errors = 'strict')) #error는 안써도 됨.
clientSock.close()




