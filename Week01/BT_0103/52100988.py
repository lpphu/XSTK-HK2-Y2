from itertools import *

# BT_103
B = { 'T1', 'T2', 'T3', 'T4', 'V1', 'V2', 'V3',  'N1', 'N2' }

# 1.
print("1.")
B1 = permutations(B,9)
print("1.")
for i in B1:
    print(i)
print()

# 2.
print("2.")
B1 = combinations(B,5)
for i in B1:
    print(i,end=' ')
print()

# 3.
print("3.")
B1 = combinations(('T1', 'T2', 'T3', 'T4'), 3)
B2 = combinations(('V1', 'V2', 'V3',  'N1', 'N2'), 2)
B3 = product(B1,B2)
for i in B3:
    print(i,end=' ')
print()

# 4.
print("4.")
B1 = combinations(('T1', 'T2', 'T3', 'T4', 'V1', 'V2', 'V3'),3)
for i in B1:
    print('N1',i,'N2')
B1 = combinations(('T1', 'T2', 'T3', 'T4', 'V1', 'V2', 'V3'),4)
print()

# 5.
print("5.")
T2 = combinations(('T1', 'T2', 'T3', 'T4'), 2)
V2 = combinations(('V1', 'V2', 'V3'), 2)
N2 = combinations(('N1', 'N2'), 2)

B1 = product(T2,V2,('N1', 'N2'))
for i in B1:
    print(i)
B1 = product(T2,N2,('V1', 'V2', 'V3'))
for i in B1:
    print(i)
B1 = product(N2,V2,('T1', 'T2', 'T3', 'T4'))
for i in B1:
    print(i)

T3 = combinations(('T1', 'T2', 'T3', 'T4'), 3)
V3 = combinations(('V1', 'V2', 'V3'), 3)

B2 = product(T3,('V1', 'V2', 'V3'),('N1', 'N2'))
for i in B2:
    print(i)
B2 = product(V3,('T1', 'T2', 'T3', 'T4'),('N1', 'N2'))
for i in B2:
    print(i)

T4 = combinations(('T1', 'T2', 'T3', 'T4'), 4)
B3 = product(T4,'V1', 'V2', 'V3',  'N1', 'N2')
for i in B3:
    print(i)