'''Created on 2022. 4. 21. 2교시~ '''
# iris data로 시각화
import pandas as pd
import matplotlib.pyplot as plt

#선생님 깃헙에서 iris.csv 가져오기
iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/iris.csv")
print(iris_data.info())
print(iris_data.head(3))

plt.scatter(iris_data['Sepal.Width'], iris_data['Petal.Width']) # scatter : 산점도
plt.show()

# pandas의 시각화
from pandas.plotting import scatter_matrix
iris_col = iris_data.loc[:, 'Sepal.Width':'Petal.Width']
scatter_matrix(iris_col, diagonal='kde')    # diagonal='kde':밀도분포
plt.show()

# seaborn
import seaborn as sns
sns.pairplot(iris_data, hue='Species', height=2)  # 카테고리는 Species로 나눔
plt.show()