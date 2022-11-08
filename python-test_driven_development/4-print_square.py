#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """print square"""
    for _ in range(size):
        print("#" * size)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, float) and size < 0:
        raise TypeError("size must be an intege")
