#!/usr/bin/python3
""" importar rectangle de "9-rectangle.py" """

Rectangle = __import__(
        "9-rectangle").Rectangle


class Square(Rectangle):
    """clase square"""
    def __init__(self, size):
        """instanciacion con size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

        def area(self):
            """metodo area"""
            return(super().area())
        def __str__(self):
            """ejecuta string"""
            return("[Square] {}/{}".
                    format(self.__size, self__size))
