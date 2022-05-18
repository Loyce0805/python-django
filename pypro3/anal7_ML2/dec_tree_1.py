'''
Created on 2022. 5. 10.
'''
# DecisionTree(의사결정나무)
# classification, regression 모두 가능하나 분류모델로 더 많이 사용된다.
# Decision Tree는 여러 가지 규칙을 순차적으로 적용하면서 독립 변수 공간을 분할하는 분류 모형이다.

import collections
from sklearn import tree

x = [[180, 15],[177, 42],[156, 35],[174, 5],[166, 33],[170, 12],[171, 7]]
y = ['man','woman','woman','man','woman','man','woman']
label_names = ['height', 'hair length']

model = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
model.fit(x, y)
pred = model.predict(x)
print(pred)

mydata = [[171, 18]]
new_pred = model.predict(mydata)
print('분류 예측 결과 : ', new_pred)

# 시각화
import pydotplus

dot_data = tree.export_graphviz(model, feature_names = label_names,
                                out_file = None, filled = True, rounded = True)
graph = pydotplus.graph_from_dot_data(dot_data)
colors = ('red', 'orange')
edges = collections.defaultdict(list)
print(edges, type(edges)) # defaultdict(<class 'list'>, {}) <class 'collections.defaultdict'>

for e in graph.get_edge_list():
    edges[e.get_source()].append(int(e.get_destination()))

print(edges) # defaultdict(<class 'list'>, {'0': [1, 2]})

for e in edges:
    edges[e].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[e][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png('tree.png')

import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread('tree.png')
plt.imshow(img)
plt.show()

