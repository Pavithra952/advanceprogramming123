import demoopenxl as xl
work_book=xl.load_workbook("C://mydatasets//hcl.xlsx.xlsx")
sheet1=work_book['sheet1']
sheet2=work_book['sheet2']
print(sheet1.max_row)
print(sheet2.max_column)
sheet1.cell(10,10).value="HCL DATA"
sheet1.cell(5,1).value='=sum(A1:A4)'
work_book.save("C//excel_data//hcl.xlsx")
excel_data=[]
for i in range(1,6):
    excel_data.append(sheet1.cell(i,3).value)
    print(excel_data)