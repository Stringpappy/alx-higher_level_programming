#!/usr/bin/python3                                                                      """python3 -c 'print(__import__("my_module").MyClass.__doc__)')"""
class Square:                                                                               """ define a  square"""
    def __init__(self, size=0):                                                                 """initialise the square"""
    self.size = size

    @property
    def size(self):
        """the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
     def area(self):
         """public function """                                                                  return (self.__size * self.__size)
