#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""
def print_square(size):
    """ python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    if ((not isinstance(size, int))):
        raise TypeError("size must be an integer")
    if ((not isinstance((size < 0)))):
        raise ValueError("size must be >= 0")
    if ((not isinstance(size < 0) and not (isinstance(size, float)))):
        raise ValueError("size must be an integer")
    print("#" * size)
