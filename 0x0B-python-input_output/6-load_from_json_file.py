#!/usr/bin/python3
"""
A python ffunction that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """func that crate and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as fi:
        return json.load(fi)
