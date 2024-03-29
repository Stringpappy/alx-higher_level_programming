#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 100):
        if number % 3 == 0:
            print("Fizz", end="")
        elif number % 5 == 0:
<<<<<<< HEAD
            print("Buzz")
        if number % 15 || number % 15 * 2 == 0 || number % 15 * 3 || number % 15 * 4 || number % 15 * 6:
            print("FizzBuzz")
=======
            print("Buzz", end="")
        elif number % 3 and number % 35== 0:
            print("FizzBuzz", end="")
>>>>>>> afd6382b36ddd60205dd267f9145b8076c44f8bf
        else :
            print(number)
