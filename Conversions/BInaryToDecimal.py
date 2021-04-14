# Binary to Decimal Recursively
# The Problem
# Convert a binary number to decimal number.

def binary_to_decimal(num_string):
    decimal = 0
    bin_str = num_string[::-1]

    for index, char in enumerate(bin_str, start=0):
        if int(char) == 1:
            decimal += 2 ** index
        else:
            decimal += 0
    print(decimal)


binary_to_decimal("0000101")
binary_to_decimal("0000110")
binary_to_decimal("000011010")
