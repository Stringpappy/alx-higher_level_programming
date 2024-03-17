#!/bin/python3
if __name__ == "__main__":
    from sys import argv
    addnum = 0
    argnum = len(argv)
    for count in range(1, argnum):
        addnum += int(argv[count])
    print("{}".format(addnum))
