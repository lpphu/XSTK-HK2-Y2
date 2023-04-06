#  52100988 Lữ Phúc Phú

import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
# %matplotlib inline 

df = pd.read_csv("iris_csv.csv") 
df.head()

#2. Hiển thị bộ dữ liệu vừa thu thập (Câu 1) dưới dạng BẢNG THỐNG KÊ phân loại theo cột loài hoa (class) và 04 cột gồm đặc trưng với kích thước ( sepallength, sepalwidth, petallength, petalwidth ).
print(df)

#3. Hiển thị dữ liệu vừa thu thập (Câu 1) dưới dạng BẢNG THỐNG KÊ với 10 dòng đầu tiên chỉ với cột loài hoa ("class").
result_1 = df.head(10)
print(result_1[['class']].to_string(index=False)) 

#4. Hiển thị dữ liệu vừa thu thập (Câu 1) dưới dạng BẢNG THỐNG KÊ với 10 dòng cuối cùng gồm cột loài hoa ("class ") và một cột kích thước với đặc trưng bất kì ( sepallength, sepalwidth, petallength, petalwidth ).
result_2 = df.tail(10)
print(result_2[['class', 'petalwidth']].to_string(index=False)) 

#5. Hiển thị bộ dữ liệu vừa thu thập (Câu 1) dưới dạng BIỂU ĐỒ.
figure, ax = plt.subplots(2, 2, figsize=(8,8))

ax[0,0].set_title("sepallength")
ax[0,0].hist(df['sepallength'], bins=8)

ax[0,1].set_title("sepalwidth")
ax[0,1].hist(df['sepalwidth'], bins=6);

ax[1,0].set_title("petallength")
ax[1,0].hist(df['petallength'], bins=5);

ax[1,1].set_title("petalwidth")
ax[1,1].hist(df['petalwidth'], bins=5);

plt.show()