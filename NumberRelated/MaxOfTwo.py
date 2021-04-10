# max of two
# The problem
# Find the max number of two numbers.
#
# Hints
# Ask the user to enter two numbers.
#
# Then, you can run a comparison to compare which one is larger.
#
# Think about it and try yourself first.

try:
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is smaller than {num2}")
    else:
        print(f"{num1} and {num2} are equal")
except ValueError:
    print("Inputs must be numbers")
