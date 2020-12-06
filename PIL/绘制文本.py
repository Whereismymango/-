from PIL import Image,ImageDraw,ImageFont
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')                 
im = Image.new('RGBA',(1000,1000),'white')
draw = ImageDraw.Draw(im)
draw.text((458,437),'Hello!','blue')

font = ImageFont.truetype('BAUHS93.TTF',52)
draw.text((678,765),'wow!','red',font)
im.save('text.png')
