# LCM
# The Problem
# For two numbers, calculate the least common multiple (LCM).

from GreatestCommonDivisor import calculate_gcd


def calculate_lcm(a, b):
    """Lowest Common Multiple
     LCM(a,b) * HCF(a,b) = a * b
     """
    return a * b / calculate_gcd(a, b)


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"LCM of {num1} and {num2} is {calculate_lcm(num1, num2)}")

except ValueError:
    print("Invalid input")
