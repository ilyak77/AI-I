import math
import numpy as np
import matplotlib.pyplot as plt


def update(X,Y,W,eta):
	delta = calGradient(X,Y,W)
	for i in range(64):
		W[i] += delta[i] *eta
	return W

def calGradient(X,Y,W):
	t = len(X)
	delta = [0]*64

	for i in range(64):
		d = 0
		for j in range(t):
			print d
			d += (Y[j] - sigmod(np.dot(W,X[j])))*X[j][i]
		delta[i] = d 

	return delta

def sigmod(x):
	return 1 / (1 + math.exp(-x))
	


fp = open('train3.txt','r')
X = []
Y = []
for line in fp.readlines():
	X.append([int(i) for i in line.split()])
	Y.append(1)

fp.close() 

fp = open('train5.txt','r')
for line in fp.readlines():
	X.append([int(i) for i in line.split()])
	Y.append(0)

fp.close()

W = [0]*64

eta = 0.02 / len(X)

for i in range(10000):
	W = update(X,Y,W,eta)