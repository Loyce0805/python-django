'''Created on 2022. 4. 21. 1교시~ '''
import  numpy as np
import matplotlib.pyplot as plt

x=np.arange(10)

"""
# 방법1: matplotblib 스타일의 인터페이스로 시각화
plt.figure() #plot 그림 생성
plt.subplot(2, 1, 1) #plot 두 개 그리기. (row, column, panel number)
plt.plot(x, np.sin(x))
plt.subplot(2,1,2)
plt.plot(x, np.cos(x))
plt.show()


# 방법2: matplotlib의 개체지향 인터페이스로 시각화
fig, ax = plt.subplots(nrows=2, ncols=1)  # ax는 axes
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()
"""

""" 
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.hist(np.random.randn(10), bins=10, alpha=0.5) # bins는 구간수. alpha는 투명도. 0에 가까울수록 투명함.
# 표준 정규분포를 따른다. | bins=데이터 값을 나누는 구간 # 연속형 데이터일 때 이 방법이 좋은 방법이다. 히스토그램을 써서.
ax2.plot(np.random.randn(10))
plt.show()
"""

#데이터 양이 많을 때는 히스토그램, 산점도, 박스 플롯 등이 좋다.
#데이터 양이 많지 않을 때 막대, 파이 그래프 등이 좋다.
data = [50, 80, 100, 70, 90]

plt.bar(range(len(data)), data) #세로 막대 그래프
plt.show()

err = np.random.rand(len(data)) #rand(): 균등분포
# err에 표시할 수 있는 것: 표준편차, 오차, 신뢰구간 등
plt.barh(range(len(data)), data, xerr=err, alpha=0.5) #가로 막대 그래프
plt.show()

plt.pie(data, explode=(0, 0.1, 0, 0, 0), colors=['yellow', 'red', 'blue']) # explode로 조각 분리, 튀어나오게 가능. 색상 변경 가능
plt.title('pie chart')
plt.show()

plt.boxplot(data) #4분위수 표현 가능. 데이터 분포를 알기에 적합하다! 아웃라이어(이상치) 확인에 유용하다.
plt.show()


#-----버블 차트-----
n = 30
np.random.seed(0)
x = np.random.rand(n)
y = np.random.rand(n)
color = np.random.rand(n)
scale = np.pi * (15 * np.random.rand(n)) ** 2
plt.scatter(x, y, s = scale, c = color) # scatter : 산포도
plt.show()

#시계열 데이터 : 일정한 시간동안 수집된 순서가 있는 데이터
import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000, 4),
                     index = pd.date_range('1/1/2000', periods=1000), columns=list('abcd'))
print(fdata.head())

fdata = fdata.cumsum()   # 누적합
plt.plot(fdata)
plt.show()


# pandas의 plot 기능
fdata.plot()
fdata.plot(kind='bar')
fdata.plot(kind='box')
plt.xlabel('time')
plt.ylabel('data')
plt.show()