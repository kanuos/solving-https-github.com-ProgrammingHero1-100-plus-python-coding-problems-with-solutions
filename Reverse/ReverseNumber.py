# Reverse a number
# The problem
# Reverse a number.

def reverse_number(num: int) -> int:
    reverse_num = 0
    while num > 0:
        reverse_num = reverse_num * 10 + num % 10
        num //= 10
    return reverse_num


try:
    n = int(input("Enter a number : "))
    print(f"Reverse of {n} is {reverse_number(n)}")
except ValueError:
    print("Input must be a number")
