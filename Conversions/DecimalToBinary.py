# Decimal to Binary
# The Problem
# Convert a decimal number to binary number.

try:
    decimal = int(input("Enter a decimal number : "))
    binary = bin(decimal)
    print(f"{decimal} base 10 = {binary} base 2")
except ValueError:
    print("Input must be a number")
