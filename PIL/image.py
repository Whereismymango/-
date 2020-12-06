from PIL import Image
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')
cat = Image.open('zophie.png')
print(cat.size)
print(cat.filename)
print(cat.format)
print(cat.format_description)
cat.save('cat.jpg')
newcat = Image.open('cat.jpg')
print(newcat.size)
i = Image.new('RGBA',(100,200),color = (127,38,241))
i.save('1.png')
new = cat.crop((335,345,565,560))    #裁剪图片
new.save('new.png')

#复制和粘贴
catcopy = cat.copy()
catcopy.paste(new,(0,0))
catcopy.paste(new,(398,448))
catcopy.save('copy.png')

