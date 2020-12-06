import openpyxl,os
os.chdir(r'C:\Intel\SGC\新建文件夹\excel')
wb = openpyxl.load_workbook('q.xlsx')
print(wb.active.title)
sheet = wb.active
for row in sheet.values:
	for value in row:
		if value == None:
			pass
		else:
			print(value,end = '  ')
	print()

for i in sheet.rows:
	for j in i:
		print(j,end = '  ')
	print()
	
print(sheet[1:3])
	
#wb.save('qq.xlsx')
