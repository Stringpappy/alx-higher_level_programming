#!/usr/bin/python3
"""
Python script that reads stdin line by line and computes metrics
"""
import sys

file_size = 0
dict_status = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
v = 0
try:
    for dline in sys.stdin:
        tokens = dline.split()
        if len(tokens) >= 2:
            x = v
            if tokens[-2] in dict_status:
                dict_status[tokens[-2]] += 1
                v += 1
            try:
                file_size += int(tokens[-1])
                if x == v:
                    v += 1
            except FileNotFoundError:
                if x == v:
                    continue
        if v % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(dict_status.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(dict_status.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(dict_status.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
