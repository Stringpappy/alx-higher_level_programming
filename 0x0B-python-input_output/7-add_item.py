#!/usr/bin/python3
"""
A python Script that adds all arguments to a Python list,
and then saves them to a file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    my_jlist = load_from_json_file(filename)
except FileNotFoundError:
    my_jlist = []

for args in argv[1:]:
    my_jist.append(arg)

save_to_json_file(my_jlist, filename)
