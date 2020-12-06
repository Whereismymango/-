import PyPDF2
a = open(r'C:\Users\Administrator\Desktop\解约函.pdf','rb')
b = open(r'C:\Users\Administrator\Desktop\blank.pdf','rb')
writer = PyPDF2.PdfFileWriter()
reada = PyPDF2.PdfFileReader(a)
readb = PyPDF2.PdfFileReader(b)
for i in range(reada.numPages):
    page = reada.getPage(i)
    writer.addPage(page)
writer.addPage(readb.getPage(readb.numPages-1))

c = open(r'C:\Users\Administrator\Desktop\merge.pdf','wb')
writer.write(c)
c.close()