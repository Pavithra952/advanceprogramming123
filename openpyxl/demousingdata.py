import openpyxl as xl
from dataclasses import dataclass
@dataclasses
class Person:
    name:str
    contact:int
    email:str
    location:str
wb=xl.Workbook()
ws=wb.active
persons=[
    Person(name="Raju",contact=454545,email='raju@gmail.com',location='banglore'),

]