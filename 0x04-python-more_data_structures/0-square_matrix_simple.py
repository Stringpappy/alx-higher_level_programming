#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    d = matrix.copy()

    for detail in range(len(matrix)):
        d[detail] = list(map(lambda f: f**2, matrix[detail]))
    return (d)
