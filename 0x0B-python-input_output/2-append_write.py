#!/usr/bin/python3
"""
a python function that appends a string
"""


def append_write(filename="", text=""):
    """eturns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as fi:
        return fi.write(text)
