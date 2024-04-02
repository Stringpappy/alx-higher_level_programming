#!/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    another_list = []
    for stuff in range(list_length):
        try:
            division = my_list_1[stuff] / my_list_2[stuff]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            another_list.append(division)
    return another_list

