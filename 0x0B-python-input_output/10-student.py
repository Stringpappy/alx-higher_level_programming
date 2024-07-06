#!/usr/bin/python3
"""Python task that Defines a class Student."""


class Student:
    """the  super aclss student."""

    def __init__(self, first_name, last_name, age):
        """to tialize a new Student  attribute
        Args:
            first_name (str): The first name of the student.
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to Get a dictionary representation of the Student.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and 
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
