#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argnum = len(argv) - 1
    if argnum < 0:
        print(f"{argnum} argument")
    elif argnum == 1:
        print(f"{argnum} arguments")
    else:
        print(f"{argnum} arguments")
    for  count in range(argnum):
        print(f"{count + 1}: {argv[count + 1]}")
