__author__ = 'william'

import re

def generateCode():
    return 0

def validateName(name):
    return 0

def validateEmail(email):
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return True
    else:
        return False

def validateSalary(salary):
    return 0

def validateId(id):
    return 0

def validatePhone(phone):
    return 0
