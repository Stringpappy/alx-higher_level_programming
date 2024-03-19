#!/bin/python3
if __name__ == "__main__":
    from sys import argv
    addnum = 0
    arglen = len(argv)
    for count in range(1, arglen):
        addnum += int(argv[count])
    print("{}".format(addnum))
