# The problem
# Take two numbers from the users.
# Calculate the result of second number power of the first number.

try:
    num1 = int(input("Enter base: "))
    num2 = int(input("Enter exponent: "))
    print(f"{num1} ^ {num2} = {num1 ** num2}")
except ValueError:
    print("Base and exponents must be integers")
