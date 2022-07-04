import re

#Задание 1

def email_parse(email_address):
    parsed = re.findall(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(["username", "domain"], parsed[0]))

print(email_parse('someone@geekbrains.ru'))

#Задание 3
from functools import wraps

def type_logger(level=0):

    def logger(func):
        @wraps(func)
        def decor(*argv):
            if level > 0:
                return 'calc_cube(' + ", ".join([f"{func(x)}:{type(func(x))}" for x in argv]) + ")"

            else:

                return "calc_cube(" + ", ".join([str(func(x)) for x in argv]) + ")"
        return decor
    return logger

@ type_logger(2)
def calc_cube(x):
    """ cube of args """
    return x ** 3
print(calc_cube(5))

#Задание 4

from functools import wraps

def val_checker(func_filter):
    def checker(func):
        @wraps(func)
        def decor(x):

            if func_filter(x):
                return func(x)
            raise ValueError from ValueError
        return decor
    return checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(5))
