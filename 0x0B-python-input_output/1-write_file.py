#!/usr/bin/python3
"""
A python function that Contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as fi:
        return fi.write(text)
