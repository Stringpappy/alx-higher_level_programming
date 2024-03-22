#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = a_dictionary.copy()
    key_l = list(x.keys())

    for c in key_l:
        x[c] *= 2

    return (x)
