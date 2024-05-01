#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""Rectangle = __import__("9-rectangle.py").Rectangle

class Square(Rectangle):
    """subclaas of rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

        def area(self):
            """area of a square"""
            return size ** 2

        def __str__(self):
            """suare string"""
            return "[Square] " + str(self.__size) + "/" + str(self.__size)
