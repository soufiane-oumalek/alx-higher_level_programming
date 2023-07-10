#!/usr/bin/python3
"""defines class"""


class MyInt(int):
    """initiliaze class"""

    def __eq__(self, value):
        """override operator != value"""
        return self.real != value

    def __ne__(self, value):
        """override operator == value"""
        return self.real == value
