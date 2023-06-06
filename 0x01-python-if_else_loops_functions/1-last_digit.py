#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str = "last of digit"
if last_digit > 5:
    print(f"{str} {number:d} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"{str} {number:d} is {last_digit:d} and is zero")
else:
    print(f"{str} {number:d} is {last_digit:d} and is less than 6 and not 0")
