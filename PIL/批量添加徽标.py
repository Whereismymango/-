
from PIL import Image
import os,time
w = time.time()
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')                 
comparison = 300
filename = 'catlogo.png'
logo = Image.open(filename)
a,b = logo.size
a = int(a*100/b)
b = 100
newlogo = logo.resize((a,b))

os.makedirs('Logo',exist_ok = True)
for i in os.listdir('.'):
	if not (i.lower().endswith('png') or i.lower().endswith('jpg')) or i == filename:
		continue
	im = Image.open(i)
	c,d = im.size
	
	
	if c > comparison or d > comparison:
		if c>d:
	
			d = int(d*comparison/c)
			c = comparison
		else:
	
			c = int(c*comparison/d)
			d = comparison
	
	else:
		d = int(d*comparison/c)
		c = comparison
		im = im.resize((c,d))
	
	print('Resizing {0}'.format(i))
	im = im.resize((c,d))
	
	print('Adding logo to {0}...'.format(i))
	im.paste(newlogo,(c-a,d-b),newlogo)        #这里如果没有第三个参数，会把不透明的像素复制过来，影响观感
	im.save(os.path.join('Logo',i))
	print(im.size)
q = time.time()
print(q-w)