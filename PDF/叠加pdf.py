
import PyPDF2,os
os.chdir(r'C:\Intel\SGC\新建文件夹\PDF')
pdf1 = open('0.1 N高氯酸在醋酸标准液 -中文版.pdf','rb')
pdf2 = open('2-Pyrrolidinone -英文版.pdf','rb')
pdf1read = PyPDF2.PdfFileReader(pdf1)
pdf2read = PyPDF2.PdfFileReader(pdf2)
o = pdf2read.getPage(0)
merge = PyPDF2.PdfFileWriter()
for i in range(pdf1read.numPages):
	obj = pdf1read.getPage(i)
	obj.mergePage(o)
	merge.addPage(obj)
	
	
pdf3 = open('叠加.pdf','wb')
merge.write(pdf3)
pdf1.close()
pdf2.close()
pdf3.close()

	
	


