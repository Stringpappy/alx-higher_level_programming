#!/usr/bin/python3
"""
A python function that writes an Object to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """ funnc Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as fi:
        json.dump(my_obj, fi)
