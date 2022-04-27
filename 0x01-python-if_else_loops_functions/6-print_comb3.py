#!/usr/bin/python3
for numero1 in range(10):
    for numero2 in range(10):
        if numero2 > numero1 and numero1 != 8:
            print(f"{numero1:d}{numero2:d}", end=', ')
print("89")
