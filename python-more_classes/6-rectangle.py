#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle"""


class Rectangle:
    """empty class"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        empty = ""
        if (self.__width == 0 or self.__height == 0):
            return empty
        else:
            for _ in range(self.__height):
                for _ in range(self.__width):
                    empty += "#"
                empty += '\n'
        return empty[:-1]

    def __repr__(self):
        return(f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
