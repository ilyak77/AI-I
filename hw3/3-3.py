from random import randint
from math import pow
import matplotlib.pyplot as plt

def convert(B):
    f = 0
    base = 1
    for i in range(0, len(B)):
        f += base * B[i]
        base *= 2
    return f

def genRandom(n):
    b=[]
    for i in range(0,10):
        b.append(randint(0,1))
    return b

n = 10
alpha = 0.25
numerator = 0
denominator = 0
Z = 128
p = 1
l =[]
t = []
for i in range(0, 1000000):
    B = genRandom(n)
    f = convert(B)
    pf = (1-alpha)/(1+alpha) * pow(alpha, abs(Z - f))
    denominator += pf
    if B[7] == 1:
        numerator += pf
    if denominator > 0:
        p = numerator / denominator
    if (i+1) % 2000 == 0:
        #print p
        t.append(i)
        l.append(p)

plt.plot(t,l)
plt.show()