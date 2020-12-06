class Makeimage:
	def __init__(self,width,height,x,y):
		self.width = width +10
		self.height = height +10
		self.widths = self.width*x+10
		self.heights = self.height*y+10
		
	def make(self):
		from PIL import Image
		o = Image.new('RGBA',(self.widths,self.heights),'blue')
		e,f = o.size
		for i in range(10,e,self.width):
			for j in range(10,f,self.height):
				print(i,j)
				o.paste(x,(i,j))
		o.save('你想要的.png')
		print('完成喽，哈哈哈！')

from PIL import Image
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')                  #在这里输入图片路径
x = Image.open('new.png')                                    #在这里输入你想平铺的图片全名
a,b =x.size
Makeimage(a,b,5,5).make()





