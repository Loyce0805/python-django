# 재귀함수(recursive function) : 함수가 자기자신을 호출
def countDown(n):
    if n == 0:
        print('완료')
    else:
        print(n, end = ' ')
        countDown(n - 1)              # 자신을 호출

countDown(5)

print()
def tot(n):
    if n == 1:
        print('탈출')
        return True
    return n + tot(n - 1)

res = tot(10)
print('10까지의 합은 ', res)

print()
# factorial : 1부터 어떤 양의 정수 n까지의 정수를 모두 곱한 것
def facFunc(a):
    if a == 1:return 1    # 아니면 True 아니면 0 으로 return
    print(a)
    return a * facFunc(a - 1)

print('5! : ', facFunc(5))


print('종료')


















    