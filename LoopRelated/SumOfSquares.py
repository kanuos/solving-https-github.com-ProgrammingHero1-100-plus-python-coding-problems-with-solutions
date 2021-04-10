# Sum of squares
# The problem
# Take a number as input. Then get the sum of the numbers. If the number is n. Then get
#
# 0^2+1^2+2^2+3^2+4^2+.............+n^2

try:
    print("Calculate the sum of squares from 1 - N numbers:")
    number = int(input("Enter the value of 'N' : "))
    if number <= 0:
        raise ValueError
    # arithmetic progression formulae
    # S = [n(n+1)(2n+1)]/6
    sum_of_square = (number * (number + 1) * ((2 * number) + 1)) / 6
    print(f"Sum of the square from 1 to {number} : {sum_of_square}")
except ValueError:
    print("N must be a positive non-zero integer")
