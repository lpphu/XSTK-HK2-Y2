import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
# %matplotlib inline 

'''Example 01'''

df = pd.read_csv("/iris_csv.csv") 
df.head()

# '''Example 02'''

# df.info()

# RangeIndex: 150 entries, 0 to 149
# Data columns (total 5 columns):
#  #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   sepallength  150 non-null    float64
#  1   sepalwidth   150 non-null    float64
#  2   petallength  150 non-null    float64
#  3   petalwidth   150 non-null    float64
#  4   class        150 non-null    object 
# dtypes: float64(4), object(1)
# memory usage: 6.0+ KB
# df.shape

# (150, 5)


# ## Statistics about dataset
# df.describe()

# '''Example 03'''
# ## checking for null values

# df.isnull().sum()

# sepallength    0
# sepalwidth     0
# petallength    0
# petalwidth     0
# class          0
# dtype: int64

# ## Univariate analysis
# df.groupby('class').agg(['mean', 'median'])  # passing a list of recognized strings
# df.groupby('class').agg([np.mean, np.median])

# '''Example 04'''
# ## Box plot 
# plt.figure(figsize=(8,4)) 
# sns.boxplot(x='class',y='sepalwidth',data=df ,palette='YlGnBu')

# '''Example 05'''
# ## Distribution of particular species
# sns.distplot(a=df['petalwidth'], bins=40, color='b')
# plt.title('petal width distribution plot')

# '''Example 06'''
# ## count of number of observation of each species

# sns.countplot(x='class',data=df)

# '''Example 07'''
# ## Correlation map using a heatmap matrix

# sns.heatmap(df.corr(), linecolor='white', linewidths=1)

# '''Example 08'''
# ## Multivariate analysis – analyis between two or more variable or features
# ## Scatter plot to see the relation between two or more features like sepal length, petal length,etc
# axis = plt.axes()

# axis.scatter(df.sepallength, df.sepalwidth)

# axis.set(xlabel='Sepal_Length (cm)',
#    ylabel='Sepal_Width (cm)',
#    title='Sepal-Length vs Width')

# '''Example 09'''
# sns.scatterplot(x='sepallength', y='sepalwidth', hue='class', data=df)
# plt.show()

# '''Example 10'''
# ## From the above graph we can see that
# # Iris-virginica has a longer sepal length while Iris-setosa has larger sepal width
# # For setosa sepal width is more than sepal length
# ## Below is the Frequency histogram plot of all features
# axis = df.plot.hist(bins=30, alpha=0.5)
# axis.set_xlabel('Size in cm');

# '''Example 11'''
# # From the above graph we can see that sepalwidth is longer than any other feature followed by petalwidth
# ## examining correlation
# sns.pairplot(df, hue='class')

# '''Example 12'''
# figure, ax = plt.subplots(2, 2, figsize=(8,8))

# ax[0,0].set_title("sepallength")
# ax[0,0].hist(df['sepallength'], bins=8)

# ax[0,1].set_title("sepalwidth")
# ax[0,1].hist(df['sepalwidth'], bins=6)

# ax[1,0].set_title("petallength")
# ax[1,0].hist(df['petallength'], bins=5)

# ax[1,1].set_title("petalwidth")
# ax[1,1].hist(df['petalwidth'], bins=5)

# '''Example 13'''
# # From the above plot we can see that –
# # - Sepal length highest freq lies between 5.5 cm to 6 cm which is 30-35 cm
# # - Petal length highest freq lies between 1 cm to 2 cm which is 50 cm
# # - Sepal width highest freq lies between 3 cm to 3.5 cm which is 70 cm
# # - Petal width highest freq lies between 0 cm to 0.5 cm which is 40-45 cm