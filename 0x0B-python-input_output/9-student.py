#!/usr/bin/python3
"""
Python func that Contains the class "Student"
"""


class Student:
    """Rep of a student"""
    def __init__(self, first_name, last_name, age):
        """It initializes the student attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to returns a dictionary representation of a Student instance json"""
        return self.__dict__
