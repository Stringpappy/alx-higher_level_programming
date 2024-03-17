#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    if num < 1:
        print(f"{num} arguments")
    elif num == 1:
        print(f"{num} argument")
    else:
        print(f"{num} argument")
    for count in range(num):
        print(f"{count +1 }: {argv + 1}arguments)")
