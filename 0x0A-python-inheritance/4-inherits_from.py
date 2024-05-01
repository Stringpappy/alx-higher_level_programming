#/usr/bin/python3
""" function that returns True if the object is an 
instance of a class that inherited directly or indirectly"""


def inherits_from(obj, a_class):
    """check if object is a subclass of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
