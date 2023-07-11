#!/usr/bin/python3
"""defines From JSON string to Object function"""


def from_json_string(my_str):
    """function that returns an object
    (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
