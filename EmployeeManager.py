__author__ = 'william'

from Employee import Employee



def modifyEmployee(id,emp):

    ln = searchEmployee(id)
    replace_line("Employee.txt", ln-1, emp.getEmployeeData())


def searchEmployee(id):
    linenumber=0;
    with open("Employee.txt") as openfile:
        for line in openfile:
            linenumber += 1
            for part in line.split():
                if id in part:
                    print part
                    return linenumber
    return 0


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def insertEmployee(emp):
    file = open("Employee.txt", "a")
    file.write(emp.getEmployeeData())

    file.close()

def listEmployees():
    file = open('Employee.txt', 'r')
    for line in file:
        print line,

emp = Employee("aa11","William","william.zx1@gmail.com","0","1804199301762","33165891")
emp2 = Employee("aa12","QQiam","william.zx1@gmail.com","0","1804199301762","33165891")
emp3 = Employee("aa13","QQiam","william.zx1@gmail.com","0","1804199301762","33165891")

listEmployees()
searchEmployee("aa12")
modifyEmployee("aa13", emp2)




