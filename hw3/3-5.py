
from math import log
import matplotlib.pyplot as plt

def lu(judge):
	token = judge.upper().strip('\n').split(' ')
	p = 1.0
	for i in range(0,len(token)):
		p *= cal1(token[i])
	return log(p*1.0)

def cal1(val1):
	return tokenDict[val1]*1.0/ totalCount

def lb(judge):
	token = judge.upper().strip('\n').split(' ')
	pa = token[0]
	p = cal2('<s>',pa)
	for i in range(1, len(token)):
		if not token[i] in orderDict[token[i-1]]:
			print 'no %s followed by %s' % (token[i-1], token[i])
			break
		else:
			p *= cal2(token[i-1],token[i])
	return log(p*1.0)

def cal2(val1, val2):
	return orderDict[val1][val2]/tokenDict[val1];

def lm(judge, r):
	token = judge.upper().strip('\n').split(' ')
	pa = token[0]
	p = cal2('<s>',pa)*(1-r)
	for i in range(1,len(token)):
		if not token[i] in orderDict[token[i-1]]:
			p *= (1-r)*cal1(token[i])
		else:
			p *= (1-r)*cal1(token[i]) + r*cal2(token[i-1],token[i])
	return log(p*1.0)



voc = open('vocab.txt','r')
tokenDict = {}
tokenList = []
for token in voc.readlines():
	token = token.strip('\n');
	tokenList.append(token)
	tokenDict[token] = 0

uni = open('unigram.txt','r')
totalCount = 0
index = 0
for count in uni.readlines():
	tokenDict[tokenList[index]] = int(count)
	totalCount += int(count)
	index += 1

# (a)
for token in tokenList:
	if token[0] == 'B':
		print 'for word %s, the probality is %f' % (token, tokenDict[token]*1.0 / totalCount)


bi = open('bigram.txt', 'r')
orderDict = {}
for line in bi.readlines():
	line = line.split('\t')
	i1 = int(line[0]) - 1
	i2 = int(line[1]) - 1
	count2 = float(line[2])
	if not tokenList[i1] in orderDict.keys():
		orderDict[tokenList[i1]] = {}
	orderDict[tokenList[i1]].update({tokenList[i2]:count2})

#(b)
b = sorted(orderDict['ONE'].items(), key = lambda x: x[1], reverse = True)
for i in range(0,10):
   print ('The word %s has probality %f') % (b[i][0], b[i][1]*1.0/tokenDict['ONE'])

#(c)
print lu('The stock market fell by one hundred points last week')
print lb('The stock market fell by one hundred points last week')
#(d)
print lu('The fourteen officials sold fire insurance')
print lb('The fourteen officials sold fire insurance')

#(e)
pp = []
rr = []
for r in range(0,100,10):
	pp.append(lm('The fourteen officials sold fire insurance',r*1.0/100))
	rr.append(r*1.0/100)

print pp
print rr

plt.plot(rr,pp)
plt.show()
