import threading, time
from threading import Thread, Condition

g_count = 0  # 전역변수는 자동으로 스레드의 공유자원이 됨.
lock = Condition()    # 스레드 공유 자원 접근에 제한을 강제하기 위한 잠극객체

def threadCount(id, count):
    global g_count
    
    for i in range(count):
        # lock.acquire()
        print('id %s==>count:%s, g_count:%s'%(id, i, g_count))
        g_count += 1
        # lock.release()    #lock을 통해 공유자원의 충돌이 안나게 할 수 있다.
        
for i in range(1, 6):
    Thread(target = threadCount, args = (i, 5)).start()
    
time.sleep(1) #여기서 지체를 하니까 join없이 아래 print문이 마지막에 수행가능

print('최종 g_count : ', g_count)
print('bye')