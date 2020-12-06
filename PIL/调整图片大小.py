from PIL import Image
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')                 
x = Image.open('cat.jpg')                                    
a,b =x.size
a = x.resize((a-300,b-200))
a.save('size.png')




