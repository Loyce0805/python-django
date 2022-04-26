# 멀티 채팅 클라이언트 : socket, thread

import socket
import threading
import sys

def handle(socket):    
    while True:
        data = socket.recv(1024)
        if not data:continue
        print(data.decode('UTF_8'))
        
sys.stdout.flush()         # 파이썬의 표준 출력은 버퍼링이 된다.버퍼링 된 내용을 flush()로 클리어. 안쓰면 버퍼가 지워지지 않아서 출력이 제대로 안될수도 있음.

name = input('채팅명 입력 : ')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('121.134.105.61', 5555))
cs.send(name.encode('UTF_8'))

th = threading.Thread(target = handle, args = (cs,))
th.start()

while True:
    msg = input()     # 채팅 메세지를 입력
    sys.stdout.flush()
    if not msg:continue
    cs.send(msg.encode('UTF_8'))

cs.close()