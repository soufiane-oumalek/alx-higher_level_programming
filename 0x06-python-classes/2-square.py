#!/usr/bin/python3
class Square:
    """declare class Square"""
    def init(self, size=0):
        """intialize square
        Args:
            size(int): the size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
