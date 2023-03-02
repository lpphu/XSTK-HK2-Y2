# 52100988 Lữ Phúc Phú

from itertools import *
import math
import random
import matplotlib.pyplot as plt
import numpy as np

blue = ['B1', 'B2', 'B3', 'B4']
red = ['R1', 'R2', 'R3', 'R4', 'R5']

''' 1. '''
print("1.")
E = blue
for i in red:
    E.append(i)
print(E)

''' 2. '''
print('2.')
BALLS_39 = list(combinations(E,3))
print(len(BALLS_39))

''' 3. '''
print("3.")
X = [0, 1, 2, 3]
print(X,"Lấy được 0 quả bóng màu xanh, Lấy được 1 quả bóng màu xanh, Lấy được 2 quả màu xanh, Lấy được 3 quả màu xanh")

''' 4. '''
print("4.")
P_0 = 0
P_1 = 0
P_2 = 0
P_3 = 0
for i in BALLS_39:
    temp = ''.join(i)
    match(temp.count('B')):
        case 1:
            P_1 += 1
        case 2:
            P_2 += 1
        case 3:
            P_3 += 1
        case _:
            P_0 += 1
P_1 = P_1
P_2 = P_2
P_3 = P_3
print('P(X=1) =',P_1/len(BALLS_39),'; P(X=2) =',P_2/len(BALLS_39),'; P(X=3) =',P_3/len(BALLS_39))

''' 5. '''
print("5.")
EX = P_1/len(BALLS_39)*1 + P_2/len(BALLS_39)*2 + P_3/len(BALLS_39)*3
print("EX =",EX)

''' 6. Phương sai để bốc được quả bóng màu xanh '''
print("6.")
# Tính giá trị trung bình
avg = (P_1 + P_2 + P_3)/3

# Tính hiệu của các giá trị với giá trị trung bình và sau đó bình phương chúng
d_1 = pow((P_1-avg),2)
d_2 = pow((P_2-avg),2)
d_3 = pow((P_3-avg),2)

# Tính trung bình của các giá trị vừa tính
avg_d = (d_1 + d_2 + d_3)/3

# Phương sai là căn bậc 2 của giá trị vừa tìm được
VARX = math.sqrt(avg_d)

print("VARX = ",VARX)

''' 7. '''
data = [P_0, P_1, P_2, P_3]
count_blue = ["0 ball have Blue","1 ball have Blue","2 balls have Blue", "3 ball have Blue"]

plt.pie(data, labels = count_blue)
# plt.legend()
plt.show()