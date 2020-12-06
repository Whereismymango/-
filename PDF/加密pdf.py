
import PyPDF2,os
os.chdir(r'C:\Intel\SGC\新建文件夹\PDF')
pdf1 = open('0.1 N高氯酸在醋酸标准液 -中文版.pdf','rb')

pdf1read = PyPDF2.PdfFileReader(pdf1)


write = PyPDF2.PdfFileWriter()
for i in range(pdf1read.numPages):
	obj = pdf1read.getPage(i)
	
	write.addPage(obj)
write.encrypt('yonghu','yongyouzhe')	
	
pdf3 = open('加密.pdf','wb')
write.write(pdf3)
pdf1.close()

pdf3.close()

	
	


