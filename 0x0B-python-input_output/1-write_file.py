#!/usr/bin/python3
"""defines text file for write function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    and returns the number of characters written
    Args:
    @filename: the name of file
    @text: the text of the file
    """
    with open(filename, 'w+') as f:
        return f.write(text)
