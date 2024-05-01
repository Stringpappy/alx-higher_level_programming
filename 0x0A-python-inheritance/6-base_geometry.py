#!/usr/bin/python3
""" class and exception"""


class BaseGeometry:
    """super cass!"""
    def area(self):
        """way to compute the area"""
        raise Exception("area() is not implemented")
