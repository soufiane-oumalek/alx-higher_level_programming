#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dgt = abs(number) % 10
str = "Last digit of"
if number < 0:
    dgt = -dgt
if dgt > 5:
    str2 = "and is greater than 5"
elif dgt == 0:
    str2 = "and is 0"
else:
    str2 = "and is less than 6 and not 0"
print(f"{str} {number:d} is {dgt} {str2}")
