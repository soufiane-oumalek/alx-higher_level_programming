#!/usr/bin/python3
"""defines class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified
    class ; otherwise False.
    Args:
    @obj: is an object
    @a_class: a class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
