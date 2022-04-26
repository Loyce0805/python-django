# numpy : 고속연산, ndarray를 지원
# 데이터 분석 관련 모듈 전체 생태계의 핵심을 이루고 있기에 잘 다룰 줄 알아야 한다.

# 평균, 분산, 표준편차 구하기 (모집단 / 표본 통계량)
grades = [1, 3, -2, 4]  # 변량(변수, 확률값, 관측값)

def show_grades(grades):
    for g in grades:
        print(g, end = ' ')

show_grades(grades)

def grades_sum(grades):
    tot = 0
    for g in grades:
        tot += g
    return tot
print()
print('합은 ', grades_sum(grades))

def grades_avg(grades):
    tot = grades_sum(grades)
    avg = tot / len(grades)
    return avg
print('평균은 ', grades_avg(grades))

def grades_variance(grades):     # 분산 구하기
    avg = grades_avg(grades)
    vari = 0
    for su in grades:
        vari += (su - avg) ** 2   # (변량 - 평균) ** 2   ==> 변량-평균이 편차
    return vari / len(grades)   # 모집단으로 계산(python)
    #return vari / (len(grades) - 1)  # 표본집단으로 계산(R) 
    # 분산이 크면 산포도가 크고, 상관계수가 0과 가깝다.
    # 산포도가 작으면 분산이 작고 상관계수가 1과 가깝다.   
print('분산은 ', grades_variance(grades))

import math
def grades_std(grades):   # 표준편차 구하기
    #return grades_variance(grades) ** 0.5  
# 분산에 루트를 씌워준다. 0.5를 제곱한게 루트 평균값과 얼마나 차이가 나는지는 표준편차를 이용
    return math.sqrt(grades_variance(grades))
print('표준편차는 ', grades_std(grades))

print('numpy로 계산')
import numpy as np
# print('합은 ', numpy.sum(grades))
print('합은 ', np.sum(grades))
print('평균은 ', np.average(grades))
print('평균은 ', np.mean(grades))
print('분산은 ', np.var(grades))
print('표준편차는 ', np.std(grades))