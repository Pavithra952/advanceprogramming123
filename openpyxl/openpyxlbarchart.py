from openpyxl import Workbook
from openpyxl.chart import ScatterChart,Reference
workbook=Workbook()
sheet=workbook.active
rows=[["pavi","pavithra","pavi2"],[1,2,3],[3,4,5],[5,6,7]]
for row in rows:
    sheet.append(row)
# workbook.save("C://mydatasets//mysheet.xlsx")
chart=ScatterChart()
xdata=Reference(worksheet=sheet,
               min_row=1,
               max_row=8,
               min_col=1,
               max_col=3)
ydata=Reference(worksheet=sheet,
               min_row=1,
               max_row=8,
               min_col=1,
               max_col=3)
chart.add_data(xdata,ydata, titles_from_data=True)
sheet.add_chart(chart,"E2")
workbook.save("C://mydatasets//Scatter.xlsx")

