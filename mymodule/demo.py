from collections import defaultdict
dd=defaultdict(float)
incomes=[('Books',1250.00),
         ('Books',1300.00),
         ('Books',1420.00),
         ('Tutorials',560.00),
         ('Tutorials',630.00),
         ('Courses',750.00),
         ('Courses',2500.00),
         ('Courses',2430.00),
         ('Courses',2750.00),]
for p,e in incomes:
    dd[p]+=e
for b,p in dd.items():
    print('{} Total{}'.format(b,p))