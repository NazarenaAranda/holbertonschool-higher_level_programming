#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a = 0
    suma = 0
    if isinstance(roman_string, str):
        for a in range(len(roman_string) - 1):
            if rom[roman_string[a]] >= rom[roman_string[a + 1]]:
                suma += rom[roman_string[a]]
            else:
                suma -= rom[roman_string[a]]
            a += 1
        suma += rom[roman_string[a]]
        return suma
    return 0
