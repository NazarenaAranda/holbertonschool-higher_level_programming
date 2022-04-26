#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_sig = abs(number) % 10
if number < 0:
    num_sig = -num_sig
print(f"Last digit of {number} is {num_sig} ", end='')
if num_sig > 5:
    print("and is greater than 5")
elif number % 10 == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
