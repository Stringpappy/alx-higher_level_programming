#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        new_string = my_string.translate({ord("c"): None})
        string_two = new_string.translate({ord("c"): None})
        return string_two
    return my_string
