#!/usr/bin/python3
""" class and exception"""


class BaseGeometry:
    """super cass!"""
    def area(self):
        """way to compute the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """initilising"""
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
