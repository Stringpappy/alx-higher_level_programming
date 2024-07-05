#!/usr/bin/python3
"""Python func that  Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    The functin that Represent Pascal's Triangle of size n.
    """
    if zn <= 0:
        return []

    triangles = [[1]]
    x = len(triangles)
    while x != n:
        dtri = triangles[-1]
        dtmp = [1]
        for v in range(len(dtri) - 1):
            dtmp.append(dtri[v] + dtri[v + 1])
        dtmp.append(1)
        triangles.append(dtmp)
    return triangles
