from itertools import *

# # BT_101
# E = {3, 2, 1}

# # 1.
# E1 = combinations(E,2)
# print("1.",end=' ')
# for i in E1:
#     print(i,end=' ')
# print()

# # 2.
# E2 = permutations(E,2)
# print("2.",end=' ')
# for i in E2:
#     print(i,end=' ')
# print()

# # 3.
# E3 = product(E, repeat=2)
# print("3.",end=' ')
# for i in E3:
#     print(i,end=' ')
# print()

# # BT_102
# E = {'W1', 'W2', 'W3', 'W4', 'B1', 'B2', 'B3'}

# # 1.
# print("1.")
# E1 = combinations(E,2)
# s=0
# for i in E1:
#     s+=1
#     print(i,end=' ')
# print()
# print("Have",s,"ways")

# # 2.
# print("2.")
# s=0
# E1 = product(('W1', 'W2', 'W3', 'W4'),('B1', 'B2', 'B3'))
# for i in E1:
#     s+=1
#     print(i,end=' ')
# print()
# print("Have",s,"ways")

# # 3.
# print("3.")
# s=0
# E1 = product(('W1', 'W2', 'W3', 'W4'),('B1', 'B2', 'B3'))
# for i in E1:
#     s+=1
#     print(i,end=' ')
# E1 = combinations(('W1', 'W2', 'W3', 'W4'),2)
# for i in E1:
#     s+=1
#     print(i,end=' ')
# print()
# print("Have",s,"ways")

# # BT_103
# B = { 'T1', 'T2', 'T3', 'T4', 'V1', 'V2', 'V3',  'N1', 'N2' }

# # 1.
# print("1.")
# B1 = permutations(B,9)
# print("1.")
# for i in B1:
#     print(i)
# print()

# # 2.
# print("2.")
# B1 = combinations(B,5)
# for i in B1:
#     print(i,end)
# print()

# # 3.
# print("3.")
# B1 = combinations(('T1', 'T2', 'T3', 'T4'), 3)
# B2 = combinations(('V1', 'V2', 'V3',  'N1', 'N2'), 2)
# B3 = product(B1,B2)
# for i in B3:
#     print(i,end=' ')
# print()

# # 4.
# print("4.")
# B1 = combinations(('T1', 'T2', 'T3', 'T4', 'V1', 'V2', 'V3'),3)
# for i in B1:
#     print('N1',i,'N2')
# B1 = combinations(('T1', 'T2', 'T3', 'T4', 'V1', 'V2', 'V3'),4)
# print()

# # 5.
# print("5.")
# T2 = combinations(('T1', 'T2', 'T3', 'T4'), 2)
# V2 = combinations(('V1', 'V2', 'V3'), 2)
# N2 = combinations(('N1', 'N2'), 2)

# B1 = product(T2,V2,('N1', 'N2'))
# for i in B1:
#     print(i)
# B1 = product(T2,N2,('V1', 'V2', 'V3'))
# for i in B1:
#     print(i)
# B1 = product(N2,V2,('T1', 'T2', 'T3', 'T4'))
# for i in B1:
#     print(i)

# T3 = combinations(('T1', 'T2', 'T3', 'T4'), 3)
# V3 = combinations(('V1', 'V2', 'V3'), 3)

# B2 = product(T3,('V1', 'V2', 'V3'),('N1', 'N2'))
# for i in B2:
#     print(i)
# B2 = product(V3,('T1', 'T2', 'T3', 'T4'),('N1', 'N2'))
# for i in B2:
#     print(i)

# T4 = combinations(('T1', 'T2', 'T3', 'T4'), 4)
# B3 = product(T4,'V1', 'V2', 'V3',  'N1', 'N2')
# for i in B3:
#     print(i)

# BT_104
# A = {'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9'}

# M3 = combinations(('M1', 'M2', 'M3', 'M4', 'M5', 'M6'),3)
# W2 = combinations(('W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9'),2)

# ans = product(M3,W2)
# for i in ans:
#     print(i)

# BT_105
card = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K'}
suit = {'♠' , '♣', '♦', '♥'}
deck = list(product(card,suit))

' ' ' Câu 1 ' ' '
# C5 = combinations(deck, 5)
# for i in C5:
#     print(i)

' ' ' Câu 2 ' ' '
# red = list(product(card,('♦', '♥')))
# black = list(product(card,('♠' , '♣')))

# C5 = product(red,combinations(black,4))
# for i in C5:
#     print(i)

' ' ' Câu 3 ' ' '
# C5 = combinations(deck, 5)
# for i in C5:
#     print(i[0])


# S5 = product(combinations(suit,3),suit,suit)
