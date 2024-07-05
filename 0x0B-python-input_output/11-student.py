#!/usr/bin/python3
"""
A python task that Contains the class "Student"
"""


class Student:
    """the super student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the studen atribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to returns a dictionary representation of a Student instance
        with the listed attribute attributes"""
        if att is None:
            return self.__dict__
        dict_new = {}
        for arg in att:
            try:
                dict_new[arg] = self.__dict__[arg]
            except FileNotFoundError:
                pass
        return dict_new

    def reload_from_json(self, json):
        "" to "replaces all attributes of the Student instance"""
        for args in json:
            try:
                setattr(self, args, json[key])
            except FileNotFoundError:
                pass
