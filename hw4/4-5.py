import numpy as np

def calculate(array):
	A = []
	B = []
    
	for i in range(4):
		B.append(float(0))
		A.append([])
		for j in range(4):
			A[i].append(float(0))

	for i in range(4):
		for j in range(4):
			cur = 0.0
			for k in range(4, len(array)):
				cur += array[k-j-1]*array[k-i-1]
			A[i][j] = cur

	for i in range(4):
		cur = 0.0
		for k in range(4,len(array)):
			cur += array[k] * array[k-i-1]
		B[i] = cur

	A = np.array(A,float)
	B = np.array(B,float)
	X = np.dot(np.linalg.inv(A) , B)
	return X

def error(array,X):
	Y = []
	Y.append(array[0])
	Y.append(array[1])
	Y.append(array[2])
	Y.append(array[3])
	for i in range(4, len(array)):
		cur = X[0]*array[i-1] + X[1]*array[i-2] + X[2]*array[i-3] + X[3]*array[i-4]
		Y.append(cur)

	e = 0.0
	for i in range(len(Y)):
		#e += (Y[i] - array[i+4]) **2
		e += (Y[i] - array[i]) **2
	e /= len(Y)
	print e



#fp = open('nasdaq00.txt', 'r')
fp = open('nasdaq01.txt', 'r')
array2000 = []
for line in fp.readlines():
	line = line.strip('\n').split(' ')
	array2000.append(float(line[0]))

X = []
X = calculate(array2000)
print X

error(array2000,X)



