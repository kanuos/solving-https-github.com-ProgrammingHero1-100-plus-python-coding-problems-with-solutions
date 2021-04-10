# Create a random number
# The problem
# Create a random number between 0 to 10

import random

try:
    number = int(input("How many numbers to generate : "))
    while number > 0:
        num = random.randint(0, 10)
        print(f"Number generated : {num}")
        number -= 1

except ValueError:
    print("Numbers must be positive non-zero integer")
