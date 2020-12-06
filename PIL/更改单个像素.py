from PIL import Image
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')                 
x = Image.new('RGBA',(1000,1000))
for i in range(1000):
	for y in range(1000):
		a = int((i+y)*0.1)
		b = int(0.15*i+150)
		c = int((i+y)*0.25)
		x.putpixel((i,y),(a,b,c))

print(x.getpixel((999,999)))

	
x.save('change.png')



