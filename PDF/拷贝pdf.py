
import PyPDF2,os
os.chdir(r'C:\Intel\SGC\新建文件夹\PDF')
pdf1 = open('0.1 N高氯酸在醋酸标准液 -中文版.pdf','rb')
pdf2 = open('2-Pyrrolidinone -英文版.pdf','rb')
pdf1read = PyPDF2.PdfFileReader(pdf1)
pdf2read = PyPDF2.PdfFileReader(pdf2)
pdf3 = PyPDF2.PdfFileWriter()

for i in range(pdf1read.numPages):
	obj = pdf1read.getPage(i)
	pdf3.addPage(obj)
	
	
for i in range(pdf2read.numPages):
	obj = pdf2read.getPage(i)
	pdf3.addPage(obj)
	
	
allpdf = open('合并.pdf','wb')
pdf3.write(allpdf)
pdf1.close()
pdf2.close()
allpdf.close()