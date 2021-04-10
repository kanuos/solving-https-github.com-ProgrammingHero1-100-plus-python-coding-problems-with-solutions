# Floor division
# The problem
# Find the floor division of two numbers.
#
# Hints
# Floor division means the integer part of a division operation.
# For example, if you divide 17/5 the quotient will be 3.4

try:
    num1 = float(input("Enter the dividend : "))
    num2 = float(input("Enter the divisor : "))
    remainder = num1 % num2
    quotient = num1 // num2
    print(f"Dividend : {num1}\nDivisor : {num2}\nRemainder : {remainder}"
          f"\nQuotient : {quotient}")
except ValueError:
    print("Input must be numbers")
except ZeroDivisionError:
    print("Infinite")
