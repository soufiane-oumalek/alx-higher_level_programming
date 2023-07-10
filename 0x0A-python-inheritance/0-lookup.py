#!/usr/bin/python3
"""lookup"""


def lookup(obj):
    """returns the list of available
    attributes and methods of an object
    Args
    @obj: object
    Return: list of available
    """
    return dir(obj)
