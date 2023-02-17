# 52100988 Lữ Phúc Phú

from itertools import *

' ' ' Exercise01 ' ' '
S = list(product({'M','F'},repeat=3))
temp = []
for i in S:
    s = ''.join(i)
    temp.append(s)
S = temp
print("1.",S)

' ' ' Exercise02 ' ' '
print("2.",len(S))

' ' ' Exercise02 ' ' '
B = []
for i in S:
    if 'F' in i:
        B.append(i)
print("3.",B)

' ' ' Exercise03 ' ' '
A = []
for i in S:
    if 'FFF' in i:
        A.append(i)
print("4.",A)

' ' ' Exercise04 ' ' '
P = len(A)/len(B)
print("5.",P)




