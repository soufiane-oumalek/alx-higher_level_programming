#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """declare class Square"""
    def __init__(self, size=0):
        """intialize square
        Args:
            size(int): the size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
