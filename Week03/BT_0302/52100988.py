# 52100988 Lữ Phúc Phú

from itertools import *

' ' ' Exercise01 ' ' '
S = list(product({'B','G'},repeat=3))
temp = []
for i in S:
    s = ''.join(i)
    temp.append(s)
S = temp
print("1.",S)

' ' ' Exercise02 ' ' '
A = []
for i in S:
    c = 0
    for j in i:
        if j == 'B':
            c += 1
    if c == 2:
        A.append(i)
B = []
for i in S:
    if 'G' in i:
        B.append(i)
print(A)
print("3.",len(A)/len(B))