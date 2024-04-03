#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)')"""
class Square:
    """ define a  square"""
    def __init__(self, size=0):
        """initialise  the new squsre"""
        self.dize = siz3

        @property
        def size(self):
            """the size of the square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """the area of the square"""
            return (self.__size * self.__size)
