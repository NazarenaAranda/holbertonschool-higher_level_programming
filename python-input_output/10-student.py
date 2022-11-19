#!/usr/bin/python3
"""class Student that defines a student"""


class Student():
    """class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dictt = {}
        if attrs is None:
            return self.__dict__
        if type(attrs) == list:
            for i in attrs:
                try:
                    if type(i) == str:
                        dictt[i] = self.__dict__[i]
                except Exception:
                    Exception
        return dictt
