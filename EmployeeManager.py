__author__ = 'william'

from Employee import Employee



def editEmployee(code,emp):

    ln = searchLine(code)
    replace_line("Employee.txt", ln-1, emp)

def findValue(val):
    print(val)
    with open("Employee.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if val in part:
                    return val
    return  ' '


def searchLine(id):
    linenumber=0;
    with open("Employee.txt") as openfile:
        for line in openfile:
            linenumber += 1
            for part in line.split():
                if id in part:
                    print part
                    return linenumber
    return 0

def searchEmployee(id):
    if len(id)==4:
        with open("Employee.txt", 'r') as openfile:
            for line in openfile:
                if id in line:
                    return line
    return ' '


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def insertEmployee(emp):
    file = open("Employee.txt", "a")
    file.write(emp)

    file.close()

def listEmployees():
    str=""
    file = open('Employee.txt', 'r')
    for line in file:
        str += line
        print line
    return str

emp = Employee("aa11","William","william.zx1@gmail.com","0","1804199301762","33165891")
emp2 = Employee("aa12","Arturo","william.zx1@hotmail.com","0","1804199301763","33165892")
emp3 = Employee("aa13","QQiam","william.zx1@gg.com","0","1804199301764","33165893")



