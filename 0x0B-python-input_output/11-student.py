#!/usr/bin/python3
"""clase"""


class Student:
    """iniciar clase"""
    def __init__(self, first_name, last_name, age):
        """atributos"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """devolver diccionario"""

        if attrs is not None:
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}

        return self.__dict__

    def reload_from_json(self, json):
        """remplzar"""

        for key, value in json.items():
            self.__dict__[key] = value
