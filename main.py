__author__ = 'william'

import socket
import ValidateEmployee
from Employee import Employee
val = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2222

print('Connecting to the server...')
s.connect((host, port))
print('Connection established...')

msg = s.recv(1024)

def getValidatedEmployee(code):
    uni = 'unique,'
    uniE = 'unique,'
    uniN = 'unique,'
    name = raw_input('Enter Name: \n')
    if ValidateEmployee.validateName(name):
        print(name + ' Is not valid')
        return None

    email = raw_input('Enter Email: \n')
    if ValidateEmployee.validateEmail(email):
        print(email + ' Is not valid')
        return None

    uniE += email
    s.send(uniE.encode('utf-8'))
    enc = s.recv(1024)
    if enc.decode('utf-8') == email:
        print("Email Duplicated")
        return None

    salary = raw_input('Enter Salary: \n')
    if ValidateEmployee.validateSalary(salary):
        print(salary + ' Is not valid')
        return None

    id = raw_input('Enter ID: ')
    if ValidateEmployee.validateId(id):
        print(id + ' Is not valid')
        return None

    uni += id
    s.send(uni.encode('utf-8'))
    enc = s.recv(1024)
    if enc.decode('utf-8') == id:
        print("ID Duplicated")
        return None

    phone = raw_input('Enter Phone number: \n')
    if ValidateEmployee.validatePhone(phone):
        print(str(phone) + ' Is not valid')
        return None

    uniN += phone
    s.send(uniN.encode('utf-8'))
    enc = s.recv(1024)
    if enc.decode('utf-8') == phone:
        print("Phone Duplicated")
        return None



    emp = Employee(code,name,email,salary,id,phone)
    print("Validated")
    return emp


def insertEmployee():
    cod = 'insert,'

    code = ValidateEmployee.generateCode()
    print('Code: ' + str(code))

    cod2="unique,"
    cod2 += code
    s.send(cod2.encode('utf-8'))
    enc = s.recv(1024)
    res = enc.decode('utf-8')
    if res == code:
        print "Code already exists try again"
        return


    emp = getValidatedEmployee(code)

    if emp:
        cod += emp.getEmployeeData()
    else:
        return

    s.send(cod.encode('utf-8'))
    print("Employee Added Correctly \n")


def editEmployee():
    cod ='edit,'
    cod2="search,"

    code = raw_input("Enter EmployeeCode \n")
    cod2 += code
    s.send(cod2.encode('utf-8'))
    enc = s.recv(1024)
    res = enc.decode('utf-8')
    if res != ' ':
        print(res)
    elif res:
        print('Code: ' + str(code))
        print('Not Found')
        return


    emp = getValidatedEmployee(code)
    if emp:
        cod += code+","
        cod += emp.getEmployeeData()
    else:
        return

    s.send(cod.encode('utf-8'))
    print("Employee Edited Correctly")


def searchEmployee():
    cod = 'search,'
    cod += raw_input('Enter Employee code: ')
    s.send(cod.encode('utf-8'))
    enc = s.recv(1024)
    res = enc.decode('utf-8')
    if res != ' ':
        print(res)
    elif res:
        print('Not Found')

def listEmployee():
    cod='list'
    s.send(cod.encode('utf-8'))
    enc = s.recv(1024)
    print(enc.decode('utf-8'))

while val:
    print ("""
    1.Insert Employee
    2.Edit Employee
    3.Search Employee
    4.List Employee
    5.Exit
     """)
    try:
        val = int(raw_input("Enter Number: \n"))
        print val
        if val == 1:
            insertEmployee()
        elif val == 2:
            editEmployee()
        elif val == 3:
            searchEmployee()
        elif val == 4:
            listEmployee()
        elif val == 5:
             break
        else:
            print("Error")
    except ValueError:
        print("That's not a Number!")




