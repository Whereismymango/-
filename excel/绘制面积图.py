import os
os.chdir(r'C:\Intel\SGC\新建文件夹\excel')
from openpyxl import Workbook
from openpyxl.chart import AreaChart,Reference,Series
wb = Workbook()
ws = wb.active
rows = [
['Number','Batch1','Batch2'],
[2,40,30],
[3,40,25],
[4,50,30],
[5,30,10],
[6,25,5],
[7,50,10]
]
for i in rows:
	ws.append(i)

chart = AreaChart()
chart.title = 'Area chart'
chart.style = 3
chart.x_axis.title = 'Test'
chart.y_axis.title = 'Percentage'

cat = Reference(ws,min_col=1,min_row=1,max_row=7)
data = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=7)
chart.add_data(data)
chart.set_categories(cat)

ws.add_chart(chart,'a10')
wb.save('area.xlsx')