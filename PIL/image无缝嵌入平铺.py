from PIL import Image
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')



y = Image.open('new.png')

c,d = y.size
o = Image.new('RGBA',((c+10)*5+10,(d+10)*10+10),'pink')
e,f = o.size
for i in range(10,e,c+10):
	for j in range(10,f,d+10):
		print(i,j)
		o.paste(y,(i,j))
o.save('1.png')
