import openpyxl,os
os.chdir(r'C:\Intel\SGC\新建文件夹\excel')
wb = openpyxl.load_workbook('小说合并.xlsx')
sheet = wb.active

n = 1 
'''这里让n等于1，主要是因为无法从excel表找到各小说的名字，可能要用到正则，该步需要进一步完善'''   
for i in list(sheet.columns):
	content = []
	for j in i:
		text = j.value
		content.append(text)
		
		if text != None:
			name = text
		else:
			pass
		
	txt = open(str(n)+'_copy.txt','a')
	for i in range(len(content)):
		if content[i] != None:
			txt.write(str(content[i]))        
		else:
			pass
	txt.close()
	print('已完成'+str(n))
	n += 1
