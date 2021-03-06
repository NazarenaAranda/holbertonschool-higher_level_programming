#!/usr/bin/python3
""" clase """


class Square:
    """ inicializar """
    def __init__(self, size=0, position=(0, 0)):
        """ asdf """
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                print('\n' * self.__position[1], end='')
            for j in range(self.__size):
                print(" " * self.position[0] + '#' * self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) != 2 or type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
