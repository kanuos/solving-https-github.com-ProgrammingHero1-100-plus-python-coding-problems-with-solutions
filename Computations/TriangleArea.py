# Triangle Area
# The problem
# Take three sides of a triangle. And then calculate the area of the triangle.
import math


def check_valid_triangle_sides(a, b, c):
    return a + b > c and a + c > b and b + c > a


def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


try:
    s1 = float(input("Enter the first side of the triangle : "))
    s2 = float(input("Enter the second side of the triangle : "))
    s3 = float(input("Enter the third side of the triangle : "))
    if not check_valid_triangle_sides(s1, s2, s3):
        raise ValueError("Invalid triangle sides")
    print(f"The area of the triangle with sides {s1}, {s2} and {s3} is {calculate_area(s1, s2, s3)}")
except ValueError as err:
    print(err)
