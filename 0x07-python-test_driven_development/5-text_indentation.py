#!/usr/bin/python3
"""
Module for 5-text_indentation
Program prints organized text
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    f = 0
    for j in text:
        if j == " " and f == 1:
            f = 0
            continue
        print(j, end='')
        if j in ".:?":
            f = 1
            print('\n')
