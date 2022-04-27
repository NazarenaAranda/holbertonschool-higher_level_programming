#!/usr/bin/python3
def fizzbuzz():
    for numero in range(1, 101):
        if numero % 15 == 0:
            print("FizzBuzz ", end='')
        elif numero % 5 == 0:
            print("Buzz ", end='')
        elif numero % 3 == 0:
            print("Fizz ", end='')
        else:
            print(f"{numero} ", end='')
