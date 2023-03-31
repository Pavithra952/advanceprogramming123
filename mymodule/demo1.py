from collections import defaultdict
dd=defaultdict(float)
ds=defaultdict(int)
incomes=[('books',1250.00),('books',1300.00),('books',1420.00)]
for d,e in incomes:
    dd[d]=dd[d]+e
print(dd)