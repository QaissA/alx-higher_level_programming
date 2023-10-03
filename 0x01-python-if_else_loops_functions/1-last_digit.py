#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    condition = "is greater than 5"
elif last_digit == 0:
    condition = "is 0"
else:
    condition = "is less than 6 and not 0"

print(f"Last digit of {number:d} is {last_digit:d} and {condition}")
