#!/usr/bin/python3
"""function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the
specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """return True or False"""
    if isinstance(obj, a_class) and a_class is not type(obj):
        return True
    else:
        return False
