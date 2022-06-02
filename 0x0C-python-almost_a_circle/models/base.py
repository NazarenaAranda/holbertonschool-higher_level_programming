#!/usr/bin/python3
"""crear clase"""


class Base:
    """ dfghjkl """
    __nb_objects = 0

    def __init__(self, id=None):
        """condiciones"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

