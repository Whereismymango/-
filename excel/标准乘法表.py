def caluate(n):
	import openpyxl,os
	from openpyxl.styles import Font,colors,Alignment
	os.chdir(r'C:\Intel\SGC\新建文件夹\excel')
	wb = openpyxl.Workbook()
	sheet = wb.active
	
	
	
	
	
	for i in range(1,n+1):
		for j in range(1,n+1):
			if i >= j:
				sheet.cell(row = i,column = j,value = i*j)
			else:
				pass
	wb.save('标准乘法表.xlsx')

caluate(9)