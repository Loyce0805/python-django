'''
Created on 2022. 4. 18. 

'''
# numpy 기본 이해
# python의 list는 유연성이 좋지만 컴퓨터 자원이 많이 소모.
# ndarray는 데이터 검색 효율적이고 메모리를 효과적으로 관리하나 유연성이 떨어진다.

import numpy as np

print(np.__version__)

s = 'tom'   # scalar
print(s, type(s))

ss = ['tom', 'james', 'oscar']
print(ss, type(ss))    # <class 'list'>
ss2 = np.array(ss)
print(ss2, type(ss2))  # <class 'numpy.ndarray'>

print('-------------list/ndarray 기억상태 구분')
li = list(range(1, 10))
print(li)
print(id(li[0]), id(li[1]))
print(li * 10)
print('-' * 10)

for i in li:
    print(i * 10, end = ' ')

print()
print([i * 10 for i in li])

print() # list to ndarray
num_arr = np.array(li)
print(num_arr)
print(id(num_arr[0]), id(num_arr[1]))
print(num_arr * 10)

print()
#a = np.array([1,2,3.2])  # 데이터는 상위 타입을 따른다. 배열이기 때문에 타입이 일치. 묶음형 자료 int -> float -> complex -> str
a = np.array([1,2,3])
print(a, type(a), a.dtype, a.shape, a.ndim, a.size)
print(a[0])   # 인덱싱
print(a[1:3]) # 슬라이싱
print(a[-1])  # 이건 여집합이 아니라 뒤에서부터 카운팅

print()
b = np.array([[1,2,3], [4,5,6]])
print(b, type(b), b.dtype, b.shape, b.ndim, b.size)
print(b[0])   # 인덱싱
print(b[1:3,]) # 슬라이싱
print(b[-1,])  # 이건 여집합이 아니라 뒤에서부터 카운팅
print(b[0,0], b[1,1])
print(b[[0]])

print()
c = np.zeros((2, 2))   # 2행 2열을 0으로 채워준다.
print(c)

d = np.ones((1, 2))    # 1행 2열을 1로 채워준다.
print(d) 

e = np.full((2, 2), fill_value = 7)    # 2행 2열을 7로 채워준다.
print(e)

f = np.eye(3)    # 단위행렬 생성. 3행 3열로 주 대각만 1로 나머지는 0으로 
print(f) 

print()
print(np.random.rand(5), np.mean(np.random.rand(5)))   # 균등 분포
print(np.random.randn(5), np.mean(np.random.randn(5))) # 정규 분포

np.random.seed(1)
print(np.random.randn(2, 3))

print(np.random.randint(10, size = 6))          # 1차원
print(np.random.randint(10, size = (3, 4)))     # 2차원
print(np.random.randint(10, size = (3, 4, 5)))  # 3차원

print()
print(list(range(0,10)))
print(np.arange(10))

print('------인덱싱, 슬라이싱-------')
a = np.array([1,2,3,4,5])
print(a[1:5:2])

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #중복 list로 ndarray 생성. 순서가 있는 묶음형 자료로 ndarray 생성 가능.
print(a[:])     # 전부 출력
print(a[1:])
print(a[-1:])
print(a[0], a[0][0], a[0, 0],a[[0]])
# a[0]는 1차원으로 반환 / a[0][0]와 a[0, 0]는 scalar / a[[0]]는 2차원으로 반환
print(a[1:, 0:2])

print()
print('서브 배열')
b = a[:2, 1:3]  # 서브 배열
print(b)
print(b[0,0])
print(a[0,1])
print()
b[0,0] = 88
print(b)
print()
print(a)

print()
print('배열 복사')
c = a[:2, 1:3].copy()   # 배열 사본 복사
print(c)
c[0,0] = 99
print(c)
print()
print(a)

print('-----------------------')
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.shape)
r1 = a[1, :]
r2 = a[1:2, :]
print(r1, r1.shape)
print(r2, r2.shape)

print()
a = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print(a.shape)
print(a)
b = np.array([0,2,0,1])
print(b, b.shape)
print()
print(np.arange(4))
print(a[np.arange(4), b])

print('--------------4교시-------------')
print()
bool_idx = (a > 10)
print(bool_idx)

print(a[bool_idx])  #True 값을 가지는 것만 출력됨
print(a[a > 10])    #10을 초과하는 값만 출력됨