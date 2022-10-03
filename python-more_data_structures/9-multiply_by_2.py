#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary2 = a_dictionary.copy()
    for i in list(dictionary2):
        dictionary2[i] = dictionary2[i] * 2
    return dictionary2
