#!/usr/bin/python3
"""print_sorted"""


class MyList(list):
    """inherits list"""  
    def print_sorted(self):
        """class MyList that inherits from list
        """
        print(sorted(self))
