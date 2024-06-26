#!/usr/bin/python3
""" The goal of it is to manage id attribute in
all your future classes and to avoid
duplicating the same code"""


class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
