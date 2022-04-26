# Thread
# process는 실행가능한 파일을 말한다. 프로세스는 현재 실행 중인 프로그램을 의미하면 tesk라고도 부른다.
# process의 작은 실행단위를 thread라고 한다. thread 기법을 이용하면 여러 개의 thread를 통해 여러 개의 작업을 할 수 있다.
# multi thread에 의해 multi tasking이 가능하다.

import threading, time

def run(id):
    for i in range(1, 11):
        print('id:{}-->{}'.format(id, i))
        time.sleep(0.5)

        
# 1) thread 사용 X
# run('일')   #   순차적
# run('이')

# 2) thread 사용 O    # thread는 랜덤하게 수행됨.
th1 = threading.Thread(target = run, args = (' 일',))
th2 = threading.Thread(target = run, args = (' 이',))   #target은 수행할 메서드 run, args는 id target이 실행이 종료되면 그때 스레드가 끝남.
th1.start()    # 스레드를 실행
th2.start()

th1.join()   # 메인 스레드의 수행을 대기 너 기달려 사용자정의스레드가 끝날때까지 그러면 프로그램종료가 맨 마지막에 수행됨.
th2.join()
print('프로그램 종료')
        
