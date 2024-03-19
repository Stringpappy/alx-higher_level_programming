#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    if num < 1:
        print(f"{num} argument")
    elif num == 1:
        print(f"{num} arguments")
    else:
        print(f"{num} argument")
    for count in range(num):
        print("{}: {:s}".format(count + 1, argv[count + 1]))
