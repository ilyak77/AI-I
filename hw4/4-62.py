import math
import numpy as np
import matplotlib.pyplot as plt


def update(X,Y,W):

	t = len(X)
	delta = [0]*64

	for i in range(t):
		d = Y[i] - sigmod(np.dot(X[i],W))
		for j in range(len(X[i])):
			delta[j] += d * X[i][j]
	h = hessian(X,W)
	print h
	for i in range(64):
		W[i] += h* delta[i]

	return W
     
def sigmod(x):
	return 1 / (1 + math.exp(-x))
	
def hessian(X,W):
	h = 0.0
	for i in range(len(X)):
		h += sigmod(np.dot(X[i],W)) * sigmod(np.dot(X[i],-1 * np.array(W))) * np.matrix(X[i]) *np.matrix(X[i]).getT()
	return h
		

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

for i in range(10):
	W = update(X,Y,W)