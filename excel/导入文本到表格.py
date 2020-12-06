import openpyxl,os
os.chdir(r'C:\Intel\SGC\新建文件夹\excel')
wb = openpyxl.Workbook()
sheet = wb.active
a = []
for i in os.listdir('.'):
	if i.lower().endswith('txt'):
		a.append(i)
	else:
		pass
n = 1	
for name in a:
	
	j = open(name)
	content = j.readlines()
	for i in range(1,len(content)+1):
		sheet.cell(column = n,row = i,value = content[i-1])
	n += 1
	print('已完成'+name)
wb.save('小说合并'+'.xlsx')
print('合并完成')
	
