#!/usr/bin/python3
"""class square"""
Rectangle = __import__("9-rectangle.py").rectangle


class Square(Rectangle):
    """subclass of rectangle"""

    def __init__(self, size):
        """initilising"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

        def area(self):
            """for square"""
            return self.size ** 2
