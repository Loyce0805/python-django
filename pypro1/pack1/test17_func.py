# 함수 장식자 (function decorator) : meta 기능이 있음.
# 장식자는 또 다른 함수를 감싼 함수다.

def make2(fn):
    return lambda:'안녕 ' + fn()

def make1(fn):
    return lambda: '반가워 '+ fn()

def hello():
    return'홍길동'

hi = make2(make1(hello))
print(hi())

print()

@make2
@make1
def hello2():
    return'고길동'

print(hello2())

print()
hi2 = hello2()
print(hi2)
print(id(hi2), id(hello2()))

hi3 = hello2
print(hi3())

        
        
        
        



    
    
     










