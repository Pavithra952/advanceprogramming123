import openpyxl as xl
from openpyxl.styles import Font,Alignment
wb=xl.load_workbook("C:\mydatasets//pavithra.xlsx")
sh=wb.active
font=Font(bold=True,size=20)
algnmt=Alignment(horizontal='center')
sh['A1'].font=font
sh['A1'].alignment=algnmt
wb.save("C:\mydatasets//pavithra.xlsx")
