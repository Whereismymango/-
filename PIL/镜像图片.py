from PIL import Image
import os
os.chdir(r'C:\Intel\SGC\新建文件夹\PIL')                 
x = Image.open('cat.jpg')                                    

x.transpose(Image.FLIP_LEFT_RIGHT).save('水平镜像.png')
x.transpose(Image.FLIP_TOP_BOTTOM).save('垂直镜像.png')



