'''
Created on 2022. 5. 16.
'''
# MLP : 다층신경망(Multi Layer Perceptron) - 선형 / 비선형 분류가 가능
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
# label = np.array([0,0,0,1]) # and
# label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0])   # xor

# ml = MLPClassifier(hidden_layer_sizes=30, activation='relu',          # 레이어 1개에만 노드 30개
#                   solver='adam', learning_rate_init = 0.01).fit(feature, label) # activation = 활성화함수, solver = The solver for weight optimization, learning_rate_init = 학습율 얼마씩 이동할건가
ml = MLPClassifier(hidden_layer_sizes=(10, 10, 10), activation='relu',  # 레이어 1개당 노드를 10개씩
                solver='adam', learning_rate_init = 0.01).fit(feature, label)
print(ml)

pred = ml.predict(feature)
print('pred : ', pred)
print('acc : ', accuracy_score(label, pred))
 

 