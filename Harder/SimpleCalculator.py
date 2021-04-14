# Simple Calculator
# Create a simple calculator.
# That will be able to take user input of two numbers and the operation the user wants to perform.

try:
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num2} + {num1} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num2} - {num1} = {num2 - num1}")
    print(f"{num2} * {num1} = {num2 * num1}")
    print(f"{num1} * {num2} = {num2 * num1}")
    print(f"{num1} / {num2} = {num1 / num2 if num2 != 0 else 'Infinity'}")
    print(f"{num2} / {num1} = {num2 / num1 if num1 != 0 else 'Infinity'}")

except ValueError as err:
    print(err)
