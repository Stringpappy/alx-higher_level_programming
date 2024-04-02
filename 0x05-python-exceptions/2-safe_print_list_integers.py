#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    not_aph = 0
    for stuff in range(x):
        try:
            print("{:d}".format(my_list[stuff]), end='')
            not_aph += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return not_aph
