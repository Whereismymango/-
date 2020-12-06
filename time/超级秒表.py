import time
print('Press ENTER to begin .Afterwards ,press ENTER to "click" the stopwatch.Press Ctrl_c to quit')
input()
print('Started')
starttime = time.time()
lasttime = starttime
lapnum = 1
try:
	while True:
		input()
		laptime = round(time.time()-lasttime,2)#实际上代码处理也需要时间，如果把这里2改的大一点，就会发现第一圈总时间和圈时间是不一样的
		totaltime = round(time.time()-starttime,2)
		print('Lap {0}:{1}({2})'.format(lapnum,totaltime,laptime))
		lapnum += 1
		lasttime = time.time()
except KeyboardInterrupt:
	print('\nDone')
