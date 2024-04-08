#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""
def text_indentation(text):
    """ python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text[x]) == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?":
            if text[x] in ".?:":
                print("\n")
            x = x + 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
