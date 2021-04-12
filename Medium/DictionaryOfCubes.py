# Cube Sum
# The Problem
# With a given integral number n, write a program to calculate the sum of cubes.

def sum_of_cubes(n: int) -> (int, list):
    entries = []
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
        entries.append(f"{i}^3")
    return total, entries


try:
    num = int(input("Enter the value of N : "))
    result, words = sum_of_cubes(num)
    print(" + ".join(words) + f" = {result}")
except ValueError:
    print("Expected number")
