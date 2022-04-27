'''Created on 2022. 4. 20. 7교시~ '''
# 시각화 : 많은 양의 데이터를 효율적으로 그래프로 만들어 인사이트를 정확하게 얻어낼 수 있다.
# https://brunch.co.kr/@dimension-value/56 <- 시각화를 해야하는 이유

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')  #한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False  #한글 깨짐 방지 후 음수 깨짐 방지

x = ["서울", "인천", "수원"]  # 순서가 있는 tuple과 list는 가능! set은 안됨!
y = [5, 3, 7]

# plt.plot(y)
# plt.xlim([-1, 3]) # 축 경계값 지정
# plt.ylim([0, 10])
# plt.yticks(list(range(0,11,3))) #tick 설정
# plt.plot(x, y)
# plt.show()

# data = np.arange(1, 11, 2)
# print(data)
# plt.plot(data)
# x = [0, 1, 2, 3, 4]
# for a, b in zip(x, data):
#     plt.text(a, b, str(b))
# plt.show()

# sin 곡선 구하기
x = np.arange(10)
y = np.sin(x)
print(x, y)
#plt.plot(x, y)
#plt.plot(x, y, 'bo') #파란색 동그란 점
#plt.plot(x, y, 'r+') #빨간색 더하기 기호
#plt.plot(x, y, 'go-.', linewidth=1, markersize=7)  #초록색 동그란 점/파선으로 연결  #lw=2, marker='o', c='g'
#plt.show()


#---hold---
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# plt.figure(figsize=(10, 5))
# plt.plot(x, y_sin, 'r')
# plt.scatter(x, y_cos)    # 산점도
# plt.xlabel('x축')         # x축 이름
# plt.ylabel('y축')         # y축 이름
# plt.legend(['sine', 'cosine'])  # 범례 (그래프가 뭘 나타내는지 보여주는거임)
# plt.show()


#---subplot---
plt.subplot(2, 1, 1) #2행1열, focus는 1행이 갖는다
plt.plot(x, y_sin, 'r')
plt.title('사인 그래프')
plt.subplot(2, 1, 2)
plt.scatter(x, y_cos)
plt.title('코사인 그래프')
plt.show()


#---꺽은 선 그래프---
irum = ['a', 'b', 'c', 'd', 'e']
kor = [80, 50, 70, 70, 90]
eng = [60, 70, 80, 70, 60]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bs-.')
plt.title('시험 점수')
plt.ylim([0, 100])
plt.legend(['국어', '영어'], loc=4)
plt.grid(True)

fig = plt.gcf() #그래프를 이미지로 저장
plt.show()
fig.savefig('plot1.png')

from matplotlib.pyplot import imread
img = imread('plot1.png')
plt.imshow(img)

plt.show()