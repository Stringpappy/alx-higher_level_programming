#!/usr/bin/python3
"""Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherit from class BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of rect calculation."""
        return self.__width * self.__height

    def __str__(self):
        """ string representation of Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
