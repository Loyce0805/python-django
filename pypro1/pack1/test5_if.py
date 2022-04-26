# if
var = 5

if var >= 3:
    print('크구나')
    print('참일 때 수행')


print('end1 ')

if var >= 3:
    #print('크구나2')
    pass
else:
    print('작구나2')

print('end2')

print()
money= 1000
age = 23
if money >= 500:
    item = 'apple'
    if age <= 30:
        msg = 'young'
    else:
        msg = 'old'
else:
    item = 'orange'
    if age > 20:
        msg = 'man'
    else:
        msg = 'child'
        
print(item, msg)

print()
jum = 70
# jum = int(input('점수 입력 : '))
# print(jum, type(jum))
res = ' ' 

if jum >= 90:
    res = 'a'
elif jum >= 80:
    res= 'b'
else:
        res = 'c'    
print('res :' + res)

if 90 <= jum <= 100:
    res = 'a'
elif 70 <= jum < 90:
    res= 'b'
else:
        res = 'c'    
print('res :' + res)

print()
names = ['정화', '재이', '일환']
print(names[0])
if '재이' in names:
    print('친구야~')
else:
    print('누구?')
    
print()
a = 'kbs'
b = 9 if a == 'kbs' else 11
print(b)

a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)

print()
a = 3
if a < 5:
    print(0)
elif a < 10:
    print(1)
else:
    print(2)

print(0 if a < 5 else 1 if a < 10 else 2)

print()
res = a * 2 if a > 5 else a + 2
print(res)

print((a + 2, a * 2)[a > 5])         # a > 5가 조건 위에꺼랑 똑같은 말임





















