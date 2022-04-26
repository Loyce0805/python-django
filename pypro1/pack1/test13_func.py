# 변수의 생존 범위 (scope rule) : 전역변수, 지역변수
# 접근 우선 순서 : local > Enclosing function > Global

player = '전국대표'   # 전역변수 : 현재 모듈의 어디서든 공유가 가능
print(player)

def funcSoccer():
    name = '신선해'   # 지역변수 : 현재 함수 내에서만 유효
    player = '지역대표'
    print(name, player)

funcSoccer()
#print(name)             # NameError: name 'name' is not defined 함수 내에서만 유효한 지역변수 name
print(player)

print('-----------------')
a = 10; b = 20; c = 30
print('1): a:{} b:{} c:{}'.format(a, b, c))

def foo():
    a = 40
    b = 50
    def bar():
        #c = 60
        global c          # 전역변수
        nonlocal b      # foo 함수 수준의 변수(Enclosing function)
        print('2): a:{} b:{} c:{}'.format(a, b, c))       #bar 에서 abc 찾고 없으면 foo에서 찾고 없으니 더 위로 올라가서 전역변수를 찾음
        c = 60                   # UnboundLocalError: local variable 'c' referenced before assignment / global c 때문에 전역변수 c에 60을 준거임
        b = 70
    bar()
    print('3): a:{} b:{} c:{}'.format(a, b, c))  
    
    
foo()
print('처리 후): a:{} b:{} c:{}'.format(a, b, c))

print('-------------')
g = 1
def func():
    global g
    a = g
    g = 2
    return [a, g]

print(func())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        