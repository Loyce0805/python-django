#수령액은 급여액 – 공제액
datas = []
import time
def inputfunc():
    count=0
    while True:
     
        def processfunc(n, name, pay, year):
            wy=(time.localtime()[0])-int(year)
            p0 = int(pay) #기본금
            p1 = 0 #근속수당
            p2 = 0 #공제액
            p3 = 0 #수령액
            
            if wy <= 3 and wy >=0:
                p1=150000
            elif wy <= 8 and wy >=4:
                p1=450000
            elif wy >=9:
                p1=1000000
            
            if p0 >= 3000000:
                p2=0.5
            elif p0 >= 2000000:
                p2=0.3
            elif p0 < 2000000:
                p2=0.15
                
            p3=(p0+p1)- (p0+p1)*p2
            datas.append((n, name, p0, wy, p1, p2, p3))
                    
        print('사번, 이름, 기본금, 입사년도')
        n, name, pay, year = input().split(',')
        processfunc(n, name, pay, year)
        
        print('계속하시겠습니다?(y/n)')
        end=str(input())   
        count+=1
        
        if end=='y':
            continue
        elif end=='n':
            print('사번 이름 기본금 근무년수 근속수당 공제액 수령액')
            print(datas)
            print('처리 건:', count)
            break
        
        
inputfunc()   