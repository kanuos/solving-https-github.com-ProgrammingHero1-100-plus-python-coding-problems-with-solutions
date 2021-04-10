# Divisible by 3 and 5
# The problem
# For a given number, find all the numbers smaller than the number.
# Numbers should be divisible by 3 and also by 5.

try:
    num = int(input("Enter a number : "))
    counter = 0
    for i in range(num):
        if i % 15 == 0:
            print(f"{i} is divisible by 3 and 5.")
            counter += 1
    print(f"There are {counter} numbers between 0 and {num}(not inclusive) "
          f"that are divisible by 3 and 5")
except ValueError:
    print("Input must be an integer")
