#!/usr/bin/python3
"""class LockedClass with no class or object attribute"""

class LockedClass:
    """dstop the user from ynamically creating new instance attributes, 
    except if the new instance called first_name"""

    __slots__ = ["first_name"]

