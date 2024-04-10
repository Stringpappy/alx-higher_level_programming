#!/bin/usr/python3
def magic_string(n):
    magic_string.n = getattr(magic_string, 'n', 0) +1
    result = "BestSchool, " * (magic_string.n - 1) + "BestSchool"
    return (result)

