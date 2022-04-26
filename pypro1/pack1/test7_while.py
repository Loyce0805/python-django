# while : continue, break

a = 0

while a < 10:
# while True:
# while 1:
# while 1.5: 
# while -1.5:
    a += 1
    if a == 5:continue
    # if a == 7:break
    print(a)
else:
    print('while의 정상 처리')
    
print('while 수행 후 a : %d'%a)

# 난수
import random
# random.seed(1) # 랜덤하게 나온 수 고정
# print(random.random())  # 실수
# print(random.randint(1, 10))

#임의의 숫자 알아 내기
num = random.randint(1, 10)
while True:
    print('1 ~ 10 사이의 컴이 가진 예상 숫자 입력')
    guess = int(input())
    
    if guess == num:
        print('성공' * 10)
        break
    elif guess < num:
        print(' 더 큰 수 입력')
    elif guess > num:
        print('더 작은 수 입력')