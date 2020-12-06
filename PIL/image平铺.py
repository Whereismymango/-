from PIL import Image
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')
x = Image.open('cat.jpg')
y = Image.open('new.png')
a,b = x.size
c,d = y.size
for i in range(0,a,c+10):
	for j in range(0,b,d+10):
		print(i,j)
		x.paste(y,(i,j))
x.save('1.jpg')
