#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dgt = abs(number) % 10
if number < 0:
    lst_dgt = -lst_dgt
if lst_dgt > 5:
    print(f"Last digit of {number:d} is {lst_dgt:d} and is greater than 5")
elif lst_dgt == 0:
    print(f"Last digit of {number:d} is {lst_dgt:d} and is 0")
else:
    print(f"Last digit of {number:d} is {lst_dgt:d} and is less than 6 and not 0")
