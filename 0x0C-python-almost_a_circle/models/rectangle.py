#!/usr/bin/python3
""" rectangle module"""
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

    #@width.setter
    #def width(self, value):
        #"""setter for width"""
        #if not isinstance(value, int):
            #raise TypeError("width must be an integer")
        #elif value <= 0:
            #raise ValueError("width must be > 0")
        #self._width = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    #@height.setter
    #def height(self, value):
    #    """Setter height attribute"""
    #    if not isinstance(value, int):
    #        raise TypeError(f"height must be an integer")
    #    if value <= 0:
    #        raise ValueError(f"height must be > 0")
    #    self.__height = value
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        for val in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """return rect, id, x/y"""
        return f"[Rectangle]({id(self)}) {self.__x}/{self.__y}\
    - {self.__width}/{self.__height}"

    def update(self, *args):
        """assigns an argument to each attribute:"""
        if args:
            lent = len(args)
            if lent > 0:
                self.__id = args[0]
            if lent > 1:
                self.__width = args[1]
            if lent > 2:
                self.__height = args[2]
            if lent > 3:
                self.__x = args[3]
            if lent > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.item():
                setattr(self, key, valu)
