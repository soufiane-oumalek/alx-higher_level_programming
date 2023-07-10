#!/usr/bin/python3
"""defines class"""


def is_same_class(obj, a_class):
    """function that returns True if the object
    is exactly an instance of the specified class;
    otherwise False.
    Args:
    @obj: is an object
    @a_class: is the class
    Returns True of false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
