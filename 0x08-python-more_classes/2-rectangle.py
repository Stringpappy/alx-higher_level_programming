#!/usr/bin/python3
"""class that define an empty rectangle"""


class Rectangle:
    """the class rectangle with empty instance and field"""
    def __nit__(self, width =0, height=0):
        self.width = width 
        self.height = height
    
    @property
    def width(self):
        """ set the rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """ set the rectangle width """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
