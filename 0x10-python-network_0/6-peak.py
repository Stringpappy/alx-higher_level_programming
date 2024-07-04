#!/usr/bin/python3
"""
The funtion Find Peak task 6
"""


def find_peak(list_of_integers):
    """find the peak of the integers"""
    if list_of_integers == []:
        return None

    thesize = len(list_of_integers)
    if thesize == 1:
        return list_of_integers[0]
    elif thesize == 2:
        return max(list_of_integers)

    cent = int(thesize / 2)
    peak = list_of_integers[cent]
    if peak > list_of_integers[cent - 1] and peak > list_of_integers[cent + 1]:
        return peak
    elif peak < list_of_integers[cent - 1]:
        return find_peak(list_of_integers[:cent])
    else:
        return find_peak(list_of_integers[cent + 1:])
