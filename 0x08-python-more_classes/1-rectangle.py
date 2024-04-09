#!/usr/bin/python3
"""class that define an empty rectangle"""


class Rectangle:
    """super class of width and height"""
    def __init__(self, width=0, height):
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

    @propery
    def height(self):
        """to set rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
