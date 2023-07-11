#!/usr/bin/python3
"""defines text file for write function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    and returns the number of characters written
    """
    with open(filename, 'w+', encoding="utf-8") as f:
        return f.write(text)
