'''
Created on 2022. 4. 26.
'''
# 표준편차, 분산의 중요성 : 데이터의 분포 파악

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(1) # seed를 1로 고정시킴
print(stats.norm(loc = 1, scale = 2).rvs(10)) # loc는 기댓값 scale은 표준편차, rvs는 random variable sampling 정규분포를 따르는 난수 10개

print('---------------------')
centers = [1, 1.5, 2]
col = 'rgb'

std = 0.05  # 표준편차 0.01, 1 ... 표준편차가 작을수록 패턴이 뚜렷하다.
datas = []

for i in range(3):
    datas.append(stats.norm(loc = centers[i], scale = std).rvs(100))  # 난수값을 datas list에 추가. 표준편차 0.01
    plt.plot(np.arange(100) + i * 100, datas[i], '*', color = col[i])
    
plt.show()