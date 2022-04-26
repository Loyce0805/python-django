# 반복문 for : 형식)for target in 묶음형 object: ...
for i in [1,2,3,4,5]:
    print(i, end = ' ')
    
print()

for _ in [1,2,3,4,5]:
    print('반복')

print()
for i in (1,2,3,4,5):
    print(i, end = ' ')
    
print()
for i in {1,2,3,4,5}:
    print(i, end = ' ')
    
print()
soft = {'java' : '웹용', 'python' : '만능', 'oracle' : '디비'}
for i in soft.items():
    print(i, end = ' ')
    print(i[0], i[1])
    
print()
for i in soft.keys():
    print(i, end = ' ')
    
print()
for i in soft.values():
    print(i, end = ' ')
    
print()
for k, u in soft.items():
    print(k)
    print(u)
    
print()
li = ['a', 'b', 'c']
for idx, data in enumerate(li):   # 이거 자주 쓴다고 한다
    print(idx, ')', data)
    
print()
for n in [2, 3]:
    print('--{} 단--'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{0}*{1}={2}'.format(n, i, i * n))
        
print()
datas = [1,2,3,4,5]
for i in datas:
    if i == 2: continue
    if i == 4: break
    print(i, end = ' ')
else:
    print('정상 종료일 때 수행')
    
print()
jumsu = [95, 70, 60, 50, 100]
number = 0
for jum in jumsu:
    number += 1
    if jum < 70:continue
    print('%d번은 합격'%number)
    
print()
li1 = [3, 4, 5]
li2 = [0.5, 1, 2]
for a in li1:
    for b in li2:
        print(a + b, end = ' ')
        
print()
li1 = [3, 4, 5]
li2 = [0.5, 1, 2]
result = []
for a in li1:
    for b in li2:
        #print(a + b, end = ' ')
        result.append(a + b)
        
print(result)
    
print()
datas = [a + b for a in li1 for b in li2]
print(datas)
    