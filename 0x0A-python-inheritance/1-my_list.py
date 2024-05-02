#!/usr/bin/python3
"""class that inherit from a list"""


class MyList(list):
    """sub  class"""
    def print_sorted(self):
        """ printing sorted list"""
        print(sorted(self))
