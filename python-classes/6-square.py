#!/usr/bin/python3
"""Class Square"""


class Square():
    """instantion"""
    def __init__(self, size=0, position=(0, 0)):
        """ size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (len(value) != 2 or type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
