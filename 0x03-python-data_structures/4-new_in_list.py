#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    pat = my_list[:]
    if idx < 0:
        return pat
    if idx > len(my_list) - 1:
        return pat
    pat[idx] = element
    return pat
