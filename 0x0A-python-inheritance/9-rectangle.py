#!/usr/bin/python3
""" class rectangle that inherite from basegeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectngle(BaseGeometry):
    """a subclass of super class basegeometry"""
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

        def area(self):
            """area of a rectangle"""
            return self.__width * self.__height

        def __str__(self):
            """string rep method"""
            return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
