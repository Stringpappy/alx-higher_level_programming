#!/usr/bin/python3
""" rectangle module"""


class BaseGeometry:
    """super cass!"""

    def __init__(self, width, height, value):
        """initalising"""
        self.width = width
        self.height = height
        self.value = value
    def area(self):
        """way to compute the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """initilising"""
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
    def __init__(self, width, height):
        """initalising"""
        self.integer_validdator("height", height)
        self.__width = width
        self.__height = height
