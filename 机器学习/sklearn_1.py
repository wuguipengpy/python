from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier #导入分类器
knn = KNeighborsClassifier(n_neighbors=3) #选取邻居个数

'''path = 'D:\python\iris.data'
with open(path) as wenjian:
    df = pd.read_csv(wenjian, header= None)
X = df.iloc[0:150, [0, 2]].values
plt.scatter(X[0:50,0], X[:50,1])
plt.scatter(X[50:100,0], X[50:100,1])
plt.scatter(X[100:150,0], X[100:150, 1])
plt.legend(loc='upper left')
plt.show()'''
iris = datasets.load_iris()
X = iris.data #数据集
y = iris.target #分类
knn.fit(X, y)#数据拟合
k = knn.predict([[6.7,3.3,5.7,2.5]])
print(k)
