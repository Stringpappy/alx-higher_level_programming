#!/usr/bin/python3
"""function that returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """attribute and object for lookup
    args: obj: Object list
    Returns: List"""
    return dir(obj)
