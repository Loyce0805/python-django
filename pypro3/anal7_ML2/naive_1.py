''' 
Created on 2022. 5. 16. 
'''
# 나이브베이즈 모델 : 베이지 정리를 이용
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

x = np.array([1,2,3,4,5])   # 독립변수 x
x = x[:, np.newaxis]    # 차원확장(matrix로)
print(x)
y = np.array([1,3,5,7,9])   # 종속변수 y    #vector

model = GaussianNB().fit(x, y)
print(model)    # GaussianNB()
pred = model.predict(x)
print(pred)     # [1 3 5 7 9]
print('acc : ', metrics.accuracy_score(y, pred))    # acc :  1.0

# 새로운 값으로 분류
new_x = np.array([[0.5], [2], [7], [12], [0.1]])
new_pred = model.predict(new_x)
print(new_pred)     # [1 3 9 9 1]
# 독립변수의 개수가 너무 적어 믿음이 덜 가지만... 이런 식으로 모델을 만든다!

print('- - - One-Hot Encoding - - - - - - - - -')\
# 방법1. np.eye()
x = '1,2,3,4,5'
x = x.split(',')
x = np.eye(len(x))
print(x)    # (5, 5) 행렬 +  주대각이 1이다.

# 방법2. OneHotEncoder 사용
x = '1,2,3,4,5'
x = x.split(',')
x = np.array(x)
x = x[:, np.newaxis]
one_hot = OneHotEncoder(categories = 'auto')
x2 = one_hot.fit_transform(x).toarray()
print(x2)   # (5, 5) 행렬 +  주대각이 1이다.
y = np.array([1,3,5,7,9])

model2 = GaussianNB().fit(x2, y)
print(model2)   # GaussianNB()
pred2 = model2.predict(x2)
print(pred2)    # [1 3 5 7 9]