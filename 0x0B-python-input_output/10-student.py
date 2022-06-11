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
        dicti = self.__dict__
        if attrs is None:
            return dicti

        dic = {key: value for key, value in dicti.items() if key in attrs}
        return dic
