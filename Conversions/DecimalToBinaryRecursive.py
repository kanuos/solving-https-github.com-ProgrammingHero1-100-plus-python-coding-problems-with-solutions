# Decimal to Binary Recursively
# The Problem
# Convert a decimal number to binary number.

def decimal_to_bin_iterative(number: int) -> str:
    """ Convert a decimal number to binary """
    number = abs(number)
    __binary = []
    while number > 0:
        __binary.append(str(number % 2))
        number //= 2
    reversed(__binary)
    return "".join(__binary)


def decimal_to_bin_recursive(number):
    if number == "0" or number == "1":
        return str(number)
    return f"{int(number) % 2}" + decimal_to_bin_recursive(str(int(number) // 2))


try:
    decimal = int(input("Enter a decimal number : "))
    print(f"{decimal} base 10 = {decimal_to_bin_iterative(decimal)} base 2")
    print(f"{decimal} base 10 = {decimal_to_bin_recursive(decimal)} base 2")
except ValueError:
    print("Input must be a number")
