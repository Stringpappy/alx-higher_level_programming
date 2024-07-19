#!/usr/bin/python3
"""clss square that inherit fro Revtngle"""
from models.rectangle import Rectangle

class square(Rectangle):
    """subclass"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, size, size, x, y)

        def __str__(self):
            """str"""
            return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
