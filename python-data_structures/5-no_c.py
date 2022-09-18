#!/usr/bin/python3
def no_c(my_string):
    c = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            c += i
    return c
