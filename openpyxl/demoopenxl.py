import openpyxl as xl
wb=xl.load_workbook("C://mydatasets//book3.xlsx")
sheet=wb['Sheet1']
l=[]
l1=[]
sheet=wb.active
for i in range(1,5):
     l1=[]
     for j in range(1,4):
        l1.append(sheet.cell(i,j).value)
     l.append(l1)

print(l)
