#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    somefunc = dir()
    for count in range (0,len(somefunc)):
        if somefunc[count][:2] != "__":
            print("{:s}".format(somefunc[count]))
