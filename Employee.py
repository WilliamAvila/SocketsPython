class Employee:
    empCount = 0

    def __init__(self, codeEmployee, name, email, salary, id, phone):
        self.codeEmployee = codeEmployee
        self.name = name
        self.email = email
        self.salary = salary
        self.id=id
        self.phone = phone
        Employee.empCount += 1



    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

    def getEmployeeData(self):
       return self.codeEmployee+" "+self.name+" "+self.email+" "+self.salary+" "+self.id+" "+self.id+"\n"


