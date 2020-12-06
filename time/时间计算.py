import time
def calcProd():
	p = 1
	for i in range(1,100000):
		p = p*i
	return p

starttime = time.time()
p = calcProd()
endtime = time.time()
print('结果是   {0}'.format(p))
print('累计用时：',endtime-starttime)