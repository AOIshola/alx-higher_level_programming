#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    ld = (number % 10) * -1
    number *= -1
else:
    ld = number % 10

output = f"Last digit of {number} is {ld}"
if ld > 5:
    print(f"{output} and is greater than 5")
elif ld == 0:
    print(f"{output} and is 0")
else:
    print(f"{output} and is less than 6 and not 0")
