# 52100988 Lữ Phúc Phú

import pandas as pd
import matplotlib.pyplot as plt
# Đọc bộ dữ liệu Iris vào DataFrame
df = pd.read_csv("company_sales_data.csv")
print("Câu 2:Hiển thị bộ dữ liệu ")
print(df)


x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

# Vẽ biểu đồ
plt.plot(x, y)

# Đặt tên cho trục x và y, và tên cho biểu đồ
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.title('Biểu đồ dạng đường')

# Hiển thị biểu đồ
plt.show()