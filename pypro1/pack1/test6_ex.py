#문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
i = 1; hap = 0
while i <= 100:
    if i% 3 == 0 and i % 2 != 0:
        # print(i)
        hap += i
    i += 1
print('합은', hap)


#문2) 2 ~ 5 까지의 구구단 출력
print()
i = 2
while i <= 5:
    j = 1
    while j <= 9:
        i * j
        print(str(i) + '*' + str(j) + '=' + str(i*j))
        j += 1
    i += 1


#문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 합을 출력
print()
i = -1
hap = 0
while 1:
    hap += i
    if i<0:
        i = i*(-1)+2
    else:
        i = i*(-1)-2
    if i == -101:
        break

print('합은', hap)


#문4) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
aa = 2; count = 0
while aa <= 1000:
    imsi = False
    bb = 2
    while bb <= aa - 1:
        if aa % bb == 0:
            imsi = True
        bb += 1
        
    if imsi == False:
        print(aa, end = ' ')   
        count += 1
    
    aa += 1
    
print('갯수 :', count)




















