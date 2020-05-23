class employee():
    head=[]
    def __init__(self,name,age):
        self.name=name
        self.age=age
        employee.head.append(self)

employee('sangeet',29)
employee('sid',30)
employee('sharaf',27)

for i in employee.head:
    if i.age>29:
        del i
    try:
        print(i.age,i.name)
    except:
        print("object destroyed")

for i in employee.head:
    print("final result--------------",i.age,i.name)
print("=====above i is a temp object so del that not removing object ")
del employee.head[1]

for i in employee.head:
    print("final result--------------",i.age,i.name)
print("================now object deleted============")