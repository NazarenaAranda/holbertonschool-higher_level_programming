#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """public instance method"""
    def print_sorted(self):
        print(sorted(self))
