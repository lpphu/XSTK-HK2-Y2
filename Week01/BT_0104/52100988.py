from itertools import *

# BT_104
A = {'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9'}

M3 = combinations(('M1', 'M2', 'M3', 'M4', 'M5', 'M6'),3)
W2 = combinations(('W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9'),2)

ans = product(M3,W2)
for i in ans:
    print(i)