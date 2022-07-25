#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 1:
        print('#')
    elif size == 0:
        return
    else:
        print(''.join(['\n' if x % (size + 1) == 0 else '#'
                       for x in range(1, size ** 2 + size)]))
