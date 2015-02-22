__author__ = 'william'

import re
import string

import random
from random import randint

def generateCode():
    code = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWZYZ') for i in range(2))
    num = randint(0, 9)
    nm2 = randint(0, 9)
    code += str(num) + str(nm2)
    return code

def validateName(name):
    if not re.match('^[A-Za-z]*$', name):
        return True
    else:
        return False


def validateEmail(email):
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return True
    else:
        return False

def validateSalary(salary):
    if not re.match('^[0-9]*$', salary):
        return True
    else:
        return False

def validateId(id):
    if not re.match('^[0-9]{13}$', id):
        return True
    else:
        return False

def validatePhone(phone):
    if not re.match('^[0-9]{8}$', phone):
        return True
    else:
        return False


