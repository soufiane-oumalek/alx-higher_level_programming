#!/usr/bin/python3
"""square characters"""


def print_square(size):
    """function that prints a square
    with the character
    @size: size for the square """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size == 0:
        return

    for i in range(size):
        [print("#", end="")for j in range(size)]
        print("")
