#!/usr/bin/python3
"""defines text file for append function"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    and returns the number of characters added
    Args:
    @filename: the name of file
    @text: the text of the file
    """
    with open(filename, "a+") as f:
        return f.write(text)
