#!/usr/bin/python3
"""an empty suare"""


class Square:
    """empty suare"""

    def __init__(self, size=0):
        """initialising"""
        self.__size = size

    @property
    def size(self):
        """property setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return square of a num"""
        return self.__size ** 2
