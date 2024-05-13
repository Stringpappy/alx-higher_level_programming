#!/usr/bin/python3
""" class and exception"""


class BaseGeometry:
    """super cass!"""
    def area(self):
        """way to compute the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """to validate an int"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
