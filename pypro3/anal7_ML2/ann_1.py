'''
Created on 2022. 5. 16. Perceptron
'''
# 인공신경망 : 단층 신경망(뉴런 또는 노드 1개) - Perceptron
# input data * 가중치의 합에 대해 임계값(활성화함수)을 기준으로 이항/다항 분류가 가능하다.

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
# label = np.array([0,0,0,1]) # and
# label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor    # => acc: 0.5, max_iter를 아무리 크게 줘도 0.5임.

ml = Perceptron(max_iter=10, eta0=0.1).fit(feature, label)
print(ml)   #Perceptron(eta0=0.1, max_iter=1) 
pred = ml.predict(feature)
print('pred : ', pred)
# pred: [0 0 0 0]    #max_iter=10 -> [0 0 0 1]
print('acc : ', accuracy_score(label, pred))    # acc: 0.75    # max_iter=10 -> 1.0