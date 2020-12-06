import openpyxl,os
os.chdir(r'C:\Intel\SGC\新建文件夹\excel')
wb = openpyxl.load_workbook('试剂柜张贴表-最终版.xlsx')
print(wb.active.title)
sheet = wb.active
sheet.freeze_panes = 'C10'


wb.save('试剂柜张贴表-处理版.xlsx')
