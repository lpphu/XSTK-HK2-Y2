# 52100988 Lữ Phúc Phú

from matplotlib import pyplot as plt


p = 0.1
X = [0,1,2,3,4,5]

''' Exercise 01 '''
def ex_01(x,p,k):
    return p**k*(1-p)**(len(x)-k)
print(ex_01(X,p,2))

''' Exercise 02 '''
def binomial(x,p):
    ans = []
    for i in x:
        ans.append(ex_01(x,p,i))
    return ans
y = binomial(X,0.1)

s=0
for i in y:
    s+=i
print(s)

plt.bar(X,y,width=0.1)
plt.show()