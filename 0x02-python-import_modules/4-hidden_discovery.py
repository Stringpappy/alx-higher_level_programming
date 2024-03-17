#!/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    somfunc = dir()
    funclen = len(somefunc)
    for count in range (0, funclen):
        if somefunc[count][:2] != "__":
            print("{:s}".format(somefunc[count]))
