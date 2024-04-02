#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    digit = 0
    try:
        for stuff in range(x):
            print(f"{my_list[stuff]}", end='')
            digit += 1
    except IndexError:
        pass
    print()
    return digit
