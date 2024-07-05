#!/usr/bin/python3
"""
Pythn func that Contains the "class_to_json" function
"""


def class_to_json(obj):
    """func that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)"""
    return obj.__dict__
