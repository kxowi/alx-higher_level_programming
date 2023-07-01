#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """class defines a square"""
    def __init__(self, size=0):
        """initializes the square
        Args:
             size (int): size of a side of the square
        Return:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the square's area"""
        return (self.__size ** 2)
