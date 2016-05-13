__author__ = 'zhewang711'
import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def __init__(self):
        self.array_00 = []
        self.array_01 = []
        self.A = []
        self.B = []
        self.X = None
        self.predict_01 = []
        self.predict_00 = []

    def _read_data(self):
        fp = open('nasdaq00.txt', 'r')
        for line in fp:
            self.array_00.append(float(line[:-1]))
        fp.close()
        fp = open('nasdaq01.txt', 'r')
        for line in fp:
            self.array_01.append(float(line[:-1]))
        fp.close()

    def _calculate_matrix(self):
        # linear equations: Ax=B, where x is [a1, a2, a3]

        # initialize Matrix A and B
        for i in range(3):
            self.B.append(None)
            self.A.append([])
            for j in range(3):
                self.A[i].append(float(0))

        # compute Matrix A
        for i in range(3):
            for j in range(3):
                tmp = 0.0
                for t in range(3, len(self.array_00)):
                    tmp += self.array_00[t-j-1]*self.array_00[t-i-1]
                self.A[i][j] = tmp

        # compute Matrix B
        for i in range(3):
            tmp = 0.0
            for t in range(3, len(self.array_00)):
                tmp += self.array_00[t]*self.array_00[t-i-1]
            self.B[i] = tmp
        # solve
        A = np.array(self.A, float)
        B = np.array(self.B, float)
        X = np.dot(np.linalg.inv(A) , B)
        self.X = X

    def _predict(self):
        self.predict_01.append(self.X[2]*self.array_00[-3] + self.X[1]*self.array_00[-2] + self.X[0]*self.array_00[-1])
        self.predict_01.append(self.X[2]*self.array_00[-2] + self.X[1]*self.array_00[-1] + self.X[0]*self.array_01[0])
        self.predict_01.append(self.X[2]*self.array_00[-1] + self.X[1]*self.array_01[0] + self.X[0]*self.array_01[1])
        #self.predict_01.append(self.array_01[0])
        #self.predict_01.append(self.array_01[1])
        #self.predict_01.append(self.array_01[2])

        for i in range(3, len(self.array_01)):
            tmp = self.X[0]*self.array_01[i-1] + self.X[1]*self.array_01[i-2] + self.X[2]*self.array_01[i-3]
            self.predict_01.append(tmp)

        self.predict_00.append(self.array_00[0])
        self.predict_00.append(self.array_00[1])
        self.predict_00.append(self.array_00[2])
        for i in range(3, len(self.array_00)):
            tmp = self.X[0]*self.array_00[i-1] + self.X[1]*self.array_00[i-2] + self.X[2]*self.array_00[i-3]
            self.predict_00.append(tmp)



    def _cal_MSE(self):
        MSE_1 = 0
        for i in range(len(self.array_01)):
            MSE_1 += (self.predict_01[i] - self.array_01[i])**2
        MSE_1 /= len(self.array_01)

        MSE_0 = 0
        for i in range(len(self.array_00)):
            MSE_0 += (self.predict_00[i] - self.array_00[i])**2
        MSE_0 /= len(self.array_00)

        return MSE_0, MSE_1


if __name__ == '__main__':
    s = Solution()
    s._read_data()
    s._calculate_matrix()
    print('question1: ', s.X)
    s._predict()
    x, y = s._cal_MSE()
    print('question2: MSE2000={0} MSE2001={1}'.format(x, y))
    plt.plot(s.array_00 + s.array_01)
    plt.plot(s.predict_00 + s.predict_01)
    plt.show()