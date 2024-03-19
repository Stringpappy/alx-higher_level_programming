#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for c in matrix:
            for co in c:
                print("{}".format(co), end=' ' if co != c[-1] else '')
            print()
