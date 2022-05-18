'''
Created on 2022. 5. 12. Support Vector Machine
'''
# SVM으로 XOR(Exclusive OR) 분류 처리. XOR은 or일때만 1(참)인것.

x_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

x_df = pd.DataFrame(x_data)
feature = np.array(x_df.iloc[:, 0:2])
label = np.array(x_df.iloc[:, 2])
print(feature)
print(label)

# model = LogisticRegression()
model = svm.SVC()
model.fit(feature, label)
pred = model.predict(feature)
print('예측값 : ', pred)

print('정확도 : ', metrics.accuracy_score(label, pred))
