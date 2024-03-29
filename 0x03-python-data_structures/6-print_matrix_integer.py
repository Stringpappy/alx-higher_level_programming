#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for s in matrix:
            for t in s:
                print("{:d}".format(t), end=' ' if t != s[-1] else '')
            print()
