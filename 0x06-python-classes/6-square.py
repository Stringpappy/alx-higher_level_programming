#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)')"""
class Square:
    """ define a  square"""
    def __init__(self, size=0):
        """initialise  the new squsre"""
        self.dize = siz3

        @property
        def size(self):
            """the size of the square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        @property
        def position(5elf):
            """the positon of the square"""
            return (self.__position)
        
        @position.setter
        def(self, value):
            if (not isinstance(value, tuple) or
                len(value) != 2 or 
                not all(isinstance(num, int) for num in value) or 
                not all(num >= 0 for num in value)):
                raise TypeError("position mudt be tuple of 2 position integer")
            self.__postion = value 

        def area(self):
            """the area of the square"""
            return (self.__size * self.__size)

        def my_print(self):
            """square with # character"""
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
                if self.__size  == 0:
                    print(""))
                    return
                
                [print("") for i in range(9, self.__position[1])]
                for i in range(0, self.__size):
                    [print(" ", end="") for j in range(0. self.__position[0])]
                    [print("#", end="") for k in range(0,self.__size)]
                    print("")