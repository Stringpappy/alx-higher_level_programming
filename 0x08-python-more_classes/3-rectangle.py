#!/usr/bin/python3
"""class that define an empty rectangle"""


class Rectangle:
    """super class of width and height"""
    def __init__(self, width=0, height=0):
        """initializing a nnew rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """to set ractangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to set rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0:
            return 0
        else:
            return self.__width * self.__height

        def __str__(self):
            if self.width == 0 | self.__height == 0:
                return ""
