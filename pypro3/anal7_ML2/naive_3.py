''' 
Created on 2022. 5. 16.
'''
# weather dataset으로 비 유무 처리용 나이브베이즈 분류 모델
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from skimage import metrics

df = pd.read_csv('../testdata/weather.csv')
print(df.head(3))
print(df.info())

x = df[['MinTemp', 'MaxTemp', 'Rainfall']]
label = df['RainTomorrow'].map({'Yes':1, 'No':0})   # RainTomorrow 칼럼의 Yes는 1로, No는 0으로 바꾼다.
print(x[:3])
print(label[:3])

# train / test split
train_x, test_x, train_y, test_y = train_test_split(x, label, random_state=0)

gmodel = GaussianNB()
gmodel.fit(train_x, train_y)

pred = gmodel.predict(test_x)
print('예측값 : ', pred[:10])          # [0 0 0 0 0 0 0 0 0 0]
print('실제값 : ', test_y[:10].values) # [0 0 1 0 1 1 1 0 0 0]
print('acc : ', accuracy_score(test_y, pred))   # 0.7282608695652174
print('report : \n', classification_report(test_y, pred))
''' >> report : 
                   precision    recall  f1-score   support
    
               0       0.79      0.91      0.84        74
               1       0.00      0.00      0.00        18
    
        accuracy                           0.73        92
       macro avg       0.39      0.45      0.42        92
    weighted avg       0.63      0.73      0.68        92

'''