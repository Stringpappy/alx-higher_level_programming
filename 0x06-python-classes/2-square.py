#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)')"""
class Square:
    """define a class square"""
    def __init__ (self.size=0):
        """intialise new square"""
        if not isinstance(size,int):
            rause TypeError("size must be an integer")
        elif size < 0):
            raise ValueError("size must be >= 0")
