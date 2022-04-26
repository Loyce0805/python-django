# 반복문 : while 조건
a = 1

while a <= 5:
    print(a, end = ' ')
    a = a + 1
    
print('\nwhile 종료')

print()
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i: ' + str(i) + ', j"' + str(j))
        j += 1
    i += 1
    
print('\nwhile 종료2')

print('1 ~ 100 사이의 정수 중 3의 배수의 합')
i = 1; hap = 0
while i <= 100:
    #print(i, end = ' ')
    if i % 3 == 0:
        #print(i, end = ' ')
        hap += i
    i += 1
    
print('합은 ', hap)

print()
colors = ['r', 'g', 'b']
print(len(colors))
a = 0
while a < len(colors):
    print(colors[a], end = ':')
    a += 1
    
print()
while colors:
    print(colors.pop())
    
print(len(colors))