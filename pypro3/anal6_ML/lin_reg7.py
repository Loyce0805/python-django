''' Created on 2022. 5. 4. 1교시~ '''
# Linear Regression - 선형회귀의 평가 지표 score 정리 : MAE, MSE, RMSE, R-Sqaured
import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler  #데이터를 0~1 사이의 범위로 표준화해줌
from sklearn.preprocessing._data import MinMaxScaler

# 편차가 큰 표본 데이터 작성
sample_size = 100
np.random.seed(1)

x = np.random.normal(0, 10, sample_size)    # 평균 0, 표준편차 10, 갯수는 100개
y = np.random.normal(0, 10, sample_size) + x*30
print(x[:5])
print(y[:5])
print('상관계수 : \n', np.corrcoef(x, y))   #0.99939357

# 독립변수(x)에 대한 표준화
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1, 1))   # matrix 형태로 표준화 진행
print(x_scaled[:5])
#[ 16.24345364  -6.11756414  -5.28171752 -10.72968622   8.65407629]
# --> [[0.87492405]
#      [0.37658554]
#      [0.39521325]
#      [0.27379961]
#      [0.70578689]]    #1차원에서 2차원으로도 변함.
''' ---------2교시------- '''
print(x_scaled.shape)   #(100, 1)    2차원이 되었다!

# 시각화
# plt.scatter(x_scaled, y)
# plt.show()

model = LinearRegression().fit(x_scaled, y)
# print(model.summary())  #AttributeError: 'LinearRegression' object has no attribute 'summary'

y_pred = model.predict(x_scaled)    #학습한 데이터로 예측 결과를 얻어 실제값과 비교
print('예측값 : ', y_pred[:5]) #[ 490.32381062 -182.64057041 -157.48540955 -321.44435455  261.91825779]
print('실제값 : ', y[:5])      #[ 482.83232345 -171.28184705 -154.41660926 -315.95480141  248.67317034]

print()
''' 모델 성능 파악 '''
def regScore_func(y_true, y_pred):
    print('r2_score(결정계수):{}'.format(r2_score(y_true, y_pred))) #(실제값, 예측값) 위치 고정임! 바뀌면 안 된다.
    print('explained_variance_score(설명분산점수):{}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_error(평균제곱근오차):{}'.format(mean_squared_error(y_true, y_pred)))
    # mean_squared_error: 잔차의 제곱의 합을 표본 수로 나눈 값. 분산분석의 SSE와 같다.(Sum of Square Error)

# 함수 호출!
regScore_func(y, y_pred)
''' r2_score(결정계수):0.9987875127274646
    explained_variance_score(설명분산점수):0.9987875127274646
    mean_squared_error(평균제곱근오차):86.14795101998747        '''
# => r2_score와 explained_variance_score는 동일한 값이 나와야 한다.
#    값이 다르면 Error에 편향이 있음. 즉, 모델 학습이 잘못 되었다는 뜻. 독립변수와 종속변수가 잘못되었다...
# => MSE(평균제곱근오차)는 


print()
print('-_-_-_-_-_-_-_-_-_-_-_-_-')
# 분산이 큰 표본 데이터 작성

x = np.random.normal(0, 1, sample_size)    # 평균 0, 표준편차 1, 갯수는 100개
y = np.random.normal(0, 500, sample_size) + x*30
print(x[:5])
print(y[:5])
print('상관계수 : \n', np.corrcoef(x, y))   #0.00401167

# 독립변수(x)에 대한 표준화
scaler2 = MinMaxScaler()
x_scaled2 = scaler.fit_transform(x.reshape(-1, 1))
print(x_scaled2[:5])
#[-0.40087819  0.82400562 -0.56230543  1.95487808 -1.33195167]
# --> [[0.45631435]
#      [0.68996139]
#      [0.68996139]
#      [0.90567574]
#      [0.27871173]]
''' ---------2교시------- '''
print(x_scaled.shape)

model2 = LinearRegression().fit(x_scaled2, y)
y_pred2 = model.predict(x_scaled2)
regScore_func(y, y_pred2)
''' r2_score(결정계수):-0.23919537320391226
    explained_variance_score(설명분산점수):-0.23332910015616237
    mean_squared_error(평균제곱근오차):350026.24313706765        '''
# => r2_score: 설명력이 매우 낮아졌다.
# => mean_squared_error : 평균제곱근오차는 매우 커짐