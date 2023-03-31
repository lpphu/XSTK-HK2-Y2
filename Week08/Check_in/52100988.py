# 52100988 Lữ Phúc Phú

import pandas as pd
import matplotlib.pyplot as plt

''' Exercise 01 '''
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
iris_data = pd.read_csv(url, names=names)

''' Exercise 02 '''
iris_data_grouped = iris_data.groupby('class').agg(['mean', 'median', 'std'])
print(iris_data_grouped)

''' Exercise 03 '''
iris_data.plot(kind='scatter', x='sepal-length', y='sepal-width')
plt.show()