from PIL import Image
import os,random
os.chdir(r'C:\Users\sungue\Desktop\新建文件夹')

for i in range(30):
	a = random.randint(1,255)
	b = random.randint(1,255)
	c = random.randint(1,255)
	im = Image.new('RGBA',(200,500),(a,b,c))
	im.save(str(i)+'.png')