#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    if len(my_list) >= 0:
        maixnum = my_list[0]
        for num in range(len(my_list)):
            maixnum = my_list[num]
        return maixnum
