# 함수 작성
a = 1
b = a + 1
# 어쩌구 저쩌구 하다가 모듈의 멤버로 함수 선언

def DoFunc1():           #이게 함수 선언한거임
    print('DoFunc1 수행')         
    
c = b + 20

# 함수 호출
DoFunc1()  # 함수 호출
# 딴 짓 하다가....
res = DoFunc1()  # 함수 호출
print(res)
print(DoFunc1())

print(DoFunc1) # () 없으면 함수는 객체 함수도 객체의 주소를 가지고 있음
print(id(DoFunc1))
print(id(print))
print(id(sum))
print(id(c))

d = c                          # 주소를 치환
DoFunc2 = DoFunc1 # 주소를 치환
DoFunc2()

print('-----')
def doFunc3(arg1, arg2):    #arg1 -> parameter ( 가인수) (매개변수)
    res = arg1 + arg2
    #return res가 여기 나오면 아래 if는 다 죽은 코드다
    if res % 2 == 1:
        return                       #res 값이 홀 수면 빈손
    else:
        return res                  #짝수여야 가져온다

print('결과는 ', doFunc3(10, 20))                  #10 -> argument (실인수)
aa = doFunc3(10, 21)
print('결과는 ', aa)

print('-----')
def area_tri(a, b):
    c = a * b / 2
    aria_print(c)                       # 함수는 함수를 부를 수 있다.
    
def aria_print(c):
    print('삼각형의 면적은 ' + str(c))

area_tri(5, 6)                

print('-----')
def func1():
    print('func1 멤버 처리')
    def func2():
        print('func2 멤버 처리 : 내부 함수')
    func2()

func1()

print('-----')
def swap(a, b):
    return b, a                 #tuple로 반환(20, 10) return 값은 반드시 하나기 때문에 이것도 하나임 

a = 10; b = 20
c = swap(a, b)
print(c)
print(c[0], c[1])

print('-----')
# if 조건식 안에 함수 사용
def isOdd_func(arg):
    return arg % 2 == 1

mydict = {x:x * x for x in range(11) if isOdd_func(x)}  # 만약 if 절이 참이면 11미만까지 x를 반복해서...
print(mydict)

print('*************')
#print(dir(__builtins__))
print('현재 파일(모듈)의 객체 목록 : ', globals())



print('프로그램 종료')












