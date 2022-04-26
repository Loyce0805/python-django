'''Created on 2022. 4. 21. 2교시~ '''
#matplotlib 모듈의 기능 보충용 seaborn
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.info()) #column의 정보 확인.

sns.displot(titanic['age'])
plt.show()

sns.boxplot(y='age', data=titanic, palette='Paired')
plt.show()

# sns.countplot(x="class", data=titanic)
sns.countplot(x='class', data=titanic, hue='who') # hue="카테고리형 변수"
plt.show()

print()
t_pivot = titanic.pivot_table(index = 'class', columns='sex', aggfunc='size')
print(t_pivot)
sns.heatmap(t_pivot, cmap=sns.light_palette(color="gray", as_cmap=True), annot=True, fmt='d')
# annot=annotation
plt.show()