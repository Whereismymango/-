from PIL import Image,ImageDraw
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')                 
im = Image.new('RGBA',(1000,1000),'white')
draw = ImageDraw.Draw(im)
draw.line([0,0,50,300,60,500,500,59,59,39,509,987],'pink',2)
draw.point([9,38,87,86,985,357,64,88,76,432,67,87],'red')
draw.rectangle((5,89,78,82),'yellow','blue')
for i in range(100,200,10):
	draw.line([i,0,200,i-10],'black')
im.save('draw.png')