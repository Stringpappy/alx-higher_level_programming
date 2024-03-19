#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for count in matrix:
            for count_two  in count:
                print("{:d}".format(count_two), end=' ' if count_two != count[-1] else '')
            print()
