# GCD:
# The Problem
# Calculate the greatest common divisor (gcd) of two numbers.

def calculate_gcd(a, b):
    upper_limit = a
    if a > b:
        upper_limit = b
    for i in range(upper_limit, 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1


if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print(f"GCD of {num1} and {num2} is {calculate_gcd(num1, num2)}")

    except ValueError:
        print("Inputs must be integer numbers")
