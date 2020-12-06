from PIL import Image
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')                 
x = Image.open('cat.jpg')                                    

x.rotate(95,expand = True).save('rote.png')




