
import PyPDF2,os
os.chdir(r'C:\Intel\SGC\新建文件夹\PDF')
pdf = open('2-Pyrrolidinone -英文版.pdf','rb')
pdfcontent = PyPDF2.PdfFileReader(pdf)
print(pdfcontent.numPages)


page = pdfcontent.getPage(0)
print(page.extractText())