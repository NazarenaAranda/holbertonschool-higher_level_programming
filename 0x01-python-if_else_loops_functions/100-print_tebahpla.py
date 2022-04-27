#!/usr/bin/python3
for letras in range(122, 96, -1):
    if letras % 2:
        letras = letras - 32
    print("{:c}" . format(letras), end='')
