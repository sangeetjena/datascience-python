class employee:
    ename = ""
    age = ""
    dept = ""

    def __init__(self, ename, age, dept):
        employee.ename = ename
        employee.age = age
        employee.dept = dept

    def employee_details(self):
        """
        :rtype: object
        """
        print("employee details are ename={0}  age={1} employee dept no={2}".format(employee.ename, employee.age,
                                                                                    employee.dept))



emp = employee('sangeet', 29, 20)
print(emp.ename)
emp.employee_details()
