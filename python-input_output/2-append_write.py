#!/usr/bin/python3
"""function that appens string"""


def append_write(filename="", text=""):
    """appens string end a text file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return(f.write(text))
