#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lent = len(my_list)
    if idx < 0:
        return my_list
    if idx >= lent:
        return my_list
