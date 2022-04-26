# 연산자
# 소괄호 > 산술연산자(*, /, // > +, -) > 관계연산자 (>, >=, ==, !=, <, <=) > 논리연산자 (not, and, or) > 치환(=)
v1 = 3 # 치환
v1 = v2 = v3 = 2
print(v1, v2, v3)
print(id(v1), id(v2), id(v3)) # id 값이 다 같음

v1, v2 = 10, 20
print(v1, v2)

print('packing 연산자 : *, **')
v1, *v2 = [1, 2, 3, 4, 5]
print(v1, v2)
*v1, v2 = [1, 2, 3, 4, 5]
print(v1, v2)

*v1, v2, v3 = [1, 2, 3, 4, 5]
print(v1, v2, v3)

v1, *v2, v3 = [1, 2, 3, 4, 5]
print(v1, v2, v3)

print('-연산자 연습---')
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 3)
print(divmod(5, 3)) # (1, 2) (5를 3으로 나눈값, 5를 3으로 나눈 나머지)
print('연산자 우선 순위 :', 3 + 4 * 5)
print('연산자 우선 순위 :', (3 + 4) * 5)

print(5 > 3, 5 == 3, 5 != 3)
print(5 > 3 and 4 < 3, 5 >= 3 or 4 <= 3, not(5 > 3))

print('문자열 더하기', end = ' ') # print 는 java의 println과 같다.(문자열 더하기가 끝났으면 커서가 밑으로 내려가서 다음줄로 간다.)
print('이어쓰기')
print('대한' + '민' + "국 만세")
print('한국' * 20)

print()
a = 10
a = a + 1
a += 1
# a++ ++a : 자바의 증감 연산자는 누적으로 사용 불가
print('누적 결과 :', a) # 자바는 +하면 Str로 치환 해주지만 파이썬은 , 써야함

print('부호 변경 :', a, a * -1, -a, --a, +a, ++a, +-a)

print('문자 숫자 형변환')
#print(5 + '5')     # TypeError: unsupported operand type(s) for +: 'int' and 'str', 'float'
print(5 + int('5')) # 숫자 10
print(str(5) + '5') # 문자 55
print('나이는 ' + str(23) + '살')  

print('escape 문자 ---') # \n \b \a \t ...
print('kbs\nmbc')
print(r'c:\nbc\tbs\abc.txt') # escape 문자를 그냥 데이터로 인식하려면 r 선행해서 쓰면 escape 무시 (row r)

print()
print(True, bool(True), False, bool(False))
print(bool(-1), bool(2.3), bool(123), bool('abc'))
print(bool(0), bool(''), bool(None), bool([]), bool({})) # python에서 0은 false

# print() 함수에 서식 넣기
print()
print(format(123.45678, '10.3f')) # 123.457 3번쨰 자리로 올림
print(format(123.45678, '10.3'))
print(format(123, '10d')) # 정수로 올려줌.

print()
print('나는 나이가 %d 이다.'%23) # %뒤에가 매핑됨.
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23,'홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33)) # 0번쨰는 한국인, {1}은 33에 대입
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))

























