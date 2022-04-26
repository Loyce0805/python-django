# 반복문 for
# 웹에서 읽은 자료라 가정 : 단어 수 출력 ex) 모터를:3
ss = """

"""
import re

ss2 = re.sub(r'[^가-힣\s]', '', ss) #substitute 치환 r'~~~ 제외 하고는 '' 없애버려
print(ss2)
ss3 = ss2.split(sep=' ')
print(ss3)
print(len(ss3))
print(len(set(ss3)))

cou = {}  #  단어의 발생 횟수를 dict로 저장 사실 set일 수도 있는데 아래가 어케되는지 봐야함
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1  # cou에 {'키' : i}
print(cou)

print()
for test in ['111-1234', '일이삼-사오육칠', '2222-3333']:
    if re.match(r'^\d{3,4}-\d{4}$', test): #처음에는 숫자로 3글자 그다음엔 숫자로 네글자 그게 끝이야($)
        print(test)
    else:
        print('전화번호 ㅠㅠ')
        
print()
a = 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)

print(li)

print(list(i for i in a if i % 2 == 0))

print()
datas = [1,2,'a',True, 3.4]
li = [i for i in datas if type(i) == int]
print(li)

print()
datas = {1,1,2,2,3}
se = {i * i for i in datas}
print(se)

print()
id_name = {1:'tom', 2:'james'}
name_id = {value:key for key, value in id_name.items()} # 키와 밸류가 나오려면 items를 붙여야 한다.
print(name_id)

print()
temp = [1, 2, 3]
for i in temp:
    print(i, end = ' ')
print()
print([i for i in temp])
print({i for i in temp})

print()
# 과일 값 계산
price = {'사과':2000, '오렌지':1000, '배':3000}
guest = {'사과':2, '배':1}
bill = sum(price[f] * guest[f] for f in guest)   # sum(요소들) : 합을 구하는 내장 함수
print(bill)






