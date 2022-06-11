#!/usr/bin/python3

"""crear una clase"""


class Student:
    """ iniciar """
    def __init__(self, first_name, last_name, age):
        """atributos de instancia publicos"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return diccionario"""

        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

            return self.__dict__
