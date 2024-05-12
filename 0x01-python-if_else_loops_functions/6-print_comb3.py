#!/usr/bin/python3
for num in range(0, 10):
    for numb in range(num + 1, 10):
        if num == 8 and numb == 9:
            print("89")
        else:
            print("{:d}{:d} ," .format(num,numb), end='')
