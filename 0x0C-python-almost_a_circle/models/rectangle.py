#!/usr/bin/python3
"""rectangle module"""
from models.base import Base

class Rectangle(Base):
    """Rectangle class that  inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height attribute"""
        self.__height = value

    @property
    def x(self):
        """Getter  x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x"""
        self.__x = value

    @property
    def y(self):
        """Getter ye"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y"""
        self.__y = value

