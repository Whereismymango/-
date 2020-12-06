#coding:utf-8
import PyPDF2,os
all = {}
path = []
for a,b,c in os.walk(r'C:\Intel\SGC\试剂\MSDS'):
	for i in c:
		all[i] = os.path.join(a,i)		
print(len(all))
newall = {}
for i,j in all.items():
	if i.lower().endswith('pdf'):
		newall[i] = j
	
print(len(newall))


for i,j in newall.items():
	
	write = PyPDF2.PdfFileWriter()
	file = open(j,'rb')
	fileread = PyPDF2.PdfFileReader(file)
	if fileread.isEncrypted :
		print('.........................                          ............',i,'已加密')
	else:
		for page in range(fileread.numPages):
			write.addPage(fileread.getPage(page))
		#write.encrypt('yonghu')
		os.chdir(r'C:\Intel\SGC\试剂\MSDS\机密整理')
		newpdf = open(str(i)+'_encrypt.pdf','wb')
		write.write(newpdf)
		print('已完成',i)
		file.close()
		newpdf.close()
	






