import pandas as pd
from functools import reduce
l=[]
sheet_names=['jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec']
for i in sheet_names:
    df=pd.read_excel("C://mydatasets//Book1.xlsx",sheet_name=i)
    l.append(df)
data=reduce(lambda left,right:pd.merge(left,right,on='product_id',how='inner'),l)
print(l)
data.to_excel("C://mydatasets//project_excel.xlsx")