#!/usr/bin/python3
import random
ldigit = " "
number = random.randint(-10000, 10000)
if number < 0:
    ldigit = number % -10
else:
    ldigit = number % 10
if ldigit > 5:
    print(f"Last digit of {number} is {ldigit} and is greater than 5")
elif ldigit == 0:
    print("""Last digit of {:d} is {:d} and is 0""".format(number, ldigit))
elif ldigit < 6 and ldigit != 0:
    print(f"Last digit of {number} is {ldigit} and is less than 6 and not 0")
