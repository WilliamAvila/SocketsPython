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
        st = self.codeEmployee+" "
        st += self.name+" "+self.email+" "+str(self.salary)+" "+str(self.id)+" "+str(self.phone)+"\n"
        return st

