#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    var = number % 10
    print (f"{var:d}", end='')
    return (var)
