#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = len(my_list)
    n_list = []
    for count in range(j):
        if my_list[count] % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return (n_list)
