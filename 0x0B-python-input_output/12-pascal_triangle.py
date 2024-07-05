#!/usr/bin/python3
"""python fun Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """func that  Represent Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    trians = [[1]]
    while len(trians) != n:
        dtri = trians[-1]
        dtmp = [1]
        for itr in range(len(dtri) - 1):
            dtmp.append(dtri[itr] + dtri[itr + 1])
        dtmp.append(1)
        trians.append(dtmp)
    return trians
