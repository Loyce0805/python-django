# 일급함수 지원 성립 조건 : 함수안에 함수 선언 / 인자로 함수를 전달할 수 있어야함 / 반환값이 함수인 경우 
def func1(a, b):
    return a + b

func2 = func1  # 주소를 치환 id 한번 확인해보자

print(func1(2, 3))
print(func2(2, 3))

print()
def func3(f):                       # f는 매개 변수 => 매개변수로 함수를 사용
    def func4():                    # 함수안에 함수를 선언 (내부함수)
        print('나는 내부함수야~~')
    func4()
    return f                           # 반환값이 함수

mbc = func3(func1)             #func1 을 f에게 주소치환함(넘겨줌)
print(mbc(2, 3))

print('----람다(lambda) 함수 - 축약함수: 이름이 없는 한 줄 짜리 함수 -----------------')
# def를 쓸 정도로 복잡하지 않거나, def를 쓸 수 없는 곳에 사용
# 형식 : lambda 인자,...  :  표현식       <== return 없이 결과를 반환
def Hap(x, y):
    return x + y

print(Hap(1, 2))

print((lambda x, y:x + y)(1, 2))

g = lambda x, y: x * y           # 주소를 넘겨(치환)받으면 lambda도 더 쓸 수 있음. 하지만 보통 1회용으로 씀 
print(g(3, 4))
imsi = g(3, 4)
print(imsi)

print()
# 람다도 가변인수 사용 가능
kbs = lambda a, su=10:a + su
print(kbs(5))
print(kbs(5, 6))

sbs = lambda a, *tu, **di:print(a, tu, di)
sbs(1,2,3,m=4,n=5)

print()
li = [lambda a,b:a+b, lambda a,b:a*b]
print(li[0](3,4))
print(li[1](3,4))

print()
# filter(함수, sequence자료)
print(list(filter(lambda a:a < 5, range(10))))   # 내용이 작을 땐 람다로 처리하자
print(list(filter(lambda a:a % 2, range(10))))   # 0은 False 1은 True
print(list(filter(lambda a:a % 5 == 0 or a % 7 == 0, range(1, 101))))














