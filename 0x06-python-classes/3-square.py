#!/usr/bin/python3
"""an empty suare"""


class Square:
    """empty suare"""
    def __init__(self, size=0):
        self.__size = size
        """intialise new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """public function """
        return (self.__size * self.__size)
