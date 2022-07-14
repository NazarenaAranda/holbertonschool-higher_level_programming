#!/usr/bin/python3
"""definiendo la clase"""


class MyInt(int):
    """hereda de int"""
    def __eq__(self, result):
        """eq -> a == b"""
        return False

    def __ne__(self, result):
        """ne -> a != b"""
        return True
