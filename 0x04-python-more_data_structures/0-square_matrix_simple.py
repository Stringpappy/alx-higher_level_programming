#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    d = []
    for detail in matrix:
        d.append([f*2 for f in d])
    return d

