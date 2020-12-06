import matplotlib.pyplot as plt
from random import choice

class manbu():
	def __init__(self,n):
		self.n = n
		self.x = [0]
		self.y = [0]
	def run(self):
		while len(self.x) < self.n:
			xcho = choice([0,1,2,3,4])
			xstep = choice([-1,1])
			xstep = xcho*xstep
			ycho = choice([0,1,2,3,4])
			ystep = choice([-1,1])
			ystep = ycho*ystep
			if xstep == ystep == 0:
				continue
			next_x = self.x[-1] + xstep
			next_y = self.y[-1] + ystep
			self.x.append(next_x)
			self.y.append(next_y)
			
		
a = manbu(4000)
a.run()
x = a.x	
y = a.y
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.scatter(x,y,s =14,c = x,cmap = plt.cm.Reds)
plt.title('随机漫步',fontsize = 14)
plt.xlabel('x轴',fontsize = 14,c = 'red')
plt.ylabel('y轴',fontsize = 14)
plt.tick_params(axis = 'both',which = 'major', labelcolor = 'red')

plt.show()
		

		