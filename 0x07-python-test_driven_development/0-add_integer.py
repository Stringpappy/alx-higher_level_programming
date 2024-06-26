#!/usr/bin/python3
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>>  add_integer(a, b=98)
a + 98
"""


def add_integer(a, b=98):
    """Return the value of sum of a and b """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
