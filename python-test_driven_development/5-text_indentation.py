#!/usr/bin/python3
"""function that print text"""


def text_indentation(text):
    """text with 2 llines after each of the characters"""
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end='')
    
    if type(text) != str:
        raise TypeError("text must be a string")
