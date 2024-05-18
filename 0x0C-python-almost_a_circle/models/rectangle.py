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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height attribute"""
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter  x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <  0:
            raise ValueError(f"x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter ye"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y"""
        if not isinstance(value, int):
            raise TypeError(f"y must be an integer")
        if valuee <  0:
            raise ValueError(f"y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.height):
            print("#" * self.width)
     
     def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})
        "

    def update(self, *args):
        """update"""
    l = len(args)
    if l >= 1:
        self.id = args[0]
    if l >= 2:
        self.width = args[1]
    if l >= 3:
        self.height = args[2]
    if l >= 4:
        self.x = args[3]
    if l >= 5:
        self.y = args[4]

    def perimeter(self):
        return 2 * (self.width + self.height)
