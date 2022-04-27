#!/usr/bin/python3
def uppercase(str):
    aux = 0
    for l in str:
        aux = ord(l)
        if aux >= 97 and aux <= 122:
            aux -= 32
        print(f"{aux:c}", end='')
    print('')
