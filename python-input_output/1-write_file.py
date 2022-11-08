#!/usr/bin/python3
"""function that write text"""


def write_file(filename="", text=""):
    """write text"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
