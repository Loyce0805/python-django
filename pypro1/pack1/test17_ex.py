def inputfunc():
    tmp = 1
    while True:
        print('사번,이름,기본급,입사년도를 입력하세요')
        data = list(input().split(","))
        processfunc(data)
        
        yn = input('계속 하시겠습니까? y/n : ')
        if yn == 'y':
            tmp +=1
            continue
        else:
            print('처리한 건수 : {}건'.format(tmp))
            break
        

def processfunc(data):
    num,name,income,year = data
    a = 2022 - int(year)
    bonus = 0
    tax= 0
    if a>=9:
        bonus = 1000000
    elif a>=4:
        bonus = 450000
    else:
        bonus = 150000
               
    total = int(income)+bonus
    if total >= 3000000:
        tax=0.5
    elif total >= 2000000:
        tax=0.3
    else:
        tax= 0.15
           
    print('{} {} {} {} {} {} {}'.format(num,name,income,a,bonus,total*tax,total-total*tax))

inputfunc()
