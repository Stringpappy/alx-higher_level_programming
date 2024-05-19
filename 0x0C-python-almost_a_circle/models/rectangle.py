#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that  inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter height attribute"""
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError(f"width must be > 0")
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
            raise TypeError(f"height must be an integer")
        if value < 0:
             raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter ye"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y"""
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value < 0:
             raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """print # instead of value"""
        for l in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """return rect, id, x/y"""
        return f"[Rectangle] ({id(self)}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """assigns an argument to each attribute:"""
        if args:
            l = len(args)
            if l > 0:
                self.__id = args[0]
            if l > 1:
                self.__width = args[1]
            if l > 2:
                self.__height = args[2]
            if l > 3:
                self.__x = args[3]
            if l > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.item():
                setattr(self, key, valu)
