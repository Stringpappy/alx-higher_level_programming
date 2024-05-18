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
            p = 2 * (self.width + self.height)
            return p


    def __str__(self):
        """ Returns a string representation of the rectangle with # characters."""
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for x in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str

    def __repr__(self):
        """
        Returns a string representation of the rectangile object.
        """
        return (f"Rectangle(width={self.width}, height={self.height}")