# 52100988 Lữ Phúc Phú

' ' ' BT_0405 ' ' '
from itertools import *


E = {'0','1','2','3','4','5','6'}

' ' ' a. ' ' '
print("a.")
N3 = product(E,repeat=3)
ans_a = []
for i in N3:
    temp = ''.join(i)
    if temp[0] == '0':
        continue
    ans_a.append(temp)
print(ans_a)

' ' ' b. ' ' '
print("b.")
N3 = combinations(E,4)
ans_a = []
for i in N3:
    temp = ''.join(i)
    if temp[0] == '0':
        continue
    ans_a.append(temp)
print(ans_a)




