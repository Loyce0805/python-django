# 묶음 자료형
# 자료형 중에서 int, float, bool, complex : 객체 하나를 참조
# 자료형 중에서 str, list, tuple, set, dict : 객체값 여러 개를 요소로 참조

# str : 문자열 자료형. 순서 O : 인덱싱/슬라이싱 가능, 수정 X
s = 'sequence'
print('길이 : ', len(s))
print('특정문자 포함 위치 확인 :', s.count('e'), s.count('m'), s.find('e'))
# 다량의 문자열 관련 함수 
print(id(s))
s = 'bequence' # 새로운 객체를 치환
print(id(s))

# 인덱싱, 슬라이싱 가능
s = 'sequence'
print(s, s[0], s[3], s[7], s[-1], s[-3]) # 인덱싱
print(s[0:3]) # 슬라이싱(0이상 3미만)    [시작:끝:간격]
print(s[-4:-1]) # -4부터 -1 미만
print(s[:3]) # 3 미만 까지
print(s[3:]) # 3 포함 이후로
print(s[2:7:1]) # 2부터 7미만까지 증가치는 1
print(s[2:7:2]) # 2부터 7미만까지 증가치는 2
print(s[::2]) # 하나 걸러 하나씩 나오라는거 
print(s[2:5] + '만세')

ss = 'mbc kbs'
result = ss.split(sep = ' ') # sep = ' ' 를 통해(띄어쓰기) 분리하기
print(result)
print(':'.join(result)) # 합치기

print('\n\nList type--- : 순서 O, 수정 O, 요소값 중복 O. 요소들을 []로 감쌈')
a = [1, 2, 3, '문자열', 4.5, True]
print(a, type(a))
b = [a, 100, 200] # 중복 리스트 가능
print(b)

print()
family = ['엄마', '아빠']
print(family, id(family))
family[0] = '어머니'
print(family, id(family))
family.append('나') # append 는 뒤에 추가
family.insert(1, '여동생') # 1번째에 추가 (아빠였는데 여동생이 추가됨)
family.extend(['삼촌', '이모']) # 확장이라 list로 다 들어감
family += ['고모'] # 이렇게 해도 추가
print(family)

family.remove('나') # 이러면 '나'가 빠짐 그리고 중복 안됨 -> 값에 의한 삭제
del family[0] # 0번째인 어머니도 지워짐 이건 중복 가능 -> 순서에 의한 삭제
print(family)
del family # 이건 전체를 날리는거임
# print(family)

print('\n\nTuple type--- : 리스트와 유사하나 검색속도가 더 빠름. 순서 O, 수정 X, 요소값 중복 O. 요소들을 ()로 감쌈.')
# t = ('a', 10, 'b')
t = 'a', 10, 'b' # 위와 동일 하지만 가독성을 위해 소괄호 두르는게 좋다.
print(t, type(t))
print(t[0])
#t[0] = 'k' # TypeError: 'tuple' object does not support item assignment 수정 불가
a = (1) # <class 'int'>
b= (1,) # <class 'tuple'>
print(type(a), type(b))

# 형변환이 가능하다 Tuple
aa = [1,2,3]
bb = tuple(aa)
print(type(bb))
aa = list(bb)
print(type(aa))

print('\n\nSet type--- : 순서 X. 수정 X. 중복 불가가 강점. 요소들을 {}로 감쌈')
a = {1,2,3,1}
print(a, type(a))
#print(a[0]) # TypeError: 'set' object is not subscriptable 순서가 없음. 인덱싱이 불가
b = {3, 4}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a - b, a | b, a & b) # 차집합, 합집합, 교집합 순

b.update({5, 6})
b.update([7, 8])
b.update((9, 10))
print(b)
b.discard(6) # 6 지우기 해당 값이 없으면 통과
b.remove(7) # 7 지우기 해당 값이 없으면 에러
print(b)

print() # 넣었다 빼면 중복값 없어지니 list를 set에 담군다
aa = [1,2,2,3,5,5]
print(aa, type(aa))
bb = set(aa)
print(bb, type(bb))
aa = list(bb)
print(aa, type(aa))

print('\n\nDict type--- : 순서 X. 수정 O. 요소들을 {"키":"값"}로 감쌈')
mydic = dict(k1 = 1, k2 = 'abc', k3 = 3.4)
print(mydic, type(mydic))

dic = {'파이썬':'뱀', '자바':'커피', '스프링':['용수철', '웹처리']} # 밸류값에 집합형 자료가 들어갈 수도 있음. key는 유니크 해야함
print(dic, type(dic))
print(dic['스프링'])
# print(dic[0]) # 오류가 뜬다. 순서가 없기 때문.

dic['오라클'] = '예언자' # 추가
print(dic)
del dic['오라클'] # 삭제
print(dic)
dic['파이썬'] = '만능 언어' # 수정
print(dic)






