from collections import namedtuple
t1=('Rahul',10,290,5,8900)
person=namedtuple("P","name age place")
x=person("Raju",23,"banglore")
print(x)