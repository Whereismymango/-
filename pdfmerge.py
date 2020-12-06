import PyPDF2,os
os.chdir(r'C:\Users\sungue\Desktop\新建文件夹')
pdfs = []
for i in os.listdir(r'C:\Users\sungue\Desktop\新建文件夹'):
	if i.lower().endswith('pdf'):
		pdfs.append(i)
print(len(pdfs))
pdfwriter = PyPDF2.PdfFileWriter()
a = 0
b = 0
blankobj = open(r'C:\Users\sungue\Desktop\blank.pdf','rb')
blankpdfreader = PyPDF2.PdfFileReader(blankobj)
blankpageobj = blankpdfreader.getPage(blankpdfreader.numPages-1)
for i in pdfs:
	obj = open(i,'rb')
	pdfreader = PyPDF2.PdfFileReader(obj)
	if pdfreader.isEncrypted:
		a += 1
		print('第' + str(pdfs.index(i)+1) + '项文件' + i + '已加密无法破解')
	else:
		c = pdfreader.numPages
		if c % 2 == 0:
			for pagenum in range(pdfreader.numPages):
				pageobj = pdfreader.getPage(pagenum)
				pdfwriter.addPage(pageobj)
			print('已写入第' + str(pdfs.index(i)+1) + '项偶数页: ' + i)
		elif c % 2 != 0:
			for pagenum in range(pdfreader.numPages):
				pageobj = pdfreader.getPage(pagenum)
				pdfwriter.addPage(pageobj)
			pdfwriter.addPage(blankpageobj)
			print('已写入第' + str(pdfs.index(i)+1) + '项奇数页: ' + i)
		b += 1
pdfoutput = open('1.pdf','wb')
pdfwriter.write(pdfoutput)
pdfoutput.close()
print('一共合并成功' + str(b) + '项文件')
print('一共合并失败' + str(a) + '项文件')
	


