#!/usr/bin/python3
"""Prints"""


def say_my_name(first_name, last_name=""):
    """ function that prints My name is
    <first name> <last name>
    Args:
    @first_name: printe the first name
    @last_name: printe the last name """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be string")
    print("My name is {} {}".format(first_name, last_name))
