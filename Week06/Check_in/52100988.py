# 52100988 Lữ Phúc Phú

from matplotlib import pyplot as plt

'''  Exercise_01 '''
def bemoulli(p):
    return [1-p,p]

'''  Exercise_02 '''
x = [0,1]
y = bemoulli(0.8)

plt.bar(x,y,width=0.1)
plt.show()

'''  Exercise_03 '''
def mean(p):
    return p

def var(p):
    return p*(1-p)

def std(p):
    return var(p)**(1/2)


