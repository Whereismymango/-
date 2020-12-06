import openpyxl,os
os.chdir(r'C:\Intel\SGC\新建文件夹\excel')
def insert():
	a = input('请问您想对哪个文件执行插入操作插入？ ')
	b = int(input('请问您想在第几行插入？ '))
	c = int(input('请问您想插入几行？ '))
	
	wb = openpyxl.load_workbook(a)
	sheet = wb.active

	sheet.insert_rows(b,c)
	wb.save('insert.xlsx')

insert()