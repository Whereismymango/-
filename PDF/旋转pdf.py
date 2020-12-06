
import PyPDF2,os
os.chdir(r'C:\Intel\SGC\新建文件夹\PDF')
pdf1 = open('0.1 N高氯酸在醋酸标准液 -中文版.pdf','rb')
pdf1read = PyPDF2.PdfFileReader(pdf1)
pdfwrite = PyPDF2.PdfFileWriter()
for i in range(pdf1read.numPages):
	rotatepdf = pdf1read.getPage(i).rotateCounterClockwise(90)
	pdfwrite.addPage(rotatepdf)
	
pdf2 = open('旋转.PDF','wb')
pdfwrite.write(pdf2)
pdf1.close()
pdf2.close()