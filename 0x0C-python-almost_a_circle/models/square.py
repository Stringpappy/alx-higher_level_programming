#!/usr/bin/python3
"""
module that  contains the "Square" class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """func that Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, lv in kwargs.items():
                if key == "id":
                    if lv is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = lv
                elif key == "size":
                    self.size = lv
                elif key == "x":
                    self.x = lv
                elif key == "y":
                    self.y = lv

    def to_dictionary(self):
        """ func that Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """func that Return the print() a str representation of a Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
