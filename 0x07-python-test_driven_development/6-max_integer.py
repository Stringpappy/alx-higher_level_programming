#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""
def max_integer(list=[]):
    """ python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    if len(list) = 0:
        return None
    outcome = list[0]
    x = 1
    while x < len(list):
        if list[x] > outcome:
            outcome = list[x]
            x += 1
            return outcome

